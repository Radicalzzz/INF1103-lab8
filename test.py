from supplier import Supplier

from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

supplier1 = Supplier("5001", "ABC Supplies", "contact@abcsupplies.com")
supplier1.display_information()

keyboard = PhysicalProduct("P001", "Mechanical Keyboard", 79.99, 50, 1.2, supplier1)
ebook = DigitalProduct("D001", "Learn Python Programming", 19.99, 100, 5.0, supplier1)

del supplier1

print("keyboard supplier:", keyboard.get_supplier().display_information())
print("ebook supplier:", ebook.get_supplier().display_information())