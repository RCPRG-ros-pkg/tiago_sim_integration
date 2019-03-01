#!/bin/bash

#copy .world files from tiago_sim_integration package to pal_gazebo_worlds
source_dir=/home/robot/tiago_public_ws/src/tiago_sim_integration/worlds
dest_dir=/home/robot/tiago_public_ws/src/pal_gazebo_worlds/worlds

cd $source_dir
for f in *.world
    do 
    if [ ! -f $dest_dir/"$f" ]
    then
        echo "Copying file $f"
	cp -v "$f" $dest_dir/"$f"
    else
        echo "File $f already exists in desination directory"
    fi
done
