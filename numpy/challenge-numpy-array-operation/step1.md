# Problem Statement

You have been given a NumPy array called `transactions` that contains information about each customer's purchase. The array has the following shape: `(num_customers, num_products)`, where `num_customers` is the number of unique customers in the dataset and `num_products` is the number of unique products that the company sells. Each element in the array represents the number of times a customer has purchased a product.

You need to perform the following array operations on the `transactions` array:

1. Calculate the total number of purchases for each customer.
2. Calculate the total number of purchases for each product.
3. Calculate the total revenue generated by each customer (assume that each product costs $10).
4. Calculate the total revenue generated by each product.
5. Calculate the average number of purchases per customer.
6. Calculate the average number of purchases per product.

Overall your task is to write a function called `customer_stats` that takes in a NumPy array `transactions` and returns a dictionary with the following keys and values:

- `'total_purchases_by_customer'`: A NumPy array of shape `(num_customers,)` containing the total number of purchases for each customer.
- `'total_purchases_by_product'`: A NumPy array of shape `(num_products,)` containing the total number of purchases for each product.
- `'total_revenue_by_customer'`: A NumPy array of shape `(num_customers,)` containing the total revenue generated by each customer.
- `'total_revenue_by_product'`: A NumPy array of shape `(num_products,)` containing the total revenue generated by each product.
- `'average_purchases_per_customer'`: A float representing the average number of purchases per customer.
- `'average_purchases_per_product'`: A float representing the average number of purchases per product.

Note that the values in the dictionary should be rounded to 2 decimal places.

You can assume that the input array `transactions` is a NumPy array of integers.

**Constraints:**

- All integers in `transactions` are non-negative and less than or equal to 100.
- The maximum number of unique customers is 1000.
- The maximum number of unique products is 100.

**Example:**

```python
>>> import numpy as np
>>> transactions = np.array([
...     [1, 2, 3],
...     [0, 1, 0],
...     [4, 0, 2]
... ])
>>> customer_stats(transactions)
{
    'total_purchases_by_customer': array([6, 1, 6]),
    'total_purchases_by_product': array([5, 3, 5]),
    'total_revenue_by_customer': array([ 60,   0,  60]),
    'total_revenue_by_product': array([20, 30, 20]),
    'average_purchases_per_customer': 4.33,
    'average_purchases_per_product': 2.67
}
```

In the following steps, the challenge is divided into multiple steps. Please finish them one by one.
