from django.shortcuts import render, redirect

# Create your views here.
from .models import Transactions
from .forms import TransactionForm

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
    
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})