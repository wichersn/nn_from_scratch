import simple_logistic_neuron
import numpy as np
import pandas as pd

# This uses the data from the Kaggle competition here: https://www.kaggle.com/c/ghouls-goblins-and-ghosts-boo

df = pd.read_csv('../kaggle_ghost_data/train.csv', header=0)

df = pd.concat([df, pd.get_dummies(df['type'], prefix='type')], axis=1)

df = pd.concat([df, pd.get_dummies(df['color'], prefix='color')], axis=1)
df = df.drop(['color', 'type', 'id'], axis=1)

df = df.reindex(np.random.permutation(df.index))

percent_train = .8
num_train = int(len(df)*percent_train)
train = df[:num_train]
test = df[num_train:]

train_y = train.filter(regex="type").values.tolist()
train_x = train.filter(regex="^((?!type).)*$").values.tolist()
test_y = test.filter(regex="type").values.tolist()
test_x = test.filter(regex="^((?!type).)*$").values.tolist()

neurons = [simple_logistic_neuron.LogisticNeuron(len(train_x[0]), .01) for i in range(len(train_y[0]))]

def get_accuracy(test_x, test_y):
    num_right = 0
    for i in range(len(test_x)):
        x = test_x[i]
        y_ = test_y[i]

        y = [neuron.predict(x) for neuron in neurons]
        pred = np.argmax(y)

        if np.argmax(y_) == pred:
            num_right += 1

    return num_right / float(len(test_x))

start = 0
print_num = 10000
for i in range(100000):
    x = train_x[start]
    y_ = train_y[start]

    for n in range(len(neurons)):
        neurons[n].update_w(x, y_[n])

    if(i % print_num == 0):
        print(get_accuracy(test_x, test_y))

    start += 1
    if start >= len(train_x):
        start = 0