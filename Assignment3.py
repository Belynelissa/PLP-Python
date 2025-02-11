# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.


def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    A discount is only applied if it is 20% or higher.
    
    :param price: Original price of the item.
    :param discount_percent: Discount percentage to apply.
    :return: Final price after applying discount (if applicable).
    """
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price  # No discount applied

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"Discount applied! The final price after {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The price remains: {price:.2f}")
