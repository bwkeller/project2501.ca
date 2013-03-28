<!-- 
.. title: Action Items from December 2012
.. slug: action
.. date: 2013/03/28 16:34:55
.. tags: research, mathjax
.. link: 
.. description: Action Items on verifying uNoncool
-->

Item 1: Single Star Case without Cooling
===============================================================================
Single star test, run in a 20x20x20 kpc box. dESN= 1e51

Part 1a: Energy Evolution
-------------------------------------------------------------------------------
[<img src="Research/action/energy_budget_all.png" width=800>](Research/action/energy_budget_all.png)
[<img src="Research/action/energy_budget_internal.png" width=800>](Research/action/energy_budget_internal.png)

Part 1b: Bubble Radius
-------------------------------------------------------------------------------
Edge of bubble is estimated using the maximum of
$$ P \propto \rho(u+uNoncool)$$
[<img src="Research/action/bubble_radius.png" width=800>](Research/action/bubble_radius.png)

Item 2: Star Cluster with Cooling
===============================================================================
I used a box of 2x2x2 kpc, with uniform temperature 1000K and density 1 H/cc. The total
mass in the box was 2e8 Msol. I generated a cluster of stars with a total mass
of 1e4 Msol, and random positions within a sphere of radius 5 pc.  If the resolution
was good enough, I used particles of mass 0.3 times the gas mass.  Otherwise, I simply used
a single particle with mass 1e4 Msol.  I ran the following resolutions:

<table>
	<tr>
		<td>Number of Particles</td>
		<td>Particle Mass $(M_\odot)$</td>
	</tr>
	<tr>
		<td>4.1e3 $(16^3)$</td>
		<td>4.9e4</td>
	</tr>
	<tr>
		<td>3.2e4 $(32^3)$</td>
		<td>6.1e3</td>
	</tr>
	<tr>
		<td>2.6e5 $(64^3)$</td>
		<td>7.6e2</td>
	</tr>
	<tr>
		<td>2.1e6 $(128^3)$</td>
		<td>95</td>
	</tr>
	<tr>
		<td><del>1.6e7 $(256^3)$</del></td>
		<td><del>12</del></td>
	</tr>
	<tr>
		<td><del>1.3e8 $(512^3)$</del></td>
		<td><del>1.5</del></td>
	</tr>
</table>
After starting the runs, I realized the above struck-out runs are too big to finish quickly.  
I may add them later.

I chose the box size based on an estimate of how large it would need to be to allow the blast
pressure to return to ambient.  I ran the box without cooling to get an upper limit as to this
value, and based on that decided I needed to reduce dESN to 1e50 in order to allow me to run
lower resolutions at a small number of particles (ie, that I could use a small box)

NOTE (JAN 13 2013): It appears I was mistaken about needing the lower value of dESN.  In fact,
running with dESN=1e50 is useless, since the SN energy cools away effectively instantaneously
(see figure below).
I will now try running with dESN=1e51.  Hopefully I won't need to use a bigger star cluster.
[<img src="Research/action/dESN_1e50.png" width=800>](Research/action/dESN_1e50.png)


Part 2a: SN-Only FB 
-------------------------------------------------------------------------------
[<img src="Research/action/cooling_bubble_radius.png" width=800>](Research/action/cooling_bubble_radius.png)
[<img src="Research/action/hot_gas.png" width=800>](Research/action/hot_gas.png)

Part 2b: Pseudo-ESFB
-------------------------------------------------------------------------------
For this test, I shifted the time of the IC forward 4Myr, dropped the density to 0.1 H/cc
and knocked the temperature up to 1e4K.  The mass resolution is thus 10x better for the
same N from part a.

[<img src="Research/action/ESF_cooling_bubble_radius.png" width=800>](Research/action/ESF_cooling_bubble_radius.png)
[<img src="Research/action/ESF_hot_gas.png" width=800>](Research/action/ESF_hot_gas.png)
