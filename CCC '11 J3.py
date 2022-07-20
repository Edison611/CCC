n1 = int(input())
n2 = int(input())

nums = 2
def sumac(a,b,nums):
    if b > a:
        return nums
    return sumac(b,a-b,nums+1)
print(sumac(n1,n2,nums))
