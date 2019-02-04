# palindrome index checker


a = 'hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'
c = a[::-1]
print c
l = len(a) - 1
print l

for i in range(0, len(a) / 2):
    if a == a[::-1]:
        print -1
    elif a[i] != a[l - i]:
        if (a[i + 1] == a[l - i]) and (a[i + 2] == a[l - i - 1]):
            print i
            i += 1
        elif (a[i] == a[l - i - 1]) and (a[i + 2] == a[l - i - 2]):
            print l - i
            i += 1

"""
a = 0
while a < 6:
    for i in range(9):
        if i == 3:
            break
    print "3 is encountered"
    a += 1

print "loop ended!"
"""




