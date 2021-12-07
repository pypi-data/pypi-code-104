import setuptools
import aviv_cdk

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aviv-cdk", # Replace with your own username
    version=aviv_cdk.__version__,
    author="Jules Clement",
    author_email="jules.clement@aviv-group.com",
    description="Aviv CDK Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aviv-group/aviv-cdk-python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    py_modules=[
        'bin.aws_local',
        'bin.sfn_extract'
    ],
    data_files=[
        ("share/aviv-cdk/cfn-resources", ["lambdas/cfn_resources/requirements.txt"])
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'aviv-aws=bin.aws_local:cli',
            'aviv-cdk-sfn-extract=bin.sfn_extract:cli'
        ],
    },
    install_requires=[
         "boto3>=1.18.40",
         "botocore>=1.21.40",
         "click>=8.0.0",
         "aws-parsecf>=1.1"
         "aws-cdk-core>=1.124",
         "aws-cdk-aws-iam>=1.124",
         "aws-cdk-aws-s3>=1.124",
         "aws-cdk-aws-lambda>=1.124",
         "aws-cdk-aws-events>=1.124",
         "aws-cdk-aws-events-targets>=1.124",
         "aws-cdk-aws-ssm>=1.124",
         "aws-cdk-aws-secretsmanager>=1.124"
   ],
    setup_requires=['pytest-runner>=5.3.0'],
    tests_require=['pytest'],

    extras_require={
        "cicd": [
            "aws-cdk-aws-cloudformation",
            "aws-cdk-aws-codebuild",
            "aws-cdk-aws-codecommit",
            "aws-cdk-aws-codepipeline",
            "aws-cdk-aws-codepipeline-actions",
            "aws-cdk-aws-codestarconnections",
            "aws-cdk-pipelines",
            "pyyaml>=5.4"
        ],
        "nextstep": [
            "aws-cdk-aws-stepfunctions",
            "aws-cdk-aws-stepfunctions-tasks"
        ],
        "data": [
            "aws-cdk-glue",
            "aws-cdk-athena"
        ]
    },
    python_requires='>=3.8',
    use_2to3=False,
    zip_safe=False
)
