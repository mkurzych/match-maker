from models.clean import get_data
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = get_data()
X = df.drop(columns=['dec'])
y = df['dec'].to_frame()

# Preprocess the data
# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
