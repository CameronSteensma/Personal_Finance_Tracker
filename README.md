Finance Tracker

A web application to track income and expenses, view spending trends, and manage financial transactions.

Tech Stack

Backend: Django (Python)
Frontend: Django Templates + Bootstrap 5
Database: SQLite (development) / PostgreSQL (production-ready)
Styling: Bootstrap 5 for responsive UI
Icons & Branding: Custom favicon
Version Control: Git & GitHub

Features

Add, Edit, and Delete Transactions: Manage income & expenses in an intuitive UI.
Category Management: Categorize transactions for better insights.
Dynamic Charts: Visual representation of monthly spending trends using Matplotlib.
Responsive Design: Works across desktop and mobile devices.
Secure Forms: CSRF protection enabled on all forms.
Error Handling: Friendly error pages for missing routes and invalid inputs.

Best Practices Implemented

Separation of Concerns: Clear separation between views, models, and templates.
Static Files Management: Proper use of Django static files for favicon, CSS, and images.
Environment Variables: Sensitive settings (e.g., secret keys, database URLs) stored in .env.
Modular Templates: Reusable templates for layout consistency across pages.
Git Workflow: Meaningful commit messages and version history.
DRY Principle: Reduced code duplication in templates and views.


---------- HOW TO SETUP ------------

1. Clone the repository

   git clone https://github.com/YOUR_USERNAME/finance-tracker.git
   
   cd finance-tracker

3. Create virtual environment

   python -m venv venv

   source venv/bin/activate   # On macOS/Linux

   venv\Scripts\activate      # On Windows

4. Install dependencies

   pip install -r requirements.txt

5. Configure environment variables

.env file in project root:
 
  SECRET_KEY=your_secret_key_here
  
  DEBUG=True
  
  DATABASE_URL=sqlite:///db.sqlite3

6. Run migrations
7. Start the server

   python manage.py runserver

