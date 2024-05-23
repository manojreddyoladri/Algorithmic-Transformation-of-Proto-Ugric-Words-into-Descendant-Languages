import csv


class RuleMap:
    RULE_SPLIT = ", "
    rulemap = {}
    consonants = set()


    def __init__(self, rules):
        for rule in rules:
            ugric = rule["Ugric"]
            self.consonants.add(ugric)
            if ugric not in self.rulemap:
                self.SetupDictTree(ugric)
            position = rule["Position"]
            self.rulemap[ugric]["Hungarian"][position] = rule["Hungarian"].split(self.RULE_SPLIT)
            self.rulemap[ugric]["Khanty"][position] = rule["Khanty"].split(self.RULE_SPLIT)
            self.rulemap[ugric]["Mansi"][position] = rule["Mansi"].split(self.RULE_SPLIT)
            self.rulemap[ugric]["Sumerian"][position] = rule["Sumerian"].split(self.RULE_SPLIT)


    def SetupDictTree(self, UgricKey):
        self.rulemap[UgricKey] = {}
        self.rulemap[UgricKey]["Hungarian"] = {}
        self.rulemap[UgricKey]["Hungarian"]["Initial"] = []
        self.rulemap[UgricKey]["Hungarian"]["Medial"] = []
        self.rulemap[UgricKey]["Hungarian"]["Final"] = []
        self.rulemap[UgricKey]["Khanty"] = {}
        self.rulemap[UgricKey]["Khanty"]["Initial"] = []
        self.rulemap[UgricKey]["Khanty"]["Medial"] = []
        self.rulemap[UgricKey]["Khanty"]["Final"] = []
        self.rulemap[UgricKey]["Mansi"] = {}
        self.rulemap[UgricKey]["Mansi"]["Initial"] = []
        self.rulemap[UgricKey]["Mansi"]["Medial"] = []
        self.rulemap[UgricKey]["Mansi"]["Final"] = []
        self.rulemap[UgricKey]["Sumerian"] = {}
        self.rulemap[UgricKey]["Sumerian"]["Initial"] = []
        self.rulemap[UgricKey]["Sumerian"]["Medial"] = []
        self.rulemap[UgricKey]["Sumerian"]["Final"] = []

