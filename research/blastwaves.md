<!-- 
.. title: Blastwaves
.. slug: blastwaves
.. date: 2013/04/09 12:16:43
.. tags: research, mathjax
.. link: 
.. description: Various Tests Involving Blastwaves
-->


Theory/Background
=====================

Papers
---------------------
* [Chevalier 1974 *The Evolution of Supernova Remnants I. Spherically Symmetric
  Models*](http://adsabs.harvard.edu/abs/1974ApJ...188..501C)
* [Koo & McKee 1992 *Dynamics of wind bubbles and superbubbles. I - Slow winds
  and fast winds. II - Analytic
  theory*](http://adsabs.harvard.edu/abs/1992ApJ...388...93K)
* [Koo & McKee 1992 *Dynamics of Wind Bubbles and Superbubbles. II. Analytic
  Theory*](http://adsabs.harvard.edu/abs/1992ApJ...388..103K)
* [Mac Low & McCray 1988 *Superbubbles in Disk 
Galaxies*](http://adsabs.harvard.edu/cgi-bin/nph-bib_query?bibcode=1988ApJ...324..776M&db_key=AST)
* [Lagos, Lacey, & Baugh 2013 *A dynamical model of supernova feedback: gas
  outflows from the interstellar
  medium*](http://adsabs.harvard.edu/abs/2013arXiv1303.6635L)
  
  

Cooling Blastwaves
=====================

Initial Conditions
------------------
I generated a series of cubic boxes with edge size 0.5kpc, and a uniform
temperature and density of 1000K and 1 H/cc respectively.  In these boxes, I
injected $10^{53} erg$ of energy (~100 Supernovae) in a number of different ways.

*note: $16^3$ and $8^3$ boxes were run with double-sized boxes, because the
blasts appeared to be interacting with the edges in the 0.5kpc sized boxes*

Physically Convergent Runs
--------------------------
The following runs had the energy injected such that the temperature profile of
the initial conditions is identical.  Starting with the lowest ($16^3$)
resolution.

For the following plots, data was averaged in 1pc radial bins, and the colors of
each curve relate as follows: 

* Blue: $4.7\cdot 10^4$ yr
* Green: $4.7\cdot 10^5$ yr
* Red: $9.4\cdot 10^5$ yr
* Cyan: $1.4\cdot 10^6$ yr
* Magenta: $1.8\cdot 10^6$ yr


###Radial Evolution

####pressure
![pressure](../Research/blastwaves/chevalier_1panel_pressure.png)

####density
![density](../Research/blastwaves/chevalier_1panel_density.png)

####velocity
![velocity](../Research/blastwaves/chevalier_1panel_velocity.png)

####temperature
![temperature](../Research/blastwaves/chevalier_1panel_temperature.png)

####entropy
![entropy](../Research/blastwaves/chevalier_1panel_entropy.png)
