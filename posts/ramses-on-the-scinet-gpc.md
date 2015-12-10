<!-- 
.. title: RAMSES on the Scinet GPC
.. slug: ramses-on-the-scinet-gpc
.. date: 2015-10-13 14:23:04 UTC-04:00
.. tags: linux,ramses,guides
.. category: research
.. link: 
.. description: 
.. type: text
-->

[RAMSES](http://www.itp.uzh.ch/~teyssier/ramses/RAMSES.html) is an AMR
MHD cosmological code.  This is a short guide on how to run it on the Scinet
GPC.

<!-- TEASER_END -->
RAMSES is mercifully easy to get installed on the GPC.  You just need to 
use the correct fortran compiler options, which are beautifully already in the
Makefile!  Just comment the default `F90` and `FFLAGS` out, and uncomment these 
lines:

```
    F90 = mpif90
    FFLAGS = -cpp -fast $(DEFINES) -DNOSYSTEM
```

Then simply go to ramses/trunk/ramses/bin, and edit the Makefile to select the
number of dimensions you want (1, 2, or 3).  Then just run `make`, and you will
get your executable.  Don't forget to remove the `-DWITHOUTMPI` if you want to run
in parallel

After that, simply use the standard GPC submission scripts and `mpirun` to fire
up RAMSES.  
