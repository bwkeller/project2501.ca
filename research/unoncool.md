<!-- 
.. title: Nonthermal Energy in Gasoline
.. slug: unoncool
.. date: 2013/03/28 17:53:02
.. tags: research, mathjax
.. link: 
.. description: Tests on the new noncooling/nonthermal energy support added to gasoline.
-->

Energy Equation
-------------------------------------------------------------------------------
$$\frac{du}{dt} = -(\gamma-1)u\nabla\cdot v - \Lambda + 
\frac{u_{NC}}{\tau_{conv}} - \kappa\nabla^2 u$$
$$\frac{du_{NC}}{dt} = -(\gamma-1)u_{NC}\nabla\cdot v - \frac{u_{NC}}{\tau_{conv}} 
- \kappa\nabla^2 u_{NC} + \dot u_{FB}$$

This defines a new pressure as follows
 
$$P = \rho(\gamma-1)(u+u_{NC})$$

Experiments and Results
===============================================================================

Single Star Box
-------------------------------------------------------------------------------
I generated a box with an isotropic box with uniform temperature and density.  
This box contained 4096 gas particles and a single star particle.  The box was 
set to match roughly our starformation threshold ($T=1000K$, $\rho=10 cm^{-3}$).
The box is a cube with 10 kpc sides.  The gas particles have mass 
$6.09*10^7 M_{\odot}$, and the star particles have the same mass.

The timesteps used in this simulation was 807 kyr.

[<img src="../Research/noncool_comparison.png" width=800>](../Research/noncool_comparison.png)
**The above figure shows the total and thermal energy breakdown of a run with standard 
cooling gasoline with the noncooling version using the values in the output log.**

[<img src="../Research/noncool_budget.png" width=800>](../Research/noncool_budget.png)
**This figure shows the breakdown of the energy within the box in the form of 
microscopic thermal (u), microscopic nonthermal (uNoncool), kinetic, and the sum total.**

[<img src="../Research/0_noncool_maxT.png" width=800>](../Research/noncool_maxT.png)
[<img src="../Research/0_noncool_maxv.png" width=800>](../Research/noncool_maxv.png)
**The above figures show the maxiumum temperature and velocities within the box.**

### Periodic Box  ###

The above box is a pretty poor test since it is a weird cube floating in a vacuum.  
I re-ran the same simulations with periodic boundary conditions(10kpc), so that it is nicely
confined, and can give us a nice Sedov-Taylor solution.

[<img src="../Research/0_periodic_noncool_comparison.png" width=800>](../Research/0_periodic_noncool_comparison.png)
**The above figure shows the total and thermal energy breakdown of a run with standard 
cooling gasoline with the noncooling version using the values in the output log.**

[<img src="../Research/periodic_noncool_budget.png" width=800>](../Research/periodic_noncool_budget.png)
**This figure shows the breakdown of the energy within the box in the form of 
microscopic thermal (u), microscopic nonthermal (uNoncool), kinetic, and the sum total.**

[<img src="../Research/periodic_noncool_maxT.png" width=800>](../Research/periodic_noncool_maxT.png)
[<img src="../Research/periodic_noncool_maxv.png" width=800>](../Research/periodic_noncool_maxv.png)
**The above figures show the maxiumum temperature and velocities within the box.**

### Varying $\tau_{conv}$ ###
For the following runs, I switched to a lower density of $\rho=1 cm^{-3}$
[<img src="../Research/0_noncool_budget_tconv.png" width=800>](../Research/0_noncool_budget_tconv.png)
**This figure shows the breakdown of the energy within the box in the form of 
microscopic thermal (u) and microscopic nonthermal (uNoncool)**
[<img src="../Research/0_noncool_u_budget_tconv.png" width=800>](../Research/0_noncool_u_budget_tconv.png)
**This figure shows just the thermal (u) energy**
[<img src="../Research/0_noncool_maxT_tconv.png" width=800>](../Research/0_noncool_maxT_tconv.png)
[<img src="../Research/0_noncool_maxv_tconv.png" width=800>](../Research/0_noncool_maxv_tconv.png)
**The above figures show the maxiumum temperature and velocities within the box.**

### Varying $\tau_{conv}$ with Cooling ###

[<img src="../Research/0_noncool_u_budget_cooling_tconv.png" width=800>](../Research/0_noncool_u_budget_cooling_tconv.png)
**This figure shows the evolution of the thermal (u) energy in the box**
[<img src="../Research/0_noncool_unoncool_budget_cooling_tconv.png" width=800>](../Research/0_noncool_unoncool_budget_cooling_tconv.png)
**This figure shows the evolution of the nonthermalthermal (u0_noncool) energy in the box**
[<img src="../Research/0_noncool_kinetic_budget_cooling_tconv.png" width=800>](../Research/0_noncool_kinetic_budget_cooling_tconv.png)
**This figure shows the evolution of the kinetic energy in the box**
[<img src="../Research/0_noncool_total_budget_cooling_tconv.png" width=800>](../Research/0_noncool_total_budget_cooling_tconv.png)
**This figure shows the evolution of the total energy in the box**
[<img src="../Research/0_noncool_maxT_cooling_tconv.png" width=800>](../Research/0_noncool_maxT_cooling_tconv.png)
[<img src="../Research/0_noncool_maxv_cooling_tconv.png" width=800>](../Research/0_noncool_maxv_cooling_tconv.png)
**The above figures show the maxiumum temperature and velocities within the box.**
[<img src="../Research/noncool_internal_budget_cooling_tconv.png" width=800>](../Research/noncool_internal_budget_cooling_tconv.png)
**The above figure shows the total pressure-contributing internal energy**

### $10^4 M_\odot$ Star Cluster ###
I repeated the above tests using a smaller star cluster, $10030 M_\odot$, with $1.4\times10^8 M\_odot$ of gas in $33434 M_\odot$ 
particles.  The uniform density is $0.1 cm^{-3}$, and the temperature is 1000 K.  The following figures show properties this
box run with cooling gas.
[<img src="../Research/10e4Mstar_maxv.png" width=800>](../Research/10e4Mstar_maxv.png)
**The above figures show the maxiumum velocity in the box (ie, the edge of the feedback region).**
[<img src="../Research/0_10e4Mstar_internal_energy.png" width=800>](../Research/0_10e4Mstar_internal_energy.png)
**This figure shows the total pressure-contributing internal energy**

### Varying $\tau_{conv}$ with Cooling in the Stratified Box###
The following show a number of time-evolution slices.  Each pixel is the mean value of a 100 pc slice in the z direction.
#### $\tau_{conv} = 1 Myr$ ####
[<img src="../Research/timeslice_temp_tconv1.png" width=800>](../Research/timeslice_temp_tconv1.png)
[<img src="../Research/timeslice_vz_tconv1.png" width=800>](../Research/timeslice_vz_tconv1.png)
#### $\tau_{conv} = 3 Myr$ ####
[<img src="../Research/timeslice_temp_tconv3.png" width=800>](../Research/timeslice_temp_tconv3.png)
[<img src="../Research/timeslice_vz_tconv3.png" width=800>](../Research/timeslice_vz_tconv3.png)
#### $\tau_{conv} = 10 Myr$ ####
[<img src="../Research/timeslice_temp_tconv10.png" width=800>](../Research/timeslice_temp_tconv10.png)
[<img src="../Research/timeslice_vz_tconv10.png" width=800>](../Research/timeslice_vz_tconv10.png)
#### $\tau_{conv} = 30 Myr$ ####
[<img src="../Research/timeslice_temp_tconv30.png" width=800>](../Research/timeslice_temp_tconv30.png)
[<img src="../Research/timeslice_vz_tconv30.png" width=800>](../Research/timeslice_vz_tconv30.png)
#### $\tau_{conv} = 100 Myr$ ####
[<img src="../Research/timeslice_temp_tconv100.png" width=800>](../Research/timeslice_temp_tconv100.png)
[<img src="../Research/timeslice_vz_tconv100.png" width=800>](../Research/timeslice_vz_tconv100.png)
#### Starformation History ####
[<img src="../Research/SFR_tconv.png" width=800>](../Research/SFR_tconv.png)
#### Feedback Smoothing Problem ####
[<img src="../Research/tconv1_hotparticle.png" width=800>](../Research/tconv1_hotparticle.png)
[<img src="../Research/feedback_hotparticle.png" width=800>](../Research/feedback_hotparticle.png)
