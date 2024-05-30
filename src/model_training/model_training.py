# Model Training

def train_model(model, X_train, y_train):
    """
    Train the machine learning model.

    Parameters:
    - model: Machine learning model.
    - X_train (array-like): Features for training.
    - y_train (array-like): Target labels for training.

    Returns:
    - trained_model: Trained machine learning model.
    """
    try:
        trained_model = model.fit(X_train, y_train)
        return trained_model
    except Exception as e:
        print(f"An error occurred during model training: {e}")
        return None