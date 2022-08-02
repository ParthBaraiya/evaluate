import Maths.exfunc as func
import Maths.functions as f
import Maths.postfix as pf



#This function will return value of equation(without triginomatric or log functions)
def finalEval(l):        #Returns Integer
    i=0
    eval_String=[]
    ans=0
    while(1):
        if func.isFunction(l[i])==1:
            function=l[i]
            content,base=func.getSubstring(l,i+1)
            content_val=finalEval(content)
            if func.isInteger(content_val)==0:
                if content_val in f.errors.keys():
                    return content_val
            base_val=finalEval(base)
            if func.isInteger(base_val)==0:
                if base_val in f.errors.keys():
                    return base_val
            if function==f.function["log"]:
                if content_val==0:
                    return "ERROR105"
                elif content_val<0:
                    return "ERROR107"
                if base_val<0:
                    return "ERROR106"
                elif base_val==0:
                    return "ERROR104"
            eval_String.append(func.getFuncSum(function,content_val,base_val))
            baselen=0
            if base!=[0]:
                baselen=1+base.__len__()
            i=i+3+content.__len__()+baselen
        else:
            eval_String.append(l[i])
            i=i+1
        if i>=l.__len__():
            break
    eval_String=pf.getPostfix(eval_String)
    if eval_String.__len__()==1 and eval_String[0] in f.errors.keys():
        return eval_String[0]
    ans_String=[]
    i=0
    while (1):
        if pf.isFunc(eval_String[i])==1:
            function=eval_String[i]
            data=ans_String.pop()
            base=ans_String.pop()
            if function==f.cfunction["/"]:
                if base==0:
                    return "ERROR109"
            ans_String.append(func.getFuncSum(function,data,base))
        else:
            ans_String.append(eval_String[i])
        i=i+1
        if i>=eval_String.__len__():
            break
    ans=ans_String[0]
    return ans

    

#Evaluates a equation
def evaluate(s,val=0):       #Returns final ans
    eval_string=func.getEncode(s)
    eval_string=func.getList(eval_string)
    if func.checkString(eval_string) in f.errors.keys():
        return func.checkString(eval_string)
    eval_string=func.convString(eval_string,val)
    return finalEval(eval_string)
