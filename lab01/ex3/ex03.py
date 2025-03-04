def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập các phần tử cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List được tạo là:", numbers)
print("Tuple được tạo là:", my_tuple)