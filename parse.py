# Tristan Blizzard 730390144
# Honor Pledge

import sys
import re

# Globals
sp = ' '
special = ["<", ">", ")", "(", "]", "[", "\"", ".", ",", ";", ":", '"']

# Function that hard checks if "MAIL" and "FROM:" are in the cmd, along with infinite whitespace in between
def mail_from_cmd(line):
    i = 4
    if line[0] != 'M' or line.endswith("M"):
        print("ERROR --mail-from-cmd")
        return
    if line[1] != 'A' or line.endswith("A"):
        print("ERROR --mail-from-cmd")
        return
    if line[2] != 'I' or line.endswith("I"):
        print("ERROR --mail-from-cmd")
        return
    if line[3] != 'L' or line.endswith("L"):
        print("ERROR --mail-from-cmd")
        return
    if line[i] != sp:
        print("ERROR --whitespace")
        return
    while line[i] == sp:
        i+=1
    if line[i] != "F" or line.endswith("F"):
        print("ERROR --mail-from-cmd")
        return
    if line[i+1] != "R" or line.endswith("R"):
        print("ERROR --mail-from-cmd")
        return
    if line[i+2] != "O" or line.endswith("O"):
        print("ERROR --mail-from-cmd")
        return
    if line[i+3] != "M" or line.endswith("M"):
        print("ERROR --mail-from-cmd")
        return
    if line[i+4] != ":" or line.endswith(":"):
        print("ERROR --mail-from-cmd")
        return
    else:
        pathLine = line[i+5:]
        path(line, pathLine)

# Function for letting whatever amout of whitespace exist between ":" and "<", and then checks for the first "<"
def path(line, pathLine):
    i = 0
    while pathLine[i] != "<":
        if pathLine[i] != sp:
            print("ERROR --whitespace")
            return
        i+=1
    else:
        if pathLine.endswith("<"):
            print("ERROR --path")
            return
        fullLine = line
        localNameLine = pathLine[i+1:]
        localName(fullLine, localNameLine)

# Function for checking local name standards
def localName(line, localNameLine):
    i = 0
    if localNameLine[0] == sp:
        print("ERROR --string")
        return
    while localNameLine[i] != "@":
        if localNameLine[i] == sp:
            print("ERROR --mailbox")
            return
        if localNameLine[i] in special:
            print("ERROR --mailbox")
            return
        i+=1
    domainLine = localNameLine[i+1:]
    fullLine = line
    domainName(fullLine, domainLine)

# Function for domain checks, does not recurse stuff like cs.unc.edu
def domainName(line, domainLine):
    i = 0
    if domainLine[0] in special or domainLine[0] == sp:
        print("ERROR --element")
        return
    if not domainLine.endswith(">"):
        print("ERROR --element")
        return
    fullLine = line
    domainChecker(fullLine, domainLine)

# Recursive function for tracking different domains
def domainChecker(line, domainLine):
    fullLine = line
    i = 0
    while domainLine[i] != ".":
        if domainLine[i] == sp:
            print("ERROR --path")
            return
        if domainLine[i] in special:
            print("ERROR --element")
            return
        if domainLine[i+1] == ">":
            print(line)
            print("Sender ok")
            return
        i+=1
    if domainLine[i] == '.' and domainLine[i] != ">":
        domainLine = domainLine[i+1:]
        i = 0
        domainChecker(fullLine,domainLine)



def main():
    line = input()
    if line != "":
        mail_from_cmd(line)
    else:
        print("ERROR --null")

if __name__ == "__main__":
    main()
    
