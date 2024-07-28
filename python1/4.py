

#above half of even line is ok
def draw_pattern(size):
    half_size=(size//2)+1
    con1,con2,con3,con4=0,1,1,0


    for i in range(size):
        even_line=""
        odd_line=""

        if i == 0 or i== size-1:
            print("#"*size)
        elif i % 2 == 1 and i<half_size:
            even_line+="#."*con2
            even_line+="."*(size-(4+con1))
            even_line+=".#"*con2
            print(even_line)
            con1+=4
            con2+=1
        elif i%2==0 and i<half_size:
            odd_line+="#."*con3
            odd_line+="#"*(size-(4+con4))
            odd_line+=".#"*con3
            print(odd_line)
            odd_line=""
            if i == size//2:
                continue
            con3+=1
            con4+=4


        elif i % 2 == 1 and i>=half_size:
            # print(con1)
            con2-=1
            con1-=4
            # print(con2)
            even_line+="#."*con2
            even_line+="."*(size-(4+con1))
            even_line+=".#"*con2
            print(even_line)
            
            
        elif i%2==0 and i>=half_size:
            
            con3-=1
            
            con4-=4
            odd_line+="#."*con3
            odd_line+="#"*(size-(4+con4))
            odd_line+=".#"*con3
            print(odd_line)
            odd_line=""

print("*** Fun with Drawing ***")
size = 4*(int(input("Enter input : ")))-3 

draw_pattern(size)

