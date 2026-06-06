import random

subjects = [
    "The server",
    "My neighbor",
    "A government agency",
    "The intern",
    "My future self",
    "The printer",
    "A pigeon",
    "The IT department",
    "An unusually determined raccoon",
    "Someone from accounting"
]

actions = [
    "misplaced",
    "accidentally archived",
    "reorganized",
    "confiscated",
    "scheduled a meeting about",
    "converted into a spreadsheet",
    "sent to legal",
    "rejected",
    "encrypted",
    "left in a taxi"
]

objects = [
    "the project",
    "my report",
    "the budget",
    "the evidence",
    "the documentation",
    "the assignment",
    "the prototype",
    "the entire database",
    "the backup plan",
    "the presentation"
]

reasons = [
    "during routine maintenance",
    "for tax purposes",
    "by mistake",
    "to improve efficiency",
    "after a misunderstanding",
    "without proper authorization",
    "for reasons nobody can explain",
    "according to company policy",
    "during a fire drill",
    "while trying to fix something else"
]

print("Random Excuse Generator")
print("Press Enter for an excuse or type 'q' to quit.\n")

while True:
    if input("> ").lower() == "q":
        break

    excuse = (
        f"{random.choice(subjects)} "
        f"{random.choice(actions)} "
        f"{random.choice(objects)} "
        f"{random.choice(reasons)}."
    )

    print("\n" + excuse + "\n")