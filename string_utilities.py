def count_vowels(s):
    return sum(1 for ch in s if ch.lower() in "aeiou")

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

s = input("Enter a string: ")

print("Vowels:", count_vowels(s))
print("Reverse:", reverse_string(s))
print("Palindrome:", is_palindrome(s))