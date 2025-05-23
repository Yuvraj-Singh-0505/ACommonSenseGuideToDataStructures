votes = {}

def add_vote(candidate):
    if candidate in votes:
        votes[candidate] += 1  
    else:
        votes[candidate] = 1  

def count_votes():
    return votes

add_vote("Thomas Jefferson")
add_vote("John Adams")
add_vote("John Adams")
add_vote("Thomas Jefferson")
add_vote("John Adams")

print("Final vote count:")
for candidate, count in count_votes().items():
    print(candidate + ":", count)
