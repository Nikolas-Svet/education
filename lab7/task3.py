class AnimalTree:
    def __init__(self, question=None):
        self.question = question
        self.yes = None
        self.no = None

def play_game(tree):
    if not tree.yes and not tree.no:
        print(f"Это {tree.question}?")
        answer = input("Да/Нет: ").lower()
        if answer == "да":
            print("Я угадал!")
        else:
            new_animal = input("Какое животное вы загадали? ")
            new_question = input(f"Какой вопрос позволит отличить {new_animal} от {tree.question}? ")
            tree.yes = AnimalTree(new_animal)
            tree.no = AnimalTree(tree.question)
            tree.question = new_question
    else:
        answer = input(f"{tree.question} (Да/Нет): ").lower()
        if answer == "да":
            play_game(tree.yes)
        else:
            play_game(tree.no)

root = AnimalTree("Это млекопитающее?")
root.yes = AnimalTree("кошка")
root.no = AnimalTree("змея")
play_game(root)
