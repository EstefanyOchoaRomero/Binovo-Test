# Task 2: Prevent Sale Orders with Zero Quantities

![Odoo](https://img.shields.io/badge/Odoo-v18-informational)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Description
This task prevents creating sale orders with products that have a **quantity of zero**.  

- If the user tries to confirm a sale order with any line quantity equal to zero, a warning is displayed and the order confirmation is blocked.
- Adds a **button in the sale order header** to remove all lines where the product quantity is zero.
- Optional: unit tests for both functionalities.

## Features
- Block sale orders with zero-quantity lines.
- Button to remove zero-quantity lines from an order.
- Optional unit tests to ensure functionality works as expected.

## How to Test
1. Create a sale order.
2. Add one or more products with quantity 0.
3. Try to confirm the order → a warning should appear and confirmation is blocked.
4. Click the "Remove Zero Quantity Lines" button → all zero-quantity lines are deleted.

## Author
- Estefany Ochoa Romero

