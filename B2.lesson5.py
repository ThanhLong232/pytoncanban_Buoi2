#BT4
sumle = 0
n = int(input("Nhập N:"))
for i in range(1,n+1,1):
    if i%2!=0:
        sumle = sumle+i
        print(i)
print("kết quả:"+str(sumle))