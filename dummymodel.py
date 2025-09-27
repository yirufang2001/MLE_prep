class DummyModel:
    def __init__(self,version =1, bias =0.0):
        self.version = version
        self.bias = bias
        self.sets_is_fitted = False
    def _validate_input(self,X):
        if not isinstance(X,list) or not all(isinstance(x,list) for x in X):
            raise ValueError('X should be list of lists')
        if not all(all(isinstance(item,(float,int))for item in x)for x in X):
            raise ValueError('all inner value should be int or float')
        
    def fit(self,X):
        self._validate_input(X)
        self.sets_is_fitted =True
    
    def predict(self,X):
        self.fit(X)
        if not self.sets_is_fitted:
            raise RuntimeError('model is not fitted!')
        return [sum(item)+self.bias for item in X]
    
    def __str__(self):
        return (f"DummyModel(v{self.version}, bias={self.bias})")
        # print('DummyModel(r'{self.verision})')
        