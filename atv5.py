'''Escreva uma função que:
Receba uma frase como parâmetro.
Retorne uma nova frase com cada palavra com as letras invertidas.
'''

class PhraseReverser:
    def __init__(self, phrase):
        self.phrase = phrase
    
    def reverse_words(self):
        words = self.phrase.split()
        reversed_words = [word[::-1] for word in words]
        return ' '.join(reversed_words)

def main():
    phrase = input("Enter a phrase: ")
    reverser = PhraseReverser(phrase)
    reversed_phrase = reverser.reverse_words()
    print(f"Reversed phrase: {reversed_phrase}")

if __name__ == "__main__":
    main()