FROM ubuntu
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install python3 python3-pip vim zip git

RUN pip3 install --upgrade pyyaml beautifulsoup4 requests

ENV PYTHONIOENCODING utf-8

RUN mkdir /app
ADD portrety-search.py /app
RUN echo "docker cp portrety-search.py portrety_dev:/app && docker exec -ti portrety_dev bash"
RUN echo "cd /app && python3 portrety-search.py"
