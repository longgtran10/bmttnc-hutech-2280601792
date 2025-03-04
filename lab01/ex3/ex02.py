def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập các phần tử cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
reversed_list = dao_nguoc_list(numbers)
print("List sau khi đảo ngược là:", reversed_list)
