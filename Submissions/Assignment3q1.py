#block world problem using dfs
import copy;

initial = [['A'],['B','C'],[]];
goal = [[],[],['A','B','C']];

def generate(initial):
    for i in range(len(initial)):
        for j in range(len(initial)):
            if i != j:
                if len(initial[i]) > 0:
                    temp = copy.deepcopy(initial[i]);
                    temp1 = copy.deepcopy(initial[j]);
                    print(type(temp1))
                    print(temp1)
                    temp1.append(temp.pop());
                    if temp1 not in initial:
                        yield temp1;

def check(initial,goal):
    if initial == goal:
        return True;
    else:
        return False;

def dfs(initial,goal):
    stack = [];
    stack.append(initial);
    while len(stack) > 0:
        temp = stack.pop();
        if check(temp,goal):
            return temp;
        else:
            for i in generate(temp):
                stack.append(i);
    return False;

print(dfs(initial,goal));
