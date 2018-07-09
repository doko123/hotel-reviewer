FROM python:3.6-alpine3.7 as builder

LABEL maintainer="Dominika Kowalczyk <dominika15kowalczyk@gmail.com>"

######################
# Install Dependencies
######################

COPY requirements.txt /req/
RUN cd /req; pip install -r requirements.txt

######################
# Install Application
######################

FROM python:3.6-alpine3.7
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /root/.cache /root/.cache
COPY app/ /app/


######################
# Set Application Environment Variables
######################

ENV PYTHONIOENCODING=utf-8 \
    PYTHONPATH=/app \
    FLASK_APP=app.py \
    DYNACONF_SETTINGS=config.settings

WORKDIR /app

######################
# Run Application
######################

CMD ["/usr/local/bin/gunicorn", "app:application", "-b", "0.0.0.0:5000", "-t 10800"]
