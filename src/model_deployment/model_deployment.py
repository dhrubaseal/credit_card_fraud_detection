# Model Deployment

import joblib

def save_model(model, file_path):

    try:
        joblib.dump(model, file_path)
        print(f"Model saved successfully to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while saving the model: {e}")