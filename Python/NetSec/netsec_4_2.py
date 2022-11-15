import hashlib, string, time

start = time.time()

def getUpLetter(number):
	return str(unichr(ord('A')+number))

def getHexByteStr(number):
	return "%02x" % number

def md5(password, constant):
	m = hashlib.md5()
	m.update(str.encode(password + constant))
	return m.hexdigest()

def lmh(password, constant):
	while len(password) <= 14:
		password = password + "0"
	password = password.upper()
	return md5(password[:7], constant)[:16] + md5(password[7:14], constant)[:16]

def wnth(password, constant):
	while len(password) <= 14:
		password = password + "0"
	return md5(password, constant)[:32]

def chap(password, constant, challenge):
	firstHash = lmh(password, constant) + "0000000000"
	secondHash = wnth(password, constant) + "0000000000"
	res1 = md5(firstHash[:14],challenge)[:16]
	res2 = md5(firstHash[14:28],challenge)[:16]
	res3 = md5(firstHash[28:42],challenge)[:16]
	res4 = md5(secondHash[:14],challenge)[:16]
	res5 = md5(secondHash[14:28],challenge)[:16]
	res6 = md5(secondHash[28:42],challenge)[:16]
	return res1 + res2 + res3 + res4 + res5 + res6

pwd = "BOIHODBMC"
const = "NetSec1"
chall = "GoodLuck!"

print("md5 hash of " + pwd + "\nwith constant " + const + "\nis " + md5(pwd, const) + "\n")
print("lmh of " + pwd + "\nwith constant " + const + "\nis " + lmh(pwd, const) + "\n")
print("response of " + pwd + "\nwith constant " + const + "\nand " + chall + "\nis " + chap(pwd, const, chall) + "\n")

const = "NetSec1"
chall = "GoodLuck!"
# resp = "1acad1cd833b82bbe379c4984786cdf501bc0a8d020ab4ab617719e1fce1bc7f6130f8b1ff02a5d9462b8b8865213d64"
resp = "fd1c103fe67100eb4b3f6d39f177bb08332188b99f7f64cb874627e5f2dfc0519134525203266fdb948c28f744698861"

#Beispiel:
P0="W" # Passwort ist W........ also 9 Zeichen lang; Zeichen 2-9 (also P1...P8) sind Klein- und Grossbuchstaben; starten Sie Ihre Suche bei a bzw A ;)

##### Ab hier Loesung:

"""
def schreiben(text, file):
    with open("F:/Test/"+file+".txt", 'a') as file:
        file.writelines(text + "\n")


upper_alphabet = list(string.ascii_uppercase)
upper_alphabet.append("0")
hex_alphabet = list(string.ascii_lowercase)[:6]
for i in range(10):
    hex_alphabet.append(str(i))

suff = ""
for h_14_1 in hex_alphabet:
	for h_14_2 in hex_alphabet:
		for h_15_1 in hex_alphabet:
			for h_15_2 in hex_alphabet:
				exp_lmh_right = str(h_14_1) + str(h_14_2) + str(h_15_1) + str(h_15_2) + "0000000000"
				if md5(exp_lmh_right, chall)[:16] == resp[32:48]:
					print("Suffix des LMH der zweiten Hälfte: " + exp_lmh_right[:4])
					suff = exp_lmh_right[:4]


print("_______________________________________")

for p7 in upper_alphabet:
	for p8 in upper_alphabet:
		tmp = p7 + p8 + "00000"
		if md5(tmp, const)[12:16] == suff:
			pwd_right = tmp
			print("Zweite Hälfte des Passworts: " + pwd_right)
			lmh_2 = md5(pwd_right, const)[:16]
			print("LMH der zweiten Hälfte: " + lmh_2)

pwd = pwd_right[:2]
pwd_suff = "MC00000"

print("_______________________________________")
for h_7_1 in hex_alphabet:
	for h_7_2 in hex_alphabet:
		tmp = h_7_1 + h_7_2 + lmh_2[:12]
		chall_mid = md5(tmp, chall)[:16]
		if chall_mid == resp[16:32]:
			exp_lmh_mid = tmp
			print("Der mittlere Teil des erweiterten LMH ist: " + exp_lmh_mid)

print("_______________________________________")

suff_lmh_left = exp_lmh_mid[:2]
lst_lmh_left = list()

match = list()

for p0 in upper_alphabet:
	for p1 in upper_alphabet:
		for p2 in upper_alphabet:
			for p3 in upper_alphabet:
				for p4 in upper_alphabet:
					for p5 in upper_alphabet:
						pwd_left = "B" + p0 + p1 + p2 + p3 + p4 + p5
						lmh_left = md5(pwd_left, const)[:16]
						challenge_left = md5(lmh_left[:14], chall)[:16]
						if lmh_left[14:16] == suff_lmh_left:
							tupel = (pwd_left, lmh_left, challenge_left)
							lst_lmh_left.append(tupel)
							# schreiben(str(tupel), "all")
							if challenge_left == resp[:16]:
								match.append(tupel)
								print(tupel)
								print("time: " + str(time.time() - start))

pwd_list = list()
for i in range(len(pwd)):
    pwd_list.append((pwd[i],pwd[i].lower()))
"""

print("time: " + str(time.time()-start))

# for i in lst_lmh_left:
# 	exp_lmh_left = i[1][:14]
# 	tmp = md5(wort, chall)[:16]
# 	# schreiben(str((wort, tmp)), "file")
# 	if tmp == resp[:16]:
# 		print(i)
# print("time: " + str(time.time()-start))
lst = list()
for i in range(len(pwd)):
    lst.append((pwd[i],pwd[i].lower()))


def rechts(passwd):
	wnth_wert = wnth(passwd, const) + "0000000000"
	a = wnth_wert[:14]
	b = wnth_wert[14:28]
	c = wnth_wert[28:]
	a2 = md5(a, chall)[:16]
	b2 = md5(b, chall)[:16]
	c2 = md5(c, chall)[:16]

	return a2+b2+c2

qst = ""

for a in range(2):
	for b in range(2):
		for c in range(2):
			for d in range(2):
				for e in range(2):
					for f in range(2):
						for g in range(2):
							for h in range(2):
								qst = "b" + lst[1][a] + lst[2][b] + lst[3][c] + lst[4][d] + lst[5][e] + lst[6][f] + lst[7][g] + lst[8][a]
								if rechts(qst) == resp[48:]:
									print(rechts(qst) + "|" + qst)



print("time: " + str(time.time()-start))



