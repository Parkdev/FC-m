import time

# recursion
def func(a):
    time.sleep(0.1)
    func(a-1)

func(10)

