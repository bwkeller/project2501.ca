<!-- 
.. title: Perturbed Disk Slice
.. slug: perturbed_disk
.. date: 2013/03/28 17:52:43
.. tags: research, mathjax
.. link: 
.. description:  A version of Chris' disk with a cluster-forming perturbation.
-->

A Stratified Box with a Spherical, Overdense Region
===============================================================================
## IC Description
I've started with the original stratified disk from Chris, and made a few modifications.
* No more turbulence
* Central density of 1 H/cc, giving a total surface density of $\approx 12 M_\odot / pc^2$
* Particles have a mass of $182 M_\odot$
This gives an IC with the following temperature/density profile:

[<img src="../Research/perturbed_disk/disk_profile.png" width=812>](../Research/perturbed_disk/disk_profile.png)

I then sliced out a little spherical hole in the middle of the box with a radius of 21.3 pc.  Into this 
hole, I placed a spherical ball of mass $98280 M_\odot$, and a temperature of 100K.  This should keep it roughly in
pressure equilibrium with the surrounding disk, since it has a density of 100 H/cc at 100K, versus the surrounding 1 H/cc at 
$10^4$ K  Since the free-fall time for this little ball is ~5 Myr, it should collapse and form stars before the surrounding 
medium knows what happened to it.

First run, with "Standard" Gasoline Feedback
===============================================================================
### [Param File](../Research/perturbed_disk/feedback.param)
The first run did form a nice little cluster, as shown in the density image here from timestep 10 (9.4 Myr):

[<img src="../Research/perturbed_disk/cluster.png" width=800>](../Research/perturbed_disk/cluster.png)

(Stars are the white dots)
However, I've made a big mistake in making the glass (I forgot an important shuffling step, and the glass
"chunks" each have a biased density based on the order they were added).  This has been corrected, and I am 
re-running now.  The figure below shows column density looking down the z-axis (the think dimension of the box)
in the broken IC:

[<img src="../Research/perturbed_disk/oops.png" width=800>](../Research/perturbed_disk/oops.png)

#Timestep 25, $t\approx 24 Myr$

The following images show the inner $1 kpc^3$ region after the cluster 

[<img src="../Research/perturbed_disk/columndenisty_25.png" width=800>](../Research/perturbed_disk/columndenisty_25.png)

Column Density

[<img src="../Research/perturbed_disk/volumedenisty_25.png" width=800>](../Research/perturbed_disk/volumedenisty_25.png)

Volume Density

[<img src="../Research/perturbed_disk/temp_25.png" width=800>](../Research/perturbed_disk/temp_25.png)

Temperature

[<img src="../Research/perturbed_disk/outflowvelocity_25.png" width=800>](../Research/perturbed_disk/outflowvelocity_25.png)

Outflow velocity.  We have a wind!

### Comments on above plots
This IC is ideally suited for creating insanely heavy gas particles as a result of feedback!  As you can in some of the 
above plots, the center seems to be dominated by a sphere that is too uniform.  That is because it is!  That sphere is a
single massive particle, smoothed.  The plot below shows the same region, with a slice into the plane 100 pc thick.  As 
it shows, there remains a single gas particle in the center of the cluster that has had it's mass knocked up from the original
182 $M_\odot$ to 2908 $M_\odot$!  This is surely a bad thing.

[<img src="../Research/perturbed_disk/particles_25.png" width=800>](../Research/perturbed_disk/particles_25.png)

dMaxGasMass
===============================================================================
Gas particles getting 20x heavier is bad.  Greg added a dMaxGasMass parameter that may correct this.  I re-ran the above
with dMaxGasMass set to $273 M_\odot$.

[<img src="../Research/perturbed_disk/columndensity_maxgasmass_25.png" width=800>](../Research/perturbed_disk/columndensity_maxgasmass_25.png)

Column Density

[<img src="../Research/perturbed_disk/volumedensity_maxgasmass_25.png" width=800>](../Research/perturbed_disk/volumedensity_maxgasmass_25.png)

Volume Density

[<img src="../Research/perturbed_disk/temp_maxgasmass_25.png" width=800>](../Research/perturbed_disk/temp_maxgasmass_25.png)

Temperature

[<img src="../Research/perturbed_disk/outflowvelocity_maxgasmass_25.png" width=800>](../Research/perturbed_disk/outflowvelocity_maxgasmass_25.png)

Outflow velocity.

## A Cavity is Still Carved!
[<img src="../Research/perturbed_disk/particles_maxgasmass_25.png" width=800>](../Research/perturbed_disk/particles_maxgasmass_25.png)
dMaxGasMass *might* be coaxed into working, but I think the problem is deeper than heavy particles: it is that the timescale for
starformation is greater than the timescale for feedback to do any real hydro work.  All the starforming gas is consumed, leaving
a super hot (or heavy!) central particle or two that keep the rest of the ISM from flooding in to get feedbacked upon.


UNONCOOL
===============================================================================
## dNoncoolConvtime = 10 Myr

[Temperature Movie](../Research/perturbed_disk/tconv10Myr_temp.mp4)

[Velocity Movie](../Research/perturbed_disk/tconv10Myr_velocity.mp4)

## dNoncoolConvtime = -1 (Automatic Calculation)

[Temperature Movie](../Research/perturbed_disk/tconvAUTO_temp.mp4)

[Velocity Movie](../Research/perturbed_disk/tconvAUTO_velocity.mp4)

### Why does the automatic conversion give such poor results?
I don't think this is a particularly good test for using the 
automatic calculation.  Since the conversion time is:
$$ \tau_{conv} = \frac{h}{2\sqrt{u_{NC}}}$$
If h becomes very small (in high density regions like the 
perturbation I have inserted), the conversion time can also 
become very small, and I think I'm just bleeding off the 
feedback energy through cooling.  I've made a video below
showing the temperature and conversion times:

[$\tau_{conv}$](../Research/perturbed_disk/noncoolconvtime.mp4)

UNONCOOL, perturbation slightly above the plane (z = 500 pc)
===============================================================================
## dNoncoolConvtime = 10 Myr

[Temperature Movie](../Research/perturbed_disk/tconv10Myr_0.5kpc_temp.mp4)

[Velocity Movie](../Research/perturbed_disk/tconv10Myr_0.5kpc_velocity.mp4)