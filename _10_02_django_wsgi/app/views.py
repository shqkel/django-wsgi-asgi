import os
import threading
import time
from datetime import datetime

from django.http import HttpResponse


"""
django wsgi application
A. 내장서버 python manage.py runserver
    1. single process, single thread : --nothreading 옵션으로 실행
    2. single process, multi thread :(기본값) python manage.py runserver --threaded
    3. multi process 미지원
B. Gunicorn 또는 uWSGI
    1. multi process, single thread : CPU bound 작업에 적합 (thread=1~2) work_class='sync'
        - gunicorn --workers=4 --threads=1 
    2. multi process, multi thread : I/O bound 작업에 적합 (thread=2~4) work_class='gevent' | 'gthread'
        - gunicorn --workers=4 --threads=4 
"""


def index(request):
    thread_native_id = threading.get_native_id()
    thread_name = threading.current_thread().name
    request = f"Requested at {datetime.now()} by PID {os.getpid()} ({thread_native_id}-{thread_name})"
    print(request)

    time.sleep(3)
    return HttpResponse(f"Responsed at {datetime.now()} by PID {os.getpid()} ({thread_native_id}-{thread_name})")
