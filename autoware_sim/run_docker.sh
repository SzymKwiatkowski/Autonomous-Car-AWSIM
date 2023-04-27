#!/bin/bash
xhost +local:root

docker run -it --rm \
	--name=autoware \
	--runtime=nvidia \
	--env="DISPLAY" \
	--env="QT_X11_NO_MITSHM=1" \
	--volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --privileged \
  --volume="/home/user/projekt_ct/autoware_sim" \
  --volume="/home/user/projekt_ct/autoware_map" \
	--device=/dev/usb \
	--device=/dev/video0 \
	--gpus all \
	--env="XAUTHORITY=$XAUTH" \
	--volume="$XAUTH:$XAUTH" \
	--env="NVIDIA_VISIBLE_DEVICES=all" \
	--env="NVIDIA_DRIVER_CAPABILITIES=all" \
        --network=host --privileged \
	ghcr.io/autowarefoundation/autoware-universe:latest-cuda \
	bash
#!/bin/bash--nvidia --x11 --user --volume /home/user/projekt_ct/autoware --volume /home/user/projekt_ct/autoware_map -- ghcr.io/autowarefoundation/autoware-universe:latest-cuda
