"""
Album Management System

Learning Objectives:
- Advanced Object-Oriented Programming (OOP)
- Data Structure Manipulation
- Error Handling
- Advanced Python Techniques
"""

from typing import List, Optional, Union
from dataclasses import dataclass, field
from enum import Enum, auto
import uuid

class AlbumGenre(Enum):
    """Enumerate possible music genres"""
    POP = auto()
    ROCK = auto()
    ELECTRONIC = auto()
    CLASSICAL = auto()
    JAZZ = auto()
    UNKNOWN = auto()

@dataclass
class Album:
    """
    Comprehensive Album representation with enhanced features
    """
    album_name: str
    album_artist: str
    number_of_songs: int
    genre: AlbumGenre = AlbumGenre.UNKNOWN
    release_year: Optional[int] = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def __post_init__(self):
        """
        Validate album attributes after initialization
        
        Raises:
            ValueError: If input validation fails
        """
        # Validate album name
        if not self.album_name or len(self.album_name) < 1:
            raise ValueError("Album name must not be empty")
        
        # Validate number of songs
        if self.number_of_songs <= 0:
            raise ValueError("Number of songs must be positive")
        
        # Validate release year if provided
        if self.release_year and (self.release_year < 1900 or self.release_year > 2023):
            raise ValueError("Invalid release year")

    def __str__(self) -> str:
        """
        Provide a human-readable string representation
        
        Returns:
            str: Formatted album description
        """
        return (
            f"Album: {self.album_name} "
            f"by {self.album_artist} "
            f"({self.number_of_songs} songs, "
            f"Genre: {self.genre.name})"
        )

    def __repr__(self) -> str:
        """
        Provide a detailed, unambiguous representation
        
        Returns:
            str: Detailed album representation for debugging
        """
        return (
            f"Album(name='{self.album_name}', "
            f"artist='{self.album_artist}', "
            f"songs={self.number_of_songs}, "
            f"genre={self.genre}, "
            f"year={self.release_year})"
        )

    def __eq__(self, other: object) -> bool:
        """
        Compare albums for equality
        
        Args:
            other (object): Another album to compare
        
        Returns:
            bool: Whether albums are equal
        """
        if not isinstance(other, Album):
            return NotImplemented
        return (
            self.album_name == other.album_name and
            self.album_artist == other.album_artist and
            self.number_of_songs == other.number_of_songs
        )

    def __hash__(self) -> int:
        """
        Generate a hash for the album
        
        Returns:
            int: Unique hash value
        """
        return hash((self.album_name, self.album_artist, self.number_of_songs))


class AlbumCollection:
    """
    Manage a collection of albums with advanced operations
    
    Features:
    - Add/remove albums
    - Search and filter
    - Sorting and manipulation
    """
    def __init__(self):
        """Initialize an empty album collection"""
        self._albums: List[Album] = []

    def add_album(self, album: Album) -> None:
        """
        Add an album to the collection
        
        Args:
            album (Album): Album to add
        
        Raises:
            ValueError: If album already exists
        """
        if album in self._albums:
            raise ValueError(f"Album {album.album_name} already exists")
        self._albums.append(album)

    def remove_album(self, album_name: str) -> Optional[Album]:
        """
        Remove an album by name
        
        Args:
            album_name (str): Name of the album to remove
        
        Returns:
            Optional[Album]: Removed album or None
        """
        for album in self._albums:
            if album.album_name == album_name:
                self._albums.remove(album)
                return album
        return None

    def find_album(self, album_name: str) -> Optional[Album]:
        """
        Find an album by name
        
        Args:
            album_name (str): Name of the album to find
        
        Returns:
            Optional[Album]: Found album or None
        """
        return next((album for album in self._albums if album.album_name == album_name), None)

    def sort_by_songs(self, reverse: bool = False) -> List[Album]:
        """
        Sort albums by number of songs
        
        Args:
            reverse (bool): Sort in descending order
        
        Returns:
            List[Album]: Sorted list of albums
        """
        return sorted(self._albums, key=lambda x: x.number_of_songs, reverse=reverse)

    def filter_by_genre(self, genre: AlbumGenre) -> List[Album]:
        """
        Filter albums by genre
        
        Args:
            genre (AlbumGenre): Genre to filter by
        
        Returns:
            List[Album]: Albums of specified genre
        """
        return [album for album in self._albums if album.genre == genre]

    def __len__(self) -> int:
        """
        Get the number of albums in the collection
        
        Returns:
            int: Total number of albums
        """
        return len(self._albums)

    def __iter__(self):
        """
        Make the collection iterable
        
        Returns:
            Iterator of albums
        """
        return iter(self._albums)


def main():
    """
    Demonstrate the Album Management System
    
    Showcases:
    - Album creation
    - Collection management
    - Advanced operations
    """
    try:
        # Create albums with various attributes
        albums = AlbumCollection()

        # Add albums with different genres
        albums.add_album(Album(
            "Dark Side of the Moon", 
            "Pink Floyd", 
            9, 
            genre=AlbumGenre.ROCK, 
            release_year=1973
        ))
        
        albums.add_album(Album(
            "21", 
            "Adele", 
            11, 
            genre=AlbumGenre.POP, 
            release_year=2011
        ))

        # Demonstrate various operations
        print("All Albums:")
        for album in albums:
            print(album)

        print("\nSorted by Number of Songs:")
        for album in albums.sort_by_songs():
            print(album)

        # Find a specific album
        found_album = albums.find_album("21")
        if found_album:
            print(f"\nFound Album: {found_album}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
