import time
import random
import requests

# Fetch products from API
def fetch_products():
    try:
        response = requests.get('https://dummyjson.com/products')
        response.raise_for_status()
        data = response.json()
        return data['products'][:10] # Return top 10 products
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Function to get real-time prices based on base price
def get_realtime_price(base_price):
    """
    Simulates fetching the real-time price of a product by adding volatility to a base price.
    """
    # Price fluctuation: +/- 5%
    fluctuation = random.uniform(-0.05, 0.05)
    return round(base_price * (1 + fluctuation), 2)

def display_product_prices(products):
    """
    Displays real-time prices for a list of products.
    """
    print("\nReal-Time Product Prices")
    print("=" * 40)
    print(f"{'Product':<25} | {'Price':>10}")
    print("-" * 40)
    
    for product in products:
        title = product.get('title', 'Unknown')
        base_price = product.get('price', 0)
        current_price = get_realtime_price(base_price)
        print(f"{title[:25]:<25} | ${current_price:>9.2f}")
    print("=" * 40)

def main():
    print("Fetching product data from API...")
    products = fetch_products()
    
    if not products:
        print("No products found. Exiting.")
        return

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

