<!-- 
.. title: Clustered Starformation
.. slug: clustered_starformation
.. date: 2013/03/28 17:51:58
.. tags: research, mathjax
.. link: 
.. description: Using new feedback physics to look at the formation of clusters of stars
-->

Single Star 
===============================================================================

Purpose
-------------------------------------------------------------------------------
In order to drive outflows and fountains, temperatures of $\approx 10^6 K$ are
required.  Can any reasonable feedback regime produce these temperatures in the 
neighbourhood of a single star?

Description of Runs
-------------------------------------------------------------------------------
The IC in this test contains a single 1e5 Msol mass star particle in a 4x4x4
kpc periodic box filled with 1 atom/cc gas at solar metallicity (1.4e9 Msol total mass).
All runs use TOPHATFEEDBACK, LONGRANGESTEP, RTFORCE, the CHABRIER IMF, and metal +
thermal diffusion

Plots
-------------------------------------------------------------------------------

[<img src="../Research/clustered_starformation/onestar_u.png" width=800>](../Research/clustered_starformation/onestar_u.png)
[<img src="../Research/clustered_starformation/onestar_uNoncool.png" width=800>](../Research/clustered_starformation/onestar_uNoncool.png)
[<img src="../Research/clustered_starformation/onestar_maxvel.png" width=800>](../Research/clustered_starformation/onestar_maxvel.png)
[<img src="../Research/clustered_starformation/onestar_maxT.png" width=800>](../Research/clustered_starformation/onestar_maxT.png)

Turbulent Stratified Box
===============================================================================

Purpose
-------------------------------------------------------------------------------
I wanted to try and make tight clusters by dropping the starformation threshold
down to $10^4 H/cc$, close to the value of compact cores within H2 clouds.


## [Param File](../Research/clustered_starformatio/turbulent.param)

Plots and Comments
-------------------------------------------------------------------------------
This run produced a total of 76 stars by 47 Myr, and because of the high-density
gas, ground to a halt.  The actual starformation didn't kick off until $\approx 40 Myr$
because of the high density threshold.

[<img src="../Research/clustered_starformation/turbulent_phase1.png" width=800>](../Research/clustered_starformation/turbulent_phase1.png)
[<img src="../Research/clustered_starformation/turbulent_phase50.png" width=800>](../Research/clustered_starformation/turbulent_phase50.png)

When starformation did kick off, it did so in a very tight region of the simulation,
and generated some reasonable high effective temperatures.  Increasing the ZAMS Time
might let us get even higher.

[<img src="../Research/clustered_starformation/turbulent_cluster.png" width=800>](../Research/clustered_starformation/turbulent_cluster.png)
