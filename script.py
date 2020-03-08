import json
import re
import math  
p_set = []
nfa = dict()
dfa = dict()
def final_accept_states(dfa_final,nfa_final):
    i=0
    ins = 0
    x = []
    for i in dfa_final:
        for v in i:
            if v in nfa_final:
                ins = v
                if ins != []:
                    x.append(i)
    return x  

def generate_t_function(t_func_nfa,input_alphabet,PowerSet_dfa):
    b = []
    for i in PowerSet_dfa:
        for j in input_alphabet:
            a = []
            for k in i:
                for l in t_func_nfa:
                    if k == l[0] and j == l[1]:
                        for m in l[2]:
                            if m not in a:
                                a.append(m)
            b.append([i, j, a])
    return b

     
    
def make_PowerSet(set,set_size):
    pow_set_size = (int) (math.pow(2, set_size))
    # s = list(set)
    # return chain.from_set(combinations(s, r) for r in range(len(s)+1))
    counter = 0 
    j = 0 
    s=list()
    for counter in range(0, pow_set_size): 
        each_el=list()
        for j in range(0, set_size):  
            if((counter & (1 << j)) > 0):
                each_el.append(set[j])
        s.append(each_el)
    return s

if __name__ == "__main__":
    nfa = dict()
    dfa = dict()
    with open('input.json', 'r') as f:
        nfa = json.load(f)

    dfa["states"] = pow(2, nfa["states"])
    
    dfa["letters"] = nfa["letters"]
    
    PowerSet_dfa = make_PowerSet(list(range(0, nfa["states"])), nfa['states'])
    # print(PowerSet_dfa)
    dfa["t_func"] = generate_t_function(nfa["t_func"], nfa["letters"], PowerSet_dfa)

    dfa["start"] = nfa["start"]
    dfa["final"] = list()
    dfa["final"] = final_accept_states(PowerSet_dfa,nfa["final"])
 
    with open('output.json', 'w') as outfile:
        json.dump(dfa, outfile, indent=3)

