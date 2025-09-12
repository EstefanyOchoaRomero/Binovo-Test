# Custom Odoo V18 Enhancements

![Odoo](https://img.shields.io/badge/Odoo-v18-informational)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Overview
This project contains three custom enhancements for Odoo v18:

1. **Associate Blogs/News to a Company**
2. **Prevent Sale Orders with Zero Quantities**
3. **CRM Opportunity Contact Form Modifications**

---

## Task 1: Associate Blogs/News to a Company

![Task1](https://img.shields.io/badge/Task-1-blue)

**Description:**  
- Associate a blog to a single company.  
- News linked to the blog inherit the company automatically.  
- Users can view and manage only the blogs and news associated with their company and its descendants.

---

## Task 2: Prevent Sale Orders with Zero Quantities

![Task2](https://img.shields.io/badge/Task-2-blue)

**Description:**  
- Prevent confirming sale orders with zero-quantity product lines.  
- Add a button to remove all zero-quantity lines.  
- Optional unit tests for validation.

---

## Task 3: CRM Opportunity Contact Form Modifications

![Task3](https://img.shields.io/badge/Task-3-blue)

**Description:**  
- Add a selectable field for lead source: "Third Party", "Social Media", "Internet Search".  
- Display this field in backend and frontend forms.  
- On the website form: remove phone field, make company optional, make source required, and validate email.

---

## Installation
1. Copy the custom modules into your Odoo `addons` folder.  
2. Update the app list.  
3. Install each module via Apps in Odoo.  
4. Test the functionality as described in each task.

---

## Author
- Estefany Ochoa Romero

