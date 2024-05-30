# model_deployment.py

import joblib

def save_model(model, file_path):
    """
    Save the trained machine learning model to a file.

    Parameters:
    - model: Trained machine learning model.
    - file_path (str): Path to save the model.
    """
    try:
        joblib.dump(model, file_path)
        print(f"Model saved successfully to '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while saving the model: {e}")