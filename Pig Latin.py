sen = input("What will we be hiding today? Without capitalization please, I'm too tired: ").lower()
word_list = sen.split()

for i, single_word in enumerate(word_list):

    if single_word[0] in 'aeiouAEIOU':
        word_list[i] = word_list[i] + "yay"
    else:
        has_vowel = False

        for j, letter in enumerate(single_word):
            if letter in 'aeiouAEIOU':
                word_list[i] = single_word[j:] + single_word[:j] + "ay"
                has_vowel = True
                break

        if (has_vowel == False):
            word_list[i] = single_word[j:] + single_word[:j] + "ay"

result = ' '.join(word_list)
print("This is your sentence: ", result)