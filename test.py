import random
num= random.randint(1,20)
print('guess')
bingo=False
while bingo==False:
    answer=int(input())
    haha=10
    if answer<num:
        print('%d is %d too small' %(answer,haha))


    if answer>num:
        print ('%d is too big'%answer)

    if answer==num:
        print('bingo')
        bingo =True


##for i in range(1,100):
##    print(i)
##print('''\\\\_v_//let's go\\\n"ok"
##roll''')
