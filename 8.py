
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (60, 70, 80, 90, 100)
max_value = max(tuple1)
min_value = min(tuple1)
print(f"Maximum value in tuple1: {max_value}")
print(f"Minimum value in tuple1: {min_value}")
sum_tuples = tuple(sum(x) for x in zip(tuple1, tuple2))
print(f"Sum of tuple1 and tuple2: {sum_tuples}")
duplicated_tuple = tuple1 * 2
print(f"Duplicated tuple: {duplicated_tuple}")
sliced_tuple = tuple1[1:4]
print(f"Sliced tuple: {sliced_tuple}")
list_from_tuple = list(tuple1)
print(f"List from tuple1: {list_from_tuple}")
