from supplier import Supplier
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct
from inventory import Inventory
from order import Order

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

order_a = Order("O001")
order_a.add_order_line(keyboard, 2)
order_a.add_order_line(ebook, 1)

print(f"Order O001 total: ${order_a.calculate_total():.2f}")

order_b = Order("O002")
order_b.add_order_line(keyboard, 1)

line_a = order_a.get_order_lines()[0]
line_b = order_b.get_order_lines()[0]

print("Same line object:", line_a is line_b)
print("Same product object:", line_a.get_product() is line_b.get_product())
print(f"Keyboard subtotal in A: ${line_a.calculate_subtotal():.2f}")
print(f"Keyboard subtotal in B: ${line_b.calculate_subtotal():.2f}")

print("Order A:")
for line in order_a.get_order_lines():
    line.display_information()

print("Order B:")
line_b.display_information()

del line_b
del order_b

print("Keyboard still available:", keyboard.get_product_name())
print(f"Order A total: ${order_a.calculate_total():.2f}")