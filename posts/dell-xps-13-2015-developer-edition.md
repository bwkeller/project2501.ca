<!-- 
.. title: Dell XPS 13 2015 Developer Edition
.. slug: dell-xps-13-2015-developer-edition
.. date: 2015-05-28 13:24:57 UTC-04:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

What a pain in the butt this machine has been.  For a machine that comes with
Linux pre-installed, this thing sure doesn't play nicely with it.  Out of the
box, it comes with Ubuntu 14.04 installed, and mine came with the A03 BIOS.
When I first booted, the installation tool crashed halfway through, leaving me
with a semi-working system.  I had to re-flash the machine back to the factory
settings, and then try again (luckily it didn't crash the second round through).  

Even after getting Ubuntu set up, there is a horrendous bug in the touchpad
driver that makes the cursor jerk wildly around every few minutes.  I tried to
solve this issue by upgrading the OS to 14.10, but that had the unfortunate
effect of nuking the networking and leaving the machine in an unbootable state!
YAY!  Its' been a while since I did any distro hopping, so I'm going to use this
as a chance to distro hop a bit.

# Distributions
- [Elementary OS Freya](#elementary)
- [Debian Jessie w/ KDE](#debian-kde)
- [Debian Jessie w/ GNOME](#debian-gnome)
- [Debian Jessie w/ XFCE](#debian-xfce)

<div id='elementary'/>
<h2>Elementary OS Freya</h2>
Straight out of the gate, garbled text on the installer!  Guess I won't be
trying this...  Apparently this is a problem for Broadwell machines.

<div id='debian-kde'></div>
<h2>Debian Jessie (KDE edition)</h2>
Installer works.  Needs manual installation of wireless driver.

<div id='debian-gnome'/>
<h2>Debian Jessie (GNOME edition)</h2>
Installer mysteriously crashes.

<div id='debian-xfce'/>
<h2>Debian Jessie (XFCE edition)</h2>
Installer works.  Needs manual installation of wireless driver.
