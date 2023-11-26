# example from the video
# Remember: min for django for is 3.8 the extra words are for an OS
# can choose diferent if wanted, some commands below may be different in different OS
FROM python:3.8-slim-buster 

# working directory inside the container
WORKDIR /santa_app #

# bring over the requirements we already have and run/install
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copying our project to the docker folder
# Remember: . in directories referes to current
COPY . .

# finaly, like we have been doing all semester (with 1 extra step)
# let docker run the server
# the extra step is that we also need to give the host (even though it is defined in the app itself)
# this is because the app defines on the local machine (now docker)
# so we need to map actual local to docker local
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
