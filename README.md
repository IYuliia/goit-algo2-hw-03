### **Task 1: Applying the Maximum Flow Algorithm for Goods Logistics**  

#### **Objective**  
Develop a program to model a flow network for the logistics of goods from warehouses to stores using the **maximum flow algorithm**. Analyze the obtained results and compare them with theoretical knowledge.  

---

### **Task Description**  
Construct a graph model representing the flow network based on the following structure:  

#### **Connections and Capacities in the Graph**  

| From         | To         | Capacity (units) |
|-------------|-----------|------------------|
| Terminal 1  | Warehouse 1 | 25 |
| Terminal 1  | Warehouse 2 | 20 |
| Terminal 1  | Warehouse 3 | 15 |
| Terminal 2  | Warehouse 3 | 15 |
| Terminal 2  | Warehouse 4 | 30 |
| Terminal 2  | Warehouse 2 | 10 |
| Warehouse 1 | Store 1   | 15 |
| Warehouse 1 | Store 2   | 10 |
| Warehouse 1 | Store 3   | 20 |
| Warehouse 2 | Store 4   | 15 |
| Warehouse 2 | Store 5   | 10 |
| Warehouse 2 | Store 6   | 25 |
| Warehouse 3 | Store 7   | 20 |
| Warehouse 3 | Store 8   | 15 |
| Warehouse 3 | Store 9   | 10 |
| Warehouse 4 | Store 10  | 20 |
| Warehouse 4 | Store 11  | 10 |
| Warehouse 4 | Store 12  | 15 |
| Warehouse 4 | Store 13  | 5  |
| Warehouse 4 | Store 14  | 10 |

---

### **Implementation Instructions**  
1. **Apply the maximum flow algorithm** to solve the problem.  
2. Write a program that implements **Edmonds-Karp's algorithm**, or use an existing implementation to find the **maximum flow** in the constructed graph.  
3. **Analyze the results**:  
   - Determine whether the **optimal flow** has been achieved.  
   - Explain what the result means for the given logistics network.  
4. **Prepare a report** including calculations and explanations:  
   - Describe which **nodes and edges** were selected and how they correspond to real-world logistics elements.  
   - Provide a **step-by-step breakdown** of the maximum flow calculation and explain the logic behind each step.  

---

### **Technical Requirements**  
- **Use the Edmonds-Karp algorithm** to implement maximum flow calculations.  
- **The graph must match** the given structure, with **20 nodes and specified capacities**.

### **Task 2: Comparing the Efficiency of OOBTree and Dict for Range Queries**  

#### **Objective**  
Develop a program to store a large dataset of product information in two data structures — **OOBTree** and **dict** — and perform a comparative analysis of their performance in executing **range queries**.  

---

### **Task Description**  

1. **Load product data** from the provided `generated_items_data.csv` file.  
   - Each product includes:  
     - **ID** (unique identifier)  
     - **Name** (product name)  
     - **Category**  
     - **Price**  

2. **Implement two storage structures:**  
   - **OOBTree** (from the `BTrees` library), where the **ID** is the key, and the value is a dictionary containing product attributes.  
   - **dict** (Python's standard dictionary), with the same structure.  

3. **Create functions to add products:**  
   - `add_item_to_tree(tree, item_data)`  
   - `add_item_to_dict(dictionary, item_data)`  

4. **Create functions for range queries:**  
   - `range_query_tree(tree, min_price, max_price)` (should use `items(min, max)`)  
   - `range_query_dict(dictionary, min_price, max_price)` (should use **linear search**)  

5. **Measure execution time** using `timeit`:  
   - Run each **range query function 100 times** and compute the average execution time.  

6. **Output execution time results** for both data structures:  
   ```
   Total range_query time for OOBTree: X.XXXXXX seconds  
   Total range_query time for Dict: X.XXXXXX seconds  
   ```

---

### **Technical Requirements**  

- **Use only OOBTree and dict** for comparison.  
- **Implement separate functions** for:  
  - Adding products (`add_item_to_tree`, `add_item_to_dict`).  
  - Range queries (`range_query_tree`, `range_query_dict`).  
- **Use `timeit`** for precise performance measurement.  
- **Run 100 range queries** for each structure and output the total execution time.  

