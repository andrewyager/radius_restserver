#FreeRADIUS Docker image

This is a FreeRADIUS docker image that is designed to work with an external SQL database.

It mimics a live freeradius environment we run, but in some slightly different ways.

It assumes the MySQL container is linked under the hostname "mysql". The docker-compose command in the parent app demonstrates this.
