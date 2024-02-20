from datetime import datetime

# Example month string
month_str = "October"

# Convert month string to corresponding number
month_number = datetime.strptime(month_str, "%B").month

print(f"The corresponding number for {month_str} is: {month_number}")
