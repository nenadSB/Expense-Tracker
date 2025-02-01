The **Expense Tracker** is a **Python-based finance management tool** that allows users to **add, view, summarize, and visualize expenses**. It leverages **JSON for data storage** and **Matplotlib for visualization**, making it lightweight and easy to use.  

---

### **Tools and Technologies Used**  

#### **1. Python (Core Language)**
- **Purpose**: Main programming language for expense tracking and management.  
- **Features**:  
  - Handles user input, data storage, and visualization.  
  - Implements **functions for adding, viewing, summarizing, and visualizing expenses**.  

#### **2. JSON (Data Storage)**
- **Purpose**: Stores expenses in a simple and portable format.  
- **Features**:  
  - Stores expense records with **date, amount, and category**.  
  - **Read/write operations** using `json` module.  

#### **3. Matplotlib (Data Visualization)**
- **Purpose**: Creates **pie charts** for expense analysis.  
- **Features**:  
  - **Visualizes spending patterns** across different categories.  
  - **Displays category-wise spending distribution**.  

#### **4. Pathlib (File Handling)**
- **Purpose**: Manages the expense storage file (`expenses.json`).  
- **Features**:  
  - Checks if the file exists before reading.  
  - Ensures **error handling** for invalid JSON data.  

#### **5. Datetime (Date Handling)**
- **Purpose**: Ensures proper formatting and handling of expense dates.  
- **Features**:  
  - **Automatic date assignment** if not provided.  
  - Extracts **monthly summaries** for expense reports.  

---

### **Key Functionalities**
1. **Add Expense**  
   - Users enter the **amount, category, and date**.  
   - Data is stored in `expenses.json`.  

2. **View Expenses**  
   - Displays all recorded expenses with **date, amount, and category**.  

3. **Summarize Expenses**  
   - **Category-wise**: Shows total spending per category.  
   - **Month-wise**: Displays total spending per month.  

4. **Visualize Expenses**  
   - Uses **Matplotlib** to create a **pie chart** of category-wise spending.  

---

### **Summary of Tools Used**
1. **Python** – Core programming language.  
2. **JSON** – Stores expense records.  
3. **Matplotlib** – Visualizes spending with pie charts.  
4. **Pathlib** – Handles file operations securely.  
5. **Datetime** – Formats and processes expense dates.  

This **lightweight and efficient Expense Tracker** is perfect for **personal finance management**, allowing users to **log, analyze, and visualize their spending habits effortlessly**. 🚀
