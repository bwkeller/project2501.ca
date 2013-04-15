<!-- 
.. title: Timestep Debugging
.. slug: timestep
.. date: 2013/03/28 17:52:57
.. tags: research, mathjax
.. link: 
.. description: Tracking down a numerical instability when particles get too hot
-->

Confirmation of Multistepping Bug
-------------------------------------------------------------------------------
The following images are the same IC and parameters run with and without SPH
single-stepping (single-stepped image on the left, multi-stepped on the right)
The images are from timestep 96, ~9 Myr after the beginning:

### Temperature:
[<img src="../Research/timesteps/step96_temp.png" width=800>](../Research/timesteps/step96_temp.png)

### Density:
[<img src="../Research/timesteps/step96_rho.png" width=800>](../Research/timesteps/step96_rho.png)


The IC used was the one from action item 2b, 2x2x2kpc box with 0.1 H/cc density and $10^4K$ 
temperature, with a $10^4M_\odot$ star cluster at the center.  This run was the $64^3$ particle
version.

Further Investigations (Feb. 2013)
-------------------------------------------------------------------------------
It appears that there are still problems with multistepping. In the perturbed disk slice IC,
I am getting (very) large energy non-conservation.  As the following plots show, I am getting 
a handful of particles that are (much) hotter than the maximum feedback temperature ($1.8 * 10^8 K$).

[<img src="../Research/timesteps/phase_46Myr.png" width=800>](../Research/timesteps/phase_46Myr.png)
[<img src="../Research/timesteps/temperature_evolution.png" width=800>](../Research/timesteps/temperature_evolution.png)

This isn't because of a feedback problem:
[<img src="../Research/timesteps/hotparticle_uDotFB.png" width=800>](../Research/timesteps/hotparticle_uDotFB.png)

Once again, this problem goes away when singlestepping is used:
[<img src="../Research/timesteps/bad_multistepping_temp.png" width=800>](../Research/timesteps/bad_multistepping_temp.png)
[<img src="../Research/timesteps/bad_multistepping_energy.png" width=800>](../Research/timesteps/bad_multistepping_energy.png)

This is ultimately causing a crash when particle 63340 gets a massive uDotPdV applied to it.  The difference in
the phase diagrams of the single and multi-stepping runs is *very* scary:
[<img src="../Research/timesteps/phase_46Myr_badstepping.png" width=800>](../Research/timesteps/phase_46Myr_badstepping.png)
[<img src="../Research/timesteps/phase_46Myr_1step.png" width=800>](../Research/timesteps/phase_46Myr_1step.png)
[<img src="../Research/timesteps/phase_46Myr_multistep.png" width=800>](../Research/timesteps/phase_46Myr_multistep.png)

More Tests (Controlled IC)
-------------------------------------------------------------------------------
I took the perturbed disk slice IC, ran it until the perturbation was used up to form stars, and ran that as an IC
with starformation turned off.  This should let me run essentially the same set of ICs without gravity or cooling.

### Gravity Runs
#### uDots for the hottest particle
[<img src="../Research/timesteps/hotparticle_energy_evolution.png" width=800>](../Research/timesteps/hotparticle_energy_evolution.png)

### No Gravity Runs
#### Energy Conservation
[<img src="../Research/timesteps/adiabatic_energy.png" width=800>](../Research/timesteps/adiabatic_energy.png)
[<img src="../Research/timesteps/cooling_energy.png" width=800>](../Research/timesteps/cooling_energy.png)

As the above figures show, the cooling does cause some *slight* energy conservation errors
compared to the adiabatic gas, but it is nowhere near the magnitude of the previous runs.

It seems that the really extreme case of non-conservation is only happening when both gravity and cooling
is used with multistepping enabled.  This is very troublesome.

#### Energy Conservation
[<img src="../Research/timesteps/4panel_energy.png" width=800>](../Research/timesteps/4panel_energy.png)

#### Maximum Temperature 
[<img src="../Research/timesteps/4panel_maxtemp.png" width=800>](../Research/timesteps/4panel_maxtemp.png)

Cubic IC
-------------------------------------------------------------------------------
Perhaps the weird partial-periodic, many replicas IC dimensions I was using caused some of this trouble.  I made an IC
from the previous runs by cutting out the inner cubic kpc.  It still shows the same problems, but at least now it is much faster.
I plot below the uDot history of the hottest particle in the simulation (crosses are singlestep outputs):
[<img src="../Research/timesteps/hotparticle_udot_breakdown.png" width=800>](../Research/timesteps/hotparticle_udot_breakdown.png)


<a name="substeps">Detailed substeps</a>
-------------------------------------------------------------------------------
I took an output from $\approx 10$ Myr from the previous singlestep run, and ran it with a number of debugging print statements.
This allowed me to get at all of the uDots.  As the following images show, for PdV, Artificial Viscosity, and Diffusion, the 
single and multistep results do not perfectly match.  However, it looks like uDotPdV is the largest both in terms of difference
between the two runs, and just straight magnitude.  Note that the y-scale on the AV plot is logarithmic. I assume for the "right"
answer that the integrals of these curves should match. Also note that the changes in PdV heating occurs just before a 
KickClose (I'm not sure the signifigance of this).

[<img src="../Research/timesteps/hotparticle_substep_uDotPdV.png" width=800>](../Research/timesteps/hotparticle_substep_uDotPdV.png)
[<img src="../Research/timesteps/hotparticle_substep_uDotAV.png" width=800>](../Research/timesteps/hotparticle_substep_uDotAV.png)
[<img src="../Research/timesteps/hotparticle_substep_uDotDiff.png" width=800>](../Research/timesteps/hotparticle_substep_uDotDiff.png)

### One-substep $\Delta uDot$ plots
The following plots show (on an arbitrary x-axis) the difference between the singlestep and multistep uDots for all of the 
particles warmer than $10^6$ K.  Ideally, all points should lie on $y=0$.  These uDots are grabbed from the second substep, when 
the values of u and uPred begin to diverge for the singlestep and multistep versions.  

#### Checking Older Code (Without -DDTADJUST and -DLONGRANGESTEP)
[<img src="../Research/timesteps/uDot_oldcode.png" width=800>](../Research/timesteps/uDot_oldcode.png)
Clearly, we didn't introduce this bug recently.  In fact, it looks like the new timestepping code actually improved the results.

#### Halved Eta values (0.5*dEta, 0.5*dEtaCourant)
[<img src="../Research/timesteps/uDot_smalleta.png" width=800>](../Research/timesteps/uDot_smalleta.png)
Also clearly, this error term is at least $\mathcal{O}(\delta t^2)$, since it looks like most places halving Eta did *better* than
a quartering the error term.

<a name="singlesteps">Poor Singlestep Energy Conservation</a>
-------------------------------------------------------------------------------
[<img src="../Research/timesteps/singlestep_E.png" width=800>](../Research/timesteps/singlestep_E.png)