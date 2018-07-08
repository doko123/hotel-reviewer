start-flask:
	docker-compose run --rm --service-ports hotel_reviewer flask run -h 0.0.0.0
test:
	docker-compose run --rm hotel_reviewer py.test -s -v
test-flake8:
	docker-compose run --rm hotel_reviewer flake8 .