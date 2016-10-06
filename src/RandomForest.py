import random
from DecisionTree import DecisionTree

class RandomForest(object):
    def __init__(self):
        self.forest = []

    def bootstrap(self, records):
        """
        This function bootstrap will return a set of records, which has the same
        size with the original records but with replacement.
        """
        # You code here
        bag = [random.choice(records) for i in range(len(records))]
        return bag

    def train(self, tree_num, records, attributes):
        """
        This function will train the random forest, the basic idea of training a
        Random Forest is as follows:
        1. Draw n bootstrap samples using bootstrap() function
        2. For each of the bootstrap samples, grow a tree, with the following
            modification: at each node, randomly sample m of the predictors and
            choose the best split from among those variables
        """
        # Your code here
        for i in range(tree_num):
            tree = DecisionTree()
            bag = self.bootstrap(records)
            sub_attributes = random.sample(attributes, int(math.ceil(math.sqrt(len(attributes)))))
            tree.train(bag, sub_attributes)
            self.forest.append(tree)

    def predict(self, sample):
        """
        The predict function predicts the label for new data by aggregating the
        predictions of each tree
        """
        votes = [tree.predict(sample) for tree in self.forest]
        label = max(Counter(votes).iteritems, key = lambda x:x[1])[0]

        return label
