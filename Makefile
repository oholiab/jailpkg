.PHONY: env test

env: bin bin/py.test

bin:
	virtualenv --no-site-packages .

bin/py.test: bin
	bash -c "source bin/activate &&\
		pip install -r requirements.txt"

test: bin/py.test
	bash -c "source bin/activate &&\
		PYTHONPATH=$(pwd) py.test -s tests/unit/*"
