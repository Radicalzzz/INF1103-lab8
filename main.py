from inventory import Inventory
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

def add_product(inventory):

    print("\n1. Physical Product")
    print("2. Digital Product")
    product_type = input("Enter the product type (1 or 2): ").strip()

    if product_type not in ["1", "2"]:
        raise ValueError("Invalid product type. Please enter 1 or 2.")

    product_name = input("Enter the product name: ").strip()
    if not product_name:
        raise ValueError("Product name cannot be empty.")

    price = float(input("Enter the product price: "))
    if price < 0:
        raise ValueError("Price cannot be negative.")
    
    quantity = int(input("Enter the product quantity: "))
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    
    # Placeholder for generating a unique product ID
    number = 1

    while inventory.find_product(f"P{number:03d}") is not None:
        number += 1

    product_id = f"P{number:03d}"

    if product_type == "1":
        weight = float(input("Enter the product weight in kg: "))
        if weight < 0:
            raise ValueError("Weight cannot be negative.")
        product = PhysicalProduct(product_id, product_name, price, quantity, weight)

    elif product_type == "2":
        download_size = float(input("Enter the download size in MB: "))
        if download_size < 0:
            raise ValueError("Download size cannot be negative.")
        product = DigitalProduct(product_id, product_name, price, quantity, download_size)
    
    inventory.add_product(product)
    inventory.save_inventory()

    print(f"Product '{product_name}' added successfully with ID: {product_id}")

def update_stock(inventory):
    product_id = input("Enter the product ID to update stock: ").strip().upper()

    product = inventory.find_product(product_id)
    if product is None:
        print(f"Product with ID '{product_id}' not found.")
        return

    new_stock = int(input(f"Enter the new stock quantity for '{product.get_product_name()}': "))

    product.update_stock(new_stock)
    inventory.save_inventory()

    print(f"Stock for product '{product.get_product_name()}' updated to {new_stock}.")

def find_product(inventory):
    product_id = input("Enter the product ID to search: ").strip().upper()

    product = inventory.find_product(product_id)
    if product is None:
        print(f"Product with ID '{product_id}' not found.")
        return
    else:
        print("Product found:")
        product.display_information()

def main():
    inventory = Inventory()
    inventory.load_inventory()

    while True:
        print("\n============================")
        print("Inventory Management System")
        print("============================")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("\nEnter option: ").strip()

        try:
            if choice == "1":
                inventory.display_all()
            elif choice == "2":
                add_product(inventory)
            elif choice == "3":
                update_stock(inventory)
            elif choice == "4":
                find_product(inventory)
            elif choice == "5":
                inventory.save_inventory()
                print("\nInventory saved successfully.")
            elif choice == "6":
                inventory.save_inventory()
                print("\nInventory saved successfully.")
                print("Thank you for using Inventory Management System.")
                break

            else:
                print("\nInvalid option. Please choose a valid option from 1 to 6.")

        except ValueError as error:
            print(f"\nInvalid input: {error}")

if __name__ == "__main__":
    main()