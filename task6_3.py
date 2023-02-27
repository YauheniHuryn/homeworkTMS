class Cipher:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_alphabet = alphabet.copy()

    def __init__(self, cipher):
        self.cipher = cipher

        for _ in self.cipher[::-1]:

            self.new_alphabet.remove(_)
            self.new_alphabet.insert(0, _)

    def encode(self, encode_text):
        decode_list = []
        for _ in encode_text:
            if _.lower() in self.new_alphabet:
                index = self.alphabet.index(_.lower())
                if _.isupper():
                    decode_list.append(self.new_alphabet[index].upper())
                else:
                    decode_list.append(self.new_alphabet[index])
            else:
                decode_list.append(_)
        return ''.join(decode_list)

    def decode(self, decode_text):
        encode_list = []
        for _ in decode_text:
            if _.lower() in self.alphabet:
                index = self.new_alphabet.index(_.lower())
                if _.isupper():
                    encode_list.append(self.alphabet[index].upper())
                else:
                    encode_list.append(self.alphabet[index])
            else:
                encode_list.append(_)
        return ''.join(encode_list)


c = Cipher('crypto')

word1 = c.encode('Hello world')
word2 = c.decode('Fjedhc dn atidsn')
# print(c.new_alphabet)
print(word1)
print(word2)




