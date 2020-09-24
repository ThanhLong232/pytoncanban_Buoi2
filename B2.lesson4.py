#BT3
sumchan = 0
n = int(input("Nhập N:"))
for i in range(1,n+1,1):
    if i%2==0:
        sumchan = sumchan+i
        print(i)
print("kết quả:"+str(sumchan))


