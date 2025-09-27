from dummymodel import DummyModel  # 如果你的类就在当前文件，可以直接用 DummyModel()

def main():
    print("✅ Running DummyModel tests...")

    # 1. 初始化模型
    model = DummyModel(version=2, bias=1.5)
    print("Model info:", model)  # 这里会调用 __str__()

    # 2. 测试未 fit 直接 predict（应报错）
    try:
        model.predict([[1, 2], [3, 4]])
    except RuntimeError as e:
        print("Expected error:", e)

    # 3. 正常训练和预测
    X_train = [[1, 2], [3, 4], [5, 6]]
    model.fit(X_train)
    preds = model.predict([[1, 1], [2, 2], [3, 3]])
    print("Predictions:", preds)

    # 4. 错误输入测试
    bad_inputs = [
        123,                     # Not a list of list
        [[1, "a"], [3, 4]],      # Non-numeric
        [[1, 2], 3],             # Mixed structure
        [[None], [1.5]],         # None value
    ]
    for bad_X in bad_inputs:
        try:
            model.predict(bad_X)
        except ValueError as e:
            print("Caught expected input error:", e)

    print("✅ All tests complete.")


if __name__ == "__main__":
    main()