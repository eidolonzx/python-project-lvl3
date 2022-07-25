build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

renew:
	poetry build
	python3 -m pip install --user dist/*.whl --force-reinstall

run:
	poetry run page_loader

lint:
	poetry run flake8 page_loader

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml