# Model Selection

from sklearn.ensemble import RandomForestClassifier

def select_model():

    try:
        return RandomForestClassifier()
    except Exception as e:
        print(f"An error occurred during model selection: {e}")
        return None