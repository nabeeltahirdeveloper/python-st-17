# ================string
stringType = "string"
stringTwo = 'string'
stringThree = '''string'''
stringFour = """string"""

myName = "I'm Nabeel"
my_name = 'this is "Nabeel Tahir"'
myNewName = """I'm Nabeel and this is "Nabeel" """

# =========================merge string

string_one = "Nabeel"
string_two = "Tahir"
final_string = f"My Name is {string_one} {string_two}"
print(final_string)

# =========================string indexing
print(len(string_one))
print(string_one[5])


new_string = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
print(new_string[5])
newLimitedString = new_string[0:10] + "..."
print(newLimitedString)

print(new_string)
