import Maths.functions as f
import Maths.evaluate as e
import math



#This will convert string into a list
def getList(s):
    l=[]
    i=0
    flag=0
    while (1):
        if i==0:
            if isInteger(s[i])==1:
                l.append(float(s[i]))
            else:
                l.append(s[i])
        else:
            if isInteger(s[i])==1:
                if isInteger(s[i-1])==1:
                    a=l.pop()
                    l.append(a*10+float(s[i]))
                else:
                    l.append(float(s[i]))
            else:
                if s[i]==".":
                    i+=1
                    j=1
                    a=l.pop()
                    while i<s.__len__():
                        if isInteger(s[i])==1:
                            a=a+(float(s[i])/math.pow(10,j))
                            j+=1
                            i+=1
                        else:
                            flag=1
                    l.append(a)
                else:
                    l.append(s[i])
        if flag==0:
            i=i+1
        if i>=s.__len__():
            break
    return l

def hasLog(s):
    for i in s:
        if i==f.function["log"]:
            return 1
    return 0

def checkBrackets(s):
    count=0
    for i in s:
        if count==0 and i==")":
            return "ERROR112"
        if i=="(":
            count+=1
        if i==")":
            count-=1
        if i in f.function.values():
            return "ERROR110"
    if count==0:
        return 1
    else:
        return "ERROR112"

def checkString(l):
    flag="1"
    for i in l:
        if isInteger(i)==1:
            continue
        elif i in f.function.values():
            continue
        elif i in f.cfunction.values():
            continue
        elif i in f.const.values():
            continue
        elif i in f.symbols:
            continue
        elif ord(i)>=ord("A") or ord(i)<=ord("Z"):
            continue
        else:
            flag="ERROR110"
            break
    return flag


#returns a constant in a string
def getConst(l):
    d=set()
    for i in l:
        if isInteger(i)==0:
            if ord(i)>=ord("A") and ord(i)<=ord("Z"):
                d=d.union(i)
        if d.__len__()>1:
            break
    if d.__len__()==1:
        return d.pop()
    else:
        return "0"





#This function will convert constants into a particular value
def convString(l,i):
    l1=[]
    const=getConst(l)
    for j in l:
        if j==const:
            l1.append(float(i))
        elif j in f.constant_value.keys():
            l1.append(f.constant_value[j])
        else:
            l1.append(j)
    return l1





#This function will return a string with encoded functions
def getEncode(s):
    s1=s
    d=f.function
    d.update(f.const)
    for keys,values in d.items():
        l=s1.split(keys)
        if l.__len__()>1:
            s1=""
            for i in range(l.__len__()-1):
                s1=s1+l[i]+values
            s1=s1+l[l.__len__()-1]
    return s1





#this function will return substring inside a function
#remains for log function
def getSubstring(l,j):
    #if there is a log function it will return substring and base
    flag=0
    count=0
    base=[0]
    for i in range(j,l.__len__()):
        if l[i]=="(":
            flag+=1
        elif l[i]==")":
            flag-=1
        if flag==0:
            break
        count+=1
    s=[]
    flag=0
    for i in range(j+1,j+count):
        if flag==0 and l[i]==",":
            ex=base.pop()
            for k in range(i+1,j+count):
                base.append(l[k])
            break
        else:
            if l[i]=="(":
                flag+=1
            elif l[i]==")":
                flag-=1
            s.append(l[i])
    return s,base  # Returns list


#This function will search for an charecter within a list
def isFunction(c):
    l=f.function.values()
    flag=0
    if isInteger(c)==0:
        for i in l:
            if i==c:
                flag=1
                break
    return flag




#return the evaluation of a function
def getFuncSum(f,d,b=math.e):
    if f==":":
        return 1/(math.sin(d))
    elif f==";":
        return math.sin(d)
    elif f=='"':
        return math.cos(d)
    elif f=="'":
        return 1/(math.cos(d))
    elif f==">":
        return math.tan(d)
    elif f=="<":
        return 1/(math.tan(d))
    elif f=="?":
        return math.log(d,b)
    elif f=="+":
        return b+d
    elif f=="-":
        return b-d
    elif f=="*":
        return b*d
    elif f=="/":
        return b/d
    elif f=="^":
        return b**d
    



#returns true if input is integer else false
def isInteger(c):
    try:
        a=float(c)
        return 1
    except:
        return 0







