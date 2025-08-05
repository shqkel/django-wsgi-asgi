import os
import threading
import time
from datetime import datetime

from django.http import HttpResponse
import asyncio


# 동기 view
def sync_view(request):
    thread_id = threading.get_ident()
    thread_native_id = threading.get_native_id()
    thread_name = threading.current_thread().name
    request = f"Requested at {datetime.now()} by {os.getpid()} ({thread_id}-{thread_native_id}-{thread_name})"
    print(request)
    time.sleep(3)  # 3초 정지(블로킹)
    return HttpResponse(f"[Sync] Responsed at {datetime.now()} by {os.getpid()} ({thread_id}-{thread_native_id}-{thread_name})")


# 비동기 view
async def async_view(request):
    thread_id = threading.get_ident()
    thread_native_id = threading.get_native_id()
    thread_name = threading.current_thread().name
    request = f"Requested at {datetime.now()} by {os.getpid()} ({thread_id}-{thread_native_id}-{thread_name})"
    print(request)
    await asyncio.sleep(3)  # 3초 대기(논블로킹)
    return HttpResponse(f"[Async] Responsed at {datetime.now()} by {os.getpid()} ({thread_id}-{thread_native_id}-{thread_name})")
