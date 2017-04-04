# Demonstrate understanding of OOP concepts

class Book(object):
	def __init__(self, name , genre, author):
		self.name = name
		self.genre = genre
		self.author = author

class The_NoteBook(Book):
	"""The_NoteBook class inherits all the Books property
       such that, Everything that the Book class has, is contained 
       in the The_Notebook class
	"""
	def __init__(self, arg):
		super(The_NoteBook, self).__init__()
		self.arg = arg
		