all:
	python3 setup.py sdist

clean:
	rm -rf build dist *.egg-info