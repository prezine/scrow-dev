from copy import copy

from django.http import Http404
from django.shortcuts import render
from django.utils import dateparse
from django.views import View
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer, CustomerSerializer
from utils.helpers import send_invoice
from utils.token import Token


def transaction_index_view(request):
    return render(request, 'transactions/index.html')


class NewTransactionView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    transaction_serializer = TransactionSerializer
    customer_serializer = CustomerSerializer

    def post(self, request):
        customer_data = request.data.get('customer')
        transaction_data = request.data.get('transaction')

        customer = self.customer_serializer(data=customer_data)
        customer.is_valid(raise_exception=True)
        customer.save()

        if transaction_data.get('delivery_date'):
            try:
                transaction_data['delivery_date'] = dateparse.parse_datetime(
                    transaction_data.get('delivery_date')).date()
            except ValueError:
                pass

        token = Token()
        transaction_data['transaction_id'] = token.gen_token(14, ext='alphanum')

        transaction_data['customer'] = customer.data.get('id')
        transaction_data['business'] = request.user.active_business
        transaction = self.transaction_serializer(data=transaction_data)
        transaction.is_valid(raise_exception=True)
        transaction.save()

        send_invoice(customer.data, transaction.data)

        return Response(data=transaction.data)


class PaymentView(View):
    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(transaction_id=transaction_id)
        except Transaction.DoesNotExist:
            raise Http404

        if not transaction.status == 'in progress':
            raise Http404

        return render(request, 'transactions/payment.html', {'transaction': transaction})
