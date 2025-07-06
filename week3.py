#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after applying the discount if applicable, otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
def main():
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if original_price < 0 or discount_percentage < 0:
            print("Price and discount percentage must be non-negative.")
            return

        final_price = calculate_discount(original_price, discount_percentage)
        
        if final_price < original_price:
            print(f"The final price after applying a {discount_percentage}% discount on ${original_price} is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price remains: ${original_price:.2f}")
    
    except ValueError:
        print("Please enter valid numeric values for price and discount percentage.")

if __name__ == "__main__":
    main()
