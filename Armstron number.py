#test weather the given number is an armstron number or not
num=input()
number=int(num)
sum=0
digit=0
length=len(num)
num1=int(num)
print(length)
for i in range(length):
  digit=num1%10
  num1=num1//10
  sum+=pow(digit,length)
if sum==number:
  print("its an armstrong number")
else:
  print("not an armstron number")
