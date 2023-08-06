# Longest Common Subsequence

def LCS(str1: str, str2: str) -> None:
    m: int = len(str1)
    n: int = len(str2)
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    index = L[m][n]
    res = ""
    i = m
    j = n

    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            res = str1[i - 1] + res
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(f"string 1 : {str1}\nstring 2 : {str2}")
    print(f"LCS: {res}")


X = "ACADB"
Y = "CBDA"

LCS(X, Y)
