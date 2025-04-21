# album_management.py
# Written by Gower Campbell

# Learning Objective:
# - Practiced more of my object-oriented programming (OOP) including 
#   class creation, instance/special methods, and object manipulation.
# - Work with lists, sorting, and searching algorithms in Python.
# - Understand how to use Python's built-in functions like 
#  `sort`, `extend`, and `enumerate`.
# - Trying new special methods (dunder methods) to improve my submission.

class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        """Returns a string representation of the Album object."""
        return f"""({self.album_name}, {self.album_artist}, {
            self.number_of_songs})"""

    def __repr__(self):
        """Unambiguous string representation of album (used for debugging)."""
        return f"""Album('{self.album_name}', {self.number_of_songs}, '{
            self.album_artist}')"""

    def __eq__(self, other):
        """Checks if two Album objects are equal based on their attributes."""
        if isinstance(other, Album):
            return (self.album_name == other.album_name and
                    self.number_of_songs == other.number_of_songs and
                    self.album_artist == other.album_artist)
        return False

    def __lt__(self, other):
        """Compares two objects based on the number of songs (for sorting)."""
        if isinstance(other, Album):
            return self.number_of_songs < other.number_of_songs
        return NotImplemented

    def __len__(self):
        """Returns the number of songs in the album."""
        return self.number_of_songs

    def __hash__(self):
        """Allows the Album object to be used in sets and as dictionary keys."""
        return hash((self.album_name, self.number_of_songs, self.album_artist))


# Step 1: Create a list called albums1 and add five Album objects
print("\nStep 1: Creating albums1 list and adding five Album objects.")
albums1 = [
    Album("Alejandro", 9, "Lady Gaga"),
    Album("Rhythm of my Night", 10, "Corona"),
    Album("Insomnia", 12, "Faithless"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("It's Raining Men", 8, "Weather Girls")
]

# Print out the albums1 list
print("\nAlbums1:")
for album in albums1:
    print(album)


# Step 2: Sort the list according to the number_of_songs
print("\nStep 2: Sorting albums1 by the number of songs.")
albums1.sort()
print("\nAlbums1 sorted by number of songs:")
for album in albums1:
    print(album)


# Step 3: Swap the element at index 0 with the element at index 1
print("\nStep 3: Swapping the first and second elements in albums1.")
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nAlbums1 after swapping positions 1 and 2:")
for album in albums1:
    print(album)


# Step 4: Create a new list called albums2
print("\nStep 4: Creating a new list called albums2.")
albums2 = [
    Album("21", 11, "Adele"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("Born to Run", 8, "Bruce Springsteen"),
    Album("Hotel California", 9, "Eagles")
]

# Print out the albums2 list
print("\nAlbums2:")
for album in albums2:
    print(album)


# Step 5: Copy all albums from albums1 into albums2
print("\nStep 5: Copying all albums from albums1 into albums2.")
albums2.extend(albums1)
print("\nAlbums2 after copying albums from albums1:")
for album in albums2:
    print(album)


# Step 6: Add the following two albums to albums2
print("\nStep 6: Adding two more albums to albums2.")
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))
print("\nAlbums2 after adding two more albums:")
for album in albums2:
    print(album)


# Step 7: Sort albums2 alphabetically by album name
print("\nStep 7: Sorting albums2 alphabetically by album name.")
albums2.sort(key=lambda x: x.album_name)
print("\nAlbums2 sorted alphabetically by album name:")
for album in albums2:
    print(album)


# Step 8: Search for the album "Dark Side of the Moon" in albums2
print("\nStep 8: Searching for the album 'Dark Side of the Moon' in albums2.")
search_album = "Dark Side of the Moon"
for index, album in enumerate(albums2):
    if album.album_name == search_album:
        print(f"\nThe album '{search_album}' is at index {index} in albums2.")
        break

# <------Reflection-----> 
# This task helped me practise Object-Oriented Programming (OOP) in Python
# by designing this Album class with a constructor and a __str__ method for 
# better object representation. 

# I feel like I improved my skills in manipulating and organising data using
# lists of objects. I also gained experience with Python’s built-in functions
# like sort, extend, and enumerate, learning to sort lists with custom keys 
# (e.g., number_of_songs or album_name) and search using loops with enumerate.

# A key challenge was correctly implementing the sort method with custom keys,
#  but experimenting with lambda functions helped me overcome it. 
"""

# <------Bibliography-----> 
- Python Like You Mean It:
https://www.pythonlikeyoumeanit.com/Module4_OOP/Special_Methods.html
- W3Schools Python Tutorial: 
https://www.w3schools.com/python/python_lambda.asp
- GeeksforGeeks Python Programming: 
https://www.geeksforgeeks.org/sorting-algorithms-in-python/
"""

