# Hyperparameter Tuning

from sklearn.model_selection import GridSearchCV

def tune_hyperparameters(model, param_grid, X_train, y_train):

    try:
        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='accuracy')
        grid_search.fit(X_train, y_train)
        best_model = grid_search.best_estimator_
        return best_model
    except Exception as e:
        print(f"An error occurred during hyperparameter tuning: {e}")
        return None