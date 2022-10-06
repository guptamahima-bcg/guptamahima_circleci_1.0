FROM python:3.8.10-alpine3.13

WORKDIR /circleci-project-setup

COPY requirements.txt requirements.txt
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "billing_system.py"]