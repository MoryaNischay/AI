q = []
visited = []
def display(s):
    for i in s:
        print(i)
    print("-----------------------------------")

def emptybox(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == 0:
                return ([i, j])