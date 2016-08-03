"""
lossy compression 2:
our removing all vowels compression scheme made so much money in Hawaii that the stuio has bought a sequel.
This time, we're going to read a file and remove the first and last letters of all words that are more than 3 letters.
A word is any adjacent series of letters.
lc2("annakarenina.txt")
"All app amilie are lik, ac nhapp ..."
"""

def lc2(file_name):
    new_file_name = file_name.rstrip(".txt") + "_compressed.txt"
    with open(new_file_name, "w") as file_out:
        with open(file_name, "r") as file_in:
            for line in file_in:
                compressed_line = " ".join([compress_word(word) for word in line.split()])
                file_out.write(compressed_line+ "\n")
    with open(new_file_name, "r") as file_read:
        for line in file_read:
            print(line)


def compress_word(word):
    return word if len(word) <= 3 else word[1:-1]

lc2("anna_karenina.txt")