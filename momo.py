def mostVal(m,n,weights,vals):
    dp = [ 0 for _ in range(m+1)]
    for i in range(1,n+1):
        for j in range(m,0,-1):
            w = weights[i-1]
            v = vals[i-1]
            if j >= w:
                dp[j] = max(dp[j],dp[j-w]+v)
    return dp[-1]

# m,n = map(int,raw_input().split())
# weights = []
# vals = []
# for i in range(n):
#     temp = list(map(int,raw_input().split()))
#     weights.append(temp[0])
#     vals.append(temp[1])
#
# res = mostVal(m,n,vals,weights)
# print res

def newpath(source,target):
    try:
        source = source.split('/')
        newpath = '/'.join(source[-3:])
    except:
        return -1
    return target+'/'+newpath

# source = raw_input()
# target = raw_input()
# res = newpath(source,target)
# print res

def compare(op1, op2):

    return op1 in ["*", "/"] and op2 in ["+", "-"]


def getvalue(num1, num2, operator):

    num1 = float(num1)
    num2 = float(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2


def process(data, opt):

    operator = opt.pop()
    num2 = data.pop()
    num1 = data.pop()
    data.append(getvalue(num1, num2, operator))


def calculate(s):

    data = []
    opt = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            start = i
            while i + 1 < len(s) and s[i + 1].isdigit():
                i += 1
            data.append(int(s[start: i + 1]))
        elif s[i] == ")":
            while opt[-1] != "(":
                process(data, opt)
            opt.pop()
        elif not opt or opt[-1] == "(":
            opt.append(s[i])
        elif s[i] == "(" or compare(s[i], opt[-1]):
            opt.append(s[i])
        else:
            while opt and not compare(s[i], opt[-1]):
                if opt[-1] == "(":
                    break
                process(data, opt)
            opt.append(s[i])
        i += 1
    while opt:
        process(data, opt)
    res = data.pop()
    return res


s = raw_input()
res = calculate(s)
print "%.2f" % res

