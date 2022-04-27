hello_world="hello world"

def call(numeracja):
    print(str(numeracja) +" "+ hello_world)


absolut=-100
def Z():
    result=abs(absolut)
    print (abs(absolut))
    
Z()
for num in range (11):
    if (num % 2) == 0:    
        call(num)
    else:
        print("NIE MA")    