from Rules import RuleMap
import itertools

class RegularSoundChange:
    POSITIONS = ["Initial", "Medial", "Final"]
    rules = {}
    consonants = set()


    def __init__(self, RuleMapper):
        self.rules = RuleMapper.rulemap
        self.consonants = RuleMapper.consonants

    def JoinCombinations(self, words, replacements):
        combinations = list(itertools.product(words, replacements))
        for i in range(len(combinations)):
            combinations[i] = "".join(l for l in combinations[i])
        return combinations

    def JoinLetter(self, words, letter):
        for i in range(len(words)):
            words[i] = words[i] + letter
        return words

    # Core algorithm is here.
    def Generate(self, word, language):
        pindex = 0
        new_words = []
        for letter in word:
            if letter in self.consonants:
                replacements = self.rules[letter][language][self.POSITIONS[pindex]]
                if len(replacements) > 0 and len(new_words) > 0:
                    new_words = self.JoinCombinations(new_words, replacements)
                elif len(replacements) == 0 and len(new_words) > 0:
                    new_words = self.JoinLetter(new_words, letter)
                else:
                    new_words = replacements
            elif len(new_words) == 0:
                new_words = [letter]
            else:
                new_words = self.JoinLetter(new_words, letter)
        return new_words


    def GetHungarian(self, word):
        return self.Generate(word, "Hungarian")


    def GetKhanty(self, word):
        return self.Generate(word, "Khanty")


    def GetMansi(self, word):
        return self.Generate(word, "Mansi")


    def GetSumerian(self, word):
        return self.Generate(word, "Sumerian")
