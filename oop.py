# Inheritance

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
		self.arg = arg
		
#Data Abstraction and Encapsulation

class Book(object):
	"""By initializing the book class objects with
       double underscore, we are simpy making the clas
       inaccessible from outside the methos.
       
	"""
	def __init__(self, name , genre, author):
		self.__name = name
		self.__genre = genre
		self.__author = author

class The_NoteBook(Book):
	"""The_NoteBook class inherits all the Books property
       such that, Everything that the Book class has, is contained 
       in the The_Notebook class
	"""
	def __init__(self, arg):
		self.arg = arg
