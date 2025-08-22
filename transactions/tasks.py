from celery import shared_task
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from .models import Transaction

@shared_task
def process_recurring_transactions():
    today = date.today()
    recurring_transactions = Transaction.objects.filter(
        is_recurring=True,
        next_payment_date__lte=today
    )
    for transaction in recurring_transactions:
        transaction.objects.create(
            title=transaction.title,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type,
            category=transaction.category,
            date=today,
            is_recurring=transaction.is_recurring,
        )
        
        # update next occurrence
        if transaction.frequency == 'DAILY':
            transaction.next_occurrence+= timedelta(days=1)
        elif transaction.frequency == 'WEEKLY':
            transaction.next_occurrence += timedelta(weeks=1)
        elif transaction.frequency == 'BIWEEKLY':
            transaction.next_occurrence += timedelta(weeks=2)
        elif transaction.frequency == 'MONTHLY':
            transaction.next_occurrence += relativedelta(months=1)
        elif transaction.frequency == 'YEARLY':
            transaction.next_occurrence += relativedelta(years=1)
        transaction.save()