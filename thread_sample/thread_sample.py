import threading
import time

# GIL이 있기 때문에 multithreading을 해도 시간상의 성능 향상은 기대하기 어렵다

# 전역 변수
# 공유 자원(shared resource)
# 데이터 영역이나 힙 영역에 있다면 모든 스레드에서 접근 및 수정 가능

li = [i+1 for i in range(80000)]
n = 80000
offset = n//4  # 250

start = time.time()
for i in range(1000):
    li[i]*=2
elapsed = time.time() - start
print(f"elaspsed time: {elapsed}")

# def thread_main(li, n):
#     for idx in range(offset*n, offset*(n+1)):
#         li[idx] *= 2

# # 스레드를 담아둘 리스트
# threads = []

# for i in range(4):
#     th = threading.Thread(target=thread_main, args=(li, i))
#     threads.append(th)

# start = time.time()
# # 스레드가 1개 --> 5개
# for th in threads:
#     th.start()

# for th in threads:
#     th.join()
# elapsed = time.time() - start

# print(f'elapsed : {elapsed}')