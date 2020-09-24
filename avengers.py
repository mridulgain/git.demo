import sys


def thor():
	print("God of thunder!!")
	print("Bring me Thanos!!")


def default():
	if sys.argv[1] == "thor":
		thor()
	else:
		print("hello")


if __name__ == '__main__':
	default()
