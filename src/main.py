from DecisionTree import DecisionTree

def load_data(file_path):
    records = []
    file = open(file_path)
    for line in file:
        tokens = line.strip().split(',')
        records.append({"label":tokens[0], "attributes":tokens[1:]})
    attributes = range(len(records[0]["attributes"]))
    file.close()
    return records, attributes

def test_decision_tree():
    records, attributes = load_data("data/mushrooms_train.data")
    dt = DecisionTree()
    dt.train(records, attributes)
    dt.print_tree(dt.root)
    test_records = load_data("data/mushrooms_test.data")[0]
    correct_cnt = 0
    for sample in test_records:
        if dt.predict(sample) == sample["label"]:
            correct_cnt += 1
    print float(correct_cnt) / len(test_records)

if __name__ == "__main__":
    test_decision_tree()
