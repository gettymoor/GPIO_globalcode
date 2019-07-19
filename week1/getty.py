asterisk = "*"
k = 5
for a in range(1,k):
    l = asterisk * a
    print(l)
while k > 0:
    k = k - 1
    d = asterisk * k
    print(d)




def may(number):
    s=0
    while(s<number):
        
        print("****")
        s=s+1
may(8)


print("###############")


def find_char(a):
    for m in "mayor":
        if(m==a):
            break
        
    print(m==a)
find_char("f")
    