t=int(input())
print(*[ i for i in range(1,t+1) if t%i==0]  )