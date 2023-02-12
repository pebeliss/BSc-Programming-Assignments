"""
The function anagrams() gets a string consisting of at most 8 letters (a-z) 
as its input and outputs effectively all the anagrams of the input string.
The function recursion() is a help function that finds all the anagrams recursively.
"""

def recursion(anag, string, n, m, list_of_anag):
    if m == n:
        if anag not in list_of_anag:
            list_of_anag.append("".join(anag))
    else:
        for merkki in string:
            recursion(anag+merkki, string.replace(merkki, "", 1), n, m+1, list_of_anag)
 
def anagrams(string):
    list_of_anag = []
    n = len(string)
    recursion("", string, n, 0, list_of_anag)
    list_of_anag.sort()
    return list_of_anag


if __name__ == "__main__":
    print(anagrams("ab")) # [ab,ba]
    print(anagrams("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(anagrams("aybabtu"))) # 1260
