def Check_Vow(word, vowels):
    final = [each for each in word if each in vowels]
    print(len(final))
    print(f"Vowels {word} are: \n{final}")
word = input("What word do youy wanna check?\n")
vowels = "AaIiEeOoUu"
Check_Vow(word, vowels);
