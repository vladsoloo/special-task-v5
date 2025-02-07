def alternating_sum(n):
    S = 0
    sign = 1  
    for i in range(1, n + 1):
        S += sign * (1 / i)
        sign *= -1  
    return S

n = 10 
result = alternating_sum(n)
print(result)
