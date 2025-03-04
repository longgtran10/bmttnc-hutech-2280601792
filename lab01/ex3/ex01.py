def tinh_tong_so_chan(lst):
    return sum([x for x in lst if x % 2 == 0])
input_list = input("Nhập các phần tử cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print("tong cac so chan la:", tong_chan) 