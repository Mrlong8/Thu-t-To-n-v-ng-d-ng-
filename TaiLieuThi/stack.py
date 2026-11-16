#khoi luong hoa chat 
#from queue import LifoQueue
#KL={'C':12,'H':1,'O':16,'(':0}
#def sol():
#    S=LifoQueue()
#    for c in input():
#        if c in KL.keys():S.put(KL[c])
#        elif c==')':
#            t=0
#            while S.queue[-1]!=0:t+=S.get()
#            S.queue[-1]=t
#        else:S.queue[-1]*=int(c)  
#    print(sum(S.queue))
#if __name__=='__main__':
#    for i in range(int(input())):sol()
#kiem tra ngoac dung
#from queue import LifoQueue
#K = {'(': 0, ')': 0,'[': 1, ']': 1,'{': 2, '}': 2}
#def sol():
#    S = LifoQueue()
#    for c in input():
#        if c == '(' or c == '[' or c == '{':
#            if S.qsize() > 0 and S.queue[-1] < K[c]:
#                return 'Sai'
#            S.put(K[c])
#
#        elif c == ')' or c == ']' or c == '}':
#            if S.empty() or S.queue[-1] > K[c]:
#                return 'Sai'
#            S.get()
#
#    return 'Dung' if S.empty() else 'Sai'
#if __name__ == '__main__':
#    for i in range(int(input())):
#        print(sol())
#Chao don tan sv K59
#from queue import LifoQueue
#def K59(a):
#    S=LifoQueue()
#    S.put((2e9,-1))
#    k=[]
#    for i,x in a:
#        while S.queue[-1][0]<=x:S.get()
#        k.append(S.queue[-1][1])
#        S.put((x,i))
#    return k    
#if __name__=='__main__':
#    n=int(input())        
#    a=list(enumerate(list(map(int,input().split()))))
#    L=K59(a)
#    R=K59(a[::-1])[::-1]
#    for x,i,z in zip(L,range(n),R):
#        if x==-1 or z==-1: print(x+z+1,end=" ")
#        else: print(x if i-x<=z-i else z,end=" ")

        