import time
import random

def perform_heavy_calculation():
    """Simulates some work being done."""
    print("Initializing process...")
    data = [random.randint(1, 100) for _ in range(5)]
    processed = [x * 2 for x in data]
    time.sleep(0.5) # Simulate delay
    return processed

# Main execution
if __name__ == "__main__":
    results = perform_heavy_calculation()
    print(f"Processed data: {results}")
    print("Hello World")