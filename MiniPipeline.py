class MiniPipeline:
    def __init__(self, steps):
        self.steps= steps
    
    def fit(self,X):
        for name, model in self.steps[:-1]:
            # name, model = self.steps[i]
            try:
                model.fit(X)
                X = model.transform(X)
            except Exception as v:
                print('error:',v)
                raise
        _,model = self.steps[-1]
        if  hasattr(model,'fit'):
            model.fit(X)
    
    def predict(self,X):
        for name, model in self.steps[:-1]:
            # name, model = self.steps[i]
            try:
                model.fit(X)
                X = model.transform(X)
            except Exception as v:
                print('error:',v)
                raise
        _,model = self.steps[-1]
        if  hasattr(model,'predict'):
            return model.predict(X)
        else:
            raise RuntimeError(f'no predict funtion in {name}')
        
    
    def _is_model(step):
        return hasattr(step,'predict')
if __name__ == "__main__":
    class AddOne:
        def fit(self, X): return self
        def transform(self, X): return [[x + 1 for x in row] for row in X]

    class MultiplyByTwo:
        def fit(self, X): return self
        def transform(self, X): return [[x * 2 for x in row] for row in X]

    class DummyModel:
        def __init__(self, bias=0.0): self.bias = bias
        def fit(self, X): return self
        def predict(self, X): return [sum(row) + self.bias for row in X]

    pipeline = MiniPipeline([
        ("add", AddOne()),
        ("times2", MultiplyByTwo()),
        ("model", DummyModel(bias=1.5))
    ])

    pipeline.fit([[1, 2], [3, 4]])
    preds = pipeline.predict([[5, 6]])
    print("Predictions:", preds)


            



