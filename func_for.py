import time
import celery

app_celery = celery.Celery(
    'app',
    backend='redis://localhost:6379/2',
    broker='redis://localhost:6379/1'
)


@app_celery.task()
def func_toy(a, b):
    time.sleep(1)
    return a + b
