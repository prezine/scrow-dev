from django.shortcuts import render


def transaction_index_view(request):
    return render(request, 'transactions/index.html')
