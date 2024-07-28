

num=input("Enter Your List : ").split()
to_int=[int(i) for i in num]
newlist=[]
amount=len(to_int)



def check_to_zero(amount):
    if amount>=3:
        for first in range(amount-2):
            second=first+1

            for second in range(second,amount-1):    
                third=second+1
                for third in range(third,amount):
                 if to_int[first]+to_int[second]+to_int[third] == 0 and [to_int[first],to_int[second],to_int[third]] not in newlist:
                     newlist.append([to_int[first],to_int[second],to_int[third]])
    else:
        return f"Array Input Length Must More Than 2"
    return newlist
    
print(check_to_zero(amount))






