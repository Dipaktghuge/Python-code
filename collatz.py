def collatz(n):
    i=0
    while n>1:
        i=i+1
        print(n,end=" ")
        if n%2>0:
            n=3*n+1
        else:
            n=n//2
    return i
print(f"no.of step :{collatz(56728523249)}")
