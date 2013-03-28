<!-- 
.. title: SPH Particle Mass Variation with the Shocks
.. slug: sedov_sphmass
.. date: 2013/03/28 17:52:50
.. tags: research, mathjax
.. link: 
.. description: Testing the limits of SPH with different particle masses using the Sedov Blast and its Analytic Solution.
-->


Sedov Blast Experiments 
===============================================================================
## First (Good) Run
Initial run with $\alpha = 2.0$ , with the following Makefile DEFINES:
<pre><code>-DCHANGESOFT -DGASOLINE -DRTFORCE -DDIFFUSION -DDIFFUSIONTHERMAL -DDODVDS -DVSIGVISC   -DCOOLING_METAL</code></pre>

### [Parameter File](../Research/sedov_128.param)

### Radial Growth
[<img src="../Research/sedov_sphmass.png" width=800>](../Research/sedov_sphmass.png)
### Radial Velocity
[<img src="../Research/sedov_sphmass_vel.png" width=800>](../Research/sedov_sphmass_vel.png)
### Final Temperature
[<img src="../Research/sedov_sphmass_temp.png" width=800>](../Research/sedov_sphmass_temp.png)
### Final Entropy
[<img src="../Research/sedov_sphmass_A.png" width=800>](../Research/sedov_sphmass_A.png)
## Balsara switch off
### [Parameter File](../Research/0_sedov_128.param)
### Radial Growth
[<img src="../Research/sedov_sphmass_noB.png" width=800>](../Research/sedov_sphmass_noB.png)
### Radial Velocity
[<img src="../Research/sedov_sphmass_noB_vel.png" width=800>](../Research/sedov_sphmass_noB_vel.png)
### Final Temperature
[<img src="../Research/sedov_sphmass_noB_temp.png" width=800>](../Research/sedov_sphmass_noB_temp.png)
### Final Entropy
[<img src="../Research/sedov_sphmass_noB_A.png" width=800>](../Research/sedov_sphmass_noB_A.png)
## Balsara switch off, Long-range Step
### [Parameter File](../Research/1_sedov_128.param)
### Radial Growth
[<img src="../Research/sedov_sphmass_longstep.png" width=800>](../Research/sedov_sphmass_longstep.png)
### Radial Velocity
[<img src="../Research/sedov_sphmass_longstep_vel.png" width=800>](../Research/sedov_sphmass_longstep_vel.png)
### Final Temperature
[<img src="../Research/sedov_sphmass_longstep_temp.png" width=800>](../Research/sedov_sphmass_longstep_temp.png)
### Final Entropy
[<img src="../Research/sedov_sphmass_longstep_A.png" width=800>](../Research/sedov_sphmass_longstep_A.png)
## 32 Neighbour Smooth
The purpose of these runs, identical to the above save for the "original" Sedov run smoothing over half as 
many neighbours (32 vs. 64) is to see if the behaviour of varying particle masses can be roughly approximated
as a reduced smoothing length.
### [Parameter File](../Research/2_sedov_128.param)

### Radial Growth
[<img src="../Research/sedov32_sphmass.png" width=800>](../Research/sedov32_sphmass.png)
### Radial Velocity
[<img src="../Research/sedov32_sphmass_vel.png" width=800>](../Research/sedov32_sphmass_vel.png)
### Final Temperature
[<img src="../Research/sedov32_sphmass_temp.png" width=800>](../Research/sedov32_sphmass_temp.png)
### Final Entropy
[<img src="../Research/sedov32_sphmass_A.png" width=800>](../Research/sedov32_sphmass_A.png)
## Corrected Energy
The Energy in the above runs are not all equal.  Here are the same results with equal energy injection
(and thus the same self-similarity solution)
### Radial Growth
[<img src="../Research/sedov_sphmass_correctE_longstep.png" width=800>](../Research/sedov_sphmass_correctE_longstep.png)
### Radial Velocity
[<img src="../Research/sedov_sphmass_correctE_longstep_vel.png" width=800>](../Research/sedov_sphmass_correctE_longstep_vel.png)
### Final Temperature
[<img src="../Research/sedov_sphmass_correctE_longstep_temp.png" width=800>](../Research/sedov_sphmass_correctE_longstep_temp.png)
### Final Entropy
[<img src="../Research/sedov_sphmass_correctE_longstep_A.png" width=800>](../Research/sedov_sphmass_correctE_longstep_A.png)
## Corrected Energy, 32 Neighbours
### Radial Growth
[<img src="../Research/sedov32_sphmass_correctE.png" width=800>](../Research/sedov32_sphmass_correctE.png)
### Radial Velocity
[<img src="../Research/sedov32_sphmass_correctE_vel.png" width=800>](../Research/sedov32_sphmass_correctE_vel.png)
### Final Temperature
[<img src="../Research/sedov32_sphmass_correctE_temp.png" width=800>](../Research/sedov32_sphmass_correctE_temp.png)
### Final Entropy
[<img src="../Research/sedov32_sphmass_correctE_A.png" width=800>](../Research/sedov32_sphmass_correctE_A.png)
Colliding Flows Experiments 
===============================================================================
