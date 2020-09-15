#!/bin/bash

#copy .world files from tiago_sim_integration package to pal_gazebo_worlds
worlds_source_dir=~/tiago_public_ws/src/tiago_sim_integration/worlds
worlds_dest_dir=~/tiago_public_ws/src/pal_gazebo_worlds/worlds

echo -e "\nTaking care of worlds...\n"

cd $worlds_source_dir
for f in *.world
    do 
    if [ ! -f $worlds_dest_dir/"$f" ]
    then
        echo -e "\e[0mCopying file \e[93m$f"
	cp -v "$f" $worlds_dest_dir/"$f"
    else
        echo -e "File \e[92m$f \e[0malready exists in desination directory"
    fi
done

#copy/overwrite rgbd camera configs - to fix bug documented in /vmware_rgbd_mods
config_source_dir=~/tiago_public_ws/src/tiago_sim_integration/vmware_rgbd_mods
config_dest_dir=~/tiago_public_ws/src/tiago_navigation/tiago_laser_sensors/config

echo -e "\nTaking care of configs...\n"
cd $config_source_dir
for f in *.yaml
    do 
    if [ ! -f $config_dest_dir/"$f" ]
    then
        echo -e "\e[0mCopying file \e[93m$f"
	cp -v "$f" $config_dest_dir/"$f"
    else
        echo -e "File \e[92m$f \e[0malready exists in desination directory."
	cp -iv "$f" $config_dest_dir/"$f"
    fi
done
