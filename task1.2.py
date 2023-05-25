# Дан список. Вывести отдельно буквы и цифры, пользуясь filter.
# [12, 'sadf', 5643] =>['sadf'], [12,5643]

list_2 = [12, 'sadf', 5643]

res_list_2 = list(filter(lambda x: type (x) == int, list_2))
res_list_3 = list ( filter ( lambda x: type(x) != int, list_2))

print (res_list_2, res_list_3)