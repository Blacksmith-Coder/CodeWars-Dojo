import re
from decimal import Decimal

def balance(book):
    regexone = re.compile(r'[0-9]+')
    regexnum = re.compile(r'[0-9]*\.[0-9]*')
    regexstr = re.compile(r'[a-zA-Z]+')
    amount = Decimal(regexnum.match(str.split(book, '\n', 1)[0]).group())
    conteneur = str.split(book, '\n', 1)[1].split('\n')
    retour = "Original Balance: {}\r\n".format(amount)
    count = 0
    totalxpense = Decimal(0.0)
    for line in conteneur:
        if line != "":
            count = count + 1
            firstnum = regexone.search(line).group()
            secondstring = regexstr.search(line).group()
            thirdnum = Decimal(regexnum.search(line).group())
            amount -= thirdnum
            retour += "{0} {1} {2:.2f} Balance {3:.2f}\r\n".format(firstnum, secondstring, thirdnum, amount)
            totalxpense += thirdnum
    average = totalxpense / count
    retour += "Total expense  {0:.2f}\r\n".format(totalxpense)
    retour += "Average expense  {0:.2f}".format(average)
    return retour


#    ret = [regexstr.search(x) for x in conteneur if x != ""]

b1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""


print(balance(b1))
