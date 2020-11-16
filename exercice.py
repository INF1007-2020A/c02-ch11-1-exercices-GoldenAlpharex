"""
Chapitre 11.1
"""


import math
from inspect import *

from game import *

class Point2D_NoGoodPython:
	def __init__(self, x, y, name = "henlo"):
		self.__x = x
		self.__y = y
		self.__name = name
	
	def __str__(self):
		return f"({self.__x}, {self.__y})"
	
	def get_x(self):
		return self.__x

	def set_x(self, val):
		self.__x = val

	def get_y(self):
		return self.__y

	def set_y(self, val):
		self.__y = val

class MyClass:
	pass

class Point2D:
	def __init__(self, x, y, name = "henlo"):
		self.__x = x
		self.__y = y
		self.__name = name

	@property # C'est mieux d'utiliser les trucs comme ça.
	def x(self):
		return self.__x

	@x.setter
	def x(self, val):
		self.__x = val

	@property
	def y(self):
		return self.__y
	
	@y.setter
	def y(self, val):
		self.__y = val

	@property
	def name(self):
		return self.__name

	def __str__(self):
		return f"{self.name}: ({self.x}, {self.y})"

	@classmethod
	def from_list(cls, l):
		return cls(l[0], l[1])
	
	@staticmethod
	def add(p1, p2):
		return Point2D(p1.x + p2.x, p1.y + p2.y)


def main():
	# foo = Point2D_NoGoodPython(10, 20, "foo")
	# bar = Point2D(10, 20, "bar")

	# bar2 = Point2D.from_list([1, 2])
	# print(Point2D.add(bar2, bar))
	# print(bar2)
	# foo.set_x(42)
	# bar.x += 42
	# print(foo.get_x())
	# print(bar.x)
	# print(bar)

	# wpn1 = Weapon("wpn1", 40, 10)
	# print(wpn1.name)
	# print(wpn1.power)
	# print(wpn1.min_level)

	# unarmed = Weapon.make_unarmed()

	# foo = Character("foo", 100, 10, 10, 15)
	# foo.weapon = wpn1
	# foo.hp -= 9000
	# print(foo.hp)

	c1 = Character("Äpik", 200, 150, 70, 70)
	c2 = Character("Gämmör", 250, 100, 120, 60)

	c1.weapon = Weapon("BFG", 100, 69)
	c2.weapon = Weapon("Deku Stick", 120, 1)
	
	# deal_damage(c1, c2)
	turns = run_battle(c1, c2)
	print(f"The battle ended in {turns} turns.")

if __name__ == "__main__":
	main()

