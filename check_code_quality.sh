#!/usr/bin/bash

STATUS_CODE=0
echo "Black is running.."
black --config .black.toml . || ((STATUS_CODE++))
echo "Pylint is running.."
pylint --rcfile .pylintrc package1/  || ((STATUS_CODE++))
echo "Flake8 is running.."
#flake8 --config .flake8
echo "Isort is running.."
#isort . settings .isort.cfg .

echo $STATUS_CODE
