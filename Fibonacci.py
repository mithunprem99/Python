num1=1
num2=2
even =2

while num2 <= 4000000 :
    num1=num2
    num2=num1+num2
if (num2 % 2== 0):
  even= even+num2
  print(even)
