rocker --network host --privileged --nvidia --group-add video --x11 --user --name autoware \
  	--env="USER" \
	--env="RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" \
	--volume /dev \
	--volume $HOME/autoware:$HOME/autoware \
	-- ghcr.io/autowarefoundation/autoware-universe:humble-latest-arm64-dev
