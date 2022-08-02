import Maths.evaluate as e
import Maths.exfunc as ef
import Maths.functions as f

#checks if varible is valid or not i.e. if there is any error
def isValid(num):
    if ef.isInteger(num)==0:
        return 0
    else:
        return 1

#returns the interval where root is found
def getInterval(eq):
    count=0
    pos_small_no=0
    pos_big_no=1
    neg_small_no=-1
    neg_big_no=0
    
    pos_small_val=e.evaluate(eq,pos_small_no)
    pos_big_val=e.evaluate(eq,pos_big_no)
    neg_small_val=e.evaluate(eq,neg_small_no)
    neg_big_val=e.evaluate(eq,neg_big_no)

    while(count<=60):
        if isValid(pos_small_val)==0:
            if pos_small_val in ["ERROR104","ERROR105","ERROR106","ERROR107"]:
                pos_small_no,pos_big_no=pos_big_no,pos_big_no+1
                pos_small_val,pos_big_val=pos_big_val,e.evaluate(eq,pos_big_no)
                count+=1
                continue
            else:
                return {0: pos_small_val}
        if isValid(pos_big_val)==0:
            if pos_big_val in ["ERROR104","ERROR105","ERROR106","ERROR107"]:
                pos_small_no,pos_big_no=pos_big_no,pos_big_no+1
                pos_small_val,pos_big_val=pos_big_val,e.evaluate(eq,pos_big_no)
                count+=1
                continue
            else:
                return {0: pos_big_val}

        if pos_small_val==0:
            return {pos_small_val: pos_small_no}
        if pos_big_val==0:
            return {pos_big_val: pos_big_no}
        if pos_small_val/pos_big_val<0:
            return {pos_small_val: pos_small_no, pos_big_val: pos_big_no}
        pos_small_no,pos_big_no=pos_big_no,pos_big_no+1
        pos_small_val,pos_big_val=pos_big_val,e.evaluate(eq,pos_big_no)



        
        if isValid(neg_small_val)==0:
            if neg_small_val in ["ERROR104","ERROR105","ERROR106","ERROR107"]:
                neg_big_no,neg_small_no=neg_small_no,neg_small_no-1
                neg_small_val,neg_big_val=e.evaluate(eq,neg_small_no),neg_small_val
                count+=1
                continue
            else:
                return {0: neg_small_val}
        if isValid(neg_big_val)==0:
            if neg_big_val in ["ERROR104","ERROR105","ERROR106","ERROR107"]:
                neg_big_no,neg_small_no=neg_small_no,neg_small_no-1
                neg_small_val,neg_big_val=e.evaluate(eq,neg_small_no),neg_small_val
                count+=1
                continue
            else:
                return {0: neg_big_val}

        if neg_small_val==0:
            return {neg_small_val: neg_small_no}
        if neg_big_val==0:
            return {neg_big_val: neg_big_no}
        
        if neg_small_val/neg_big_val<0:
            return {neg_small_val: neg_small_no, neg_big_val: neg_big_no}
        neg_big_no,neg_small_no=neg_small_no,neg_small_no-1
        neg_small_val,neg_big_val=e.evaluate(eq,neg_small_no),neg_small_val
        count+=1
    if count>60:
        return {0: "ERROR111"}

        

#Returns perfectly formatted string
def getStructuredList(l,eff):
    m=[]
    n=[]
    for i in l:
        for j in i:
            n.append(str(j).ljust(eff+10," "))
        m.append(n)
        n=[]
    return m

