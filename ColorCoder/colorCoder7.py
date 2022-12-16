import re

def color_code_syllables(lyrics):
  # Split the lyrics into a list of lines
  lines = lyrics.split('\n')

  # Initialize the output string
  output = ""

  # Define a list of colors to use for the syllables
  colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m', '\033[98m', '\033[99m']

  # Create a dictionary to store the colors for each number of syllables
  syllable_colors = {}

  # Iterate over the lines
  for line in lines:
    # Split the line into words
    words = line.split()
    # Skip the line if it is empty or consists only of whitespace characters
    if not words:
      continue
    # Iterate over the words in the line
    for word in words:
      # Count the number of syllables in the word
      syllables = len(re.findall(r'[aeiouyAEIOUY]+', word))
      # Get the color to use for the number of syllables
      if syllables in syllable_colors:
        color = syllable_colors[syllables]
      else:
        color = colors[len(syllable_colors) % len(colors)]
        syllable_colors[syllables] = color
      # Add the colored word to the output string
      output += f"{color}{word}\033[0m "
    output += "\n"

  return output

lyrics = """Tripping off the beat kinda, dripping off the meat grinder
Heat niner, pimping, stripping, soft sweet minor
China was a neat signer, trouble with the script
Digits double dipped, bubble lipped, subtle lisp midget
Borderline schizo, sort of fine tits though
Pour the wine, whore to grind, quarter to nine, let's go
Ever since ten eleven, glad she made a brethren
Then it's last down, seven alligator seven, at the gates of heaven
Knocking, no answer, slow dancer, hopeless romancer, dopest flow stanzas
Yes, no? Villain, Metal Face to Destro
Guess so, still incredible in escrow
Just say ho, I'll test the yayo
Wild West style fest, y'all best to lay low
Hey bro, Day Glo, set the bet, pay dough
Before the cheddar get away, best to get Maaco
The worst hated God who perpetrated odd favors
Demonstrated in the perforated Rod Lavers
In all quad flavors, Lord, save us
Still back in the game like Jack LaLanne
Think you know the name, don't rack your brain
On a fast track to half insane
Either in a slow beat or that the speed of "Wrath of Kane"
Laughter, pain
"Hackthoo'ing" songs, lit in the booth with the best host
Doing bong hits on the roof, in the west coast
He's at it again
Mad at the pen
Glad that we win, a tad fat,
a bad hat for men
Grind the cinnamon, Manhattan warmongers
You can find the villain in satin, congas
The van screeches
The old man preaches
About the gold sand beaches
The cold hand reaches
For the old tan Ellesse's
Jesus
"""

print(color_code_syllables(lyrics))
