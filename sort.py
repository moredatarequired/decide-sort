import heapq

options = [
    "Compose consulting email",
    "Watch next section of Docker course",
    "Come up with next week's schedule",
    "Write task list for tomorrow",
    "Respond to Benjamin's email",
    "Laundry",
    "Go to sleep"
]


class Choice:
    def __init__(self, description):
        self.description = description

    def __lt__(self, other):
        print(f"A: {self.description}")
        print(f"B: {other.description}")
        choice = input("A or B? ")
        return len(choice) == 0 or choice.lower()[0] == "a"

    def __str__(self):
        return self.description


options = [Choice(o) for o in options]

heapq.heapify(options)

print("\n".join(str(o) for o in options))
