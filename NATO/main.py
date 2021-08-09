student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


data = pandas.read_csv("nato_phonetic_alphabet.csv")


data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

is_on = True

while is_on:
    word = input("Enter a Word\n").upper().replace(" ", "")
    

    try:
        #Normal Way

        # for letter in word:
        #     result.append(f"{letter} : {data_dict[letter]}")
        # print(result)

        result = [data_dict[letter] for letter in word]
        print(f"{result}")

    except KeyError:
        print("Sorry, only letters in the alphabet please")

    else:
        is_on = False

# Angela's way of solving it


# def generate_phonetic():
#     word = input("Enter a Word\n").upper().replace(" ", "")

#     try:
#         result = [data_dict[letter] for letter in word]
    
#     except KeyError:
#          print("Sorry, only letters in the alphabet please")
#          generate_phonetic()


#     else:
#         print(result)

# generate_phonetic()