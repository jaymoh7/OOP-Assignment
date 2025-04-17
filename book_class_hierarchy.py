class Book:
    """Base class representing a book with common attributes and methods."""
    
    def __init__(self, title, author, pages, publish_year):
        """Initialize a new Book object with basic information."""
        self.title = title
        self.author = author
        self.pages = pages
        self.publish_year = publish_year
        self.current_page = 0
        self.bookmarked_pages = []
    
    def read(self, pages):
        """Read a specified number of pages."""
        if pages <= 0:
            return "Must read at least one page."
        
        if self.current_page + pages > self.pages:
            self.current_page = self.pages
            return f"Finished reading '{self.title}'!"
        else:
            self.current_page += pages
            return f"Read {pages} pages. Now on page {self.current_page} of {self.pages}."
    
    def bookmark(self):
        """Bookmark the current page."""
        if self.current_page == 0:
            return "No page to bookmark. Start reading first!"
        
        self.bookmarked_pages.append(self.current_page)
        return f"Bookmarked page {self.current_page}."
    
    def get_reading_progress(self):
        """Calculate and return the reading progress as a percentage."""
        return (self.current_page / self.pages) * 100
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"'{self.title}' by {self.author} ({self.publish_year}), {self.pages} pages"


class Fiction(Book):
    """Subclass representing a fiction book."""
    
    def __init__(self, title, author, pages, publish_year, genre, characters=None):
        """Initialize a Fiction book with additional attributes."""
        super().__init__(title, author, pages, publish_year)
        self.genre = genre
        self.characters = characters if characters else []
    
    def add_character(self, character):
        """Add a character to the book's character list."""
        self.characters.append(character)
        return f"Added {character} to '{self.title}'."
    
    def __str__(self):
        """Return a string representation of the fiction book."""
        return f"Fiction: {super().__str__()} - Genre: {self.genre}"


class NonFiction(Book):
    """Subclass representing a non-fiction book."""
    
    def __init__(self, title, author, pages, publish_year, subject, has_index=True):
        """Initialize a NonFiction book with additional attributes."""
        super().__init__(title, author, pages, publish_year)
        self.subject = subject
        self.has_index = has_index
        self.notes = []
    
    def add_note(self, page, note):
        """Add a note to a specific page."""
        if page < 1 or page > self.pages:
            return f"Invalid page number. Book has {self.pages} pages."
        
        self.notes.append((page, note))
        return f"Note added to page {page}."
    
    def get_notes(self):
        """Return all notes taken in the book."""
        if not self.notes:
            return "No notes have been taken."
        
        notes_str = "Notes:\n"
        for page, note in self.notes:
            notes_str += f"- Page {page}: {note}\n"
        return notes_str
    
    def __str__(self):
        """Return a string representation of the non-fiction book."""
        index_str = "with index" if self.has_index else "without index"
        return f"Non-Fiction: {super().__str__()} - Subject: {self.subject} ({index_str})"


# Demo usage
if __name__ == "__main__":
    # Create a fiction book
    novel = Fiction("The Great Gatsby", "F. Scott Fitzgerald", 180, 1925, "Classic")
    novel.add_character("Jay Gatsby")
    novel.add_character("Daisy Buchanan")
    
    # Create a non-fiction book
    textbook = NonFiction("Python Crash Course", "Eric Matthes", 544, 2019, "Programming")
    textbook.add_note(42, "Important section on lists!")
    
    # Demonstrate inheritance and polymorphism
    books = [novel, textbook]
    
    print("=== Book Collection ===")
    for book in books:
        print(book)  # Uses the appropriate __str__ method based on the object type
        
    print("\n=== Reading Session ===")
    print(novel.read(50))
    print(novel.bookmark())
    print(f"Reading progress: {novel.get_reading_progress():.1f}%")
    
    print("\n=== Notes from textbook ===")
    print(textbook.get_notes())