""" Scecant method """
import Maths.evaluate as e
import Maths.exfunc as ef
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
    out_list=[["x1","f(x1)","x2","f(x2)","x","f(x)"]]
    x1=x_axis[0].__round__(eff+1)
    x2=x_axis[1].__round__(eff+1)
    fox1=y_axis[0].__round__(eff+1)
    fox2=y_axis[1].__round__(eff+1)
    l=[]
    count=0
    while(1):
        l.extend([x1,fox1,x2,fox2])
        x=((x1*fox2-x2*fox1)/(fox2-fox1)).__round__(eff+1)
        fox=(e.evaluate(eq,x)).__round__(eff+1)
        if ef.isInteger(fox)==0:
            if fox in f.errors.keys():
                return [fox]
        l.extend([x,fox])
        out_list.append(l)
        x1=x2
        x2=x
        fox1=fox2
        fox2=fox
        l=[]
        count+=1
        if (fox.__round__(eff) == 0.0 or fox1==fox2) or count>60:
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
