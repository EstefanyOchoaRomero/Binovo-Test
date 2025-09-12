# Task 1: Associate Blogs/News to a Company

![Odoo](https://img.shields.io/badge/Odoo-v18-informational)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Description
This task allows associating a blog with a single company. News items related to that blog automatically inherit the company of the blog.  

The company is set in the **blog form view**. In the **news form view**, the company is visible but **cannot be modified** (it inherits the blog's company).  

Odoo user profiles will only be able to **view and manage blogs and news** associated with their company and its descendant companies.

## Features
- Associate a blog with a specific company.
- News items inherit the company from the parent blog.
- Company field in news form is **read-only**.
- Access control: users can only see/manage blogs/news linked to their company and descendant companies.

## How to Test
1. Go to the **Blogs** menu and create a blog.
2. Set the company for the blog.
3. Create a news item linked to the blog.
4. Check that the company of the news matches the blog and cannot be edited.

## Author
- Estefany Ochoa Romero


