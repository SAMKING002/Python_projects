def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after the discount if the discount percentage is 20% or higher,
           otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to enter the original price and the discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the final price
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: ksh{final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: ksh{original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
