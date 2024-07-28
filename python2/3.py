
print('*** Odd Even ***')
type, data, mode = input("Enter Input : ").split(',')

def odd_even(type, data, mode):
    if type == "S":
        if mode == 'Odd':
            return data[0::2]
        elif mode == 'Even':
            return data[1::2]
    
    elif type == "L":
       
        big_list = data.split()
        
        if mode == 'Odd':
            return [big_list[i] for i in range(0, len(big_list), 2)]
        elif mode == 'Even':
            return [big_list[i] for i in range(1, len(big_list), 2)]


print(odd_even(type, data, mode))
