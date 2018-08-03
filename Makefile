start-flask:
	docker-compose run --rm --service-ports hotel_reviewer flask run -h 0.0.0.0
test:
	docker-compose run --rm hotel_reviewer py.test /app/tests -s -vv
test-flake8:
	docker-compose run --rm hotel_reviewer flake8 .
update-req:
	pip-compile --no-index --output-file requirements.txt requirements.in
black:
	black app -l 80
test-selenium:
	docker-compose run --rm hotel_reviewer py.test /app/tests/workflows/providers/comments -s -vv