install: 
	poetry install


brain-games: 
	poetry run brain-games


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install dist/*.whl


lint:
	poetry run ruff check


brain-calc:
	poetry run brain-calc


brain-even:
	poetry run brain-even


brain-gcd:
	poetry run brain-gcd


brain-prime:
	poetry run brain-prime


brain-progression:
	poetry run brain-progression


reinstall:
	pip install --user --force-reinstall dist/*.whl