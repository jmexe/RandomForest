__author__ = "Ming Jia"

class TreeNode(object):
    def __init__(self):
        self.isLeaf = False
        self.left = None
        self.right = None
        self.threshold = 0
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
        return False

    def classify(self, records):
        """
        This function determines the class label to be assigned to a leaf node.
        For each node t, let p(i|t) denote the fraction of training records from
        class i associated with the node t. In most cases, the leaf node is
        assigned to the class that has the majority number of training records
        """

        # Your code here
        return label

    def find_best_split(self, records, attributes):
        """
        The find_best_split() function determines which attribute should be
        selected as the test condition for splitting the trainig records.
        """

        test_condition = {}
        best_info_gain = 0
        best_threshold = 0
        best_left = None
        best_right = None
        best_attribute = 0

        #Your code here
        #Hint-1: loop through all available attributes
        #Hint-2: for each attribute, loop through all possible values
        #Hint-3: calculate information gain and pick the best attribute

        return best_threshold, best_left, best_right, best_attribute

    def train(self, records, attributes):
        self.root = self.tree_growth(records, attributes)

    def tree_growth(self, records, attributes):
        """
        """
        return root

    def predict(self, sample):
        """
        This function predict the label for new sample
        """
        return self.root.predict()
