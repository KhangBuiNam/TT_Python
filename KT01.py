import os
os.system('cls')

EVEN=[]
ODD=[]
while True:
    a=int(input("Enter some integer: "))
    if 8 <= a <= 10:
        print (' Good')
    elif 5<= a < 8:
        print ('Normal')
    elif 0<=a<5 :
        print ( 'Bad')
    elif a==-1 :
        break
    else: print ('Wrong')
    f_even = (a % 2==0)
    if f_even:
        EVEN.append(a)
    else: 
        ODD.append(a)
print ("Even integer: ",EVEN)
print ("ODD integer: ",ODD)