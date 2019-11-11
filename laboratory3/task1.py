"""З рядка видалити всі цифри і малі букви."""
q = 0
while q != "-":
    string = input("Enter string:\n")
    for i in range(0, len(string)):
        if string[i].islower() or string[i].isdigit():
            string = string[:i] + " " + string[i + 1:]
    if string.replace(" ", "") == string:
        print(string, "- result")
    else:
        print(string, "- for clarity")
        print(string.replace(" ", ""), "- without spaces")
    q = input("Press <<->> for exit or any button(s) to continue:")
