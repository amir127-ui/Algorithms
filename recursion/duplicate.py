str = input("String?")

        
def dup(s):
    length = len(s)
    if length == 0: return True
    if length % 2 != 0: return False
    a = length // 2
    if s[0:a] != s[a:length]: return False
    return dup(s[1:a])

print(dup(str))
