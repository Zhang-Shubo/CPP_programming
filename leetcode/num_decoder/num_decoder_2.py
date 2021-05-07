import copy

class Node:
    def __init__(self, ch="root"):
        self.char = ch
        self.children = []

class Tree:
    def __init__(self):
        self.root = Node()

res = []
def recrusive(num_str, start, end, token_list):
    if len(num_str[start:end]) <= 1:
        if num_str[start:end]:
            token_list.append(num_str[start:end])
        res.append(token_list)
        return
    token_n= copy.deepcopy(token_list)
    if num_str[start] == "1":
        token_n.append(num_str[start: start+2])
        recrusive(num_str, start+2, end, token_n)
        

    elif num_str[start] == "2" and int(num_str[start + 1]) <= 6:
        token_n.append(num_str[start: start+2])
        recrusive(num_str, start+2, end, token_n)
    
    token_n2 = copy.deepcopy(token_list)
    token_n2.append(num_str[start: start+1])
    recrusive(num_str, start+1, end, token_n2)
    

s = "412345123"
recrusive(s, 0, len(s), [])
print(len(res))
