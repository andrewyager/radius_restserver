FROM debian:jessie

#RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y apache2  php5 php5-cli php5-gd php5-mcrypt php5-mysql mysql-client
RUN apt-get update && apt-get install -y freeradius freeradius-mysql freeradius-utils

EXPOSE 1812
EXPOSE 1813

RUN mkdir -p /usr/src/build
RUN mkdir /usr/src/build/sql
COPY ./sql/radius-structure.sql /usr/src/build/sql/radius-structure.sql
COPY ./src/start-radius.sh /usr/src/build/start-radius.sh

COPY ./config/radiusd.conf /etc/freeradius/radiusd.conf
COPY ./config/sql.conf /etc/freeradius/sql.conf
COPY ./config/sites-available/default /etc/freeradius/sites-available/default
COPY ./config/sites-available/sql /etc/freeradius/sites-available/sql
COPY ./config/sql/mysql/dialup.conf /etc/freeradius/sql/mysql/dialup.conf
RUN ln -s /etc/freeradius/sites-available/sql /etc/freeradius/sites-enabled/sql

COPY ./src/load-test-data.sh /usr/src/build/load-test-data.sh
COPY ./sql/test-data.sql /usr/src/build/sql/test-data.sql
RUN chmod 755 /usr/src/build/load-test-data.sh


USER freerad
CMD /bin/bash /usr/src/build/start-radius.sh