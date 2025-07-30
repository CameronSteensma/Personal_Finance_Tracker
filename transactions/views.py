from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Transaction
from .forms import TransactionForm
from .charts import generate_monthly_spending_chart

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    total_income = float(sum(t.amount for t in transactions if t.transaction_type == 'INCOME'))
    total_expenses = float(sum(t.amount for t in transactions if t.transaction_type == 'EXPENSE'))
    balance = total_income - total_expenses
    
    return render(request, 'transactions/transaction_list.html', {
        'transactions': transactions,
        'total_income': total_income,
        'total_expenses': total_expenses,
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

def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/edit_transaction.html', {'form': form, 'transaction': transaction})

def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transactions/delete_transaction.html', {'transaction': transaction})

def reports_view(request):
    transactions = Transaction.objects.all()
    generate_monthly_spending_chart(transactions)
    return render(request, 'transactions/reports.html')


    

