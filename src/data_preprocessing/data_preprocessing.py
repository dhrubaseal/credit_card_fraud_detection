# data_preprocessing.py

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_data(data, numeric_features, categorical_features):
    """
    Preprocess the data by handling missing values, scaling numerical features, and encoding categorical features.

    Parameters:
    - data (DataFrame): Input data.
    - numeric_features (list): List of column names corresponding to numerical features.
    - categorical_features (list): List of column names corresponding to categorical features.

    Returns:
    - preprocessed_data (array): Preprocessed data as a NumPy array.
    """
    try:
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())])
    
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))])
    
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)])
    
        preprocessed_data = preprocessor.fit_transform(data)
        return preprocessed_data
    except Exception as e:
        print(f"An error occurred during data preprocessing: {e}")
        return None