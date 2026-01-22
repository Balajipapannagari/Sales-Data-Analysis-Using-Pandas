# Sales-Data-Analysis-Using-Pandas

##  Objective
Analyze sales data using Python Pandas to extract meaningful business insights such as revenue, profit, and sales trends.

---

## Technologies Used
- Python
- Pandas
- CSV Files

---

##  Dataset Description
### sales_data.csv
Contains order-level sales information including product, region, quantity, and price.

### product_cost.csv
Contains product-wise cost price for profit calculation.

---

##  Key Analysis Performed

###  Monthly Revenue
Calculated total revenue for each month using:
- `groupby()`
- Date transformation

###  Top Products
Identified best-selling products based on total quantity sold.

###  Region-wise Sales
Analyzed revenue contribution by region.

###  Profit Calculation
- Merged cost data using `merge()`
- Calculated profit using `apply()`

---

## Key Pandas Functions Used
- `.groupby()`
- `.merge()`
- `.apply()`
- `.dt.month_name()`

---

## ▶️ How to Run
```bash
pip install pandas
python sales_analysis.py
