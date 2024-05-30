# Feature Engineering

def engineer_features(data):

    try:
        data['new_feature'] = data['feature1'] + data['feature2']
        return data
    except Exception as e:
        print(f"An error occurred during feature engineering: {e}")
        return None