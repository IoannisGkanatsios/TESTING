# data imputation based on other features

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Copy dataframe
df = df.copy()

# Step 1: Create missing indicator
df["REBUILD_COST_MISSING"] = df["PREMISES_REBUILD_COST"].isna().astype(int)

# Step 2: Split into known vs missing
df_known = df[df["PREMISES_REBUILD_COST"].notna()]
df_missing = df[df["PREMISES_REBUILD_COST"].isna()]

# Step 3: Define features
features = [
    "PREMISES_BEDROOMS",
    "PREMISES_BATHROOMS",
    "PREMISES_PROPERTY_TYPE",
    "PREMISES_YEAR_BUILT",
    "PREMISES_YEARS_RESIDENCY"
]

target = "PREMISES_REBUILD_COST"

X = df_known[features]
y = df_known[target]

# Step 4: Handle categorical variables
categorical_features = ["PREMISES_PROPERTY_TYPE"]
numeric_features = [col for col in features if col not in categorical_features]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", "passthrough", numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Step 5: Build model pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    ))
])

# Step 6: Train model
model.fit(X, y)

# Step 7: Predict missing values
X_missing = df_missing[features]
predicted_values = model.predict(X_missing)

# Step 8: Fill back into original dataframe
df.loc[df["PREMISES_REBUILD_COST"].isna(), "PREMISES_REBUILD_COST"] = predicted_values
