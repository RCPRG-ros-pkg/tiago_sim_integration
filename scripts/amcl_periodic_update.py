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

import copy
import rospy
from std_srvs.srv import Empty
from geometry_msgs.msg import PoseWithCovarianceStamped

amcl_pose = None

def callback(data):
    global amcl_pose
    amcl_pose = data

if __name__ == "__main__":
    rospy.init_node('amcl_periodic_update', anonymous=False)

    rospy.sleep(1.0)
    
    print 'amcl_periodic_update: waiting for service /request_nomotion_update'
    rospy.wait_for_service('/request_nomotion_update')

    #try:
    request_nomotion_update = rospy.ServiceProxy('/request_nomotion_update', Empty)
    #except rospy.ServiceException, e:
    #    print "Service call failed: %s"%e
    #    self.clear_costmaps = None

    sleep_time = 5.0
    print 'amcl_periodic_update: starting periodic update every ' + str(sleep_time) + ' seconds'

    initialpose_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)

    rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, callback)

    while not rospy.is_shutdown():

        if amcl_pose is None:
            print 'amcl_pose is None'
        else:
            pose_cov = copy.copy(amcl_pose)
            pose_cov.pose.covariance = (0.001, 0.0001, 0.0, 0.0, 0.0, 0.0, 0.0001, 0.0015, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.003)
            initialpose_pub.publish( pose_cov );

        request_nomotion_update()
        try:
            rospy.sleep(sleep_time)
        except:
            break
