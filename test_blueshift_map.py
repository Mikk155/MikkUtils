import shutil
import os

from MikkUtils.__init__ import HALFLIFE, convert_blueshift_bsp

ba_canal1 = f'{HALFLIFE()}/bshift/maps/ba_canal1.bsp'
ba_canal2 = os.path.abspath( '' ) + '/ba_canal2.bsp'

convert_blueshift_bsp( ba_canal1, os.path.abspath( '' ) + '/ba_canal1.bsp' )

shutil.copy( os.path.abspath( '' ) + '/ba_canal1.bsp', ba_canal2 )

convert_blueshift_bsp( ba_canal2, ba_canal2 )
