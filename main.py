import time
import random

# Function to get real-time prices
def get_realtime_price():
    """
    Simulates fetching the real-time price of a product.
    In a real-world scenario, replace this with an actual API call.
    """
    # Price fluctuation
    return round(random.uniform(10, 500), 2)

def display_product_prices(products):
    """
    Displays real-time prices for a list of products.
    """
    print("\nReal-Time Product Prices")
    print("=" * 30)
    for product in products:
        price = get_realtime_price()
        print(f"{product:<20}: ${price:>7.2f}")
    print("=" * 30)

def main():
    # List of mirchandise
    products = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Camera"]

    print("Welcome to the Real-Time Product Price Viewer!")
    while True:
        display_product_prices(products)
        print("\nPrices refresh every 10 seconds. Press Ctrl+C to exit.")
        try:
            time.sleep(10)  # Refresh every interval
        except KeyboardInterrupt:
            print("\nExiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()

