
global count 
count = 1
def recrusive(num_str, start, end):
    if len(num_str[start:end]) <= 1:
        return

    if num_str[start] == "1":
        global count
        count = count + 1
        recrusive(num_str, start+2, end)
    elif num_str[start] == "2" and int(num_str[start + 1]) <= 6:
        count = count + 1
        recrusive(num_str, start+2, end)
    recrusive(num_str, start+1, end)

s = "12345123"
recrusive(s, 0, len(s))
print(count)
