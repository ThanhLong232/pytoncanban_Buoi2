sum = 0
n = int(input("Nhập N:"))
for i in range(1,n+1,1):
    if i==13:
        continue
    sum = sum+i
    print(i)
print("kết quả:"+str(sum))
print("TBC:"+str(sum/n))