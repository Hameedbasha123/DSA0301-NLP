def parse_cfg(sentence):
    words = sentence.lower().split()

    # Grammar:
    # S -> NP VP
    # NP -> Det N
    # VP -> V NP
    # Det -> the | a
    # N -> dog | cat | bone
    # V -> chased | found

    if len(words) != 5:
        return "Invalid Sentence"

    det1, noun1, verb, det2, noun2 = words

    # Check NP -> Det N
    if det1 not in ["the", "a"] or noun1 not in ["dog", "cat", "bone"]:
        return "Invalid Sentence"

    # Check V
    if verb not in ["chased", "found"]:
        return "Invalid Sentence"

    # Check second NP -> Det N
    if det2 not in ["the", "a"] or noun2 not in ["dog", "cat", "bone"]:
        return "Invalid Sentence"

    # Construct parse tree
    tree = f"""
S
├── NP
│   ├── Det
│   │   └── {det1}
│   └── N
│       └── {noun1}
└── VP
    ├── V
    │   └── {verb}
    └── NP
        ├── Det
        │   └── {det2}
        └── N
            └── {noun2}
"""

    return tree


# Main program
sentence = input("Enter a sentence: ")

result = parse_cfg(sentence)

print("\nOutput:")
print(result)
