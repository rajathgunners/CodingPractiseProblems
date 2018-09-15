x, y = 0, 0
def recurseSum2(s, a, b, sums):
    global x, y
    #print("a = {}, b = {}, sums = {}".format(s[a:sums], s[b:a], s[sums:]))
    #print()
    if b < -len(s):
        #print("b is {}".format(b))
        return False
    if int(s[sums:]) < int(s[a:sums]) + int(s[b:a]):
        return False
    elif int(s[sums:]) == (int(s[a:sums]) + int(s[b:a])):
        x = a
        y = b
        return True
    else:
        return recurseSum2(s, a-1, b-1, sums) or recurseSum2(s, a, b-1, sums)
    
    
def sumString2(s, a, b, sums):
    global x, y
    #print("x = {}, y = {} -len(s) = {}".format(x, y, -len(s)))
    if b < -len(s):
        return False
    if recurseSum2(s, a, b, sums):
        #print("{} == {}".format(y, -len(s)))
        if y == -len(s):
            #print("stop here")
            return True
        else:
            return sumString2(s[:sums], (x-sums)-1, (x-sums)-2, (x-sums)) or sumString2(s, a-1, b-1, sums-1)
        
    else:
        return sumString2(s, a-1, b-1, sums-1)

l = ['100200300500']
for s in l:
    if sumString2(s, -2, -3, -1):
        print('1')
    else:
        print('0')