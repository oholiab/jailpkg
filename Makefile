.PHONY: env test

env: bin bin/py.test

bin:
	virtualenv --no-site-packages .

bin/jailpkg: bin test
	bash -c "source bin/activate &&\
		pip install ."

bin/py.test: bin
	bash -c "source bin/activate &&\
		pip install -r requirements.txt"

test: tests/unit/ | bin/py.test
	bash -c "source bin/activate &&\
		PYTHONPATH=$(pwd) py.test -s tests/unit/*"

itest: bin/jailpkg
	bin/jailpkg
