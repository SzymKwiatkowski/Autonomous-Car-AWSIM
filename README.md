# Simulator usage
Simulator is based on autoware AWSIM.
## Installation
To setup environment use
```bash
./setup-dev-env.sh docker
```

And then reboot, afterwards you can launch controllable or not controllable vehicle via keyboard going to correct folder and then launching .x86_64.

# Launch simulation
Controllable:
```bash
cd ./autoware_sim/F1Tenth_v0.4 && ./F1Tenth_v0.4.x86_64
```


Uncontrollable:
```bash
cd ./autoware_sim/F1Tenth_v0.4_keyboard_control && ./F1Tenth_v0.4.x86_64
```


# Launch docker
Then to use docker:
```bash
docker pull ghcr.io/autowarefoundation/autoware-universe:latest-cuda
```

and then launch it with run and enter scripts in root to use.

# Notes

If simulator has problems try to run 
```bash
./setup-dev-env.sh
```

If then not everything is working check dependencies manually [on website](https://autowarefoundation.github.io/autoware-documentation/main/installation/autoware/source-installation/)

# Running simulator with ROS
First and foremost run import commands to import necessery libraries
```bash
vcs import /home/ws/ < /home/autoware/f1tenth.repos \
vcs import /home/ws/src < /home/autoware/autoware.repos
```
Then run installation using rosdep
```bash
rosdep install --from-paths src --ignore-src -y
```


Some missing dependencies can be fixed via:
```bash
rosdep update && sudo apt update && sudo apt install -y ros-humble-nav2-bringup
```

As well as installing magic_enum library via installation script:
```bash
cd /home/autoware/magic_enum-0.8.2  && bash build_library.sh
```

To run:
```bash
bash /home/ws/f1_launch.sh
```