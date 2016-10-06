import random

class RandomForest(object):
    def __init__(self):
        self.forest = []

    def bootstrap(self, records):
        """
        This function bootstrap will return a set of records, which has the same
        size with the original records but with replacement.
        """
        bag = []
        # You code here
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
        pass

    def predict(self, sample):
