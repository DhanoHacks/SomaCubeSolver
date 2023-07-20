from z3 import *
pieces = []
pieces.append([list("FEEV"),list("CFEV"),list("FFEE"),list("CFFE")]) #1
pieces.append([list("EEEV"),list("FFEV"),list("CFEE"),list("CFFF")]) #2
pieces.append([list("FEEV"),list("CFFE")])                           #3
pieces.append([list("FEVV"),list("FEEE"),list("CFEE"),list("CFFF")]) #4
pieces.append([list("FEEV"),list("CFEV"),list("FFEE"),list("CFFE")]) #5
pieces.append([list("EEVV"),list("FEEV"),list("FFEE"),list("CFFE")]) #6
pieces.append([list("EEV"),list("FEV"),list("FEE"),list("FFE"),list("CFE"),list("CFF")]) #7

s = Solver()
positionvars = []
fvars = []
evars = []
vvars = []
cvars = []
for i in range(len(pieces)):
    positionvar = Int(f'x_{i+1}')
    positionvars.append(positionvar)
    fvar = Int(f'f_{i+1}')
    fvars.append(fvar)
    evar = Int(f'e_{i+1}')
    evars.append(evar)
    vvar = Int(f'v_{i+1}')
    vvars.append(vvar)
    cvar = Int(f'c_{i+1}')
    cvars.append(cvar)
    s.add(positionvar>=0)
    s.add(positionvar<len(pieces[i]))
    for j in range(len(pieces[i])):
        s.add(Implies(positionvar == j,And(fvar == pieces[i][j].count("F"),evar == pieces[i][j].count("E"),vvar == pieces[i][j].count("V"),cvar == pieces[i][j].count("C"))))
s.add(Sum(fvars) == 6)
s.add(Sum(evars) == 12)
s.add(Sum(vvars) == 8)
s.add(Sum(cvars) == 1)

numsols = 0
with open("solutions.txt","w") as f:
    while s.check() == sat:
        numsols += 1
        m = s.model()
        andclause = []
        line = []
        for positionvar in positionvars:
            line.append(str(m[positionvar]))
            andclause.append(positionvar == m[positionvar])
        s.add(Not(And(andclause)))
        f.write(" ".join(line)+"\n")

print(f"found {numsols} solutions")
        
