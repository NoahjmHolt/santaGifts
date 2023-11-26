# example from the video
# Remember: min for django for is 3.8 the extra words are for an OS
# can choose diferent if wanted, some commands below may be different in different OS
FROM python:3.11.4-alpine

# working directory inside the container
WORKDIR /usr/src/santa_app

# general proper code that most people use to negate common errors
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# make sure everything is up to date and working
# then installing requirements so smooth ride 
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/santa_app/requirements.txt
RUN pip install -r requirements.txt

# import entry point and everything else
COPY ./entrypoint.sh /usr/src/santa_app/entrypoint.sh
COPY . /usr/src/santa_app/

# now run its
ENTRYPOINT [ "/usr/src/santa_app/entrypoint.sh" ]
