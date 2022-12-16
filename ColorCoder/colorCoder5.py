import re

def color_code_rhymes(lyrics):
  # Split the lyrics into a list of lines
  lines = lyrics.split('\n')

  # Create a dictionary to store the rhymes
  rhymes = {}

  # Iterate over the lines
  for line in lines:
    # Split the line into words
    words = line.split()
    # Skip the line if it is empty or consists only of whitespace characters
    if not words:
      continue
    # Get the last word in the line
    last_word = words[-1]
    # Get the rhyme by taking the last two syllables of the word
    rhyme = last_word[-2:]
    # Add the rhyme to the dictionary, or increase the count if it already exists
    if rhyme in rhymes:
      rhymes[rhyme] += 1
    else:
      rhymes[rhyme] = 1

  # Initialize the output string
  output = ""

  # Define a list of colors to use for the rhymes
  colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m', '\033[98m', '\033[99m']

  # Create a dictionary to store the colors for each rhyme
  rhyme_colors = {}

  # Iterate over the lines again
  for line in lines:
    # Split the line into words
    words = line.split()
    # Skip the line if it is empty or consists only of whitespace characters
    if not words:
      continue
    # Initialize a list to store the internal rhymes
    internal_rhymes = []
    # Iterate over the words in the line
    for i, word in enumerate(words):
      # Check if the word is the last word in the line
      if i == len(words) - 1:
        # Get the rhyme of the last word
        rhyme = word[-2:]
        # Check if the rhyme has already been added to the list of internal rhymes
        if rhyme not in internal_rhymes:
          # Add the rhyme to the list
          internal_rhymes.append(rhyme)
      else:
        # Check if the word and the next word have the same rhyme
        if word[-2:] == words[i+1][-2:]:
          # Get the rhyme of the current word
          rhyme = word[-2:]
          # Check if the rhyme has already been added to the list of internal rhymes
          if rhyme not in internal_rhymes:
            # Add the rhyme to the list
            internal_rhymes.append(rhyme)
    # Iterate over the words in the line again
    for i, word in enumerate(words):
      # Check if the rhyme of the word is in the list of internal rhymes
      if word[-2:] in internal_rhymes:
        # Get the color to use for the rhyme
        if word[-2:] in rhyme_colors:
          color = rhyme_colors[word[-2:]]
        else:
          color = colors[len(rhyme_colors) % len(colors)]
          rhyme_colors[word[-2:]] = color
        # Add the colored word to the output string
        output += f"{color}{word}\033[0m "
      # Check if the word is the last word in the line
      elif i == len(words) - 1:
        # Get the rhyme of the last word
        rhyme = word[-2:]
        # Check if the rhyme has already been added to the list of internal rhymes
        if rhyme not in internal_rhymes:
          # Get the color to use for the rhyme
          if rhyme in rhyme_colors:
            color = rhyme_colors[rhyme]
          else:
            color = colors[len(rhyme_colors) % len(colors)]
            rhyme_colors[rhyme] = color
          # Add the colored word to the output string
          output += f"{color}{word}\033[0m "
      else:
        # Add the word to the output string without coloring it
        output += f"{word} "
    output += "\n"

  return output

lyrics = """Verse 1:
I wake up every morning with a smile on my face
I thank the Lord above for another day
I brush my teeth and take a shower
And then I sit down to enjoy my favorite flower

Chorus:
I love the smell of marijuana in the morning
It's like a fresh cup of coffee, oh so adoring
I roll a joint and light it up
And let the smoke fill my lungs, it's just enough

Verse 2:
I start my day with a little meditation
I clear my mind and find my inner peace and relaxation
I put on some music and get lost in the sound
I dance and sing and let my worries drown

Chorus:
I love the smell of marijuana in the morning
It's like a fresh cup of coffee, oh so adoring
I roll a joint and light it up
And let the smoke fill my lungs, it's just enough

Bridge:
Some people say it's wrong, but I don't agree
Marijuana brings me joy and sets me free
It helps me relax and see the world
In a whole new light, it's just my girl
"""

#print(color_code_rhymes(lyrics))

doom="""
Tripping off the beat kinda, dripping off the meat grinder
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
Glad that we win, a tad fat, in a bad hat for men
Grind the cinnamon, Manhattan warmongers
You can find the villain in satin, congas
The van screeches
The old man preaches
About the gold sand beaches
The cold hand reaches
For the old tan Ellesse's
Jesus
"""

print(color_code_rhymes(doom))