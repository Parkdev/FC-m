import random

def quick_sort(li, start, end):
    if start >= end:
        return

    left = start
    right=end
    pivot=li[(start + end)//2]

    while left <= right:
        while li[left] < pivot:
            left +=1

        while li[right] > pivot:
            right -=1

        if left <= right:
            li[left], li[right] = li[right], li[left]
            left+=1
            right-=1

    quick_sort(li, start, right)
    quick_sort(li, left, end)

if __name__ == "__main__":
    while True:
        num_data=int(input("데이터 개수(종료:0):"))
        if not num_data:
            break
        data = random.radient