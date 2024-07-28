

class translator:
    def __init__(self):
        self.decimal=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        self.roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        self.roman_mix=[]
        self.deci_mix=0
    def deciToRoman(self,num):    
        for dec in range(len(self.decimal)):
            count=num//self.decimal[dec]
            if num//self.decimal[dec]>0:
                self.roman_mix.extend([self.roman[dec]]*count)
                num-=self.decimal[dec]*count
        return f"{''.join(self.roman_mix)}"
    def romanToDeci(self, s):
        if len(s)==1:
            self.deci_mix+=self.decimal[self.roman.index(s)]
            return self.deci_mix
        else:
            for first_str in range(len(s)-1):
                second_str=first_str+1
                if self.roman.index(s[first_str])<=self.roman.index(s[second_str]):
                 self.deci_mix+=self.decimal[self.roman.index(s[first_str])]
                elif self.roman.index(s[first_str])>self.roman.index(s[second_str]):
                    self.deci_mix+=(self.decimal[self.roman.index(s[second_str])]-self.decimal[self.roman.index(s[first_str])])-self.decimal[self.roman.index(s[second_str])]
                   
        self.deci_mix+=self.decimal[self.roman.index(s[second_str])]
        return self.deci_mix

num = int(input("Enter number to translate : "))
print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))