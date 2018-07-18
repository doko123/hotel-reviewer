

# Hotel_reviewer
`docker-compose build`

Run the selenium container using `docker-compose up selenium-hub` 

Wait for a chrome node
`while ! (curl -sSL "http://localhost:4444/grid/console" | grep -i chrome) >/dev/null 2>&1; do echo -n "."; sleep 0.2; done`

or wait for a firefox node
`while ! (curl -sSL "http://localhost:4444/grid/console" | grep -i firefox) >/dev/null 2>&1; do echo -n "."; sleep 0.2; done`

Run 
`make test-selenium`