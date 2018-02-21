[![Build Status](https://travis-ci.org/uribench/cicd-buzz.svg?branch=master)](https://travis-ci.org/uribench/cicd-buzz)
[![Code Quality](https://api.codacy.com/project/badge/Grade/c8156387b65b41aa95ea4034510f1de2)](https://www.codacy.com/app/uribench/cicd-buzz)
[![Maintainability](https://api.codeclimate.com/v1/badges/f405c99f0d7c968d57ec/maintainability)](https://codeclimate.com/github/uribench/cicd-buzz/maintainability)
[![BCH compliance](https://bettercodehub.com/edge/badge/uribench/cicd-buzz?branch=master)](https://bettercodehub.com/)

# cicd-buzz
Experimenting with how to build a modern CI/CD pipeline

Usage
-----
Run this Python script from the command line (or 'Git Bash') inside the ‘buzz’ directory as follows:
```
	[cicd-buzz/buzz] $ python generator.py
```

Running Local Tests
-------------------
To use the ‘pytest’ framework in the Python Virtual Environment (‘virtualenv’), after creating the 'venv' directory, type in 'Git Bash':
```
	[cicd-buzz] $ source venv/Scripts/activate
	(venv) [cicd-buzz] $ python -m pytest -v tests/test_generator.py
	(venv) [cicd-buzz] $ deactivate
	[cicd-buzz] $ 
```
For more details see:
	[1]	How to build a modern CI/CD pipeline Using free and hosted services
		https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b
Note: The above instructions and the test code in 'test_generator.py' were modified from [1].

Generating a Coverage Report
----------------------------
To generate a coverage report for this Python script, use the following commands from the command line (or 'Git Bash') inside the ‘buzz’ directory as follows:
```
	[cicd-buzz/buzz] $ coverage run generator.py
	[cicd-buzz/buzz] $ coverage report -m
```
For a nicer presentation, use 'coverage html' instead of 'coverage report -m' to get annotated HTML listings detailing missed lines:
```
	[cicd-buzz/buzz] $ coverage html
```
Note: To see the coverage html report launch 'cicd-buzz\buzz\htmlcov\index.html' 
