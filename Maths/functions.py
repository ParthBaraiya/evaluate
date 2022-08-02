import math as m

function={
    "cosec":":",
    "sin":";",
    "cos":'"',
    "sec":"'",
    "tan":">",
    "cot":"<",
    "log":"?",
    }

cfunction={
    "+": "+",
    "-": "-",
    "*": "*",
    "/": "/",
    "^": "^"
    }

symbols=[ "(", ")", "," ,"."]

const={
    "pi":"π",
    "e":"e"
    }


constant_value={
    "π":m.pi,
    "e":m.e
    }


errors={
    "ERROR101": "Invalid Equation",
    "ERROR102": "Invalid Base",
    "ERROR103": "Invalid Content",
    "ERROR104": "Invalid Base for log function: Evaluate to 0",
    "ERROR105": "Invalid Content for log function: Evaluate to 0",
    "ERROR106": "Invalid Base for log function: Evaluate to negative",
    "ERROR107": "Invalid Content for log function: Evaluate to negative",
    "ERROR108": "Derivation evalutes to zero at some point",
    "ERROR109": "Determinant Evaluates to zero at some point",
    "ERROR110": "Invalid Equation: Equation with unsupported constant or function",
    "ERROR111": "Root for this equation is either not exist or at very far in x-axis.",
    "ERROR112": "Invalid Equation: Brackets are not properly ended",
    "ERROR113": "Enter a valid equation (Equation must contain only one constant(i.e. X,Y,Z,etc))"
    }
