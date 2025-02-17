import math

def generate_sequence(k, n):
    sequence = []
    current_value = 1
    while len(sequence) < n:
        next_value = current_value + 1 / k
        sequence.append(next_value)
        current_value = next_value
    return sequence[:n]

k = 1
n = 5
result = generate_sequence(k, n)
print("Последовательность из {} чисел: {}".format(n, result))
