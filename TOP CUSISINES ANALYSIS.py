##TASK 1 LEVEL 4
#Compare the average ratings of restaurants
#with and without online delivery
import pandas as pd

df = pd.read_csv(r"C:\Users\rites\OneDrive\Desktop\sem 4\Cognifyz Technologies\Dataset .csv")

# Group by 'Has Online delivery' and calculate the mean of 'Aggregate rating'
average_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean().reset_index()

# Rename columns to give them meaningful names
average_ratings.columns = ['Has Online Delivery', 'Average Rating']

# Set the index to 'Has Online Delivery' without dropping the column
output = average_ratings.set_index('Has Online Delivery', drop=True)

# Display the result
print(output)
