import numpy as np
class MiniScaler:
    def __init__(self):
        self.min_max = None
        # self.std = None
    
    def fit(self,X):
        if not all(all(isinstance(item,(float,int))for item in x) for x in X):
            raise ValueError('all inner value should be float or int')
        cols = list(zip(*X)) 
        self.min_max = [(min(x),max(x)) for x in cols]
        # self.std = X.std(axis = 0)
    def transform(self,X):
        if not self.min_max:
            raise RuntimeError("fit has not yes be called")
        
        # self.fit(X)
        scale_X = X.copy()
        for i in range(len(X)):
            
            for j in range(len(X[0])):
                m,n = self.min_max[j]
                if m ==n:
                    scale_X[i][j] = 0
                else:
                    scale_X[i][j] = (scale_X[i][j]-m)/(n-m)
        return scale_X
    
    def __str__(self):
        if self.min_max:
            return "MiniScaler(fitted=True)"
        else:
            return "MiniScaler(fitted=False)"

X = [
    [1, 5],
    [2, 8],
    [3, 7],
]

scaler = MiniScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
print(X_scaled)  
# Expected: [
#   [0.0, 0.0],
#   [0.5, 1.0],
#   [1.0, 0.666...]
# ]