import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the CSV file
data = pd.read_csv('battery_lifecycle_multiple_data.csv')  # Update with your dataset file path

# Handle missing values if any
# For demonstration, let's fill missing values with the mean of each column
data.fillna(data.mean(), inplace=True)

# Feature and target separation
features = data.drop(columns=['RUL', 'Battery_ID'])  # RUL is the target, and Battery_ID is an identifier
target = data['RUL']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Define the random forest model
model = RandomForestRegressor(random_state=42)

# Train the model on the training data
model.fit(X_train, y_train)

# Save the model using pickle
with open('battery_lifecycle_random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)
