def decrypt_caeser_cypher(sentence, key):
    sentence = sentence.lower()
    archive = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""

    for letter in sentence:
        if letter in archive:
            letter_index = (archive.find(letter) - key) % len(archive)
            decrypted = decrypted + archive[letter_index]
        else:
            decrypted = decrypted + letter

    return decrypted

print(decrypt_caeser_cypher("Mjqqt Btwqi",5))