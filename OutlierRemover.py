import statistics
class OutlierRemover:
    def __init__(self, threshold=3):
        self.threshold = threshold
        self.mean = None
        self.std= None
        self.cols = None
        self.fitted = False
        
    def fit(self, X):
        self.cols = list(zip(*X))
        self.mean = [statistics.mean(x) for x in self.cols]
        self.std = [statistics.stdev(x) for x in self.cols]
        self.fitted = True



        """Compute mean and std for each column"""

    def transform(self, X):
        # self.fit(X)
        # outliers= set()
        if not self.fitted:
            raise RuntimeError('fit has not be run')
        res = []
        for row in X:
            outlier = False
            for i,k in enumerate(row):
                lower, upper = min(self.mean[i]-self.threshold*self.std[i],self.mean[i]+self.threshold*self.std[i]),max(self.mean[i]-self.threshold*self.std[i],self.mean[i]+self.threshold*self.std[i])
                # upper = self.mean[i]+self.threshold*self.std[i]
                if k< lower or k > upper:
                    outlier = True
                    break
            if not outlier:
                res.append(row)
        
        return res

    def __str__(self):
        return f"OutlierRemover(fitted={self.fitted})"
        """Show whether the OutlierRemover is fitted"""
X = [
    [1.0, 2.0],
    [1.5, 3.0],
    [100.0, 200.0],  # outlier
    [2.0, 2.5],
]

# threshold = 2
remover = OutlierRemover(threshold=1)
remover.fit(X)
cleaned_X = remover.transform(X)
print(cleaned_X)
# Expected cleaned_X:
# [
#     [1.0, 2.0],
#     [1.5, 3.0],
#     [2.0, 2.5]
# ]