import pandas as pd
class StandardScaler:
    def __init__(self):
        self.mean_ = None
        self.std_ = None

    def fit(self, X):
        self.mean_ = X.mean(axis =0)
        self.std_ = X.std()
        # Compute mean and std for each column
        return

    def transform(self, X):
        print(self.mean_,self.std_)
        df_standard = (X-self.mean_)/self.std_
        return df_standard
        # Apply standardization to each value
        pass

    def fit_transform(self, X):
        
        self.fit(X)
        return self.transform(X)

if __name__ == "__main__":

    data = {
        'A': [1, 2, 10],
        'B': [4, 3, 6],
        'C': [7, 7, 9]
    }
    df = pd.DataFrame(data)

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    print("Original DataFrame:")
    print(df)
    print("\nStandardized DataFrame:")
    print(df_scaled)