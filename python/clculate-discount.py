# Define the function to calculate the discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return the original price
        return price

# Get user input for the original price and discount percentage
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price after applying the discount is: {final_price}")
