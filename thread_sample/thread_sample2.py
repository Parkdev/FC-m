import threading
# 공유 자원
g_num = 0

def thread_main():
    global g_num
    for _ in range(100000):
        g_num += 1

threads = []

for i in range(50):
    threads.append(threading.Thread(target=thread_main))

for th in threads:
    th.start()

for th in threads:
    th.join()

print(f'result : {g_num:,}')