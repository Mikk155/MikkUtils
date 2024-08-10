import os

from MikkUtils.__init__ import Ripent, HALFLIFE, convert_blueshift_bsp

convert_blueshift_bsp( f'{HALFLIFE()}/bshift/maps/ba_canal1.bsp', os.path.abspath( '' ) + '/ba_canal1.bsp' )

data = Ripent( os.path.abspath( '' ) + '/ba_canal1.bsp' )

print(f'{data}')

entdata = data.export()

#print(f'{entdata}')

entdata = data.export( True )

newdata = []
newdata.append( entdata[0] )
newdata.append( entdata[1] )
newdata.append( entdata[2] )

data.__write_json__( newdata )

data.import_( delete_json=True )
