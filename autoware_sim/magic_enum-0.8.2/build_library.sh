#!/bin/bash
cmake -Bbuild/default -DCMAKE_BUILD_TYPE=Release -H.
sudo cmake --build build/default --target install
