from MikkUtils import format

# A (list indexing)
string = "It's {} am, so we should eat {}"
import random
time = random.randint( 6, 9 )
dinner = 'Mondongo'
print(f'{format( string, [ time, dinner ] ) }')

# B (dict replacement)

string = "We should do some work on {task} because {task} is a bit zzzz"
dictionary = { "task": "format.py"}
print(f'{format( string, dictionary ) }')
