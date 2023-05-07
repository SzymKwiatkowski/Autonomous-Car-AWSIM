# pip install rosbags
from rosbags.rosbag2 import Reader
from rosbags.serde import deserialize_cdr
import json

# create reader instance and open for reading
with Reader('./pose_bag') as reader:
    # topic and msgtype information is available on .connections list
    for connection in reader.connections:
        print(connection.topic, connection.msgtype)

    x_y_trajectory = []
    # iterate over messages
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == '/ground_truth/pose':
            msg = deserialize_cdr(rawdata, connection.msgtype)
            # print(msg.pose)
            x_y_trajectory.append([msg.pose.position.x, msg.pose.position.y])

traj = {
    'trajectory': x_y_trajectory
}
json_string = json.dumps(traj)
with open('waypoints.json', 'w') as outfile:
    outfile.write(json_string)