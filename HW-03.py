inv_sum = input ("please write a sum which you planed to invest for deposit: ")
list_of_inv_sum = inv_sum.split()
list_of_numbers = list(map(int, list_of_inv_sum))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
x0 = per_cent['ТКБ']
x1 = per_cent['СКБ']
x2 = per_cent['ВТБ']
x3 = per_cent['СБЕР']
depo_0 = list_of_numbers[0] * (x0 / 100)
depo_1 = list_of_numbers[0] * (x1 / 100)
depo_2 = list_of_numbers[0] * (x2 / 100)
depo_3 = list_of_numbers[0] * (x3 / 100)
list_delta_depos = [depo_0, depo_1, depo_2, depo_3]
print(list_delta_depos)

max_number = max(list_delta_depos)
print("Наибольшее число:", max_number)