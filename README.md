# pick-episode
A Python script that chooses a random file from a regex-defined list

# Function
I wrote this script to help me choose random episodes of TV shows that I have on file. It searches the current directory (the folder that the script is in) and all subdirectories for files that match a certain regular expression, then continuously chooses random selections from that list when the user presses Enter.

# Usage
Simply run the script. By default, the script matches file names using the regular expression `S\d\dE\d\d`, which is the naming convention that I used in my library. Some examples of matches to this expression:

* S01E01
* S12E04
* S06E72

You can, however, use your own regex by selecting custom regex when the script runs and entering it at the prompt (or just editing the source code).

Once you have chosen to use the default regex or enter your own, the script will create a list of files that match the regex. You can then press Enter to get random selections.

# Future modifications
I don't expect to update this in the future, but I might add an auto-mode that opens the file for you. I might also add an option to make it remember episodes that it's already chosen and not repeat them.