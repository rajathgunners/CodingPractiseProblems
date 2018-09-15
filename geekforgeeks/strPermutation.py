"""ALL POSSIBLE PERMUTATION OF A STRING"""

def permUtil(ipl, xl):
    if not xl:
        print('{}'.format(''.join(ipl)), end=' ')
    else:
        for z in xl:
            temp = list(xl)
            temp.remove(z)
            permUtil(ipl+[z], temp)
    return



def perm(instr):
    ip = list(instr)
    ip = sorted(ip)
    permUtil([], ip)
    return
        