FROM python:3.8

WORKDIR /

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT ['python', '-m', 'miniproblem']

CMD ['-u', 'miniproblem']
