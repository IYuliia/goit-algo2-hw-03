import csv
import random

def generate_data(filename, num_items=10000):
    categories = ["Electronics", "Clothing", "Home Goods", "Toys", "Sports"]
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["ID", "Price", "Name", "Category"])
        writer.writeheader()
        
        for i in range(1, num_items + 1):
            item = {
                "ID": i,
                "Price": round(random.uniform(1.0, 100.0), 2), 
                "Name": f"Product {i}",
                "Category": random.choice(categories)  
            }
            writer.writerow(item)

generate_data("generated_items_data.csv", 1000)
