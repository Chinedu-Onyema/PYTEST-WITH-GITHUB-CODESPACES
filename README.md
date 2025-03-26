# PYTEST-WITH_GITHUB-CODESPACES

# TEST BADGE
[![Python application test with Github Actions](https://github.com/Chinedu-Onyema/PYTEST-WITH-GITHUB-CODESPACES/actions/workflows/main.yml/badge.svg)](https://github.com/Chinedu-Onyema/PYTEST-WITH-GITHUB-CODESPACES/actions/workflows/main.yml)



# PYTEST INSTRUCTIONS ON CONTINOUS INTEGRATION WITH DIFFERENT PLATFORMS
pytest-tips-tricks
A primer on pytest

Introduction to Testing with pytest
Why Test?
Does anything work?
Why PyTest?
Setup Cloud Development Environments with Local CI and Compare:
Github Codespaces
AWS Cloud9
AWS Cloudshell
CI Systems with PyTest
Github Actions: https://docs.github.com/actions/automating-builds-and-tests/building-and-testing-nodejs-or-python?langId=py
AWS Code Build
Invoking pytest
Overview of pytest invocation
Simple version: make test via python -m pytest -vv test_hello.py
Adding Code Coverage: pytest-cov python -m pytest -vv --cov=hello test_hello.py
Coverage Invoke Snippit
Adding Jupyter Notebook testing:
nbval: https://github.com/computationalmodelling/nbval
nbval
Debugging Code with PDB
What is PDB and how does it work?
Alternative IPDB[https://pypi.org/project/ipdb/]
Invoke pytest with --pdb: https://github.com/paiml/testing-in-python/blob/master/chapter6/Makefile#L2
Stop on fail:
pytest -x
pytest --maxfail=2
Specify Tests: https://docs.pytest.org/en/6.2.x/usage.html?highlight=pdb#specifying-tests-selecting-tests
dir
keyword
Build a report: https://docs.pytest.org/en/6.2.x/usage.html?highlight=pdb#detailed-summary-report
Advanced pytest
Setup and Teardown
Testing Click CLI
Testing Flask API
Testing FastAPI
References
To use caching use this option: https://github.com/actions/cache/blob/main/examples.md#python---pip
Watch the pytest master class
Watch on YouTube
Watch on O'Reilly
