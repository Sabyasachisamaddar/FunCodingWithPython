def getMissingNumber(list):
    sum = 0
    size = len(list)
    ac_sum = (size * (size +1) )/2
    for i in list:
        sum = sum + i    
    return (ac_sum - sum)


n = int(input("Please enter the limit of the range :"))
mn = int(input("Please enter the missing number :"))

#Creating the List
list = []

for i in range(n+1):
   if(i != mn): 
       list.append(i)
       
print(list)
value = getMissingNumber(list)
print('Missing Number is '+ str(int(value)))

