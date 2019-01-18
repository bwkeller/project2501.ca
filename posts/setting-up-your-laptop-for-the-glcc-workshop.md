<!-- 
.. title: Setting Up Your Laptop for the GLC16 Workshop
.. slug: setting-up-your-laptop-for-the-glcc-workshop
.. date: 2016-06-13 15:10:31 UTC-04:00
.. tags: linux,guides,simulations
.. category: research
.. link: 
.. description: 
.. type: text
-->

The 2016 Great Lakes Cosmology Conference will begin on Sunday, June 19, with a
graduate student workshop on scientific python, and two popular analysis
toolkits: pynbody and yt.  Pynbody is a simulation analysis tool for working
(primarily) with particle-based datasets, such as the outputs of SPH or N-body
simulations.  yt is a community-developed analysis and visualization toolkit for
volumetric data. yt has been applied mostly to astrophysical simulation data,
but it can be applied to many different types of data including seismology,
radio telescope data, weather simulations, and nuclear engineering simulations.

The workshop will begin with an introduction to python and the Jupyter notebook,
and then have two in-depth presentations on yt and pynbody.  In order to make
things easy for you, it would be helpful if you brought a laptop with some tools
pre-installed, to follow along with the tutorials.  This post is a brief set of
instructions on how I'd recommend you set things up.  If you are a super class-A
hacker, and you can do all of this in your sleep, feel free to skip these
instructions.

<!-- TEASER_END -->
# Anaconda will be your new best friend
Since many of you may be using laptops that run macOS or Windows, which don't
come with package managers like many Linux distributions, the easiest way to
install all of the needed packages for the workshop is with Continuum Analytics'
Anaconda python distribution.  You can download it here:
[https://www.continuum.io/downloads](https://www.continuum.io/downloads).
Once you have downloaded it, follow the instructions to install it.  Even if you
are using Linux, Anaconda may still be the easiest way to go.

## Prerequisites: Numpy, Scipy, Matplotlib and Jupyter
The tools we will be using rely on the scientific python stack, with a few
core packages.  Numpy provides fast matrix and vector math, with Matlab/Fortran-like
operations.  Scipy provides miscellaneous scientific utilities like integrators,
FFTs, and regression tools.  Matplotlib is the de facto standard plotting
library for python.  Finally, Jupyter is the successor to the IPython notebook,
a web-based tool for interactive coding and data analysis.

All of these come along with the base Anaconda install.

## Install [yt](http://yt-project.org)

You can use the Anaconda package manager, conda, to install yt:

```
conda install yt
```

You can also use yt's handy install script, that will install anaconda along
with yt.  You can get that here:

[https://bitbucket.org/yt_analysis/yt/raw/yt/doc/install_script.sh](https://bitbucket.org/yt_analysis/yt/raw/yt/doc/install_script.sh)

## Install [pynbody](http://pynbody.github.io/pynbody)

Pynbody will need to get installed by hand.  The instructions to do so are here:
[http://pynbody.github.io/pynbody/installation.html](http://pynbody.github.io/pynbody/installation.html).

In brief, what you need to do once you have Anaconda is simply:
```
pip install pynbody
```

# Fetch some data

For some of the workshop, we will be working with example simulation outputs.
You should probably download these ahead of time, just in case the internet
is slow/flaky, and in case you would like to play around with the data before
the workshop.  You can download some example data here:

[https://github.com/pynbody/pynbody/releases/download/pynbody-0.2/testdata_april_2013.tar.gz](tipsy format)

## Conclusion
If all of these steps have worked for you, you should be ready for the
workshop.  If you have any trouble with any of the above steps, please feel free
to email me: kellerbw AT mcmaster.ca
