import pandas

SCRIPT_ACTIVE = True
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {
    row.letter:row.code for (index, row) in alphabet_df.iterrows()
}
while SCRIPT_ACTIVE:
    user_input = input("Enter a word: ")
    try:
        NATO_TRANSLATION = [
            alphabet_dict[letter] for letter in user_input.upper()
        ]
    except KeyError:
        print("Only letters, please.")
    else:
        print(NATO_TRANSLATION)
