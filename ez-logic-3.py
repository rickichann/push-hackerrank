
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

def swap_case(s):

    unify = []

    for i_stnc in s:
        if i_stnc.lower() == i_stnc:
            unify.append(i_stnc.upper())
        else:
            unify.append(i_stnc.lower())
    return (''.join(unify))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



