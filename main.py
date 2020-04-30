import pandas as pd
'''
V. 26

q0=A; q1=B; q2=C; q3=D;

d(q0,a)->q1
d(q1,b)->q1
d(q1,a)->q2
d(q0,a)->q0
d(q2,c)->q3
d(q3,c)->q3
'''
arr = [
    'A>a>B',
    'B>b>B',
    'B>a>C',
    'A>a>A',
    'C>c>D',
    'D>c>D'
]


def getNFA(arr):
    nfa = {}
    for el in arr:
        x = el.split('>')
        if not x[0] in nfa:
            nfa[x[0]] = {}

        if not x[1] in nfa[x[0]]:
            nfa[x[0]][x[1]] = ''

        nfa[x[0]][x[1]] += x[2]
    return nfa


def getAutomataStates(nfa):
    states = []
    for x in nfa:
        states.append(x)

    for x in nfa:
        for y in nfa[x]:
            if len(nfa[x][y]) > 1:
                if not nfa[x][y] in states:
                    states.append(nfa[x][y])
            else:
                if not nfa[x][y][0] in states:
                    states.append(nfa[x][y][0])
    return states


def getAutomataMethods(nfa):
    methods = []

    for x in nfa:
        for j in nfa[x]:
            if not j in methods:
                methods.append(j)
    return methods


def convertNFA2DFA(nfa, states, methods):
    dfa = nfa.copy()
    for s in states:
        if not s in dfa:
            separated = list(s)
            for m in methods:
                temp = []

                for sp in separated:
                    if m in dfa[sp]:
                        temp.append(dfa[sp][m])

                if not s in dfa:
                    dfa[s] = {}

                dfa[s][m] = ''.join(set(''.join(temp)))
                states.append(''.join(set(''.join(temp))))

    return dfa


nfa = getNFA(arr)
states = getAutomataStates(nfa)
methods = getAutomataMethods(nfa)
dfa = convertNFA2DFA(nfa, states, methods)

nf = pd.DataFrame(nfa)
nf = nf.fillna("-")
print(nf.transpose())
print('\n')

df = pd.DataFrame(dfa)
df = df.fillna("-")
print(df.transpose())