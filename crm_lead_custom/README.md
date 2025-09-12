# Task 3: CRM Opportunity Contact Form Modifications

![Odoo](https://img.shields.io/badge/Odoo-v18-informational)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

## Description
Customize the **CRM Opportunities module** and its contact form.

### Backend
- Add a **selectable field** for users to indicate the source of the company lead:
  - "Third Party"
  - "Social Media"
  - "Internet Search"
- Display this field in the **form view**.

### Website (Frontend)
- Remove the **phone field**.
- Make the **company field optional**.
- Show the **source field**, which is **required**.
- Validate the email field.

## Features
- Add source selection to opportunities.
- Backend and frontend integration.
- Optional email validation.
- Frontend form customization for better user experience.

## How to Test
1. Go to CRM → Opportunities → Create new opportunity.
2. Verify the source selection field is displayed in the form.
3. On the website contact form, try submitting without selecting the source → should fail.
4. Ensure phone is removed and company is optional.
5. Check email validation works correctly.

## Author
- Estefany Ochoa Romero

