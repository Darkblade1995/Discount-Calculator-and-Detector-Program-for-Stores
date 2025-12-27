# Discount-Calculator-and-Detector-Program-for-Stores

Real Discount Detection Program
Overview

This project is a console-based Python program designed to help users identify whether a store discount is real, moderate, or misleading.
It analyzes the original price, the displayed price, and an additional coupon percentage to calculate the true discount and determine if the offer actually benefits the customer.

The goal of the program is to prevent deceptive pricing practices commonly known as fake discounts or price makeup.

How It Works

The program asks the user to enter:

The original product price

The currently displayed price

A coupon percentage applied at checkout

Using this information, the program:

Calculates the final price after applying the coupon

Determines the real discount percentage compared to the original price

Calculates the total savings

Classifies the offer as Real, Moderate, or Fraudulent

Discount Evaluation Logic

The offer is classified based on the real discount value:

REAL OFFER

Real discount ≥ 20%

Final price is lower than the original price

MODERATE OFFER

Real discount between 8% and 20%

NOT A REAL OFFER (Makeup or Fake Discount)

Real discount < 8%

Or final price is equal to or higher than the original price

This logic helps users make informed purchasing decisions.

Features

Real discount calculation based on actual price comparison

Coupon application validation

Detection of fake or misleading discounts

Clear classification of offers

Input validation and error handling

User-friendly console output

Technologies Used

Python 3

Standard Python features:

try-except for error handling

Arithmetic operations for financial calculations

Conditional logic for decision making

How to Run

Make sure you have Python 3 installed.

Run the script from the terminal:

python discount_detector.py


Enter the requested values when prompted.

Learning Outcomes

This project demonstrates:

Practical use of conditional logic

Real-world financial calculations

Input validation and exception handling

Clear classification of business rules

Development of consumer-focused utility programs

It is a beginner-friendly yet practical project, suitable for programming portfolios.

Author

Luis Fernando Agamez Atehortua
