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

* $16^3$ Particle Mass: $763 M_\odot$
* $32^3$ Particle Mass: $95.4 M_\odot$
* $64^3$ Particle Mass: $11.9 M_\odot$
* $128^3$ Particle Mass: $1.50 M_\odot$
* $256^3$ Particle Mass: $0.187 M_\odot$

<a name="convergence">Physically Convergent Runs</a>
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


###Radial Evolution (Multiple Resolutions)

####pressure
![pressure](../Research/blastwaves/chevalier_4panel_pressure.png)

####density
![density](../Research/blastwaves/chevalier_4panel_density.png)

####velocity
![velocity](../Research/blastwaves/chevalier_4panel_velocity.png)

####temperature
![temperature](../Research/blastwaves/chevalier_4panel_temperature.png)

####entropy
![entropy](../Research/blastwaves/chevalier_4panel_entropy.png)

###Convergence ($256^3$ vs. $128^3$)
The following plots show the results of a run at $256^3$ resolution (solid line)
vs. at $128^3$ resolution (circles).  As the figures show, there is little
difference in both the position of the shock and the internal bubble properties,
so the $128^3$ resolution should be sufficient.

####temperature
![temperature](../Research/blastwaves/convergence_temperature.png)

####density
![density](../Research/blastwaves/convergence_density.png)

####entropy
![entropy](../Research/blastwaves/convergence_entropy.png)

####total momentum
![totalmomentum](../Research/blastwaves/convergence_totalmomentum.png)

####total momentum (Early)
![totalmomentum](../Research/blastwaves/convergence_totalmomentum_early.png)

####total energy
![totalenergy](../Research/blastwaves/convergence_totalenergy.png)

Evolution of the Cooling Blastwave ($256^3$ particles at previous $128^3$ resolution)
-------------------------------------------------------------------------------------
Based on the previous resolution study, I've chosen the $128^3$ version of the
IC as the fully converged resolution ($1.5 M_\odot$ per particle).  I've made a
larger version of this box, with 1kpc edges, and ran it for longer (100
timesteps, ~4.7Myr).
###Time Evolution

#### Total Energy
![energyevolution](../Research/blastwaves/energy_evolution.png)

#### Total Momentum
![momentumevolution](../Research/blastwaves/momentum_evolution.png)

###Radial Evolution

####[pressure](../Research/blastwaves/chevalier_movie_pressure.mp4)
![pressure](../Research/blastwaves/chevalier_1panel_pressure.png)

####[density](../Research/blastwaves/chevalier_movie_density.mp4)
![density](../Research/blastwaves/chevalier_1panel_density.png)

####[velocity](../Research/blastwaves/chevalier_movie_velocity.mp4)
![velocity](../Research/blastwaves/chevalier_1panel_velocity.png)

####[temperature](../Research/blastwaves/chevalier_movie_temperature.mp4)
![temperature](../Research/blastwaves/chevalier_1panel_temperature.png)

####[entropy](../Research/blastwaves/chevalier_movie_entropy.mp4)
![entropy](../Research/blastwaves/chevalier_1panel_entropy.png)

####[momentum](../Research/blastwaves/chevalier_movie_momentum.mp4)
![momentum](../Research/blastwaves/chevalier_1panel_momentum.png)

####[mass](../Research/blastwaves/chevalier_movie_mass.mp4)
![mass](../Research/blastwaves/chevalier_1panel_mass.png)

<a name="shellinstability">Blastwave "Fingers" (Shell Instability)</a>
-------------------
James is concerned about the "fingers" that we are beginning to see in the images of
the high-resolution runs.  I've made some movies that show what's going on at
the shell/bubble/ISM interface:  _It is a Vishniac Instability!_  We can
finally resolve them!  This obviously complicates the question of analyzing the
results of these simulations, since the instabilities kick in < 1Myr.  The below
videos show the growth of these instabilites in the shell in temperature,
velocity, and density.
####[Shell Instability (Temperature)](../Research/blastwaves/fingers_temp.mp4)
####[Shell Instability (Density)](../Research/blastwaves/fingers_rho.mp4)
####[Shell Instability (Radial Velocity)](../Research/blastwaves/fingers_vel.mp4)

<a name="windmodel">Adiabatic Wind Models with Radiative Shells (a la Mac Low &
McCray)</a>

####[Gasoline's SNe Energy Output]
![SNe](../Research/blastwaves/SNe_luminosity.png)
