def is_palindrome(s):
   
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
