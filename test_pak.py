import os

from MikkUtils.__init__ import pak

pPak = pak( os.path.abspath( '' ) + '/test_pak.pak' )

pPak.extract( os.path.abspath( '' ) + '/test_pak/')