import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .reports import get_monthly_category_summary
from collections import defaultdict
from django.conf import settings

def generate_monthly_spending_chart(transactions):
    monthly_summary = defaultdict(lambda: defaultdict(float))
    
    for t in transactions:
        month = t.date.strftime('%Y-%m')
        amount = float(t.amount)
        category_name = str(t.category)
        monthly_summary[month][category_name] += amount if t.transaction_type == 'INCOME' else -amount
        
    # Convert the summary to a DataFrame
    data = []
    for month, categories in monthly_summary.items():
        row = {'Month': month}
        row.update(categories)
        data.append(row)
    df = pd.DataFrame(data).fillna(0)
    
    if df.empty:
        print("No data available for chart generation.")
        return
    
    # Melt the DataFrame for seaborn
    df_melted = df.melt(id_vars='Month', var_name='Category', value_name='Amount')
    
    # Plot
    plt.figure(figsize=(10,6))
    sns.barplot(data=df_melted, x='Month', y='Amount', hue='Category')
    plt.title('Monthly Spending by Category')
    plt.ylabel('Amount ($)')
    plt.xlabel('Month')
    plt.legend(title='Category')
    plt.tight_layout()
    
    # Ensure the static directory exists
    charts_dir = os.path.join(settings.BASE_DIR, 'static', 'charts')
    os.makedirs(charts_dir, exist_ok=True)
    
    
    # Save the plot to a static folder (for web display)
    filepath = os.path.join(charts_dir, 'monthly_spending_chart.png')
    plt.savefig(filepath)
    print(f"Chart saved to {filepath}")
    plt.close()