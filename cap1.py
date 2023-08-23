def calculate_parking_fee(day, hours, minutes):
    if day.lower() in ["monday", "tuesday", "wednesday"]:
        rate = 2.00
    elif day.lower() in ["thursday", "friday"]:
        rate = 2.50
    elif day.lower() in ["saturday", "sunday"]:
        rate = 3.00
    else:
        return "Invalid day"

    total_minutes = hours * 60 + minutes
    if total_minutes % 60 > 5:
        total_hours = (total_minutes // 60) + 1
    else:
        total_hours = total_minutes // 60

    total_cost = total_hours * rate
    return total_cost

def main():
    day = input("Enter the day of the week: ")
    hours = int(input("Enter the hours parked: "))
    minutes = int(input("Enter the minutes parked: "))

    parking_fee = calculate_parking_fee(day, hours, minutes)
    if isinstance(parking_fee, str):
        print(parking_fee)
    else:
        print("The parking fee is $%.2f" % parking_fee)

if __name__ == "__main__":
    main()
