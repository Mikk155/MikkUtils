"""
The MIT License (MIT)

Copyright (c) 2024 Mikk

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import struct
from json import loads as __json_loads__

#========================================================
# jsonc
#========================================================

def jsonc( obj : list[str] | str ) -> dict | list:

    '''
    Loads a text file and skips single-line commentary before loading a json object
    '''

    __js_split__ = ''

    __lines__: list[str]

    if isinstance( obj, list ):
        __lines__ = obj
    else:
        __lines__ = open( obj, 'r' ).readlines()

    for __line__ in __lines__:

        __line__ = __line__.strip()

        if __line__ and __line__ != '' and not __line__.startswith( '//' ):

            __js_split__ = f'{__js_split__}\n{__line__}'

    return __json_loads__( __js_split__ )

#========================================================
# format
#========================================================

def format( string: str, arguments: list[str] | dict, cut_not_matched : bool = False ) -> str:
    '''
    Formats the given string replacing all the closed brackets with the corresponding indexes of arguments
    '''

    if isinstance( arguments, list ):

        for __arg__ in arguments:

            string = string.replace( "{}", str( __arg__ ), 1 )

        if cut_not_matched and string.find( '{}' ) != -1:

            string.replace( '{}', '' )

    elif isinstance( arguments, dict ):

        for __oarg__, __narg__ in arguments.items():

            string = string.replace( "{"+__oarg__+"}", str( __narg__ ) )

            #if cut_not_matched: -TODO find open-bracket and check until closes for removing
    else:

        raise Exception( 'arguments is not a list or dict')

    return string

#========================================================
# Vector
#========================================================

class Vector:
    '''
    Vector class
    '''
    def __init__( self, x:int|str=0, y=0, z=0 ):

        if isinstance( x, str ):

            __values__ = x.split( ',' ) if x.find( ',' ) != -1 else x.split()

            if len( __values__ ) < 3:
                __values__ += [ '0' ] * ( 3 - len( __values__ ) )

            self.x, self.y, self.z = [ self.__parse_value__(v) for v in __values__[:3] ]

        else:
            self.x = self.__parse_value__(x) if isinstance( x, ( float, int ) ) else 0
            self.y = self.__parse_value__(y) if isinstance( y, ( float, int ) ) else 0
            self.z = self.__parse_value__(z) if isinstance( z, ( float, int ) ) else 0

    def __parse_value__( self, __value__ ):

        __value__ = float( __value__ )

        if __value__.is_integer() or __value__ == int( __value__ ):

            return int( __value__ )
        
        return __value__

    def to_string( self, quoted : bool = False ):
        '''
        Converts the vector to string
        
        ``quoted`` if true, returns separating each number by a quote
        '''
        _y = str(self.y).split('.')[0] if str(self.y).endswith( '.0' ) else self.y
        _z = str(self.z).split('.')[0] if str(self.z).endswith( '.0' ) else self.z
        _x = str(self.x).split('.')[0] if str(self.x).endswith( '.0' ) else self.x

        if quoted:
            return f'{_x}, {_y}, {_z}'
        return f'{_x} {_y} {_z}'

    def __add__(self, other):

        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        if isinstance( scalar, Vector ):
            return Vector(self.x * scalar.x, self.y * scalar.y, self.z * scalar.z)
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__( self, other ):
        if isinstance( other, Vector):
            return ( self.x == other.x and self.z == other.z and self.y == other.y )
        return False

    def __ne__( self, other ):
        return not self.__eq__(other)

    def __getitem__( self, ang ):

        if ang == 0:
            return self.x

        elif ang == 1:
            return self.y

        elif ang == 2:
            return self.z

        else:
            raise Exception(f"No matching {ang}")

    def __setitem__(self, ang, new):

        if ang == 0:
            self.x = self.__parse_value__( new )

        elif ang == 1:
            self.y = self.__parse_value__( new )

        elif ang == 2:
            self.z = self.__parse_value__( new )

        else:
            raise Exception(f"No matching {ang}")

    def __repr__(self):
        return f"Vector( {self.x}, {self.y}, {self.z} )"