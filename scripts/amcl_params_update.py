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
import dynamic_reconfigure.client

if __name__ == "__main__":

    rospy.init_node('amcl_params_update', anonymous=False)

    # Wait for initialization of the system
    rospy.sleep(5.0)

    dynparam_client = dynamic_reconfigure.client.Client('amcl')
    config = dynparam_client.get_configuration()

    params = {
        'odom_alpha1': 0.1,
        'odom_alpha2': 0.1,
        'odom_alpha3': 0.002,
        'odom_alpha4': 0.002,
        'laser_max_beams': 200,
        'update_min_d': 0.1,
        'update_min_a': 0.05

    }

    # Check if the parameters we are changing are available.
    for param_name in params:
        if not param_name in config:
            raise Exception('Parameter "' + param_name + '" is not present in config of amcl.')

    config = dynparam_client.update_configuration(params)
    print 'amcl_params_update DONE'
