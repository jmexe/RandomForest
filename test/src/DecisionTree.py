__author__ = "Ming Jia"
from collections import Counter
import unittest
import math
import random

class TreeNode(object):
    def __init__(self, isLeaf=False):
        self.isLeaf = isLeaf
        self.left = None
        self.right = None
        self.threshold = ""
        self.attribute = 0
        self.label = ""

    def predict(self, sample):
        if self.isLeaf:
            return self.label
        if sample["attributes"][self.attribute] == self.threshold:
            return self.left.predict(sample)
        else:
            return self.right.predict(sample)

class DecisionTree(object):
    def __init__(self):
        self.root = None

    def stopping_cond(self, records, attributes):
        """
        The stopping_cond() function is used to terminate the tree-growing
        process by testing whether all the records have either the same class
        label or the same attribute values.
        """
        # Your code here
        if len(set(record["label"] for record in records)) < 2:
            return True
        return False

    def classify(self, records):
        """
        This function determines the class label to be assigned to a leaf node.
        For each node t, let p(i|t) denote the fraction of training records from
        class i associated with the node t. In most cases, the leaf node is
        assigned to the class that has the majority number of training records
        """
        # Count the labels and return the majority label
        labels = Counter([record["label"] for record in records])
        label = max(labels.iteritems(), key=lambda x:x[1])[0]
        return label

    def entropy(self, records):
        """
        This function calculates the entropy of given set of records
        """
        labels = Counter([record["label"] for record in records])
        entropy = 0.0
        for label in labels.iteritems():
            prob = float(label[1]) / float(len(records))
            if prob > 0:
                entropy = entropy - prob * math.log(prob, 2)
        return entropy

    def find_best_split(self, records, attributes):
        """
        The find_best_split() function determines which attribute should be
        selected as the test condition for splitting the trainig records.
        """
        test_condition = {}
        best_info_gain = 0
        best_threshold = ""
        best_left = None
        best_right = None
        best_attribute = 0

        #Your code here
        #Hint-1: loop through all available attributes
        #Hint-2: for each attribute, loop through all possible values
        #Hint-3: calculate information gain and pick the best attribute
        entropy = self.entropy(records)
        for attribute in attributes:
            # Split the records into two parts based on the value of the selct
            # attribute
            values = set([record["attributes"][attribute] for record in records])

            for threshold in values:
                for threshold in values:
                    left = []
                    right = []
                    # split the records based on the threshold selected
                    for record in records:
                        if record["attributes"][attribute] == threshold:
                            left.append(record)
                        else:
                            right.append(record)
                    # calculate the information gain based on the new split
                    info_gain = entropy - float(len(left) * self.entropy(left) + len(right) * self.entropy(right)) / len(records)
                    # if the information gain is better the best split we have tested
                    # set this split as the best split
                    if info_gain > best_info_gain:
                        best_info_gain, best_threshold, best_left, best_right, best_attribute = info_gain, threshold, left, right, attribute

        return best_threshold, best_left, best_right, best_attribute

    def train(self, records, attributes):
        self.root = self.tree_growth(records, attributes)

    def tree_growth(self, records, attributes):
        """
        """

        if self.stopping_cond(records, attributes):
            leaf = TreeNode(True)
            leaf.label = self.classify(records)
            return leaf
        else:
            root = TreeNode()
            # Split the records into two parts
            best_threshold, best_left, best_right, best_attribute = \
                self.find_best_split(records, attributes)

            if best_left is None or len(best_left) == 0 or best_right is None or len(best_right) == 0:
                root.label = self.classify(records)
                root.isLeaf = True
                return root

            root.threshold, root.attribute, root.left, root.right = \
                best_threshold, best_attribute, \
                self.tree_growth(best_left, attributes), \
                self.tree_growth(best_right, attributes)
        return root

    def predict(self, sample):
        """
        This function predict the label for new sample
        """
        return self.root.predict(sample)

    def print_tree(self, node, indent=""):
        if node == None:
            pass
        else:
            print indent + "(" + node.threshold + "," + str(node.attribute) + "," + node.label + ")"
            self.print_tree(node=node.left, indent="-" + indent)
            self.print_tree(node=node.right, indent="-" + indent)


class TestDecisionTree(unittest.TestCase):
    def setUp(self):
        self.dt = DecisionTree(20)
    def test_classify(self):
        records = [{"label":"A"}, {"label":"B"}, {"label":"B"}]
        self.assertEqual(self.dt.classify(records), "B")
    def test_entropy(self):
        records = [ {"label":"0"}, {"label":"0"}, {"label":"0"}, {"label":"0"},
                    {"label":"0"}, {"label":"1"}]
        # expected entropy : ~0.65
        self.assertTrue(math.fabs(self.dt.entropy(records) - 0.65) < 0.001)
    def test_split(self):
        """
        sample is from textbook p153
        feature list :
            Home Owner: 0=No, 1=Yes
            Marital Status: 0=Single, 1=Married, 2=Divorced
            Annual Income: unit=K
        """
        records = [ {"label":"No",  "attributes":[1, 0, 125]},
                    {"label":"No",  "attributes":[0, 1, 100]},
                    {"label":"No",  "attributes":[0, 0, 70]},
                    {"label":"No",  "attributes":[1, 1, 120]},
                    {"label":"Yes", "attributes":[0, 2, 95]},
                    {"label":"No",  "attributes":[0, 1, 60]},
                    {"label":"No",  "attributes":[1, 2, 220]},
                    {"label":"Yes", "attributes":[0, 0, 85]},
                    {"label":"No",  "attributes":[0, 1, 75]},
                    {"label":"Yes", "attributes":[0, 0, 90]}]
        threshhold, left, right, attribute = self.dt.find_best_split(records, [0, 1, 2])
        self.assertEqual(attribute, 1)
    def test_stopping_cond(self):
        records = [{"label":"A"}]
        self.assertTrue(self.dt.stopping_cond(records, [0, 1, 2]))
        self.assertTrue(self.dt.stopping_cond([], [0, 1, 2]))
        records = records + [{"label":"B"}, {"label":"B"}]
        self.assertFalse(self.dt.stopping_cond(records, [0, 1, 2]))

if __name__ == "__main__":
    unittest.main()
