
# 📦 Order Management System

A Python-based command-line application designed to manage clients, products, and orders using **dictionaries and tuples**.
This system allows users to create orders, consult information, and generate simple reports.

---

## Features

* **Client Management**: Register clients using a unique ID and store their information.
* **Product Management**: Display available products with their ID, name, and price.
* **Order Creation**: Create orders by linking clients with selected products.
* **Order Consultation**: Search and display orders by client ID.
* **Report Generation**: View summaries of orders including products and total cost.
* **Input Validation**:

  * Ensures numeric IDs
  * Prevents invalid inputs
  * Verifies existing clients before creating orders

---

## Project Structure

The project is organized into different functions (can be in one or multiple files):

* `main.py`: Main menu and program execution
* `client.py`: Handles client registration
* `product.py`: Stores and displays product data
* `orders.py`: Manages order creation and consultation
* `reports.py`: Generates summaries and final reports

---

## Data Structures Used

* **Dictionaries (`dict`)**:
  Used to store clients, products, and orders.

* **Tuples (`tuple`)**:
  Used to store product details (ID, name, price).

Example:

```python
dic_orders = {
    101: {
        "products": ((1, "Burger", 10), (2, "Soda", 5)),
        "total": 15
    }
}
```

---

## Requirements

* Python 3.x

---

## How to Run

1. Download or clone the project files
2. Open a terminal in the project folder
3. Run the program:

```bash
python main.py
```

4. Follow the menu instructions displayed on screen

---

## Notes

* This project focuses on **basic Python concepts**
* Only **dictionaries and tuples** are used
* No external libraries are required
* Data is stored temporarily (no database or files yet)

---

## Future Improvements

* Add CSV file storage
* Implement update and delete options
* Improve menu navigation
* Add graphical user interface (GUI)

