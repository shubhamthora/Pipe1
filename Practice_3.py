from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Print the first date
print(current_date.strftime('%Y-%m-%d'))

# Loop to print the remaining dates
for i in range(9):
    # Add two weeks to the current date
    current_date += timedelta(days=14)
    
    # Print the new date
    print(current_date.strftime('%Y-%m-%d'))
