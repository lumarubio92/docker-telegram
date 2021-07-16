
FROM python:3.10.0b3-alpine3.14
WORKDIR /home/app 
COPY app /home/app
RUN pip install requests
RUN pip install schedule
RUN /bin/cp /usr/share/zoneinfo/America/Mexico_City  /etc/localtime && echo 'America/Mexico_City ' >/etc/timezone

