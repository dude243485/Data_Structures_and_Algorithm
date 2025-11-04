def palindrome(integer):
    s = str(integer)
    for i in range(len(s)):
        if (s[i] != s[len(s) -1 -i]):
            return False
    return True

print(palindrome(12329))
