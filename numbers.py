list1 =[g for g in range(1,50)]
print("main:",list1)
print("\n")

list =[t for t in list1 if t%2==1]
print("odd:",list)
print("\n")

list3 =[l for l in list1 if l%2==0]
print("even:",list3)
print("\n")


'''if num > 1:
       for i in range(2,num):
           if (num % i) == 0:'''
