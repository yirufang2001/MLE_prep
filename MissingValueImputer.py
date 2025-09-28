import statistics
from collections import Counter
class MissingValueImputer:
    def __init__(self,strategy = 'mean'):
        self.strategy = strategy
        self.mean = []
        self.median = []
        self.most_frequent = []
        self.fitted = False
        if strategy not in ['mean','median','most_frequent']:
            raise ValueError ('strategy invalid')
    
    def fit(self,X):
        cols = list(zip(*X))
        for col in cols:
            cleaned_col = [val for val in col if val is not None]
            m = statistics.mean(cleaned_col)
            n = statistics.median(cleaned_col)
            k = statistics.mode(cleaned_col)
            self.mean.append(m)
            self.median.append(n)
            self.most_frequent.append(k)
        self.fitted= True
        return self
    
    def transform(self,X):
        if not self.fitted:
            raise RuntimeError("fit is not runned")
        for i in range(len(X)):
            for j in range(len(X[0])):
                if self.strategy == 'mean':
                    f=self.mean[j]
                elif self.strategy== 'median':
                    f=self.median[j]
                else:
                    f = self.most_frequent[j]
                if X[i][j] is None:
                    X[i][j] = f
        return X
    
    def fit_transform(self,X):
        return self.fit(X).transform(X)
    
    def __str__(self):
        return f"MissingValueImputer(strategy={self.strategy}, fitted={self.fitted})"

X = [
    [1.0, 2.0],
    [None, 4.0],
    [3.0, None],
    [2.0, 6.0],
]

imputer = MissingValueImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)
print(X_imputed) 


