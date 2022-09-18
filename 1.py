for i in range(int(input())):
    s = input().lower()

    
    print("It is a palindrome" if s == s[-1::-1] else "It is not a palindrome")
