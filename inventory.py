import json

from product import Product
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id:str) -> None:
        product = self.find_product(product_id)
        if product is not None:
            self.__products.remove(product)

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("No products in inventory.")
            return
        
        print("\nCurrent Inventory:")
        print("-------------------------------------------------------")

        for index, product in enumerate(self.__products):
            if index > 0:
                print()

            product.display_information()
            print(product.get_fulfilment_info())
            if isinstance(product, PhysicalProduct):
                print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")

        print("-------------------------------------------------------")

    def get_products(self):
        return self.__products.copy()

    def save_inventory(self):
        data = []

        for product in self.__products:
            product_data = {
                "id": product.get_product_id(),
                "name": product.get_product_name(),
                "price": product.get_price(),
                "stock": product.get_stock()
            }

            if isinstance(product, PhysicalProduct):
                product_data["type"] = "physical"
                product_data["weight"] = product.get_weight()

            elif isinstance(product, DigitalProduct):
                product_data["type"] = "digital"
                product_data["download_size"] = product.get_download_size()

            else:
                raise ValueError(f"Unsupported product type: {type(product)}")

            data.append(product_data)

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_inventory(self):
        try:
            with open("inventory.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return inventory

        loaded_products = []        

        for product_data in data:
            product_type = product_data.get("type")

            if product_type == "physical":
                product = PhysicalProduct(
                    product_data["id"],
                    product_data["name"],
                    product_data["price"],
                    product_data["stock"],
                    product_data["weight"]
                )

            elif product_type == "digital":
                product = DigitalProduct(
                    product_data["id"],
                    product_data["name"],
                    product_data["price"],
                    product_data["stock"],
                    product_data["download_size"]
                )

            else:
                raise ValueError(f"Unsupported product type: {product_type}")
            
            loaded_products.append(product)
            
        self.__products = loaded_products