import csv
from RegularSoundChange import RegularSoundChange
from Rules import RuleMap

DEBUG = True
INPUT_PATH = "Data/words.txt"
RULES_PATH = "Data/rules.txt"


def LoadInput(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read().split(", ")


def LoadRules(path):
    rules = []
    with open(path, 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter='\t')
        for row in csv_reader:
            rules.append(row)
    return rules


if __name__ == "__main__":
    if DEBUG: print("**********************************")
    if DEBUG: print("*** START REGULAR SOUND CHANGE ***")
    if DEBUG: print("**********************************")
    if DEBUG: print()
    if DEBUG: print("Loading input from,", INPUT_PATH)
    words = LoadInput(INPUT_PATH)
    if DEBUG: print("Load rules from", RULES_PATH)
    RuleMapper = RuleMap(LoadRules(RULES_PATH))
    if DEBUG: print("Generate rule mapping.")
    RSC = RegularSoundChange(RuleMapper)
    if DEBUG: print("Start processing words.")
    for word in words:
        HungarianWords = RSC.GetHungarian(word)
        print(f"Ugric:{word} | Language:Hungarian | Generated:{HungarianWords}")
        KhantyWords = RSC.GetKhanty(word)
        print(f"Ugric:{word} | Language:Khanty | Generated:{KhantyWords}")
        MansiWords = RSC.GetMansi(word)
        print(f"Ugric:{word} | Language:Mansi | Generated:{MansiWords}")
        SumerianWords = RSC.GetSumerian(word)
        print(f"Ugric:{word} | Language:Sumerian | Generated:{SumerianWords}")
    if DEBUG: print()
    if DEBUG: print("********************************")
    if DEBUG: print("*** END REGULAR SOUND CHANGE ***")
    if DEBUG: print("********************************")
