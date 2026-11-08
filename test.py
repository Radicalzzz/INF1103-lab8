from supplier import Supplier

from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

from inventory import Inventory

supplier1 = Supplier("5001", "ABC Supplies", "contact@abcsupplies.com")
supplier1.display_information()

keyboard = PhysicalProduct("P001", "Mechanical Keyboard", 79.99, 50, 1.2, supplier1)
ebook = DigitalProduct("D001", "Learn Python Programming", 19.99, 100, 5.0, supplier1)

del supplier1

print("keyboard supplier:", keyboard.get_supplier().display_information())
print("ebook supplier:", ebook.get_supplier().display_information())

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(keyboard)
print("A", inventory_a.find_product("P001") is keyboard)
inventory_a.remove_product("P001")
print("A", inventory_a.find_product("P001"))

keyboard.display_information()

inventory_b.add_product(keyboard)
print("B", inventory_b.find_product("P001") is keyboard)