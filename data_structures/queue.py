"""
Queue Data Structure (with Real-World Use Case)
===============================================

This module demonstrates:

1. A basic queue using Python lists (FIFO: First In, First Out)
2. A real-world use case: a simple matchmaking system like in online games

Use Cases:
- Task scheduling
- Breadth-first search (BFS) in graphs
- Game matchmaking (players waiting in line)
"""

# -------------------------------
# ✅ Basic Queue Implementation
# -------------------------------
class Queue:
    """
    A simple queue using Python lists.

    Methods:
        - enqueue(item): Add item to the end
        - dequeue(): Remove item from the front
        - is_empty(): Check if queue is empty
        - size(): Return current number of items
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("dequeue from empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def __repr__(self):
        return f"Queue(front -> back): {self.items}"


# --------------------------------------
# 🎮 Advanced Example: Matchmaking Queue
# --------------------------------------
class Player:
    """
    Represents a player in a game lobby.

    Attributes:
        - name (str): Player's name
        - skill_level (int): Optional skill rating (1–10)
    """
    def __init__(self, name, skill_level=5):
        self.name = name
        self.skill_level = skill_level

    def __repr__(self):
        return f"{self.name}(Skill {self.skill_level})"


class MatchmakingQueue:
    """
    A matchmaking system that forms matches from players in a queue.

    Players are matched in groups of 2. You can customize group size.

    Methods:
        - add_player(): Enqueues a player
        - form_match(): Dequeues 2 players to form a match
        - show_queue(): Displays current waiting players
    """
    def __init__(self):
        self.queue = Queue()

    def add_player(self, player):
        print(f"🎮 Player joined: {player}")
        self.queue.enqueue(player)

    def form_match(self):
        """Form a match with the first 2 players in the queue."""
        if self.queue.size() >= 2:
            p1 = self.queue.dequeue()
            p2 = self.queue.dequeue()
            print(f"🔥 Match formed: {p1} vs {p2}")
        else:
            print("Not enough players to form a match.")

    def show_queue(self):
        """Display the current queue of waiting players."""
        print("🧑‍🤝‍🧑 Waiting Queue:", self.queue)


# ----------------------
# 🧪 Run Demo Scenarios
# ----------------------
if __name__ == "__main__":
    print("✅ Basic Queue Example")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue size:", q.size())
    print("Dequeued item:", q.dequeue())
    print("Queue after dequeue:", q)
    print()

    print("🎮 Game Matchmaking Simulation")
    lobby = MatchmakingQueue()
    lobby.add_player(Player("Alice", 7))
    lobby.add_player(Player("Bob", 6))
    lobby.add_player(Player("Charlie", 8))
    lobby.add_player(Player("Diana", 9))
    lobby.show_queue()
    lobby.form_match()
    lobby.form_match()
    lobby.form_match()  # not enough players
    lobby.show_queue()
