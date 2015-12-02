.PHONY: env pipinstall

env: bin

bin: | pipinstall
	virtualenv --no-site-packages .

pipinstall:
	bash -c "source bin/activate &&\
		pip install -r requirements.txt
