def swipe(n):
    # 先定义递归函数来实现从后到前和从前到后的打印
    def recursive_print(n):
        if n < 10:  # 基准条件: 当n只有一位数时
            print(n)
        else:
            print(n % 10)  # 打印最后一位
            recursive_print(n // 10)  # 递归调用处理剩余的数字
            print(n % 10)  # 回溯时再次打印该位数字

    # 开始递归
    recursive_print(n)

    def is_odd (n):
       if n%2==0:
        return False
       else:
          return True
    
    
    
def is_odd(n):
    return n % 2 != 0
def is_prime(n):
    return n%2!=0

def skip(n):
    if is_odd(n):
        def skip_odd(n):
            if n == 1:
                return 1
            else:
                return n * skip_odd(n - 2)
        return skip_odd(n)
    else:
        def skip_even(n):
            if n == 2:
                return 2
            else:
                return n * skip_even(n - 2)
        return skip_even(n)
    a=skip(8)
    a
def isprime(n):
    divisor=1
    def is_prime(n, divisor=2):
    # 基本情况1：如果 divisor 的平方大于 n，说明 n 是素数
     if divisor * divisor > n:
        return True
    # 基本情况2：如果 n 能被 divisor 整除，说明 n 不是素数
    if n % divisor == 0:
        return False
    # 递归情况：检查下一个可能的除数
    return is_prime(n, divisor + 1)
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def check_all(i):
        "Check whether no number from i up to n evenly divides n."
        if i == n:      # could be replaced with i > (n ** 0.5)
            return True
        elif n % i == 0:
            return False
        return check_all(i + 1)
    return check_all(2)
    print("ehh")
# 测试用例
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(17)) # True
print(is_prime(20)) # False
steps=0
def hailstone(n):
    global steps
    if n==1:
        return steps
    elif is_odd:
        n=3*n+1 
        print("n")
    else:
        n//=2
        print("n")
    steps+=1
    return hailstone(n)



        

             
          


        

          