from MikkUtils.__init__ import Vector

# Init
VecPos = Vector( 10, 10, 0 )

print(VecPos)

# Modify X
VecPos.x = 5
print(VecPos.to_string())

# Modify X
VecPos[0] = 10
print(VecPos.to_string(True))

# Multiply Vectors
VecPos = VecPos * 2
print(VecPos.to_string(True))
VecPos = VecPos * Vector( 2, 4, 0 )
print(VecPos.to_string(True))

# sub
VecPos = VecPos - Vector( 30, 70, 10 )
print(VecPos.to_string(True))

# add
VecPos = VecPos + Vector( 10, 20, -10 )
print(VecPos.to_string(True))

print( VecPos == Vector( 0, 0, 0 ) )

print( VecPos == VecPos )
print( VecPos == Vector( VecPos.x, VecPos.y, VecPos.z ) )

VecPos = Vector( "25 0 0" )
print(VecPos.to_string(True))

VecPos = Vector( "30, 0, 0" )
print(VecPos.to_string(True))
