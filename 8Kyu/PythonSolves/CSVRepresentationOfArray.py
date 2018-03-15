def toCsvText(array):
    ret = ""
    longTab = len(array) - 1
    countTab = 0
    for line in array:
        longLine = len(line) - 1
        countLine = 0
        for item in line:
            if countLine == longLine:
                ret += "{}".format(item)
            else:
                ret += "{},".format(item)
            countLine += 1
        if countTab == longTab:
            ret += ""
        else:
            ret += "\n"
        countTab += 1
    return ret


myarray = [[ 0, 1, 2, 3, 45 ],[ 10,11,12,13,14 ],[ 20,21,22,23,24 ],[ 30,31,32,33,34 ]]

print(toCsvText(myarray))
