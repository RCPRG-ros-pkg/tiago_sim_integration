#!/usr/bin/env python

# Copyright (c) 2019, Robot Control and Pattern Recognition Group,
# Institute of Control and Computation Engineering
# Warsaw University of Technology
#
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the Warsaw University of Technology nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYright HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Author: Dawid Seredynski
#

import rospy
import tf

import sys
import rospy
import math
import copy

import tf
import tf2_ros
from std_msgs.msg import ColorRGBA
from interactive_markers.interactive_marker_server import *
from interactive_markers.menu_handler import *
from visualization_msgs.msg import *
from geometry_msgs.msg import *
import tf_conversions.posemath as pm
from tf.transformations import euler_from_quaternion

class PoseIntMarker:
    def __init__(self, frame_id):
        # create an interactive marker server on the topic namespace simple_marker
        self.br = tf2_ros.TransformBroadcaster()
        self.frame_id = frame_id
        self.tf = Transform()
        self.tf.translation.x = 0.0
        self.tf.translation.y = 0.0
        self.tf.translation.z = 0.0
        self.tf.rotation.x = 0
        self.tf.rotation.y = 0
        self.tf.rotation.z = 0
        self.tf.rotation.w = 1

        self.server = InteractiveMarkerServer('pose_int_marker_' + self.frame_id)
        self.insert6DofGlobalMarker()
        self.server.applyChanges()

    def spinOnce(self):
        t = TransformStamped()
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = "world"
        t.child_frame_id = self.frame_id
        t.transform = self.tf
        self.br.sendTransform(t)

    def insert6DofGlobalMarker(self):
        int_position_marker = InteractiveMarker()
        int_position_marker.header.frame_id = 'world'
        int_position_marker.name = 'pose_int_marker_' + self.frame_id
        int_position_marker.scale = 1.0
        int_position_marker.pose.position.x = self.tf.translation.x
        int_position_marker.pose.position.y = self.tf.translation.y
        int_position_marker.pose.position.z = self.tf.translation.z
        int_position_marker.pose.orientation = self.tf.rotation

        int_position_marker.controls.append(self.createInteractiveMarkerControl6DOF(InteractiveMarkerControl.ROTATE_AXIS,'y'));
        int_position_marker.controls.append(self.createInteractiveMarkerControl6DOF(InteractiveMarkerControl.MOVE_AXIS,'x'));
        int_position_marker.controls.append(self.createInteractiveMarkerControl6DOF(InteractiveMarkerControl.MOVE_AXIS,'z'));

        self.server.insert(int_position_marker, self.processFeedback);
        self.server.applyChanges();

    def processFeedback(self, feedback):
        if ( feedback.marker_name == 'pose_int_marker_' + self.frame_id ):
            self.tf.translation.x = feedback.pose.position.x
            self.tf.translation.y = feedback.pose.position.y
            self.tf.translation.z = feedback.pose.position.z
            self.tf.rotation = feedback.pose.orientation
            rpy = euler_from_quaternion( (self.tf.rotation.x, self.tf.rotation.y, self.tf.rotation.z, self.tf.rotation.w) )
            print 'translation: [' + str(self.tf.translation.x) + ', ' + str(self.tf.translation.y) + ', ' + str(self.tf.translation.z) + ']'
            print 'rotation: ' + str(rpy[2])
            #print "(", self.tf.translation.x, ",", self.tf.translation.y, ",", self.tf.translation.z, "),", "(", self.tf.rotation.x, ",", self.tf.rotation.y, ",", self.tf.rotation.z, ",", self.tf.rotation.w, ")"

    def createInteractiveMarkerControl6DOF(self, mode, axis):
        control = InteractiveMarkerControl()
        control.orientation_mode = InteractiveMarkerControl.FIXED
        if mode == InteractiveMarkerControl.ROTATE_AXIS:
            control.name = 'rotate_';
        if mode == InteractiveMarkerControl.MOVE_AXIS:
            control.name = 'move_';
        if axis == 'x':
            control.orientation = Quaternion(1,0,0,1)
            control.name = control.name+'x';
        if axis == 'y':
            control.orientation = Quaternion(0,1,0,1)
            control.name = control.name+'x';
        if axis == 'z':
            control.orientation = Quaternion(0,0,1,1)
            control.name = control.name+'x';
        control.interaction_mode = mode
        return control

if __name__ == "__main__":

    rospy.init_node('map_adjustment_tool', anonymous=False)

    int_marker = PoseIntMarker('map2')

    br = tf.TransformBroadcaster()

    map2_x = 0.0
    map2_y = 0.0
    map2_theta = 0.0
    while not rospy.is_shutdown():
        br.sendTransform((0, 0, 0),
                     (0,0,0,1),
                     rospy.Time.now(),
                     'map1',
                     'world')

        int_marker.spinOnce()

        rospy.sleep(0.1)
