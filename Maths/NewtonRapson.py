""" Newton Rapson method """
import Maths.evaluate as e
import Maths.exfunc as ef
import Maths.derivative as d
import Maths.exfunc2 as ef2
import Maths.functions as f
import math as m

# list model   [a,f(a),b,f(b),center,f(center)]
        
def getFinalRoot(eq,eff,interval):
    x_axis=[]
    y_axis=[]
    for key,value in interval.items():
        x_axis.append(value.__round__(eff+1))
        y_axis.append(key.__round__(eff+1))
    out_list=[["x_pre","f(x)","x"]]
    x_pre=(x_axis[1]).__round__(eff+1)
    l=[]
    count=0
    lor=0
    while(1):
        l.append(x_pre)
        fox_pre=(e.evaluate(eq,x_pre)).__round__(eff+1)
        if ef.isInteger(fox_pre)==0:
            if fox_pre in f.errors.keys():
                return [fox_pre]
        l.append(fox_pre)
        der_fox_pre=(d.getDerivation(eq,x_pre)).__round__(eff+3)
        if ef.isInteger(der_fox_pre)==0:
            if der_fox_pre in f.errors.keys():
                return [der_fox_pre]
        if der_fox_pre==0.0:
            if lor==0:
                x_pre=(x_axis[0]).__round__(eff+1)
                out_list=[["x_pre","f(x)","x"]]
                l=[]
                continue
            else:
                return ["ERROR109"]
        x=(x_pre-(fox_pre/der_fox_pre)).__round__(eff+1)
        l.append(x)
        out_list.append(l)
        if x_pre.__round__(eff+1)==x.__round__(eff+1):
            break
        x_pre=x
        l=[]
        count+=1
        if fox_pre.__round__(eff) == 0.0 or count>60:
            break
    if count>=61:
        return ["ERROR111"]
    return ef2.getStructuredList(out_list,eff)



# returns the final list of iterations
def getRoot(eq,eff=0):
    status=ef.checkBrackets(eq)
    if ef.isInteger(status)!=1:
        if status in f.errors.keys():
            return status
    interval=ef2.getInterval(eq)
    if interval.__len__()==1:
        a=[]
        if interval[0] in f.errors.keys():
            return [interval[0]]
        for i in interval.values():
            a.append(i)
        return a[0]
    else:
        return getFinalRoot(eq,eff,interval)



def evaluate():
    equation=input("Enter the equation: ")
    efficiency=0
    if ef.getConst(equation)=="0":
        print("ERROR113: ",f.errors["ERROR113"])
    else:
        flag=0
        while(1):
            efficiency=input("Enter efficiency of root: ")
            if ef.isInteger(efficiency):
                efficiency=int(efficiency)
                flag=1
            if flag:
                break
            else:
                print("Invalid Input")
        if efficiency>0 and efficiency<11:
            print("Value of function is: ")
            print()
            print("_________________________________________________________________________________")
            print()
            j=0
            root=getRoot(equation,efficiency)
            if ef.isInteger(root):
                print(root)
            else:
                if root.__len__()==1:
                    if root[0] in f.errors.keys():
                        print(root[0]+": "+f.errors[root[0]])
                else:
                    for i in root:
                        if j==0:
                            print("  ".ljust(7," ")+"  |  ".join(i))
                        else:
                            print((str(j)+".").ljust(7," ")+"  |  ".join(i))
                        j=j+1
        else:
            print("Invalid Input(efficiency must be between 1 and 10)")
