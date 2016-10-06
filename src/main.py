from DecisionTree import DecisionTree
from RandomForest import RandomForest

def load_data(file_path):
    records = []
    file = open(file_path)
    for line in file:
        tokens = line.strip().split(',')
        records.append({"label":tokens[0], "attributes":tokens[1:]})
    attributes = range(len(records[0]["attributes"]))
    file.close()
    return records, attributes

def test_model(model):
    records, attributes = load_data("data/mushrooms_train.data")
    model.train(records, attributes)
    test_records = load_data("data/mushrooms_test.data")[0]
    correct_cnt = 0
    for sample in test_records:
        if model.predict(sample) == sample["label"]:
            correct_cnt += 1
    print float(correct_cnt) / len(test_records)

if __name__ == "__main__":
    test_model(DecisionTree())
