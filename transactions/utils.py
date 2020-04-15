from django.core.paginator import Paginator
from django.utils import dateparse


def validate_and_return_delivery_date(product_data):
    try:
        product_data['delivery_date'] = dateparse.parse_datetime(
            product_data.get('delivery_date')).date()
    except ValueError:
        del product_data['delivery_date']

    return product_data


def pagination(request_obj, model_instance, data_per_page):
    paginator = Paginator(model_instance, data_per_page)  # Show 25 contacts per page.

    page_number = request_obj.GET.get('page')
    return paginator.get_page(page_number)
