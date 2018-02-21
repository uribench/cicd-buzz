[![Build Status](https://travis-ci.org/uribench/cicd-buzz.svg?branch=master)](https://travis-ci.org/uribench/cicd-buzz)
[![Code Quality](https://api.codacy.com/project/badge/Grade/c8156387b65b41aa95ea4034510f1de2)](https://www.codacy.com/app/uribench/cicd-buzz)
[![Maintainability](https://api.codeclimate.com/v1/badges/f405c99f0d7c968d57ec/maintainability)](https://codeclimate.com/github/uribench/cicd-buzz/maintainability)
[![BCH compliance](https://bettercodehub.com/edge/badge/uribench/cicd-buzz?branch=master)](https://bettercodehub.com/)

# cicd-buzz
Experimenting with how to build a modern CI/CD pipeline

Running Local Tests
-------------------
To use the ‘pytest’ framework in the Python Virtual Environment (‘virtualenv’) after creating the 'venv' directory type in 'Git Bash':
```
[cicd-buzz] $ source venv/Scripts/activate
(venv) [cicd-buzz] $ python -m pytest -v tests/test_generator.py
```

For more details see (note the above instructions and the test code in 'test_generator.py' were modified):
	How to build a modern CI/CD pipeline Using free and hosted services
	https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b

