# model_evaluation.py

from sklearn.metrics import accuracy_score

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the performance of the machine learning model.

    Parameters:
    - model: Trained machine learning model.
    - X_test (array-like): Features for testing.
    - y_test (array-like): Target labels for testing.

    Returns:
    - accuracy (float): Accuracy score of the model.
    """
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy
    except Exception as e:
        print(f"An error occurred during model evaluation: {e}")
        return None