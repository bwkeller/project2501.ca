<!-- 
.. title: Reproducing the paper <i>How supernova explosions power galactic winds</i>
.. slug: creasey
.. date: 2013/03/28 17:51:12
.. tags: research, mathjax
.. link: 
.. description:  A few figures and notes relating to <i>How supernova explosions power galactic winds</i> by Creasey et. al.
-->

## Derivation of Outflow
----------------------------
To calculate the mass-flow through a surface, we can take the definition of the SPH density:
$$ \rho  = \sum_{i} m_i W(\mathbf{r_i}, h_i) $$

$$ \frac{\partial \rho}{\partial t} = \sum_{i} m_i \frac{\partial}{\partial t} W(\mathbf{r}_i, h_i) $$

Which yields:

$$ \frac{\partial \rho}{\partial t} = \sum_{i} m_i \frac{\mathbf{v}_i}{h_i} \frac{\partial W(x)}{\partial x} $$

since $x = \Delta r / h$

For the standard M4 Cubic spline kernel (I got this from Thomas and Couchman 1992):

$$ W(x) = \frac{1}{4\pi} \cases{ 4-6x^2+3x^3 & \text{if} x\le 1 \cr (2-x)^3) & \text{if} 1 \lt x \le 2 \cr 0 & \text{elsewhere} } $$

So:

$$ \frac{\partial W(x)}{\partial x}  = \frac{3}{4\pi} \cases{ 4x+3x^2 & \text{if} x\le 1 \cr (2-x)^2) & \text{if} 1 \lt x \le 2 \cr 0 & \text{elsewhere} } $$

To get a surface flux, I took the equation for &part; &rho; / &part; t and 
calculated the mass flux through the surface with normal **n** as the sum for each 
particle, where &Delta; r is calculated as the distance to the surface:

$$ \frac{\partial \Sigma}{\partial t} = \sum_{i} m_i \frac{\mathbf{v}_i \cdot \mathbf{n}}{h_i} \frac{\partial W(x)}{\partial x} $$
 
## Figures
----------------------------
### Massloading and Flux Plots
<img src="../Research/creasey/creasey_figure9.png">
The above figure shows the calculated mass-loading factor &beta; versus gas surface 
density for a number of my feedback recipes.

<img src="../Research/creasey/creasey_massloading_time.png">
This figure is similar to the above figure, but show the massloading as a function of
time to examine the evolution of &beta;

<img src="../Research/creasey/creasey_inflow.png">
The above figure shows simply the mass inflow rate calculated for the various feedback
schemes I have tried.

### Velocity Profiles
#### MAGICC Feedback
<img src="../Research/creasey/creasey_figure1c_MAGICC_10Myr_wide.png">

<img src="../Research/creasey/creasey_figure1c_MAGICC_10Myr.png">
The above 2 plots show the velocity profile derived using MAGICC feedback at 10 Myr,
just after the first ~600 stars have formed.  As the figure shows, the early stellar
feedback hasn't yet stopped the inflow.

<img src="../Research/creasey/creasey_figure1c_MAGICC_30Myr_wide.png">

<img src="../Research/creasey/creasey_figure1c_MAGICC_30Myr.png">
The above 2 plots show the velocity profile derived using MAGICC feedback at 30 Myr,
just after the first bout of SNe activity has occured.  As you can see, inflow has 
become outflow!

#### Gasoline SNe Feedback
<img src="../Research/creasey/creasey_figure1c_feedback_10Myr_wide.png">

<img src="../Research/creasey/creasey_figure1c_feedback_10Myr.png">
This shows the Gasoline SNe feedback velocities at 10Myr.  No feedback of any kind has
happened yet.

<img src="../Research/creasey/creasey_figure1c_feedback_30Myr_wide.png">

<img src="../Research/creasey/creasey_figure1c_feedback_30Myr.png">
This shows the Gasoline SNe feedback velocity profile just after the first bout of SNe,
at 30 Myr.  As you can see, this is not nearly as effective as MAGICC in driving an 
outflow, although it does seem to be starting to blister out into the inflow near the 
center of the slice.

