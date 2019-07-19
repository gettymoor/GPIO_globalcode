def is_even(x):
    if x % 2 is 0:
        return True
    else:
        return False
  
num = [1,56,234,87,4,76,24,69,90,135]

N = list(filter(is_even,num))

#N = list(map(is_even,num))
print("is_even: " ,N)

S = list(filter(lambda x : x % 2 is 0, num))

print ("lambda: " , S)