from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Transaction
from .forms import TransactionForm
from .charts import generate_monthly_spending_chart
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('transaction_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'transactions/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')
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
    
@login_required
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})

@login_required
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

@login_required
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transactions/delete_transaction.html', {'transaction': transaction})

@login_required
def reports_view(request):
    transactions = Transaction.objects.all()
    generate_monthly_spending_chart(transactions)
    return render(request, 'transactions/reports.html')

def admin_view(request):
    return render(request, 'transactions/admin_view.html')

def accounts_view(request):
    return render(request, 'transactions/accounts.html')

def users_view(request):
    return render(request, 'transactions/users.html')

