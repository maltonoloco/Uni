#Initialisierung
def ksa(key, l):
    s = list()
    for i in range(256):
        s.append(i)

    #Scrambling
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i%l])%256

        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s

def prga(s, d):
    j = 0
    out = list()
    for i in range(d):
        j = (j + s[i])%256

        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        out.append(s[(s[i] + s[j])%256])
    return out

k = [228, 160, 149, 185, 24, 158, 135, 30]
s = ksa(k, 8)
print(prga(s, 17))