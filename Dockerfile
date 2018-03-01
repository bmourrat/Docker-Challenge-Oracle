FROM python:2.7-slim
# we work with python 2.7

ADD . /
# set up the directory where we work, inside the container

RUN pip install --trusted-host pypi.python.org -r requirements.txt
# install the libraries we need to run the .py

CMD [ "python", "server.py" ]
# run server.py when the container launches