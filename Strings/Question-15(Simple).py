# Question 135: Reverse the words in a given string.
def reverse_words_optimal(s):
    stack = []
    word = ""
    for char in s:
        if char != " ":
            word += char
        else:
            if word:
                stack.append(word)
                word = ""
    if word:
        stack.append(word)

    reversed_str = ""
    while stack:
        reversed_str += stack.pop() + " "
    return reversed_str[:-1]

string = "the sky is blue"

print(f"Optimal: {reverse_words_optimal(string)}")

string = "  hello world  "

print(f"Optimal: {reverse_words_optimal(string)}")