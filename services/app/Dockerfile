# base image
# Decreased hosting costs since less disk space is used
# Quicker build, download, and run times
# More secure (since there are less packages and libraries)
# Faster deployments

FROM python:3.7.2-alpine

# install dependencies
RUN apk update && \
apk add --virtual build-deps gcc python-dev musl-dev && \
apk add postgresql-dev && \
apk add netcat-openbsd

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD ["/usr/src/app/entrypoint.sh"]
