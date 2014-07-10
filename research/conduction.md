<!-- 
.. title: Thermal Conduction in gasoline
.. slug: conduction
.. date: 2013/05/09 13:13:05
.. tags: research, mathjax
.. link: 
.. description: Adding thermal conductivity to gasoline
-->

Conduction Theory
=====================
The equation for conduction from Tielens is simply:

$$ K(T) = K_0 T^{5/2}$$

If we take the internal energy, in erg/g, or a gas with mean molecular mass 
$\mu$ (in g):

$$ u = \frac{3}{2} \frac{k_B T}{\mu}$$

We can rewrite the conduction equation in terms of internal energy:

$$ T = \frac{2}{3} \frac{u \mu}{k_B}$$

$$\mathcal{K}(u) = K_0 (\frac{2}{3} \frac{u \mu}{k_B})^{5/2}$$

$$\mathcal{K}(u) = \mathcal{K}_0 u^{5/2}$$

where:

$$\mathcal{K_0} = K_0 (\frac{3}{2} \frac{k_B}{\mu})^{-5/2}$$
