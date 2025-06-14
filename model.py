from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class AIModel:
    def __init__(self):
        self.model = None
        self.feature_names = None
        self.train()

    def train(self):
        iris = load_iris()
        self.feature_names = iris.feature_names
        X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)

    def predict(self, input_data):
        prediction = self.model.predict([input_data])[0]
        return {
            "input": dict(zip(self.feature_names, input_data)),
            "prediction": int(prediction)
        }

