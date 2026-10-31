def calculate_electricity_bill():
    try:
        
        units = float(input("Enter the number of units consumed: "))
        

        if units < 0:
            raise ValueError("Units consumed cannot be negative.")
            
    except ValueError as e:
        
        print(f"\n[Error] Invalid input: {e}")
        print("Please enter a valid positive number.")
        
    else:
        
        fixed_charge = 50.0  # Base meter charge
        bill_amount = fixed_charge
        
       
        if units <= 100:
            bill_amount += units * 3.0
        elif units <= 200:
            bill_amount += (100 * 3.0) + ((units - 100) * 4.5)
        else:
            bill_amount += (100 * 3.0) + (100 * 4.5) + ((units - 200) * 6.0)
            
       
        print("\n--- Electricity Bill Summary ---")
        print(f"Units Consumed : {units}")
        print(f"Total Amount   : ${bill_amount:.2f}")
        
    finally:
        
        print("\nThank you for using the Electricity Bill Calculator!")

# Run the program
if __name__ == "__main__":
    calculate_electricity_bill()
