l1=list(map(int,input().split()))
l2=list(map(int,input().split()))

if(len(l1)==len(l2)):
    s1=list(map(str,l1))[::-1]
    s2=list(map(str,l2))[::-1]
    s3="".join(s1)
    s4="".join(s2)
    s5=int(s3)+int(s4)
    s6=list(str(s5))[::-1]
    s7 = list(map(int,s6))
    print(s3)
