import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print([i[1].code for i in data.iterrows()])
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
while True:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
        break
    except KeyError:
        print("Sorry, only letters are allowed in alphabet.")
