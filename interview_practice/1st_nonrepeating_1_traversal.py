# i/p="ABCDBAGHC"
# o/p=D
def create_dictionary(Char_String):
    new_D = {}
    for character in Char_String:
        if character not in new_D:
            new_D.setdefault(character, 1)
        else:
            new_D[character] += 1


def first_nonrepeating(Char_String):


    print (new_D)
Char_String="ABCDBAGHC"
print(first_nonrepeating(Char_String))
#
#     if new_D[character]==1 in new_D.items():
#         return character
# Char_String='ABCDBAGHC'
# print(first_nonrepeating(Char_String))


