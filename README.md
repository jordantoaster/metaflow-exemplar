# metaflow-exemplar

## Setup

### Prerequisites

- Python 3 installed.

- AWS CLI setup.

- AWS credentials configured. 

### Steps

1. Update ``config/config.json`` with details of an S3 bucket on AWS for run data.

2. ``source setup.sh`` - the ``source`` command ensures the environment activates in your working shell. This command sets up a virtual environment and installs the required dependencies. 

3. ``cp config.json ~/.metaflowconfig/`` -

4. ``python src/flows/training.py run``

## Cloudformation Commands

- ``aws cloudformation create-stack --stack-name metaflow-stack-test --template-body file://cloudformation/metaflow-cfn-template.yml --capabilities CAPABILITY_NAMED_IAM``
- ``aws cloudformation describe-stacks --stack-name metaflow-stack-test``

## References

- https://github.com/helli0n/metaflow-example