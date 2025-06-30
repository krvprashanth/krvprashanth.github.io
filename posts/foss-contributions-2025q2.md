<!--
.. title: FOSS Contributions 2025Q2
.. slug: foss-contributions-2025q2
.. date: 2025-07-01 23:00:00 UTC-03:00
.. tags: foss-contributions, debian, duckietown
.. author: krvprashanth
.. link: 
.. description:
.. category: nikola
-->

---
Hello everyone! I’m starting a series of quarterly posts about the contributions I’ve made or things I found interesting in collaborative Free and Open Source Software development. I will try to post one every quarter - let’s see how this goes.

# Debian
### Debian Installer / flash-kernel
Debian Raspberry Pi Maintainers wanted to explore whether they should still be building one image per family, or they could instead switch to one image per architecture (armel, armhf, arm64) and also the available set of images for running Debian on Raspberry Pi computers using/require some necessary platform-specific changes primarily in the early boot sequence and firmware handling. Unlike typical Debian systems, Raspberry Pi devices depend on proprietary bootloader and uses non-free firmware (raspi-firmware) closed-source GPU bootloader which is tightly coupled to Raspberry Pi hardware-specific differences in the initialization process. These differences are largely confined to the early boot and hardware initialization stages. Once the system boots, the userspace remains closely aligned with a typical Debian install, using Debian packages.

I was trying to build architecture-specific Raspberry Pi Debian images by integrating flash-kernel, and replacing the proprietary Raspberry Pi bootloader with an open-source boot loader U-Boot. This still depends on the Raspberry Pi non-free firmware to start, but it loads U-Boot, not Linux kernel directly and the image building process will be closer to how official Debian images boots ARM devices and flash-kernel knows how to install u-boot, device-tree blobs and Linux kernel images and initrds for various ARM boards. It's a glue between Debian and the firmware, Integrates with the kernel package with hook and U-Boot needs a script (_boot.scr_) to boot. This will be installed to _/boot_ by flash-kernel during the install process (the default script _/etc/flash-kernel/bootscript/bootscr.uboot-generic_ is used).

So, added not yet supported Raspberry Pi models and a BeagleBone Blue in flash-kernel packages even though upstream support and DTBs exist in the Debian kernel but are missing entries in the flash-kernel.

Hardware support changes: Filed bug reports to see support for Raspberry Pi Zero 2 W [(#1107524)](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1107524), 4 Model B [(#1106381)](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1106381), Compute Module 4 [(#1108236)](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1108236) and TI AM335x BeagleBone Blue [(#1108366)](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1108366) in flash-kernel package.

| Merge Requests | 
| ---   |
| [!71: Add: Support for Raspberry Pi 4 Model B](https://salsa.debian.org/installer-team/flash-kernel/-/merge_requests/71) |
| [!73: Add: Support for Raspberry Pi Zero 2 W](https://salsa.debian.org/installer-team/flash-kernel/-/merge_requests/73)  |
| [!74: Add: machine db entry for Raspberry Pi Compute Module 4](https://salsa.debian.org/installer-team/flash-kernel/-/merge_requests/74) |
| [!75: Add: Support for TI AM335x BeagleBone Blue](https://salsa.debian.org/installer-team/flash-kernel/-/merge_requests/75) |

### Debian Raspberry Pi

- Tested U-Boot package: u-boot-rpi (2023.01+dfsg-2+deb12u1) current version stable/bookworm on Raspberry Pi Zero 2 W, 4 Model B & Compute Module 4.
    - Listed the boards I tested on [https://wiki.debian.org/U-boot/Status](https://wiki.debian.org/U-boot/Status)
- Wrote an Ansible playbook to migrate the existing Debian Raspberry Pi build infrastructure from UNAM (Universidad Nacional Autónoma de México) to one of server managed by the Debian Installer team to daily auto-built Raspberry Pi Debian images and up running. 
    - [https://salsa.debian.org/krvprashanth/raspi-debian-build-farm](https://salsa.debian.org/krvprashanth/raspi-debian-build-farm)
- [https://salsa.debian.org/krvprashanth/raspi-arch-image-specs](https://salsa.debian.org/krvprashanth/raspi-arch-image-specs)



| Merge Requests |
| ---   |
| [!21: Boot Media (Software Image): Flashing Instructions using Raspberry Pi Imager](https://salsa.debian.org/raspi-team/web-raspi-img/-/merge_requests/21) |
| [!22: Fix: build errors and Ruby 3.3+ compatibility issues](https://salsa.debian.org/raspi-team/web-raspi-img/-/merge_requests/22) |


### Debian External repositories
I came across Extrepo, a super handy Debian utility for managing external repositories securely. Before this, adding external repos usually meant editing APT configs manually or running unsigned scripts - not ideal. With Extrepo, one can just search, enable, or update repos and install packages. Surprised it's not talked about more and it definitely deserves more attention!

And, I added extrepo entries for BeagleBoard.org, SatNOGS, Armbian, TuxMake, TuxSuite, TuxRun, TuxLAVA, and Texas Instruments. Enabled repository support for Raspberry Pi and Mobian targeting the upcoming Debian release, trixie and fixed outdated GPG keys for Slack, ProtonVPN, and Mobian, and also updated the issue tracker URL for Mobian.

Filed bug report to extrepo package version:0.14 to add entry for repositories (BeagleBoard.org, Texas Instruments, TuxSuite, Armbian & SatNOGS)([#1106660](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1106660)) and fixed ([#1106363](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1106363)).

| Merge Requests | 
| ---   |
| [!355: Slack: update GPG key](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/355) | 
| [!356: Add SatNOGS repositories](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/356)  | 
| [!359: Add Armbian repository](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/359)  | 
| [!361: RaspberryPi: enable repository for trixie](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/361)  | 
| [!362: Add: TuxMake and TuxSuite repository](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/362)  | 
| [!366: Add: Texas Instruments repository](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/366) | 
| [!367: Add: TuxRun and TuxLAVA repository ](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/367) |
| [!369: Add: BeagleBoard.org repository](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/369) |
| [!370: ProtonVPN: update GPG key](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/370) |
| [!377: Mobian: update GPG key and enable repository for trixie](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/377) 
| [!381: Mobian: update issue tracker URL](https://salsa.debian.org/extrepo-team/extrepo-data/-/merge_requests/381) |

#  TexasInstruments / ti-debpkgs 
- Opened issue [#4](https://github.com/TexasInstruments/ti-debpkgs/issues/4)

# Duckietown
The different NVDIA SBCs that Duckiebot uses have different compatibility strings. Fixed the [Front bumper](https://get.duckietown.com/products/bumper-set-front-back?variant=41241555140783) of Duckiebot to work on all NVDIA Jetson Nano Dev boards.

| Pull Request |
| ---   |
| [#489 Fix: address-cells placement and reorder mux@70 properties](https://github.com/duckietown/duckietown-shell-commands/pull/489)   |

# Awesome Volunteer Computing
| Pull Request |
| ---   |
| [#2 Add: multicortex-exo in platforms & Infrastructure](https://github.com/ranjithrajv/awesome-volunteer-computing/pull/2)   |



# /var/log/misc 😉
I have Raspberry Pi Zero 2 W, 4, CM4 and 5 devices. I'm grateful to Gunnar Wolf ([@gwolf](https://people.debian.org/~gwolf/)) for mentoring me to adopt and update the Raspberry Pi images creation and the Debian Project Leader has approved funding for me to purchase the rest Raspberry Pi hardware (Zero W/1/2/3) to test daily auto-built Raspberry Pi Debian images.

And, I attended Bangalore Linux Kernel Meetup (April 26, 2025, hosted at *Linux Technology Center, IBM*) and the Zephyr Project Meetup (May 17, 2025, hosted at *Texas Instruments*), both held in Bengaluru, India.
Thanks to [Duckietown Robotics](https://duckietown.com/) for sponsoring my travel to attend the Kernel Meetup.

P.S. [Duckiebot](https://docs.duckietown.com/daffy/opmanual-duckiebot/intro.html) and [Duckiedrone](https://docs.duckietown.com/daffy/opmanual-dd24/intro.html) hardware runs on **Debian GNU/Linux**


# Ending Thoughts
That’s all for Q2 2025. From now onwards, I hope to post quarterly updates and I guess this will keep people informed about my contributions and possibly attract potential contributors.

Consider [supporting me](https://krvprashanth.in/pages/about/) if you like my work.

# Helpful links
- [http://raspi.debian.net](http://raspi.debian.net)
- [https://manpages.debian.org/unstable/flash-kernel/flash-kernel.8.en.html](https://manpages.debian.org/unstable/flash-kernel/flash-kernel.8.en.html)
- [https://manpages.debian.org/unstable/extrepo/extrepo.1p.en.html](https://manpages.debian.org/unstable/extrepo/extrepo.1p.en.html)
- [https://www.nvidia.com/en-in/autonomous-machines/embedded-systems/jetson-nano/duckietown/](https://www.nvidia.com/en-in/autonomous-machines/embedded-systems/jetson-nano/duckietown/)


