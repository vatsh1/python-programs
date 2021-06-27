


def primalitycheck(a) :
    if (a in (2,3)):
        return True
    elif (a % 2 == 0 or a<2 or a % 3 == 0) :
        return False
    sq = int(a ** (1 / 2))
    i = 5
    ctr = 0
    while(i <= sq) :
        if(a % i == 0):
            ctr += 1
        i += 1
    if ctr > 0 :
        return False
    else :
        return True        


# In[ ]:


def Xdivisors_Kprimes(a) :
    div_ctr = 0
    prime_ctr = 0
    if (a <= 0):
        return 0
    else:
        i = 1
        while(i <= int(a / 2)):
            if (a % i == 0):
                div_ctr += 1
                if(primalitycheck(i)):
                    prime_ctr += 1
            i += 1
        if (primalitycheck(a)):
            return (div_ctr + 1, prime_ctr + 1)
        else:
            return (div_ctr + 1, prime_ctr)
            


def subtask1():
    T = int(input())
    if (T <= 0 or T>100):
        print('invalid entry for T')
        return 0
    else:
        iter = 1
        while (iter<=T):
            X = int(input())
            K = int(input())
            if (X<=2 or K>=X):
                res = 0
            else:
                if (K == 1):
                    for i in range(1,1073741824) :
                        if (Xdivisors_Kprimes(i) == (X,K)):
                            res = 1
                else:
                    if ((2**K)==X):
                        res = 1
                    else:
                        res = 0
            print(res)
            iter += 1
            




subtask1()



