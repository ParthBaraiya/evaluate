import Maths.exfunc as f
import Maths.functions as func



#Return the priority of a function  or charecter
def getPriority(c):
    if f.isInteger(c)==0:
        if c=="#" or c=="(" or c==")":
            return 0
        elif c=="^":
            return 3
        elif c=="/" or c=="*":
            return 2
        elif c=="+" or c=="-":
            return 1
        else:
            return 4
    else:
        return 4


#Check whether the character is function or a character
def isFunc(c):
    if c=="+" or c=="-" or c=="/" or c=="*" or c=="^":
        return 1
    else:
        return 0



#Return the postfix form of a equation
def getPostfix(l):
    i=0
    sl=["#"]
    sf=[]
    rank=0
    while (1):
        if l[i]=="(":
            sl.append(l[i])
            i+=1
        elif l[i]==")" and sl[sl.__len__()-1]=="(":
            a=sl.pop()
            i=i+1
        else:
            if getPriority(l[i])>getPriority(sl[sl.__len__()-1]):
                sl.append(l[i])
                i=i+1
            else:
                a=sl.pop()
                if isFunc(a)==1:
                    rank-=1
                else:
                    rank+=1
                sf.append(a)

        if i>=l.__len__():
            break

    while sl[sl.__len__()-1]!="#":
        a=sl.pop()
        if isFunc(a)==1:
            rank-=1
        elif isFunc(a)==0:
            rank+=1
        sf.append(a)
    if rank!=1:
        return "ERROR101"
    return sf

