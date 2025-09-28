from MissingValueImputer import MissingValueImputer
from OutlierRemover import OutlierRemover
from DummyModel import DummyModel
from MiniScalar import MiniScaler
class MiniPipeline:
    def __init__(self, steps): 
        self.steps = steps
        self.fitted = False

    def fit(self, X, y=None):
        for _,step in self.steps[:-1]:
            if hasattr(step,'fit') and hasattr(step,'transform'):
                step.fit(X)
                X =step.transform(X)
        self.fitted = True
        _,step = self.steps[-1]
        if hasattr(step,'fit'):
            step.fit(X)
        self.fitted = True
        return self
                

    def transform(self, X): 
        if not self.fitted:
            raise ValueError("fit is not run")
        for _,step in self.steps[:-1]:
            if hasattr(step,'fit') and hasattr(step,'transform'):
                X = self.transform(X)
        
        return X
    
    def predict(self, X): 
        if not self.fitted:
            raise ValueError("fit has not been run")
        for _, step in self.steps[:-1]:
            if hasattr(step, 'transform'):
                X = step.transform(X)
        _, model = self.steps[-1]
        if hasattr(model, 'predict'):
            return model.predict(X)
        raise ValueError("Final step does not have predict method")


    def __str__(self): 
        return (f"model is {self.fitted}")

X = [
    [1.0, 2.0],
    [1.5, 3.0],
    [100.0, 200.0],  # outlier
    [2.0, 2.5],
]
y = [0, 1, 0, 1]

pipe = MiniPipeline([
    ("remover", OutlierRemover(threshold=2)),
    ("scaler", MiniScaler()),
    ("model", DummyModel(version="v1"))
])

pipe.fit(X, y)
y_pred = pipe.predict(X)
print(y_pred)  