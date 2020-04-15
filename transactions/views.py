from copy import copy

from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import dateparse
from django.views import View
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from business.utils import ProductBacklogAction
from transactions.forms import StoreForm, ProductUpdateForm
from transactions.models import Customer, Product
from transactions.serializers import CustomerSerializer, ProductSerializer
from transactions.utils import validate_and_return_delivery_date, pagination
from users.permissions import IsTeamMembersOnly
from utils.helpers import send_invoice
from utils.token import Token


def transaction_index_view(request):
    return render(request, 'transactions/index.html')


def view_context(request):
    products = Product.objects.filter(business=request.user.active_business.pk, type='product')
    page_obj = pagination(request, products, 9)
    return {'products': products, 'page_obj': page_obj}


class ProductView(APIView):
    permission_classes = (IsTeamMembersOnly,)
    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.filter(transaction__business=request.user.active_business.pk)
        serializer = self.serializer_class(products, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        customer_data = request.data.get('customer')
        product_data = request.data.get('product')
        token = Token()

        if product_data.get('delivery_date'):
            product_data = validate_and_return_delivery_date(product_data)

        product_data['product_id'] = token.gen_token(35, ext='alphanum')

        product_data['business'] = request.user.active_business.pk
        product = self.serializer_class(data=product_data)
        product.is_valid(raise_exception=True)
        product.save()

        if customer_data:
            customer_data['uid'] = token.gen_token(25, ext='alphanum')
            customer_data['product'] = product.instance
            customer_data['added_by'] = request.user
            customer_serializer = CustomerSerializer(data=customer_data)
            customer_serializer.is_valid(raise_exception=True)
            customer = Customer.objects.create(**customer_data)

            send_invoice(customer, product.data)

        return Response(data=product.data)


class PaymentView(View):
    def get(self, request, customer_uid, ):
        try:
            customer = Customer.objects.get(uid=customer_uid)
        except Customer.DoesNotExist:
            raise Http404

        if not customer.transaction.status == 'in progress':
            raise Http404

        return render(request, 'transactions/payment.html', {'customer': customer})


@api_view(['GET'])
@permission_classes((IsTeamMembersOnly,))
def customers_api_view(request):
    customers = Customer.objects.filter(product__business=request.user.active_business.pk)
    serializer = CustomerSerializer(customers, many=True)

    return Response(data=serializer.data)


def customers_view(request):
    customers = Customer.objects.filter(product__business=request.user.active_business.pk, product__type='normal')
    page_obj = pagination(request, customers, 9)
    return render(request, 'transactions/customers.html', {'page_obj': page_obj})


def store_view(request):
    products = Product.objects.filter(business=request.user.active_business.pk, type='product')
    page_obj = pagination(request, products, 9)
    context = {'products': products, 'page_obj': page_obj}
    return render(request, 'transactions/store.html', context)


class StoreView(View):
    form_class = StoreForm

    def get(self, request):
        products = Product.objects.filter(business=request.user.active_business.pk, type='product')
        page_obj = pagination(request, products, 9)
        context = view_context(request)
        context['form'] = self.form_class
        return render(request, 'transactions/store.html', context)

    def post(self, request):
        context = view_context(request)
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            token = Token()
            product = form.instance
            product.product_id = token.gen_token(25, ext='alphanum')
            product.business = request.user.active_business
            product.type = 'product'
            product.added_by = request.user
            product.save()
            messages.success(request, 'Product added!')
            ProductBacklogAction().add_product(request.user, product)

        context['form'] = form
        return render(request, 'transactions/store.html', context)


def delete_product(request, product_pk):
    if request.method == 'POST':
        product = Product.objects.filter(pk=product_pk)
        if not product.exists():
            raise Http404
        ProductBacklogAction().delete_product(request.user, product[0])
        product.pop()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('store'))
    else:
        return redirect(reverse('store'))


def update_stock(request, product_pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_pk)
        if not request.POST['quantity']:
            messages.warning(request, 'Enter product quantity.')
            return redirect(reverse('store'))
        try:
            product.quantity = int(request.POST['quantity'])
            product.save(update_fields=('quantity',))
            ProductBacklogAction().update_stock(request.user, product)
            messages.success(request, 'Product deleted!')
        except ValueError:
            messages.warning(request, 'Enter valid product quantity in number')
        return redirect(reverse('store'))
    else:
        return redirect(reverse('store'))


def update_product(request, product_pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_pk)

        form = ProductUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            ProductBacklogAction().update_product(request.user, product)
            messages.success(request, 'Product updated!')
        else:
            messages.warning(request, 'Please complete all fields.')
    return redirect(reverse('store'))
