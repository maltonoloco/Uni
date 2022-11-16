# Initialisierung
def ksa(key, l):
    l = 2**l
    s = list()
    for i in range(l):
        s.append(i)

    # Scrambling
    j = 0
    for i in range(5):
        j = (j + s[i] + key[i % len(key)]) %l
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s


def prga(s, d, l):
    l = 2**l
    j = 0
    out = list()
    for i in range(d):
        i = i+1
        j = (j + s[i%l]) % l

        temp = s[i%l]
        s[i%l] = s[j]
        s[j] = temp
        out.append(s[(s[i%l] + s[j]) % l])
    return out

#k1 = [168, 202, 60, 127, 195, 61, 207, 35]
k1 = [4, 7, 5, 2, 6]
s = ksa(k1, 3)
print(prga(s, 1, 3))
#s = ksa(k1, 8)
#print(prga(s, 17, 8))

"""

k = [3, 7, 7, 2]
for i in range(7):
    t = [3, 7, 7, 2, i]
    print(t)
    s = ksa(t, 3)
    print(prga(s, 2, 3))
"""