from shipping import *

"""c1 = ShippingContainer("YML", ["books"])

print(c1.owner_code)
print(c1.contents)

c2 = ShippingContainer("MAE", ["clothes"])

print(c2.owner_code)
print(c2.contents)

c3 = ShippingContainer("ESC", ["electronics"])

print(c3.serial)
print(c3.contents)

c6 = ShippingContainer("YML", ["coffee"])
print(c6.serial)
print(ShippingContainer.next_serial)

c7 = ShippingContainer.create_empty("YML")
print(c7)
print(c7.owner_code)
print(c7.contents)"""

c8 = ShippingContainer.create_with_items("MAE", {"food", "textiles", "minerals"})
print(c8)
print(c8.owner_code)
print(c8.contents)