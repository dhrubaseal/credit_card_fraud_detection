# Model Evaluation

from sklearn.metrics import accuracy_score

def evaluate_model(model, X_test, y_test):

    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy
    except Exception as e:
        print(f"An error occurred during model evaluation: {e}")
        return None