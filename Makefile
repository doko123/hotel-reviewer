start-flask:
	docker-compose run --rm --service-ports hotel_reviewer flask run -h 0.0.0.0
test:
	docker-compose run --rm hotel_reviewer py.test /app/tests/
test-debug:
	docker-compose run --rm hotel_reviewer py.test /app/tests -s -vv --lf
test-sa:
	docker-compose run --rm hotel_reviewer python3 /app/sa_script.py
test-flake8:
	docker-compose run --rm hotel_reviewer flake8 .
update-req:
	pip-compile --no-index --output-file requirements.txt requirements.in
black:
	black app -l 80 --exclude=/app/workflows/dry_provider
