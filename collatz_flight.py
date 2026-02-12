import matplotlib.pyplot as plt
def collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence
# Числа для порівняння
numbers_to_test = [27, 26]
plt.figure(figsize=(12, 6))
for num in numbers_to_test:
    seq = collatz_sequence(num)
    steps = range(len(seq))
        # Малюємо графік
    plt.plot(steps, seq, marker='.', label=f'Число {num} (Кроків: {len(seq)-1}, Макс: {max(seq)})')
# Оформлення
plt.title("Політ «чисел-градин» (Гіпотеза Коллатца)")
plt.xlabel("Кількість кроків")
plt.ylabel("Значення числа")
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
# Додамо анотацію
seq_27 = collatz_sequence(27)
peak_val = max(seq_27)
peak_idx = seq_27.index(peak_val)
plt.annotate(f'Пік: {peak_val}', xy=(peak_idx, peak_val), xytext=(peak_idx+5, peak_val),
             arrowprops 
=dict(facecolor='black', shrink=0.05))
plt.show()
