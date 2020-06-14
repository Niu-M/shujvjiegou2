
def ss(str1,str2):

    status = {}

    def f(i,j):

        if str(i)+str(j) in status:
            return status[str(i)+str(j)]

        if i==len(str1) or j == len(str2):
            return 0

        if str1[i] == str2[j]:
            status[str(i) + str(j)] = f(i+1,j+1)+1
            return status[str(i)+str(j)]
        else:
            status[str(i) + str(j)] = max(f(i+1,j),f(i,j+1))
            return status[str(i)+str(j)]
    return f(0,0)

text1 = "abcde"
text2 = "ace"
print(ss(text1,text2))




