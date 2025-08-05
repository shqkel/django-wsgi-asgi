import requests # pip install requests
from concurrent.futures import ThreadPoolExecutor

def make_request():
    response = requests.get("http://127.0.0.1:8000/app/")
    print(response.text)

# 동시요청 보내기
threads_num = 5
with ThreadPoolExecutor(max_workers=threads_num) as executor:
    futures = [executor.submit(make_request) for _ in range(threads_num)]