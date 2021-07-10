from itertools import groupby

range_bound = (356261, 846330)

state_rule = [
    #not decreasing
    lambda s: 
        all(int(s[i]) <= int(s[i+1]) for i in range(len(s)-1)),

    #Two equal.
    lambda s: 
        any(s[i] == s[i+1] for i in range(len(s)-1)),
    
    #group.
    lambda s: 
        any(len(list(v)) == 2 for _, v in groupby(s))
]

def test(num, state_rule):
    return all(f(str(num)) for f in state_rule)

def solution(range_bound, state_rule):
    return sum(1 for i in range(range_bound[0], range_bound[1]+1) if test(i, state_rule))

def one():
    return solution(range_bound, state_rule[:2])

def two():
    return solution(range_bound, state_rule[::2])

if __name__ == "__main__":
    print(one())
    print(two()) 