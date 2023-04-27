rocker --network host --privileged --nvidia --x11 --user --name autoware \
  	--env="user" \
	--env="RMW_IMPLEMENTATION=rmw_cyclonedds_cpp" \
	--volume /dev \
	--volume $HOME/autoware:$HOME/autoware \
	-- ghcr.io/autowarefoundation/autoware-universe:latest-cuda
