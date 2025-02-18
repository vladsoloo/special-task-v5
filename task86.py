def square_by_pattern(n):
    result = 0
    for i in range(n):
        result += 2*i + 1
    return result


n = 4
print(f"{n}² = ", end="")
for i in range(n):
    print(f"{2*i + 1}", end=" + " if i < n-1 else "")
print(f" = {square_by_pattern(n)}")
