В таблиці нижче представлен час пошуку використовуючи 3 алгоритми.

Ми шукали 2 рядки які існують у текстах та рядок якого не існує.

У всіх випадках алгоритм Боєра-Мура виявився Самим швидким серед використаних алгоритмів.

Інші 2 алгоритми виявились занадто повільними у випадку з не існуючими рядком.

| Algorithm              | T1 - Time Existing   | T1 - Time Fictional  | T2 - Time Existing   | T2 - Time Fictional 
|----------------------- | -------------------- | -------------------- | -------------------- | --------------------
| Боєра-Мура             | 0.00093              | 0.00208              | 0.00149              | 0.00325             
| Кнута-Морріса-Пратта   | 0.00426              | 0.01608              | 0.00599              | 0.02018             
| Рабіна-Карпа           | 0.00936              | 0.03972              | 0.01441              | 0.06192          