import pyperclip #you have to install pyperclip first
while True:
    s = input("Enter value: ")
    l2 = [ord(c) for c in s]
    l2 = str(l2)
    l2 = l2.replace("[", "")
    l2 = l2.replace("", "")
    l2 = l2.replace(",", "")
    l2 = l2.replace("]", "")
    print('Copied to clipboard.')
    print(l2)
    pyperclip.copy(l2)
    spam = pyperclip.paste()
