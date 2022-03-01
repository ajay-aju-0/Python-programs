import grahics.rectangle as re
import grahics.circle as c
import grahics.trd_graphics.cuboid as cb
import grahics.trd_graphics.sphere as s

print("Rectangle")
print("area:",re.area(5,6))
print("perimeter:",re.perimeter(5,6))

print("Circle")
print("area:",c.area(4))
print("perimeter:",c.perimeter(4))

print("Cuboid")
print("area:",cb.area(4,5,6))
print("perimeter:",cb.perimeter(4,5,6))

print("Shere")
print("area:",s.area(5))
print("perimeter:",s.perimeter(5))