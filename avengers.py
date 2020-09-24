import sys


def hulk():
	print("Hulk SMASH!!!")


def default():
	if sys.argv[1] == "hulk":
		hulk()
	else:
		print("hello")


if __name__ == '__main__':
	default()
