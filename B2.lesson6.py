#Bt5
sum = 0
n = int(input("Nhập N:"))
for i in range(1,n+1,1):
    sum = sum+i
    print(i)
print("kết quả:"+str(sum))
print("TBC:"+str(sum/n))