# producer.py
from tasks import crawl_task

# Push a URL to the task queue
crawl_task.delay('https://znews.vn/')