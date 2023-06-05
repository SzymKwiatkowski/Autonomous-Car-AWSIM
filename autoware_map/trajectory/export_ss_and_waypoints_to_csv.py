# pip install rosbags
from rosbags.rosbag2 import Reader
from rosbags.serde import deserialize_cdr
import pandas as pd

# create reader instance and open for reading
with Reader('./pose_bag') as reader:
    # topic and msgtype information is available on .connections list
    for connection in reader.connections:
        print(connection.topic, connection.msgtype)

    x_y_waypoints = []
    states = []
    # iterate over messages
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == '/ground_truth/pose':
            msg = deserialize_cdr(rawdata, connection.msgtype)
            # print(msg.pose)
            x_y_waypoints.append([msg.pose.position.x, msg.pose.position.y])
            states.append([msg.pose.position.x, msg.pose.position.y, msg.pose.position.y,
                           msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w])

df = pd.DataFrame(x_y_waypoints)
df.to_csv('waypoints.csv', index=False)
