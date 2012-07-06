#!/bin/bash
hyde gen
hyde publish -c prod.yaml
scp ~/www_publish.zip kellerbw@physwww.mcmaster.ca:~
ssh kellerbw@physwww.mcmaster.ca "unzip -o ~/www_publish.zip -d ~/public_html"
