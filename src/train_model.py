import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


def train_model(
        X_train,
        X_test,
        y_train,
        y_test,
        feature_names
):

    model = LogisticRegression(
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    report = classification_report(
        y_test,
        predictions
    )

    importance = pd.Series(
        model.coef_[0],
        index=feature_names
    ).sort_values(ascending=False)

    # Save Model
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MODEL_DIR = os.path.join(BASE_DIR, "..", "models")

    os.makedirs(MODEL_DIR, exist_ok=True)

    joblib.dump(
        model,
        os.path.join(MODEL_DIR, "churn_model.pkl")
    )

    # Save Chart
    SCREENSHOT_DIR = os.path.join(
        BASE_DIR,
        "..",
        "screenshots"
    )

    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    plt.figure(figsize=(10, 6))

    importance.head(10).plot(kind="bar")

    plt.title("Top 10 Important Features")

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            SCREENSHOT_DIR,
            "feature_importance.png"
        )
    )

    plt.close()

    return (
        accuracy,
        report,
        matrix,
        importance
    )