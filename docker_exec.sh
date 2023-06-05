if [ -z "$SUDO_USER" ]
then
      user=$USER
else
      user=$SUDO_USER
fi

xhost +local:root
XAUTH=/tmp/.docker.xauth
if [ ! -f $XAUTH ]
then
    xauth_list=$(xauth nlist :0 | sed -e 's/^..../ffff/')
    if [ ! -z "$xauth_list" ]
    then
        echo $xauth_list | xauth -f $XAUTH nmerge -
    else
        touch $XAUTH
    fi
    chmod a+r $XAUTH
fi
docker run -it \
	--name=autoware \
	--shm-size=1g \
	--ulimit memlock=-1 \
	--env="DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --privileged \
	--mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src,target=/home/ws/src,type=bind \
	--mount source=/dev/dri,target=/dev/dri,type=bind,consistency=cached \
	--mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../build,target=/home/ws/build,type=bind \
	--mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../install,target=/home/ws/install,type=bind \
	--mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../log,target=/home/ws/log,type=bind \
	--mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../../autoware_sim,target=/home/autoware,type=bind \
	--mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../../autoware_map,target=/home/autoware_map,type=bind \
	--mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../.vscode,target=/home/ws/.vscode,type=bind \
	--device=/dev/usb \
	--device=/dev/video0 \
	--gpus all \
	--env="XAUTHORITY=$XAUTH" \
	--volume="$XAUTH:$XAUTH" \
	--env="NVIDIA_VISIBLE_DEVICES=all" \
	--env="NVIDIA_DRIVER_CAPABILITIES=all" \
        --network=host \
	autoware_base \
	bash


	# docker run --sig-proxy=false \
	# -a STDOUT \
	# -a STDERR \
	# --mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src,target=/home/ws/src,type=bind \
	# --mount source=/tmp/.X11-unix,target=/tmp/.X11-unix,type=bind,consistency=cached \
	# --mount source=/dev/dri,target=/dev/dri,type=bind,consistency=cached \
	# --mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../build,target=/home/ws/build,type=bind \
	# --mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../install,target=/home/ws/install,type=bind \
	# --mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../log,target=/home/ws/log,type=bind \
	# --mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../../autoware_sim,target=/home/autoware,type=bind \
	# --mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../../autoware_map,target=/home/autoware_map,type=bind \
	# --mount source=/home/user/Autonomous-Car-AWSIM/ros_ws/src/../.vscode,target=/home/ws/.vscode,type=bind \
	# --mount type=volume,src=vscode,dst=/vscode \
	# -l devcontainer.local_folder=/home/user/Autonomous-Car-AWSIM/ros_ws/src \
	# -l devcontainer.config_file=/home/user/Autonomous-Car-AWSIM/ros_ws/src/.devcontainer/devcontainer.json \
	# -e DISPLAY=unix:0 \
	# -e ROS_LOCALHOST_ONLY=1 \
	# -e ROS_DOMAIN_ID=42 \
	# --net=host \
	# -e DISPLAY=:1 \
	# -e XAUTHORITY=/tmp/.docker.xauth \
	# --volume /tmp/.docker.xauth:/tmp/.docker.xauth \
	# --volume=/tmp/.X11-unix:/tmp/.X11-unix:rw --privileged \
	# -e QT_X11_NO_MITSHM=1 --ulimit memlock=-1 --memory=4g --runtime=nvidia --gpus all -e NVIDIA_VISIBLE_DEVICES=all -e NVIDIA_DRIVER_CAPABILITIES=all --privileged --entrypoint /bin/sh vsc-src-860d21e7015951ac09c8d99e51bcb71ae87923523e57036951a85a03433e3b52-uid -c echo Container started
