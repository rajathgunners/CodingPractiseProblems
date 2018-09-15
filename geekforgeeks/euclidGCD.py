#GCD using Euclid's Algorithm

def findGCD(a,b):
    if b is 0:
        return a
    else:
        return findGCD(b, a%b)



print(findGCD(180, 48))

    