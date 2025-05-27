class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.visited = False

    def add_friend(self, friend):
        self.friends.append(friend)

    def display_network(self):
        to_reset = [self]
        queue = [self]
        self.visited = True

        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex.name)

            for friend in current_vertex.friends:
                if not friend.visited:
                    friend.visited = True
                    queue.append(friend)
                    to_reset.append(friend)

        for node in to_reset:
            node.visited = False

alice = Person("Alice")
bob = Person("Bob")
carol = Person("Carol")
dave = Person("Dave")

alice.add_friend(bob)
bob.add_friend(alice)
bob.add_friend(carol)
carol.add_friend(bob)
carol.add_friend(dave)
dave.add_friend(carol)

alice.display_network()
