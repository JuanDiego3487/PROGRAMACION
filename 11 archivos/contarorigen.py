#Un programa que cuentee los correos de origen distintos que hay
#EN el mbox.txt.
def miFin(email):
    return len(email)


fd = open("11 archivos/mbox-short.txt", "r")

cl=0

setEmail = set()
for linea in fd:
    # print(linea)
    if linea.startswith("To:"):
        #cl += 1 
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])


fd.close()

cl = len (setEmail)
print("CAntidad de correos de origen distintos:",cl)

for email in sorted(setEmail, reverse=False):
    print(email)


