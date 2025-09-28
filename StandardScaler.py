import statistics
class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None
        self.fitted = False
    
    def fit(self, X):
        cols = list(zip(*X))
        self.mean = [statistics.mean(x) for x in cols]
        self.std = [statistics.stdev(x) for x in cols]
        self.fitted = True
        return self
        
    def transform(self, X):
        if not self.fitted:
            raise RuntimeError(' fit has not runned')
        for i in range(len(X)):
            for j in range(len(X[0])):
                m,n = self.mean[j],self.std[j]
                X[i][j] = (X[i][j]-m)/n
        return X
        # ...
        
    def fit_transform(self, X):
        return self.fit(X).transform(X)
    
        # ...
        
    def __str__(self):
        return f"model is fitted = {self.fitted}"
        # ...
X = [
    [1.0, 2.0],
    [2.0, 4.0],
    [3.0, 6.0],
]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)
# print(scaler)
# Expected:
# [
#   [-1.0, -1.0],
#   [ 0.0,  0.0],
#   [ 1.0,  1.0]
# ]