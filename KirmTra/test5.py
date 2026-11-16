t = int(input())
for i in range(t):
    s = input()
    st = []
    kt = True
    for c in s:
        if c == '(' or c == '[' or c == '{':
            st.append(c)
        else:
            if len(st) == 0:
                kt = False
                break
            x = st.pop()
            if c == ')' and x != '(':
                kt = False
                break
            if c == ']' and x != '[':
                kt = False
                break
            if c == '}' and x != '{':
                kt = False
                break
    if len(st) != 0:
        kt = False
    if kt:
        print("YES")
    else:
        print("NO")
