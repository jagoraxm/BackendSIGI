
# dependencies of system
    python 
    pipenv

# run project
    flask run
        o
    python app.py

# how to activate existing with pipenv
    pipenv shell

# create environment by virtualenv
    python -m venv env

# create file  requirements.txt
    pip freeze > requirements.txt

# install dependencies
    pip install -r requirements.txt

# by run tests
    pytest
    pytest -v

# run test of single file
    pytest tests/test_post_degree.py

# run test of single file with mark
    pytest -v -m smoke tests/test_post_degree.py

# run test of a directory
    pytest tests/

# run test coverage
    coverage run -m pytest

# run report test coverage
    coverage report 
    coverage report -m 

# run and generated report test to "html" 
    coverage html

