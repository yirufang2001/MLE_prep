class DummyModel:
    def __init__(self, version=1, bias=0.0):
        self.version = version
        self.bias = bias
        self._is_fitted = False
    
    def _validate_input(self,X):
        if not isinstance(X,list) or not all(isinstance(x,list) for x in X):
            raise ValueError("Input must be a list of lists")
        if not all(all(isinstance(x, (int, float)) for x in row) for row in X):
            raise ValueError('all input should be number!')
        

    def fit(self, X):
        self._validate_input(X)
        self._is_fitted = True
        # Validate input, then mark as fitted


    def predict(self, X):
        # self.fit(X)
        if not self._is_fitted:
            raise RuntimeError("Model is not fitted yet")
        self._validate_input(X)  # ✅ Make sure input is valid!
        return [sum(row) + self.bias for row in X]
        # Validate input, check fitted, return prediction
        # pass

    def __str__(self):
        # Optional string representation
        return f"DummyModel(v{self.version}, bias={self.bias})"
    
def main():
    print("✅ Running DummyModel tests...\n")

    # Create model with custom version and bias
    model = DummyModel(version=2, bias=1.5)
    print(model)  # DummyModel(v2, bias=1.5)

    # Case 1: Predict before fit (should raise error)
    try:
        model.predict([[1, 2]])
        print("❌ Error: predict() before fit() should raise RuntimeError")
    except RuntimeError as e:
        print(f"✔️ Caught expected error: {e}")

    # Case 2: Fit with valid input
    try:
        model.fit([[1, 2], [3, 4]])
        print("✔️ Fit passed with valid input")
    except Exception as e:
        print(f"❌ Fit failed: {e}")

    # Case 3: Predict after fitting
    try:
        predictions = model.predict([[1, 2], [3, 4]])
        expected = [sum(row) + model.bias for row in [[1, 2], [3, 4]]]
        assert predictions == expected
        print("✔️ Predict passed: output =", predictions)
    except Exception as e:
        print(f"❌ Predict failed: {e}")

    # Case 4: Invalid input to fit (not a list of lists)
    try:
        model.fit("invalid input")
        print("❌ Error: invalid input should raise ValueError")
    except ValueError as e:
        print(f"✔️ Caught expected ValueError in fit(): {e}")

    # Case 5: Predict with non-numeric data
    try:
        model.predict([[1, "a"]])
        print("❌ Error: non-numeric input should raise ValueError")
    except ValueError as e:
        print(f"✔️ Caught expected ValueError in predict(): {e}")

    # Case 6: Empty input
    try:
        model.fit([])
        print("✔️ Fit passed with empty list (edge case)")
    except Exception as e:
        print(f"❌ Error: unexpected exception with empty input: {e}")

    print("\n✅ All DummyModel tests completed.\n")

# Call main to run tests
if __name__ == "__main__":
    main()