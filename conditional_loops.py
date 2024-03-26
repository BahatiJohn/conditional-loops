def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Args:
        price (float): Original price of the item.
        discount_percent (float): Discount percentage (0 to 100).

    Returns:
        float: Final price after applying the discount.
    """
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        return price

def main():
    try:
        original_price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage (0 to 100): "))
        final_price = calculate_discount(original_price, discount_percent)
        print(f"Final price after applying the discount: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()