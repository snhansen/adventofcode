import re

with open("input") as f:
    inp = f.read().strip().split("\n")
    

ls = [line.split(": ") for line in inp]
opers = {"+": lambda x,y: x+y, "/": lambda x,y: x//y, "*": lambda x,y: x*y, "-": lambda x,y: x-y, "=": lambda x,y: int(x == y)}


def insert_nums(d):
    d_cp = dict(d)
    for var, expr in list(d.items()):
        if len(expr) == 1:
            val = expr[0]
            for var2, expr2 in d.items():
                if len(expr2) > 1:
                    var3, _, var4 = expr2
                    if var3 == var:
                        d_cp[var2][0] = val
                    elif var4 == var:
                        d_cp[var2][2] = val
            del d_cp[var]
    return d_cp


def reduce_expressions(d):
    d_cp = dict(d)
    for var, expr in d.items():
        if isinstance(expr, list):
            val1, oper, val2 = expr
            if val1.strip("-").isnumeric() and val2.strip("-").isnumeric():
                d_cp[var] = [str(opers[oper](int(val1), int(val2)))]
    return d_cp


# Part 1
res = {var: expr.split(" ") for (var, expr) in ls}
while True:
    res = insert_nums(res)
    res = reduce_expressions(res)
    if len(res) == 1:    
        break

print(int(res["root"][0]))
          

# Part 2    
res = {var: expr.replace(" ", "") for (var, expr) in ls}
res["humn"] = "X"

# Get expressions
exprs = []
for var in res["root"].split("+"):
    expr = res[var]
    while True:
        m = re.search("[a-z]+", expr)
        if not m:
            break
        insert = res[m.group(0)]
        expr = expr[:m.start(0)] + "(" + res[m.group(0)] + ")" + expr[m.end(0):]
    exprs.append(expr)


# Evaluate parentheses.
lhs, rhs = exprs
lhs = lhs.replace("(X)", "X")

start = 0
done = False
while not done:
    op, cl = None, None
    for i in range(start, len(lhs)):
        if lhs[i] == ")":
            cl = i
            break
        if i == len(lhs)-1:
            done = True
    if cl == None:
        break
    for j in range(0, i):
        if lhs[i-j-1] == "(":
            op = i-j-1
            break
    len_bef = len(lhs)
    if "X" not in (s := lhs[(op+1):cl]):
        lhs = lhs[0:op] + str(int(eval(s))) + lhs[cl+1:]
    if len_bef == len(lhs):
        start += 1


# Isolate X.
opposite = {"*": "/", "+": "-", "/": "*", "-": "+"}

def reduce_expr(lhs, rhs):
    if lhs[0] != "(":
        m = re.search("[\+\-\/\*]", lhs)
        term1 = lhs[:m.start(0)]
        term2 = lhs[m.end(0):]
        oper = m.group(0)
        if "X" in term1:
            lhs = term1
            rhs = "(" + rhs + ")" + opposite[oper] + term2
        else:
            if oper == "-":
                rhs = term1 + "-" + "(" + rhs + ")"
                lhs = term2
            elif oper == "+":
                lhs = term2
                rhs = "(" + rhs + ")" + "-" + term1
            elif oper == "*":
                lhs = term2
                rhs = "(" + rhs + ")" + "/" + term1
            elif oper == "/":
                rhs = term1 + "/" + "(" + rhs + ")"
                lhs = term2
    elif lhs[-1] != ")":
        m = re.search("[\+\-\/\*]", lhs[::-1])
        term1 = lhs[:(len(lhs)-m.end(0))]
        term2 = lhs[(len(lhs)-m.start(0)):]
        oper = m.group(0)
        lhs = term1
        rhs = "(" + rhs + ")" + opposite[oper] + term2
    return lhs, rhs
 

while True:
    if lhs == "X":
        break
    while lhs[0] == "(" and lhs[-1] == ")":
        lhs = lhs[1:-1]
    lhs, rhs = reduce_expr(lhs, rhs)

print(int(eval(rhs)))