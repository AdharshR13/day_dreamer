import random

print("Hi ! Welcome to TIC TAC TOE")

k='''
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
------------- '''

print(k)


score=0
cscore=0
#hello
#hihello
#world
#winning combinations
set1={'1','2','3'}
set2={'4','5','6'}
set3={'7','8','9'}
set4={'1','5','9'}
set5={'1','4','7'}
set6={'2','5','8'}
set7={'3','6','9'}
set8={'3','5','7'}


def s1(s):
    s=s.intersection(set1)
    s=sorted(s)
    s=set(s)
    return s

def s2(s):
    s=s.intersection(set2)
    s=sorted(s)
    s=set(s)
    return s

def s3(s):
    s=s.intersection(set3)
    s=sorted(s)
    s=set(s)
    return s
def s4(s):
    s=s.intersection(set4)
    s=sorted(s)
    s=set(s)
    return s
def s5(s):
    s=s.intersection(set5)
    s=sorted(s)
    s=set(s)
    return s
def s6(s):
    s=s.intersection(set6)
    s=sorted(s)
    s=set(s)
    return s
def s7(s):
    s=s.intersection(set7)
    s=sorted(s)
    s=set(s)
    return s
def s8(s):
    s=s.intersection(set8)
    s=sorted(s)
    s=set(s)
    return s


while(True):
    print()
    choice=input("Please enter your choice as X/O:")
    d=choice.capitalize()
    print()
    
    if(d=="X"):
        print("So you are going to play as:",d)
        u=set()
        v=set()
        for i in range(1,6,1):
            print()
            n=input("Enter a number from 1 to 9:")
            if n not in u and n not in v:
                u.add(n)
                u=sorted(u)
                u=set(u)
                k=k.replace(n,"X")
                print(k)
            elif n in u or n in v:
                print("This number as already entered")
                continue

            chckset1=s1(u)
            chckset2=s2(u)
            chckset3=s3(u)
            chckset4=s4(u)
            chckset5=s5(u)
            chckset6=s6(u)
            chckset7=s7(u)
            chckset8=s8(u)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                print("Player wins the game")
                score+=1
                break
            

            if i==5:
                print()
                print("The Game ends in a draw")
                break
            while(True):
                AI=random.randint(1,9)
                AI=str(AI)
                if AI not in u and AI not in v:
                    v.add(AI)
                    v=sorted(v)
                    v=set(v)
                    k=k.replace(AI,"O")
                    print(k)
                    break
                elif AI in u or AI in v:
                    continue
         
            chckset1=s1(v)
            chckset2=s2(v)
            chckset3=s3(v)
            chckset4=s4(v)
            chckset5=s5(v)
            chckset6=s6(v)
            chckset7=s7(v)
            chckset8=s8(v)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                print("Computer wins the game")
                cscore+=1
                break
            
    elif d=="O":
        print("So you are going to play as:",d)
        u=set()
        v=set()
        for i in range(1,6,1):            
            while(True):
                AI=random.randint(1,9)
                AI=str(AI)
                if AI not in u and AI not in v:
                    v.add(AI)
                    v=sorted(v)
                    v=set(v)
                    k=k.replace(AI,"X")
                    print(k)
                    break
                elif AI in u or AI in v:
                    continue
         
            chckset1=s1(v)
            chckset2=s2(v)
            chckset3=s3(v)
            chckset4=s4(v)
            chckset5=s5(v)
            chckset6=s6(v)
            chckset7=s7(v)
            chckset8=s8(v)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                print("Computer wins the game")
                cscore+=1
                break
            if i==5:
                print()
                print("The Game ends in a draw")
                break
            while(True):
               print()
               n=input("Enter a number from 1 to 9:")
               if n not in u and n not in v:
                    u.add(n)
                    u=sorted(u)
                    u=set(u)
                    k=k.replace(n,"O")
                    print(k)
                    break
               elif n in u or n in v:
                    print()
                    print("This number as already entered")
                    continue

            chckset1=s1(u)
            chckset2=s2(u)
            chckset3=s3(u)
            chckset4=s4(u)
            chckset5=s5(u)
            chckset6=s6(u)
            chckset7=s7(u)
            chckset8=s8(u)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                print("Player wins the game")
                score+=1
                break
    else:
        print()
        print("Please enter a valid choice")
        continue

    x=input("Do you wish to continue  yes/no:")
    x=x.capitalize()
   
    if x=="Yes" or x=="Y":
        continue
    elif x=="No" or x=="N":
        if score>cscore:
            print()
            print("Player score = ",score)
            print()
            print("Computer score = ",cscore)
            print()
            print("Player wins the battle")
        else:
            print()
            print("Player score = ",score)
            print()
            print("Computer score = ",cscore)
            print()
            print("Computer wins the battle")
        print()
        print("Thank you for playing this game")
        break

            

