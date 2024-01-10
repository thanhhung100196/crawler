# tasks.py
from celery import Celery

app = Celery('tasks', broker='pyamqp://crowd:crowd123@rabbit:5672//')

@app.task
def crawl_task(url):
    # Import the crawl function and execute it
    from crawler import crawl
    crawl(url)