.PHONY: env test

env: bin bin/py.test

bin:
	virtualenv --no-site-packages .

bin/jailpkg: bin test
	bash -c "source bin/activate &&\
		pip install --upgrade ."

bin/py.test: bin
	bash -c "source bin/activate &&\
		pip install -r requirements.txt"

requirements.txt:
	bash -c "source bin/activate &&\
		pip freeze > requirements.txt"

test: tests/unit/ | bin/py.test
	bash -c "source bin/activate &&\
		PYTHONPATH=$(pwd) py.test -s tests/unit/*"

itest: bin/jailpkg
	bash -c "source bin/activate &&\
		PYTHONPATH=$(pwd) bin/jailpkg"

clean:
	rm jailpkg/*.pyc
