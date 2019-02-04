from collections import deque
import sys

str1 = str(sys.stdin.readline().strip())
str2 = str(sys.stdin.readline().strip())

def findCount(small,big):
    count = 0
    a = big.find(small)
    vect = [big[0:a],big[a + len(small):]]
    for i in range(len(vect)):
        nsub = list(small) + list(vect[i])
        items = deque(nsub)
        for j in range(len(nsub)):
            items.rotate(1)
            it = ''.join(list(items))
            if it in big:
                count += 1

    sys.stdout.write(str(count))


if len(str1) > len(str2):
    findCount(str2,str1)
else:
    findCount(str1,str2)


"""
zswcgnrhjroxzlsbkufcnarsyyntvlmefsvbmvoxahqkeasofnqsrmywytzjjamaipisgfgccelgdzbznaynnrrcmrpdwprstwtc
uxtmfimpzvhmarltpkzcjtdituvmtbpypwsjyqzkhiqsxetpdgwuobvijndfntzarrrrrtrtinhlqqknehbiakjnglfiudgokzymevjkttpvocifknkddffddvexvvtydazqehjqpswbpzryxthgwyjjaiigvkogjuirghctzmrhurpsfyxrlcfavesxelorgqcoqqee
513
"""