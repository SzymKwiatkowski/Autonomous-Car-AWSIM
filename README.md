# Simulator usage
Simulator is based on autoware AWSIM.
## Installation
To setup environment use
```bash
./setup-dev-env.sh docker
```

And then you can launch controllable or not controllable vehicle via keyboard going to correct folder and then launching .x86_64.

Controllable:
```bash
cd ./autoware_sim/F1Tenth_v0.4 && ./F1Tenth_v0.4.x86_64
```


Uncontrollable:
```bash
cd ./autoware_sim/F1Tenth_v0.4_keyboard_control && ./F1Tenth_v0.4.x86_64
```
