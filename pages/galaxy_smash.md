<!-- 
.. title: WebGL Galaxy
.. slug: galaxy_smash
.. date: 2015-12-09 18:32:37 UTC-05:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->
<style>
    #galaxy {
        width: 95%;
        height: 60vh;
    }
</style>
<div class="row" id="galaxy">
</div>
## Description
This is a simple JS script that uses [three.js](http://threejs.org) to render
star particles in a isothermal sphere potential (this makes a nice flat rotation
curve).  The star particles have their motion followed using a simple
Leapfrog/Velocity Verlet integrator.  You can interact with the galaxy by moving
your cursor accross the field, and a perturbing mass will follow your mouse
around.
<script src="http://www.physics.mcmaster.ca/~kellerbw/smash/three.min.js"></script>
<script src="http://www.physics.mcmaster.ca/~kellerbw/smash/galaxy_smash.js"></script>
