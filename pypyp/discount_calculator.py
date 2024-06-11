def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying the discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount, or the original price if the discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Prompt the user to enter the original price and discount percentage
    try:
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        # Calculate the final price
        final_price = calculate_discount(price, discount_percent)

        # Print the final price
        if discount_percent >= 20:
            print(f"The final price after applying the discount is: ${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is: ${price:.2f}")
    except ValueError:
        print("Please enter valid numerical values for the price and discount percentage.")

if __name__ == "__main__":
    main()
