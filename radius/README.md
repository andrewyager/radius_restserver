#FreeRADIUS Docker image

This is a FreeRADIUS docker image that is designed to work with an external SQL database.

It mimics a live freeradius environment we run, but in some slightly different ways.

It assumes the MySQL container is linked under the hostname "mysql". The docker-compose command in the parent app demonstrates this.

On boot this image attempts to connect to the MySQL server, and will loop until it can to load the SQL schema (if it's not there). If there is a database called 'radius' and it can connect using the default username and password (which are radius/radius) it will assume that the database exists and it does not need to be recreated.
