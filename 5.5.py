print("ĐẬU THẾ HOÀNG")
print("MSSV:235752021610017")
import sequential_search

n = int(input("Nhập số lượng phần tử: "))
dlist = []
for i in range(n):
  element = int(input(f"Nhập phần tử thứ {i+1}: "))
  dlist.append(element)

item = int(input("Nhập phần tử cần tìm: "))

result, index = sequential_search.sequential_search(dlist, item)

if result:
  print(f"Phần tử {item} được tìm thấy tại vị trí {index}")
else:
  print(f"Không tìm thấy phần tử {item}")
