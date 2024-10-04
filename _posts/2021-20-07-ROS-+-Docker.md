---
layout: post
title: ROS + Docker
date:  2021-07-20 11:27:00 +0900
categories: [Free(dom) Software, Robotics, Linux Containers]
tags: [robotics, linux containers]
---

Intersection between ROS & Docker, development tools and strategies to advance robotic software design and deployment by utilizing advances in Linux containers.

### Why ROS + Docker?

**Repeatable, Reproducible and Deployable**   

Basically, ROS has different versions for different Ubuntu releases. Some packages are built for one version while others are build for some different version. For example, many of the open source implementations of SLAM papers are for ROS Melodic. While some are for Kinetic. This can get really frustrating and we all have the different varients of the software components that we are trying to run and we have all the hardware components and targets we are trying to deploy, execute them on and getting every software component running on every hardware component is really quite challenging.

Onother thing is if i'm collaborating with team mates, the computational environments chage so fast that's kind of hard to keep up maybe in this project where i need to collect a dataset a team mate is already written something that brought on clicks ros bags for me but in the over the time span that maybe 4 weeks the debian packages change so that something that i guess the framework is trying to resolve but it may be more complicated that maybe it might be a ROS environment variable that was set particularly on that one robot and reproducing that is really quite challenging and if i want to share that with other people having someone execute a line of scripts might not be suitable for everyone, especially maybe if they prefer on working at different distros or maybe on custom dependencies.

So, linux containers can kind of help simplify a lot of this stuff since docker provides a containerized environment, we can have any version of ROS on our systems and on different distros using docker.                                                                                                               

### Installing Docker 
 Follow the official installation guide: [https://docs.docker.com/engine/install/debian/](https://docs.docker.com/engine/install/debian/)

Or just run shell script: [debian docker install.sh](https://code.swecha.org/krvprashanth/shell-scripts/-/blob/main/docker.sh)

    #Set execute permission to script:
    chmod +x debian_docker_install.sh
    #To run your script, enter:
    ./debian_docker_install.sh
    #OR
    sh debian_docker_install.sh
    #OR
    bash debian_docker_install.sh


### Docker and Ros
- We will be using OSRF (Open Source Robotics Foundation) ROS images
     - [https://hub.docker.com/r/osrf/ros](https://hub.docker.com/r/osrf/ros)
- In ROS images we will be using `osrf/ros:melodic-desktop-full`


#### Setting Up ROS + Docker
    #Create a catkin_ws on host
    mkdir -p ~/catkin_ws/src

    #Pull docker image
    docker pull osrf/ros:melodic-desktop-full

    #Allow local connections to X server
    xhost +local:root

    #Running the docker container for the first time | With GUI Support
    docker run \
    -it \
    -v ~/catkin_ws:/root/catkin_ws \
    --env="DISPLAY=$DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --name rrcros \
    osrf/ros:melodic-desktop-full

    #Once inside the container, we add ros setup filer to bashrc
    echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

    #Exiting the container from inside
    exit  

    ############

    #Once initialized (3), we will use the following commands
    #to interact with the container:

    #Restarting the container | This will start it in background
    docker start rrcros

    #Getting inside a container running in background:
    docker exec -it rrcros bash

    #Stopping the container (from outside)
    docker stop rrcros


### References:
- [RRC Summer Session 2021 -  ROS With Docker](https://sprinkle-yam-c8c.notion.site/ROS-With-Docker-8d4973cc061148fdb7cc6f3c87529f25))
- [https://wiki.ros.org/docker](https://wiki.ros.org/docker)
- [https://wiki.ros.org/docker/Tutorials/GUI](https://wiki.ros.org/docker/Tutorials/GUI)
- [https://tuw-cpsg.github.io/tutorials/docker-ros/](https://tuw-cpsg.github.io/tutorials/docker-ros/)
