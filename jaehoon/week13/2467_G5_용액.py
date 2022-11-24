import sys 

def solution(lst,N):
    left,right = 0,N-1
    left_val, right_val = lst[left], lst[right]
    min_val = abs(left_val + right_val)

    while left<right:
        val = lst[left] + lst[right]

        if abs(val) < min_val:
            min_val = abs(val)
            left_val = lst[left]
            right_val = lst[right]

        if val < 0:
            left += 1
        elif val > 0:
            right -= 1
        elif val == 0:
            break
    
    print(left_val, right_val)

if __name__ == "__main__":
    N = int(input())
    lst = list(map(int,sys.stdin.readline().split()))
    solution(lst,N)