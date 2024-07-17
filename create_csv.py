import csv
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
random.seed(42)

# Generate data
end_date = datetime(2024, 4, 30)  # Today is April 30, 2024
start_date = end_date - timedelta(days=90)  # 3 months of data
users = 10000  
days = 90

# Create CSV file
with open('fittrack_data_3months.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "User_ID", "Has_QuickLog", "Logged_Workout"])

    for day in range(days):
        current_date = start_date + timedelta(days=day)
        for user_id in range(1, users + 1):
            has_quicklog = user_id > 5000  # First 5000 users don't have QuickLog
            
            # Simulate varying engagement levels
            base_probability = 0.5 if has_quicklog else 0.4
            day_factor = 1 + (day / 180)  # Slight increase in engagement over time
            weekday_factor = 1.2 if current_date.weekday() < 5 else 0.8  # Higher engagement on weekdays
            
            log_probability = base_probability * day_factor * weekday_factor
            logged_workout = random.random() < min(log_probability, 0.95)  # Cap at 95% to maintain some randomness
            
            writer.writerow([current_date.strftime("%Y-%m-%d"), user_id, int(has_quicklog), int(logged_workout)])

print("CSV file 'fittrack_data_3months.csv' has been created.")
