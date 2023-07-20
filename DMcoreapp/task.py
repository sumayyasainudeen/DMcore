# myapp/tasks.py
from celery.task import periodic_task
from datetime import datetime, time
from myapp.views import my_view

@periodic_task(run_every=(crontab(hour=0, minute=0)))  # Schedule to run every day at midnight
def run_my_view():
    now = datetime.now().time()
    target_time = time(21, 34)  # Set the desired time for the view function to run
    if now >= target_time:
        
        auto_assign()