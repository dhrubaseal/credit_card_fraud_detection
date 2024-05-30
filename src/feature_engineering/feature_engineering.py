# feature_engineering.py

def engineer_features(data):
    """
    Engineer new features based on existing ones.

    Parameters:
    - data (DataFrame): Input data.

    Returns:
    - data_with_features (DataFrame): Data with engineered features.
    """
    try:
        data['new_feature'] = data['feature1'] + data['feature2']
        return data
    except Exception as e:
        print(f"An error occurred during feature engineering: {e}")
        return None