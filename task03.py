import timeit
import os

from alg_bm import boyer_moore_search
from alg_kmp import kmp_search
from alg_rk import rabin_karp_search

# Завантаження текстових файлів
file1_path = "article1.txt"
file2_path = "article2.txt"

with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    text1 = file1.read()
    text2 = file2.read()

# Підрядки для пошуку (один, що дійсно існує в тексті, і один вигаданий)

existing_pattern_1 = "реалізації відомих алгоритмів"
existing_pattern_2 = "побудова рекомендаційних систем"
fictional_pattern = "lorem ipsum dolor sit amet"

# Вимірюємо час виконання кожного алгоритму для тексту 1 та обох підрядків
bm_t1_ex = timeit.timeit(lambda: boyer_moore_search(text1, existing_pattern_1), number=10)
bm_t1_fc = timeit.timeit(lambda: boyer_moore_search(text1, fictional_pattern), number=10)

kmp_t1_ex = timeit.timeit(lambda: kmp_search(text1, existing_pattern_1), number=10)
kmp_t1_fc = timeit.timeit(lambda: kmp_search(text1, fictional_pattern), number=10)

rk_t1_ex = timeit.timeit(lambda: rabin_karp_search(text1, existing_pattern_1), number=10)
rk_t1_fc = timeit.timeit(lambda: rabin_karp_search(text1, fictional_pattern), number=10)

#print("Алгоритм Боєра-Мура для тексту 1 (існуючий підрядок):", bm_t1_ex)
#print("Алгоритм Боєра-Мура для тексту 1 (вигаданий підрядок):", bm_t1_fc)

#print("Алгоритм Кнута-Морріса-Пратта для тексту 1 (існуючий підрядок):", kmp_t1_ex)
#print("Алгоритм Кнута-Морріса-Пратта для тексту 1 (вигаданий підрядок):", kmp_t1_fc)

#print("Алгоритм Рабіна-Карпа для тексту 1 (існуючий підрядок):", rk_t1_ex)
#print("Алгоритм Рабіна-Карпа для тексту 1 (вигаданий підрядок):", rk_t1_fc)

# Вимірюємо час виконання кожного алгоритму для тексту 2 та обох підрядків
bm_t2_ex = timeit.timeit(lambda: boyer_moore_search(text2, existing_pattern_2), number=10)
bm_t2_fc = timeit.timeit(lambda: boyer_moore_search(text2, fictional_pattern), number=10)

kmp_t2_ex = timeit.timeit(lambda: kmp_search(text2, existing_pattern_2), number=10)
kmp_t2_fc = timeit.timeit(lambda: kmp_search(text2, fictional_pattern), number=10)

rk_t2_ex = timeit.timeit(lambda: rabin_karp_search(text2, existing_pattern_2), number=10)
rk_t2_fc = timeit.timeit(lambda: rabin_karp_search(text2, fictional_pattern), number=10)

#print("Алгоритм Боєра-Мура для тексту 2 (існуючий підрядок):", bm_t2_ex)
#print("Алгоритм Боєра-Мура для тексту 2 (вигаданий підрядок):", bm_t2_fc)

#print("Алгоритм Кнута-Морріса-Пратта для тексту 2 (існуючий підрядок):", kmp_t2_ex)
#print("Алгоритм Кнута-Морріса-Пратта для тексту 2 (вигаданий підрядок):", kmp_t2_fc)

#print("Алгоритм Рабіна-Карпа для тексту 2 (існуючий підрядок):", rk_t2_ex)
#print("Алгоритм Рабіна-Карпа для тексту 2 (вигаданий підрядок):", rk_t2_fc)

print(f"{'| Algorithm': <24} | {'T1 - Time Existing': <20} | {'T1 - Time Fictional': <20} | {'T2 - Time Existing': <20} | {'T2 - Time Fictional': <20}")
print(f"|{'-'*23} | {'-'*20} | {'-'*20} | {'-'*20} | {'-'*20}")
print(f"{'| Боєра-Мура': <24} | {bm_t1_ex:<20.5f} | {bm_t1_fc:<20.5f} | {bm_t2_ex:<20.5f} | {bm_t2_fc:<20.5f}")
print(f"{'| Кнута-Морріса-Пратта': <24} | {kmp_t1_ex:<20.5f} | {kmp_t1_fc:<20.5f} | {kmp_t2_ex:<20.5f} | {kmp_t2_fc:<20.5f}")
print(f"{'| Рабіна-Карпа': <24} | {rk_t1_ex:<20.5f} | {rk_t1_fc:<20.5f} | {rk_t2_ex:<20.5f} | {rk_t2_fc:<20.5f}")
