class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_person(self, name):
        person = Person(name)
        self.nodes[name] = person

    def add_friendship(self, name1, name2):
        if name1 in self.nodes and name2 in self.nodes:
            self.nodes[name1].add_friend(self.nodes[name2])
            self.nodes[name2].add_friend(self.nodes[name1])

    def display(self):
        for name, person in self.nodes.items():
            friends_names = [friend.name for friend in person.friends]
            print(f"{name}: {friends_names}")

graph = Graph()
graph.add_person("Alice")
graph.add_person("Bob")
graph.add_person("Diana")
graph.add_person("Fred")

graph.add_friendship("Alice", "Bob")
graph.add_friendship("Alice", "Diana")
graph.add_friendship("Alice", "Fred")
graph.add_friendship("Bob", "Diana")
graph.add_friendship("Diana", "Fred")

graph.display()
