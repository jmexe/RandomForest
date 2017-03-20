from main import load_data
import random

def generate_noise(num):
    keymaps = load_keys("data/attributes.data")
    return [[random.choice(keymaps[j].keys()) for j in range(len(keymaps))] for i in range(num)]

def add_noise(output_file):
    noices = generate_noise(1000)
    file = open(output_file, "a")
    for noice in noices:
        file.write(','.join(noice) + '\n')
    file.close()


def load_keys(file_path):
    file = open(file_path)
    keymaps = []
    for line in file:
        tokens = line.strip().split(",")
        keymap = {}
        for i, token in enumerate(tokens):
            keymap[token] = i
        keymaps.append(keymap)
    return keymaps

def shrink_data(file_path, output_file):
    records = load_data(file_path)[0]
    sub_records = random.sample(records, 200)
    noices = generate_noise(100)
    file = open(output_file, 'w+')
    for record in sub_records:
        file.write(record['label'] + "," + ','.join(record["attributes"]) + "\n")
    for noice in noices:
        file.write(','.join(noice) + '\n')



    file.close()

if __name__ == "__main__":
    shrink_data("data/mushrooms_train.data", "data/mushrooms_train_final_mix.data")
