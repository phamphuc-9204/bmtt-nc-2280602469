#Nhập số từ người dùng
so = int(input("Nhập một số nguyên: "))
#Kiểm tra số chẵn
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "Không phải là số chẵn.")