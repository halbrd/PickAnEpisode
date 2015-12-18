import os
import re
import random

episodes = []

directory = os.path.dirname(os.path.realpath(__file__))

reply = input("Use custom episode regex? (default = 'S\d\dE\d\d') (y/n)\n> ")
while reply not in ["y", "n", "Y", "N"]:
	reply = input("> ")
customRegex = (reply == "y" or reply == "Y")

regex = "S\d\dE\d\d"
if customRegex:
	regex = input("Enter custom regex below.\n> ")

for path, subdirs, files in os.walk(directory):
	for name in files:
		if re.search(regex, name):
			episodes.append(name)

print("Episode list populated.")

# reply = input("Auto Mode? (y/n)\n> ")
# while reply not in ["y", "n", "Y", "N"]:
# 	reply = input("Auto Mode? (y/n)\n> ")
# autoMode = (reply == "y" or reply == "Y")

while True:
	input()
	name = episodes[random.randint(0, len(episodes)-1)]
	print(name, end="")
	# if autoMode:
	# 	os.startfile(name)