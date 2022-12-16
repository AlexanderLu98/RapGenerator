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

  # Iterate over the lines again
  for line in lines:
    # Split the line into words
    words = line.split()
    # Skip the line if it is empty or consists only of whitespace characters
    if not words:
      continue
    # Get the rhyme of the last word in the line
    last_word = words[-1]
    rhyme = last_word[-2:]
    # Iterate over the words in the line
    for word in words:
      # Check if the word has the same rhyme as the last word in the line
      if word[-2:] == rhyme:
        # If the rhyme appears more than once, color the word red, otherwise color it green
        if rhymes[rhyme] > 1:
          output += f"\033[91m{word}\033[0m "
        else:
          output += f"\033[92m{word}\033[0m "
      else:
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
It helps me relax and see the world in a new way
So I'll keep smoking every single day

Chorus:
I love the smell of marijuana in the morning
It's like a fresh cup of coffee, oh so adoring
I roll a joint and light it up
And let the smoke fill my lungs, it's just enough"""

print(color_code_rhymes(lyrics))
