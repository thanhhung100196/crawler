# tasks.py
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def crawl_task(url):
    # Import the crawl function and execute it
    from crawler import crawl
    crawl(url)