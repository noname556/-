login_id = []
login_pw = []

f = open('ID_PW.txt', 'r')
lines = f.readlines()

for line in lines:
    tamp = line.split(",")
    tamp[1] = tamp[1].split("\n")[0]
    print(tamp)
