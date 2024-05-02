fp1=open('user.txt','r')
data=fp1.read()
print(data)

fp2=open('emp.txt','w')
fp2.write(data)

print("Written Successfully")

fp1.close()
fp2.close()