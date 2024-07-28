
print("*** Rabbit & Turtle ***")
inputs = input("Enter Input : ").split()

d = round(float(inputs[0]), 2)
vr = round(float(inputs[1]), 2)
vt = round(float(inputs[2]), 2)
vf = round(float(inputs[3]), 2)




def fly_dis(d,vr,vt,vf):
    t=d/(vt-vr)

    return t*vf


result=fly_dis(d,vr,vt,vf)
print(f"{result:.2f}")