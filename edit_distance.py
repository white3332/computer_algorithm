def edit_distance(s,t,m,n):
    print(s[:m], t[:n])
    if m == 0: return n
    if n == 0: return m
    
    if s[m-1] == t[n-1]:
        return edit_distance(s,t,m-1,n-1)
    
    return 1 + min(
                edit_distance(s,t,m,n-1),
                edit_distance(s,t,m-1,n),
                edit_distance(s,t,m-1,n-1))
    
s = "bcd"
t = "abc"
m = len(s)
n = len(t)
print("문자열:",s,t)
print("편집거리(분할정복)=", edit_distance(s,t,m,n))