from metaflow import FlowSpec, step, IncludeFile, batch, S3, Parameter, current
import time
import numpy as np
from io import StringIO
from random import choice
from sklearn import linear_model
from sklearn.metrics import r2_score

class RegressionModel(FlowSpec):

    # Include a local file.
    DATA_FILE = IncludeFile(
        'dataset',
        help='Text File With Regression Numbers',
        is_text=True,
        default='dataset.txt')

    @step
    def start(self):

        print("flow name: %s" % current.flow_name)
        print("run id: %s" % current.run_id)
        print("username: %s" % current.username)

        # Data is an array of lines from the text file containing the numbers
        raw_data = StringIO(self.DATA_FILE).readlines()

        # Cast strings to float and prepare for training
        self.dataset = [[float(_) for _ in d.strip().split('\t')] for d in raw_data]

        # store dataset as train and test set
        split_index = int(len(self.dataset) * 0.8)
        self.train_dataset = self.dataset[:split_index]
        self.test_dataset = self.dataset[split_index:]

        # Branch into two nodes, training two versions of the model basedon parameters.
        self.normalise = [True, False]
        self.next(self.train_model, foreach='normalise')

    # @batch(gpu=1, memory=80000)
    @step
    def train_model(self):

        # Get the input fan out parameter
        self.normalise = self.input

        # build the model
        x_train = np.array([[_[0]] for _ in self.train_dataset])
        y_train = np.array([_[1] for _ in self.train_dataset])
        x_test = np.array([[_[0]] for _ in self.test_dataset])
        y_test = np.array([_[1] for _ in self.test_dataset])

        # Create linear regression model
        regr = linear_model.LinearRegression()
        regr.fit(x_train, y_train)

        # Get and store results.
        y_pred = regr.predict(x_test)
        self.r2 = r2_score(y_test, y_pred)
        print("Test set results: {}".format(self.r2))

        # Store model
        self.model = regr
     
        # finally join with the other runs
        self.next(self.join_runs)

    @step
    def join_runs(self, inputs):

        # merge r2 from runs with different parameters
        self.results_from_runs = {
            input.normalise:{'metrics': input.r2}
            for input in inputs
        }
        print("Current results: {}".format(self.results_from_runs))

        # Pick random model for now (lowest loss in real world)
        self.best_r2 = choice(list(self.results_from_runs.keys()))

        self.next(self.deploy)

    @step
    def deploy(self):
        """
        TODO: Deployment logic
        """
        self.next(self.end)

    @step
    def end(self):
        """
        The final step is empty here, but cleaning operations and/or sending hooks for downstream deployment tasks
        is a natural necessity for machine learning DAGs.
        """
        print('Dag ended!')

if __name__ == '__main__':
    RegressionModel()