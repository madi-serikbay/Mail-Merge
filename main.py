#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# Method 1, Using read() function
# with open("Input/Names/Invited_names.txt") as data_names:
#     invited_names = data_names.read()
#
#     names_list = []
#     n = ""
#     for name in invited_names:
#         if name != "\n":
#             n += name
#         elif name == "\n":
#             names_list.append(n)
#             n = ""
#
# with open("Input/Letters/starting_letter.txt") as data_letter:
#     starting_letter = data_letter.read()
#
# for name in names_list:
#     x = starting_letter.replace("[name]", name)
#     with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
#         file.write(x)


# Method 2, Using read_lines() function
with open("Input/Names/invited_names.txt") as data_invited_names:
    invited_names = data_invited_names.readlines()

with open("Input/Letters/starting_letter.txt") as data_starting_letter:
    starting_letter = data_starting_letter.read()

names = []
for name in invited_names:
    names.append(name.strip())

for name in names:
    x = starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(x)

