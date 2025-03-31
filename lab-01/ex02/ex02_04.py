#Tạo danh sách (List)
j=[]
#Duyệt 2000 -> 3200, kiểm tra chia hết cho 7 và bội số của 5
for i in range(2000,3201):
    if(i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))