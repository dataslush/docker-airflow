FROM python:3.8-buster

RUN apt-get update -y \
    && apt-get install -y python3-dev python3-pip build-essential \
    && apt-get install gcc -y \
    && apt-get install sudo -y \ 
    && apt-get clean 

RUN adduser --disabled-password --gecos '' datum-oracle
ENV PATH="$PATH:/home/datum-oracle/.local/bin"
WORKDIR /home/datum-oracle
USER datum-oracle
RUN python -m pip install --upgrade pip

# We can install custom .whl package as well
RUN pip install requests