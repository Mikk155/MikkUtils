import os

from MikkUtils.__init__ import jsonc

obj = os.path.abspath( '' ) + '/test_jsonc.json'

# A
with open( obj, 'r' ) as f:
    json_obj = jsonc( f.readlines() )
    print( f'{json_obj}')

# B
json_obj = jsonc(  open( obj, 'r' ).readlines() )
print( f'{json_obj}')
