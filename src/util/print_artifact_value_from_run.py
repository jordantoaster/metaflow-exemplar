# Demonstrates how you can programmatically access data artifacts - for a given flow run.
# Example: print(Step('RegressionModel/1654355240855157/start').task.data.dataset)

from metaflow import Step
print(Step('<Flow Name>/<RUN ID>/<STEP NAME>').task.data.<VARIABLE NAME>)