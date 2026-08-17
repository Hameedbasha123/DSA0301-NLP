def check_agreement(subject, verb):

    # Feature structures
    subjects = {
        "he": ("singular", "third"),
        "she": ("singular", "third"),
        "it": ("singular", "third"),
        "we": ("plural", "first")
    }

    verbs = {
        "eats": "singular",
        "sleeps": "singular",
        "eat": "plural",
        "sleep": "plural"
    }

    subject = subject.lower()
    verb = verb.lower()

    # Check whether subject and verb are valid
    if subject not in subjects or verb not in verbs:
        return False

    subject_number = subjects[subject][0]
    verb_number = verbs[verb]

    # Agreement occurs when number matches
    return subject_number == verb_number


# Main program
subject = input("Enter subject: ")
verb = input("Enter verb: ")

result = check_agreement(subject, verb)

print("\nOutput:")
print(result)
