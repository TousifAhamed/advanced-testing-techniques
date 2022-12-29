# advanced-testing-techniques
This is the repo for testing techniques

# Setup

1. Create and Source Virtualenv

```bash
virtualenv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
```

2. Create Scaffold

```bash
touch Makefile && touch test_hello.py && touch hello.py && touch requirements.txt
```

3. Populate `Makefile`

```bash
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py 

all: install lint test
```

### How to debug

* Print
* pdf
* testing