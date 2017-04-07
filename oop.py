
#methods
class Book(object):
	"""Methods are basically functions within
		a class. The first definition of a method
		has to be a reference "self" to the instance
		of the class
	"""
	def __init__(self, name):
		self.name = name

#constructor

"""
The __init__ keyword acts as a constructor in python
Though strictly speaking python does not have its own
explicit constructor method like other languages like C++
"""
def __init__(self, name):
	self.name = name

	
#Destructor

"""
what holds true for python constructor is also true for destructors
the keyword __del__ is used in place of a destructor
"""	

class Book(object):
	def __init__(self,name):
		self.name = name
	def __del__(self):
		print "Destructor initiated"
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
       inaccessible from outside the method.
	   class Encapsulation(object):
			def __init__(self, a, b, c):
				self.public = a
				self.__private = b
				self.__protected = c
       
	"""
	def __init__(self, name , genre, author):
		self.name = name
		self.__genre = genre
		self._author = author

class The_NoteBook(Book):
	"""The_NoteBook class inherits all the Books property
       such that, Everything that the Book class has, is contained 
       in the The_Notebook class
	"""
	def __init__(self, arg):
		self.arg = arg
