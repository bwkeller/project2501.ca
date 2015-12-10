<!-- 
.. title: Making Mock Observations with Sunrise & Docker
.. slug: making-mock-observations-with-sunrise-docker
.. date: 2015-09-15 22:54:37 UTC-04:00
.. tags: docker,sunrise,linux
.. category: 
.. link: 
.. description: 
.. type: text
-->

In a previous post, I described how

#Setting up the docker instance
##Data volumes for file sharing
We will need somewhere to place our simulation outputs, configuration files, and
ultimately, the output of sunrise.  We will also need to let our docker
container read and write to this directory.  All you need to do in order to do
this is use the `-v host_directory:container_directory` switch when starting
your container.  This will mount `host_directory` in the docker container at the
`container_directory` mountpoint.  In other words, we start our docker image
with something like this command:

```
docker run -t -i -v ~/sunrise_data:/sunrise_data bwkeller/sunrise:latest 
/bin/bash
```

#
