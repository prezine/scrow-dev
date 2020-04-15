from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from business.models import Business
from finance.helper import bank_details_validation
from finance.models import Bank
from finance.serializers import BankSerializer


class BankDetailsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BankSerializer

    def get(self, request):
        try:
            queryset = Bank.objects.get(pk=request.user.active_business.bank.pk)
        except Bank.DoesNotExist:
            return Response(data={})

        serializer = self.serializer_class(queryset)
        return Response(data=serializer.data)

    def post(self, request):
        data = {
            'bank_name': request.data.get('bank_name'),
            'account_number': request.data.get('account_number')
        }
        serializer = bank_details_validation(request.user.active_business.pk, data)
        bank = serializer.save()

        business = Business.objects.get(pk=request.user.active_business.pk)
        business.bank = bank
        business.save()

        return Response(data=serializer.data)

    def put(self, request):
        data = {
            'bank_name': request.data.get('bank_name'),
            'account_number': request.data.get('account_number')
        }
        serializer = bank_details_validation(request.user.active_business.pk, data)
        serializer.save()

        return Response(data=serializer.data)
