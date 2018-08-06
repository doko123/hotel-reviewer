FROM joyzoursky/python-chromedriver:3.6-selenium as builder

LABEL maintainer="Dominika Kowalczyk <dominika15kowalczyk@gmail.com>"

######################
# Install Dependencies
######################

COPY requirements.txt /req/
RUN cd /req; pip install -r requirements.txt

######################
# Install Application
######################

FROM joyzoursky/python-chromedriver:3.6-selenium
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /root/.cache /root/.cache

# Copy the current directory contents into the container at /app
COPY app/ /app/

# Make port 80 available to the world outside this container
EXPOSE 80

######################
# Set Application Environment Variables
######################

ENV PYTHONIOENCODING=utf-8 \
    PYTHONPATH=/app \
    FLASK_APP=app.py \
    DYNACONF_SETTINGS=config.settings

# Set the working directory to /app
WORKDIR /app

######################
# Run Application
######################
# Run app.py when the container launches
CMD ["/usr/local/bin/gunicorn", "app:application", "-b", "0.0.0.0:5000", "-t 10800", "--workers=2", '--worker-class="egg:meinheld#gunicorn_worker"', "gunicorn_test:app"]
