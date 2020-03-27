from finance.models import Bank
from finance.serializers import BankSerializer


def bank_details_validation(business_id, form_data):
    try:
        queryset = Bank.objects.get(pk=business_id)
    except Bank.DoesNotExist:
        queryset = None

    data = {
        'bank_name': form_data.get('bank_name'),
        'account_number': form_data.get('account_number')
    }
    serializer = BankSerializer(queryset, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer
