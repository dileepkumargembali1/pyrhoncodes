# method1
#reverse of the string using simple iterations
num=int(input())
dummy=num
reverse=0
while num>0:
  remainder=num%10
  reverse=(reverse*10)+remainder
  num=num//10
print(f"revers of a number is {reverse}")
