import asyncio
import os
import threading
from datetime import datetime

from django.http import HttpResponse


async def index(request):
    thread_id = threading.get_ident()
    thread_native_id = threading.get_native_id()
    thread_name = threading.current_thread().name
    request = f"Requested at {datetime.now()} by {os.getpid()} ({thread_id}-{thread_native_id}-{thread_name})"
    print(request)
    await asyncio.sleep(3)  # 3초 대기(논블로킹)
    return HttpResponse(f"[Async] Responsed at {datetime.now()} by {os.getpid()} ({thread_id}-{thread_native_id}-{thread_name})")
