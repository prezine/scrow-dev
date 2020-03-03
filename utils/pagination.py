from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 1_000_000_000

    def get_paginated_response(self, data):
        current_page = 1

        for i in self.page.paginator.page_range:
            if self.page.number == i:
                current_page = i

        return Response({
            'pagination': {
                'count': self.page.paginator.count,
                'per_page': self.page_size,
                'total': self.page.paginator.num_pages,
                'from': self.page.paginator.page_range[0],
                'to': self.page.paginator.num_pages,
                'current_page': current_page,
                'last_page': self.page.paginator.num_pages,
            },
            'results': data,
        })
