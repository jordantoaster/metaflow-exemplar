# metaflow-exemplar

## Setup

### Prerequisites

- Python 3 installed.

- AWS CLI setup.

- AWS credentials configured. 

### Steps

1. Update ``config/config.json`` with an s3 bucket of choice, a default is in place.

2. ``source setup.sh`` - the ``source`` command ensures the environment activates in your working shell. This command sets up a virtual environment, installs the required dependencies and moves the metaflow config into the right folder. 

3. ``python src/flows/training.py run`` from the root terminal.

## Cloudformation Commands

Note: Not working due to permissions errors on stack create.

- ``aws cloudformation create-stack --stack-name metaflow-stack-test --template-body file://cloudformation/metaflow-cfn-template.yml --capabilities CAPABILITY_NAMED_IAM``
- ``aws cloudformation describe-stacks --stack-name metaflow-stack-test``

## References

- https://github.com/helli0n/metaflow-example

## Todo
- Cloudformation working to enable creation of batch job submissions to AWS (ask ops team on best approach/permissions?)
    - Or run in personal AWS. 