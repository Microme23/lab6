def uniqueLetters(text):
    letterCounts = {}

    for char in text:
        if char.isalpha():
            charLower = char.lower()
            letterCounts[charLower] = letterCounts.get(charLower, 0) + 1

    unique = [char for char, count in letterCounts.items() if count == 1]
    print("Літери, які зустрічаються лише один раз:", ", ".join(unique))


text = input("Введіть текст латинськими літерами: ")
uniqueLetters(text)