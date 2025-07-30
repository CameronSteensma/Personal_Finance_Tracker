from django.shortcuts import render

# Create your views here.
from .models import Transactions

def transaction_list(request):
    transactions = Transactions.objects.all().order_by('-date')
    total_income = float(sum(t.amount for t in transactions if t.transaction_type == 'INCOME'))
    total_expense = float(sum(t.amount for t in transactions if t.transaction_type == 'EXPENSE'))
    balance = total_income - total_expense
    
    return render(request, 'transactions/transaction_list.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
    })