---
layout: post
title: Setting Up the Embedded Linux development environment
date:  2022-01-28 11:27:00 +0900
categories: [Embedded Linux, System Installation setup tools]
tags: [GNU/Linux, Embedded Linux, System installation setup tools]
---

The procedure for setting up a GNU/Linux host development environment to build the embedded linux application.

- There are two ways to start with embedded Linux
  - Use **tools provided and supported by vendors** like MontaVista, Wind River or TimeSys. These tools comes with their own development and environment. These are mix of open-source components and proprietary tools.
  - Use **community tools**. These are completely open, supported by the community. 
- I prefer using community developed tools which are free softwares where we have access to source code or browse it moreover it respect user data.
   - However, knowing the concepts, switching to proprietary tools will be easy


### OS for Linux development
 I strongly recommend to use GNU/Linux as the desktop operating system to embedded Linux development, for multiple reasons.
- All community tools are developed and designed to run on Linux. Trying to use them on other operating systems (Windows, Mac OS X) will lead to trouble.
- As Linux also runs on the embedded device, all the knowledge gained from using Linux on the desktop will apply similarly to the embedded device.
- If you are stuck with a Windows desktop, at least you should use GNU/Linux in avirtual machine (such as VirtualBox which is open source), though there could be a small performance penalty. With Windows 10, you can also run your favorite native Linux distro through Windows Subsystem for Linux (WSL2)

### Desktop Linux distribution
- To get started you need to download any good and sufficiently recent Linux desktop distribution that can be used for the development workstation
   - Debian, Fedora, openSUSE, Trisquel, etc.
- I prefer Debian, it's a free operating system, used by a wide range of organizations, large and small, as well as thousands of volunteers around the world work together on the Debian operating system, prioritizing Free and Open Source Software. . 
- make sure that you obtain a Linux distribution that is compatible with your hardware. For example, you might select a 32-bit i386 image or a 64-bit amd64 image.

For example, if you want to start with the Debian distribution, you can
download an ISO-formatted image that you would use to install Debian
Linux from [https://www.debian.org/distrib/](https://www.debian.org/distrib/)

### Linux root and non-root users
Linux is a multi-user operating system. The **root user is the administrator**, and it can do privileged operations such as mounting filesystems, configuring the network, creating device files, changing thesystem configuration, installing or removing software. All **other users are unprivileged**, and cannot perform these administrator-level operations and the system has been configured so that the user account created first is allowed to run privileged operations through a program called `sudo`.
- Example: `sudo mount /dev/sda1 /mnt/disk`

### Software packages
The distribution mechanism for software in GNU/Linux is different from the onein Windows. Linux distributions provides a central and coherent way of installing, updating and removing applications and libraries: **packages**
- Packages contains the application or library files, and associatedmeta-information, such as the version and the dependencies
   - `.deb` on Debian,`.rpm` on Red Hat, Fedora, openSUSE

Packages are stored in repositories, usually on HTTP or HTTPS servers. We should only use packages from official repositories for our distribution, unless strictly required.

### Managing software packages
Instructions for Debian based GNU/Linux systems
- Package repositories are specified in `/etc/apt/sources.list` and in files under `/etc/apt/sources.list.d/`
- To update package repository lists:

      sudo apt update
- To find the name of a package to install, the best is to use the search engine on https://packages.debian.org. You mayalso use:

      apt-cache search <keyword>
- To install a given package:
   
      sudo apt install <package>
- To remove a given package:
   
      sudo apt remove <package>
- To install all available package updates:

      sudo apt dist-upgrade
- Get information about a package:

      apt show <package>
- Graphical interfaces
   - Synaptic for GNOME
   - KPackageKit for KDE

Further details on package management: https://www.debian.org/doc/manuals/debian-reference/ch02.en.html 

### Host vs. target
When doing embedded development, there is always a split between the _host_, the development workstation, which is typically a powerful PC. The _target_, which is the embedded system under development. These are connected by various means: almost always a serial line for debuggingpurposes, frequently a networking connection, sometimes a JTAG interface forlow-level debugging.

### Serial line communication program
An essential tool for embedded development is a serial line communicationprogram, like _HyperTerminal_ in Windows. There are multiple options available in Linux: `Minicom`,`Picocom`,`Gtkterm`,`Putty`,`screen` and the new `tio`(https://github.com/tio/tio).
- we recommend using the simplest of them:`Picocom`
   - Installation with `sudo apt install picocom`
   - Run with `picocom -b BAUD_RATE /dev/SERIAL_DEVICE`.
   - Exit with `[Ctrl][a] [Ctrl][x]`
- `SERIAL_DEVICE` is typically
   - `ttyUSBx` for USB to serial converters
   - `ttySx` for real serial ports
- Most frequent command: `picocom -b 115200 /dev/ttyUSB0`

### Command line
Using the command line is mandatory for many operations needed for embeddedLinux development. It is a very powerful way of interacting with the system, with which we can save a lot of time.
- Some useful tips
   - We can use several tabs in the Gnome Terminal
   - Remember that you can use relative paths (for example:`../../linux`) in additionto absolute paths (for example: `/home/user`)
   - In a shell, hit `[Control] [r]`, then a keyword, will search through the commandhistory. Hit `[Control] [r]` again to search backwards in the history
   - We can directly copy/paste paths from the file manager to Gnome Terminal by drag-and-drop.
