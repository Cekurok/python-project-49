install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games

brain-event:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

lint:
	poetry run flake8 brain_games

pack:
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl