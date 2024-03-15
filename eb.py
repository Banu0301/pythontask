def calculate_electricity_bill(units_consumed):
    # Define the free units threshold
    free_units = 100

    # Define charge per unit for extra units
    charge_per_unit = 5.50  # Adjust this rate as needed

    # Calculate charge for free units
    if units_consumed <= free_units:
        free_units_charge = 0
        extra_units = 0
    else:
        free_units_charge = free_units * charge_per_unit
        extra_units = units_consumed - free_units

    # Calculate charge for extra units
    extra_units_charge = extra_units * charge_per_unit

    # Calculate total charge
    total_charge = free_units_charge + extra_units_charge

    print(f"You consumed {units_consumed} units.")
    print(f"Charge for {free_units} free units: ₹{free_units_charge:.2f}")
    print(f"Charge for {extra_units} extra units: ₹{extra_units_charge:.2f}")
    print(f"Total charge: ₹{total_charge:.2f}")

# Example usage:
user_units = int(input("Enter the number of units consumed: "))
calculate_electricity_bill(user_units)
