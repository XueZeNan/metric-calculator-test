class MetricCalculator:
    def __init__(self):
        self.results = []
    
    def calculate_mean(self, data):
        if(len(data)==0):
            raise ZeroDivisionError("data列表为空，无法计算平均值（除数为0）！")
        return sum(data) / len(data)
    
    def calculate_accuracy(self, y_true, y_pred):
        if(len(y_true)==0):
            raise ValueError("y_true列表为空，无法计算准确率（除数为0）！")
        if len(y_true) != len(y_pred):
            raise ValueError("y_true 和 y_pred 长度不一致")
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_true)
    
    def add_metric(self, name, value):

        self.results.append((name, value))
    
    def get_results(self):
        return self.results
