from collections import defaultdict
from datetime import datetime
from .models import Transaction

def get_monthly_category_summary(transactions):
    # fetch all transaction objects
    transactions = Transaction.objects.all()
    # create a dictionary to hold the summary
    monthly_summary = defaultdict(lambda: defaultdict(float))
    
    for transaction in transactions:
        month = transaction.date.strftime('%Y-%m')
        amount = float(transaction.amount)
        monthly_summary[month][transaction.category] += amount if transaction.transaction_type == 'INCOME' else -amount

    return monthly_summary