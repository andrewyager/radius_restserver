#!/bin/bash
cd /var/www/html
bower install --config.interactive=false
npm install grunt-wiredep --save-dev
grunt wiredep