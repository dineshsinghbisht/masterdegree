from sklearn.linear_model import LinearRegression # pip3 install scikit-learn
import pandas as pd

# Sample data
data = {
    'Square_Feet': [1500,1800,2400,3000,1200,2200,2600,1400,2800,1600],
    'Bedrooms': [3,4,4,5,2,3,4,2,5,3],
    'Age_Years': [10,5,15,8,20,12,7,18,4,9],
    'Price': [250000,320000,350000,420000,200000,310000,370000,230000,410000,260000]
}
df = pd.DataFrame(data)

# Train model
X = df[['Square_Feet', 'Bedrooms', 'Age_Years']]
y = df['Price']

model = LinearRegression()
model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
