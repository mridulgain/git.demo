import sys


def hulk():
	print("Hulk SMASH!!!")


def thor():
	print("God of thunder!!")
	print("Bring me Thanos!!")


def cap():
	print("Avengers assemble")


def default():
	if sys.argv[1] == "thor":
		thor()
	elif sys.argv[1] == "hulk":
		hulk()
	elif sys.argv[1] == "cap":
		cap()
	else:
		print("hello")


if __name__ == '__main__':
	default()
