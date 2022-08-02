""" Regula Falsi or False Position Method"""
import Maths.evaluate as e
import Maths.exfunc as ef
import Maths.exfunc2 as ef2
import Maths.functions as f
import math as m

# list model   [a,f(a),b,f(b),center,f(center)]        
def getFinalRoot(eq,eff,interval):
    x_axis=[]
    y_axis=[]
    count=0
    for key,value in interval.items():
        x_axis.append(value.__round__(eff+1))
        y_axis.append(key.__round__(eff+1))
    out_list=[["a","f(a)","b","f(b)","center","f(center)"]]
    count=0
    l=[]
    while(1):
        l.extend([x_axis[0].__round__(eff+1),y_axis[0].__round__(eff+1),x_axis[1].__round__(eff+1),y_axis[1].__round__(eff+1)])
        a=x_axis[0]
        b=x_axis[1]
        foa=e.evaluate(eq,a).__round__(eff+1)
        if ef.isInteger(foa)==0:
            if foa in f.errors.keys():
                return [foa]
        fob=e.evaluate(eq,b).__round__(eff+1)
        if ef.isInteger(fob)==0:
            if fob in f.errors.keys():
                return [fob]
        next_point=((a*fob-b*foa)/(fob-foa)).__round__(eff+1)
        ans=e.evaluate(eq,next_point).__round__(eff+1)
        if ef.isInteger(ans)==0:
            if ans in f.errors.keys():
                return [ans]
        l.append(next_point)
        l.append(ans)

        out_list.append(l)
        count+=1
        if (x_axis[0]-x_axis[1]).__round__(eff) == 0.0 or (x_axis[0]-x_axis[1]).__round__(eff) == -0.0 or ans.__round__(eff)==0.0 or count>60:
            break
        
        if ans<0:
            i=y_axis.index(min(y_axis))
            x_axis[i]=next_point
            y_axis[i]=ans
        elif ans>0:
            i=y_axis.index(max(y_axis))
            x_axis[i]=next_point
            y_axis[i]=ans
        l=[]
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
