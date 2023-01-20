lint:
	black . --line-length 79 -t py37 --skip-string-normalization
	isort . --check-only --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 -l 79

test:
	pytest .

down:
	docker-compose down

up:
	docker-compose up
