import sys

n = int(input().rstrip())

for lab in range(n):
    size = int(input().rstrip())
    lydia = input().rstrip()
    
    we = "".join(["S" if c == "E" else "E" for c in lydia])
    print("Case #%s: %s" % (lab +1, we))
