
print("*** multiplication or sum ***")

number_input=input("Enter num1 num2 : ")
number1_input,number2_input=number_input.split()

number1_int=int(number1_input)
number2_int=int(number2_input)

# print(number1_int)
# print(number2_int)

def multi_or_sum(number1_int,number2_int):
    if number1_int*number2_int>1000:
        return number1_int+number2_int
    else:
        return number1_int*number2_int


print(f"The result is {multi_or_sum(number1_int,number2_int)}")
