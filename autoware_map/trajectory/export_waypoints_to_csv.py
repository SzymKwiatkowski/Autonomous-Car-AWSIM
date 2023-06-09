# pip install rosbags
from rosbags.rosbag2 import Reader
from rosbags.serde import deserialize_cdr
import pandas as pd

# create reader instance and open for reading
with Reader('./lots_waypoints') as reader:
    # topic and msgtype information is available on .connections list
    for connection in reader.connections:
        print(connection.topic, connection.msgtype)

    x_y_waypoints = []
    states = []
    controls = []
    # iterate over messages
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == '/ground_truth/pose':
            msg = deserialize_cdr(rawdata, connection.msgtype)
            # print(msg.pose)
            x_y_waypoints.append([msg.pose.position.x, msg.pose.position.y])
            states.append([msg.pose.position.x, msg.pose.position.y, msg.pose.position.y,
                           msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w])
        if connection.topic == '/control/command/control_cmd':
            msg = deserialize_cdr(rawdata, connection.msgtype)
            controls.append([msg.longitudinal.speed, msg.longitudinal.acceleration, msg.longitudinal.jerk,
                             msg.lateral.steering_tire_angle, msg.lateral.steering_tire_rotation_rate])
            

df_waypoints = pd.DataFrame(x_y_waypoints)
df_waypoints.columns = ['pose.x', 'pose.y']
df_waypoints.to_csv('waypoints.csv', index=False)

# df_states = pd.DataFrame(states)
# df_states.columns = ['pose.x', 'pose.y', 'pose.z', 'orientation.x', 'orientation.y', 'orientation.z', 'orientation.w']
# df_states.to_csv('states.csv', index=False)

# df_controls = pd.DataFrame(controls)
# df_controls.to_csv('controls.csv', index=False)