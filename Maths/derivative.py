import Maths.evaluate as e
import Maths.exfunc as func
import Maths.functions as f
#returns the deerivated value of a function
def getDerivation(equation,value):
    h=0.00000001
    a=e.evaluate(equation,value+h)
    if (a in f.errors.keys()):
        return a
    b=e.evaluate(equation,value)
    if (b in f.errors.keys()):
        return b
    derivation=(a-b)/h
    return derivation
