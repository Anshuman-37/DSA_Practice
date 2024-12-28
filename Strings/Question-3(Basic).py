# Question 3: Check if a string is a palindrome.
def is_palindrome(word:str) -> bool:
    start = 0
    end = len(word)-1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

str = "laal"
print(is_palindrome(str))

str1 = "label"
print(is_palindrome(str1))
