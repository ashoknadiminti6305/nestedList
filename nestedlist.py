x=1011
y=str(x)
decimal=0
n=len(y)
for i in range(n):
    decimal+=int(y[i])*(2**(n-1-i))
print(decimal)