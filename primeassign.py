#print prime number from 2 to 50
#first nor= 2 ,end nor=50 2,3,5,7,11,13,....
N=2
while(N<=50):
    count=0
    i=2
    while(i <= N//2):
        if(N % i == 0):
            count=count+1
            break
        i=i+1
    if(count == 0 and N !=1):
        print(N)
    N=N+1




