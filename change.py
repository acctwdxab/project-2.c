print("Please enter an amount in cents less than a dollar.")
num = int(input())
print("Your change will be:")
resultQ=num//25
resultD=(num%25)//10
resultN=(num%25)%10//5
resultP=((num%25)%10)%5
print("Q: ", resultQ)
print("D: ", resultD)
print("N: ", resultN)
print("P: ", resultP)