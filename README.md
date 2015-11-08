# radius_restserver
REST Endpoint for FreeRadius Server

This includes a (very insecure) FreeRADIUS 2.0 server and a Django app for accessing RADIUS data.
We're hoping this will one day be a replacement for ARA.

This is designed to be built with docker-compose

something like…

```
docker-compose up -d
docker-compose run --rm radius /usr/src/build/load-test-data.sh
```

You probably want to use `docker-compose logs` a lot.

The web app is exposed on port 81 in docker-compose. We develop with docker-machine and this works nicely.
