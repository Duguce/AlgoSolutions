# -*- coding: utf-8  -*-
abcList = list(map(int, input().split(' ')))
abcList.sort()
abcSort = input()
print(abcList[ord(abcSort[0]) - ord('A')], abcList[ord(abcSort[1]) - ord('A')], abcList[ord(abcSort[2]) - ord('A')],
      sep=' ')
