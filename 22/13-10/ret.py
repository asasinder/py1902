number = int (input("Enter the number: "))
sum = (number // 1000) + (number // 10 // 10 // 10 % 10) + (number // 10 // 10 % 10)  + (number // 10 % 10) + (number % 10)
mul = (number // 1000) * (number // 10 // 10 // 10 % 10) * (number // 10 // 10 % 10)  * (number // 10 % 10) * (number % 10)
print(sum,',',mul)
