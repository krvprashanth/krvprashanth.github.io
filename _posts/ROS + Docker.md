---
layout: post
title: ROS + Docker
date:  2021-11-20 11:27:00 +0900
categories: [Free(dom) Software]
tags: [robotics, linux containers]
---

Intersection between ROS & Docker, development tools and strategies to advance robotic software design and deployment by utilizing advances in Linux containers.

### Why ROS + Docker?

**Repeatable, Reproducible and Deployable**   

Basically, ROS has different versions for different Ubuntu releases. Some packages are built for one version while others are build for some different version. For example, many of the open source implementations of SLAM papers are for ROS Melodic. While some are for Kinetic. This can get really frustrating and we all have the different varients of the software components that we are trying to run and we have all the hardware components and targets we are trying to deploy, execute them on and getting every software component running on every hardware component is really quite challenging.

Onother thing is if i'm collaborating with team mates, the computational environments chage so fast that's kind of hard to keep up maybe in this project where i need to collect a dataset a team mate is already written something that brought on clicks ros bags for me but in the over the time span that maybe 4 weeks the debian packages change so that something that i guess the framework is trying to resolve but it may be more complicated that maybe it might be a ROS environment variable that was set particularly on that one robot and reproducing that is really quite challenging and if i want to share that with other people having someone execute a line of scripts might not be suitable for everyone, especially maybe if they prefer on working at different distros or maybe on custom dependencies.

So, linux containers can kind of help simplify a lot of this stuff since docker provides a containerized environment, we can have any version of ROS on our systems and on different distros using docker.                                                                                                               


### References:
- [https://wiki.ros.org/docker](https://wiki.ros.org/docker)
- [https://wiki.ros.org/docker/Tutorials/GUI](https://wiki.ros.org/docker/Tutorials/GUI)
- [https://tuw-cpsg.github.io/tutorials/docker-ros/](https://tuw-cpsg.github.io/tutorials/docker-ros/)
