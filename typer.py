from getopt import getopt
from pynput.keyboard import Controller
import random
from sys import argv, stdin
from time import sleep

delay=0
jitter=0
lag=0

def main():
	parse(argv[1:])

	keyboard = Controller()

	sleep(delay / 1000)

	for line in stdin:
		press(keyboard, line)
		press(keyboard, "\r\n")

def parse(params):
	global delay
	global jitter
	global lag

	optlist, args = getopt(params, 'd:j:l:')
	optlist = dict(optlist)

	delay  = int(optlist.get('-d', 0))
	jitter = int(optlist.get('-j', 0))
	lag    = int(optlist.get('-l', 0))

def press(keyboard, string):
	for i in range(0, len(string)):
		keyboard.press(string[i])
		keyboard.release(string[i])
		sleep((lag - jitter + random.randint(0, jitter * 2)) / 1000)

if __name__ == '__main__':
	main()
