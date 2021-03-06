print("Mad-libs generator!")
print("")
character = input("Character: ")
thing = input("Something: ")
quote = input("Quote: ")
string = ""

for i in range(len(quote) + 20):
    string += "="

print(string)
print("One day", character, "went to castle and saw", thing + ".")
print('When he saw that', thing, 'he said:', quote)
