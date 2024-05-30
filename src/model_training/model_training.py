# Model Training

def train_model(model, X_train, y_train):
 
    try:
        trained_model = model.fit(X_train, y_train)
        return trained_model
    except Exception as e:
        print(f"An error occurred during model training: {e}")
        return None