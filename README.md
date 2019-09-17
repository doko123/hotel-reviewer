# Hotel_reviewer
##### The aim of this project is to collect available comments about specified hotel from accommodation providers.
##### Next bunch of the newest comments are analyzed with sentiment and based on that the score of positive side is calculated.
##### This should ease future customers to make a correct choice to book.

### Setup commands
1. Run application:
    - `make start-flask`
2. Wait until docker is build and up and go to:   
    - `http://localhost:5000/home`
    
OR DEVELOPMENT PURPOSES:
    
1. Create network:  
    - `docker network create hotel_review`
2. Build application:   
    - `docker-compose build`
2. Run application
    - `docker-compose up` or `make start-flask`

### Tests and code linters:
1. Run tests: 
    - `make test` or
    - `docker-compose run --rm hotel_reviewer py.test /app/tests`
2. Run tests with debug and last failed flag:
    - `make test-debug` or
    - `docker-compose run --rm hotel_reviewer py.test /app/tests -s -vv --lf`
2. Run flake8:
    - `make test-flake8` or
    - `docker-compose run --rm hotel_reviewer flake8 .`
3. Run python code formatter
    - `make black`

### Continuous Integration:
1. Feature branch name must pass the regex formula:
    - `/\d+\-[feature|bug]+\/.+/`
2. All branches must pass circle-ci tests before merge to master branch
3. Only squash and merge is accepted way of merging to master

#### Positive scenario view:
![positive_scenario](https://github.com/doko123/hotel-reviewer/blob/master/app/docs/positive_scenario.png)

#### Negative scenario view:
![negative_scenario](https://github.com/doko123/hotel-reviewer/blob/master/app/docs/negative_scenario.png)