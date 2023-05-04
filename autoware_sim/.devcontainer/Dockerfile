ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ENV AMENT_CPPCHECK_ALLOW_SLOW_VERSIONS=1


# customize bash
COPY bashrc-git-prompt /tmp/
RUN curl -L https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh >> /etc/skel/.bashrc \
    && cat /tmp/bashrc-git-prompt >> /etc/skel/.bashrc \
    && rm -rf /tmp/bashrc-git-prompt \
    && echo "source /opt/ros/humble/setup.bash" >> /etc/skel/.bashrc


RUN apt-get update && apt-get install -y --no-install-recommends \
    bison \
    clang-tidy \
    iputils-ping \
    flex \
    libncurses5-dev \
    libtins-dev \
    nmap \
    ros-humble-libg2o \
    ros-humble-magic-enum \
    ros-humble-mavros-msgs \
    ros-humble-nmea-msgs \
    ros-humble-rtcm-msgs \
    usbutils \
    vim


# install custom python packages
RUN python3 -m pip --no-cache-dir install \
    autopep8


CMD ["/bin/bash"]
LABEL maintainer="Amadeusz Szymko (amadeusz.szymko@put.poznan.pl)"
