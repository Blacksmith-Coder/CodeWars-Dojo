import re
from decimal import Decimal


def balance(book):
    regexspec = re.compile(r'[0-9]*\.[0-9]*|[0-9]+')
    regexone = re.compile(r'[0-9]+')
    regexnum = re.compile(r'[0-9]*\.[0-9]*')
    regexstr = re.compile(r'[a-zA-Z]+')
    amount = Decimal(0.0)
    m = regexspec.match(book)
    if m:
        print(m.group())
        amount = Decimal(m.group())
    conteneur = str.split(book, '\n', 1)[1].split('\n')
    retour = "Original Balance: {0:.2f}\r\n".format(amount)
    count = 0
    totalxpense = Decimal(0.0)
    for line in conteneur:
        if line != "":
            bool1 = regexone.search(line).group().strip() != "" or regexone.search(line) is not None
            bool2 = regexstr.search(line).group().strip() != "" or regexstr.search(line) is not None
            bool3 = regexnum.search(line).group().strip() != "" or regexnum.search(line) is not None
            if bool1 and bool2 and bool3:
                firstnum = regexone.search(line).group()
                secondstring = regexstr.search(line).group()
                thirdnum = Decimal(regexnum.search(line).group())
                count = count + 1
                amount -= thirdnum
                retour += "{0} {1} {2:.2f} Balance {3:.2f}\r\n".format(firstnum, secondstring, thirdnum, amount)
                totalxpense += thirdnum
            else:
                retour += "Error"
    average = totalxpense / count
    retour += "Total expense  {0:.2f}\r\n".format(totalxpense)
    retour += "Average expense  {0:.2f}".format(average)
    return retour


#    ret = [regexstr.search(x) for x in conteneur if x != ""]

b1 = """1818
129 Grocery;! 24.8?;
160 Gasoline 120.90
131 Vegetables;! 13.6?;
131 Grocery 17.5
130 Fruits 93.5
125 Tyres 12.2
"""


#regextest = re.compile('[0-9]*\.[0-9]*')
#print(regextest.search(multi, re.MULTILINE))

print(balance(b1))
