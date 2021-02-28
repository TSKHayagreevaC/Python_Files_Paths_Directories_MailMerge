# Reading Through A FIle...

# with open("my_files.txt") as file:
#     # file = open('my_files.txt')
#     contents = file.read()
#     print(contents)

# Writing Through A File...
#
# with open("my_files.txt", mode="w") as file:
#     file.write("New Text...")

# Appending A File...

# with open("my_files.txt", mode="a") as file:
#     file.write("\nAppended Text...")

# Operating Files From Different Location Such As Desktop...

# with open("/Users/SRIKANTH HAYAGREEVA/OneDrive/Desktop/my_files.txt") as file:
#     # file = open('my_files.txt')
#     contents = file.read()
#     print(contents)

# Mail Merge Code...

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

