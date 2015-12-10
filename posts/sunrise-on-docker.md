<!-- 
.. title: Sunrise on Docker
.. slug: sunrise-on-docker
.. date: 2015-08-01 11:42:19 UTC-04:00
.. tags: docker,sunrise,linux
.. category: research
.. link: 
.. description: 
.. type: text
-->

Sunrise is a popular "Monte-Carlo Radiation Transfer code for calculating
absorption and scattering of light in astrophysical situations" (it's hosted on
bitbucket [here](https://bitbucket.org/lutorm/sunrise)).  Unfortunately, it is
notoriously finnicky to get installed, as it relies on specific point release
versions of nearly a dozen different libraries.  This is exactly the sort of
problem that [Docker](https://docker.com) is supposed to solve, at scale:
distributing packages along with all of the library infrastructure they require
in one self-contained image.  If you are skeptical about docker's performance,
check out this paper IBM Research has published:  [in nearly every metric, docker
performance is within 5% of native
bare-metal](http://domino.research.ibm.com/library/cyberdig.nsf/papers/0929052195DD819C85257D2300681E7B/$File/rc25482.pdf)

I'm going to build a docker image with a working
install of sunrise, that should save me and my fellow grad students days of
wrestling with angry, old C++ libraries.  Details below the fold.

<!-- TEASER_END -->
#TLDR; just give me the image!
If you don't care to build your own image, I have uploaded the results of the
instructions below to [Docker Hub](https://hub.docker.com/r/bwkeller/sunrise/).
You can check it out there, and fetch the results with this command:

    docker pull bwkeller/sunrise


#Building the Sunrise image by hand
##Getting docker ready
I won't waste time explaining how to install docker, as that is both
well-documented elsewhere and system-specific.  I am writing this tutorial from
a Debian Stretch system, and it also has worked on my laptop running Ubuntu
15.04.  I am a Debian fan, so we're going to build our container off of a Debian
base.  First, let's grab it, and check that it works:

    docker pull debian:jessie
    docker run debian:jessie cat /etc/apt/sources.list

If that pipes out some standard looking Debian repos, we've now got a working
Debian Jessie (the latest stable version) image.

##Build a base image
I'm going to try first building Sunrise interactively, and then write a
dockerfile to automate the process.   First thing I need to do is get the
basics.  I'll start up my Debian image, and begin installing some essentials:

    docker run  -t -i debian:jessie /bin/bash

Once I'm in the image, I can fetch some of the needed components from apt:
    
    apt-get update
    apt-get install cpio libtbb-dev libtool build-essential units wget vim openmpi-bin mercurial git autoconf libbz2-dev zlib1g-dev libccfits-dev libcfitsio-dev libcfitsio-bin

I will make a directory for my sunrise stuff too.
    
    mkdir sunrise

I'm then commit this as, in case I need to roll back (knowing Sunrise, this may 
be necessary).

    docker commit -m "Added basic stuff from apt" -a "Your Name" CONTAINER_ID
    username/sunrise:free-base

Now we can start our new image and futz around, while still being able to revert
back here and not need to re-install all of the tools from apt.

    docker run -t -i username/sunrise:free-base /bin/bash

##Installing icc
Unfortunately, sunrise will not compile with any free compilers.  We will need
to get the Intel C++ compiler, install that in our image, and then remove it
once we have sunrise built (since we can't legally redistribute it.)  You can
get this from Intel, and you may need to pay for it.  If you qualify though, you
can get a free version from [here](https://software.intel.com/en-us/qualify-for-free-software).
We now also have the additional complication that we will need to make
statically-linked binaries so that we can remove the Intel libraries and not
break everything. 

Once you've got the installer, you will need to set an environment variable to
prevent the from segfaulting:

    export USER=root

It will also want some packages.

    cd /where-intel-compiler-is
    ./install.sh

Be sure to de-select ia32, since we don't want it moaning about missing
libraries.

When it is done, make sure icc is in our path:

    source /opt/intel/bin/iccvars.sh intel64

##Installing the redistributable Intel libraries

    wget 
    cd /
    ./install.sh --install-dir=/usr/local
    source /usr/local/lib/bin/compilervars.sh

##Getting the libraries
Now we need to begin by fetching all of the varied specific versions of
libraries that sunrise relies on.

###Boost
Fetch it:
    
    cd sunrise/
    wget 'http://downloads.sourceforge.net/project/boost/boost/1.48.0/boost_1_48_0.tar.bz2?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fboost%2Ffiles%2Fboost%2F1.48.0%2F&ts=1438447283&use_mirror=tcpdiag'
    mv boost* boost_1_48_0.tar.bz2
    tar xvjf boost_1_48_0.tar.bz2
    rm boost_1_48_0.tar.bz2
    cd boost*/

Patch this ancient version of boost so it compiles with a modern compiler:

    wget --no-check-certificate https://svn.boost.org/trac/boost/raw-attachment/ticket/6165/libstdcpp3.hpp.patch
    patch -p0 < libstdcpp3.hpp.patch
    for file in `grep -r -l TIME_UTC *`; do sed -i -e 's/TIME_UTC/TIME_UTC_/' $file; done

Build it:

    sed -i -e 's/using intel-linux/using intel-linux : : : <compileflags>-shared-intel <linkflags>-shared-intel/' project-config.jam
    echo "using mpi : /opt/intel/impi/5.0.3.048/intel64/bin/mpicc ;" > user-config.jam
    ./bootstrap.sh --without-libraries=python --with-toolset=intel-linux
    ./b2 --user-config=user-config.jam install



###Blitz
Fetch it:

    hg clone http://blitz.hg.sourceforge.net/hgweb/blitz/blitz
    cd blitz/
    hg checkout ab84372f3dce

Build it:

    autoreconf -fiv
    export CXX=icpc
    export CC=icc
    export CXXFLAGS='-O2 -pthread -shared-intel'
    export CFLAGS='-O2 -pthread -shared-intel'
    export LDFLAGS='-pthread -shared-intel'
    ./configure --enable-threadsafe --disable-cxx-flags-preset --enable-serialization 
    make lib
    make install

That was easy!

###libPJutil
Fetch it:
    
    hg clone https://bitbucket.org/lutorm/libpjutil
    cd libpjutil/

Build it:

    autoreconf -fiv
    ./configure
    make

And of course, we finally need to set up our units:
    
    export UNITSFILE=/usr/share/units.dat

##Building Sunrise itself
We are finally ready to install the monster itself.  Let's fetch the source
first.
    
    git clone https://bwkeller@bitbucket.org/lutorm/sunrise.git
    cd sunrise/

Got to configure some environment variables:
    
    autoreconf -fiv
    export CPPFLAGS="-I/usr/local/include -I/usr/local/include/libPJutil -shared-intel"
    export CFLAGS="-O2 -pthread -shared-intel"
    export LDFLAGS='-pthread -shared-intel'
    export CXXFLAGS="-O3 -pthread -shared-intel"
    ./configure

Build the monster:

    make
    make install

#Making it Redistributable
We now need to remove all of the non-free components (read: Intel compiler)

    rm -rf /sunrise
    /opt/intel/parallel_studio_xe_2015/uninstall.sh --default
    rm -rf /opt/intel

#Finalize Install
We now need to make sure all of the libraries are in ```$LD_LIBRARY_PATH``` when
we start our image:
    
    echo "source /usr/local/bin/compilervars.sh intel64" >> /etc/bash.bashrc
    echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib" >> /etc/bash.bashrc

The last thing we need to do is remove some temporary files and clean up the
image.

    rm -rf /tmp/intel*
    echo > ~/.bashrc

And we are done!  We now have a working, redistributable docker image with
sunrise installed on it.  Just commit:

    docker commit commit -m "A winner is you" -a "Your Name" CONTAINER_ID username/sunrise:latest
