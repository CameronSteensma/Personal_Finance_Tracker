from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'transaction_type', 'category', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'transaction_type': forms.Select(choices=[('INCOME', 'Income'), ('EXPENSE', 'Expense')]),
        }
        