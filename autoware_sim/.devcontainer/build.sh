DOCKER_BUILDKIT=1 docker build --network=host \
    --build-arg BASE_IMAGE=ghcr.io/autowarefoundation/autoware-universe:humble-latest-cuda \
    -t ghcr.io/autowarefoundation/autoware-universe:humble-latest-cuda-dev .
