import sys


def cap():
	print("Avengers assemble")


def default():
	if sys.argv[1] == "cap":
		cap()
	else:
		print("hello")


if __name__ == '__main__':
	default()
