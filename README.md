# Marsyard Simulation with Automated Randomised Object Placement

This Repo helps teams and organizers generate diverse `.sdf` world files for testing ERC 2025 Challenge 1 solutions.

## Overview

This work extends the efforts of the Mindcloud team, aiming to simplify testing with slightly varied world environments.

The script modifies an existing `.sdf` file by assigning each specified landmark a new random location. This new location is constrained by an offset, ensuring the landmark remains within a 1-unit radius circle of its original pose.

*   **Teams** can leverage this environment to rigorously evaluate the robustness and adaptability of their models under controlled yet dynamically varied simulation conditions.
*   The adopted approach is modular and inherently scalable, enabling seamless integration of new models into the environment. It is designed for fine-tuning and offers high adaptability to accommodate evolving scene composition requirements.
  ## Installation and Setup
  The worlds and the models folder for the husarion_gz_worlds package can be found at the https://drive.google.com/drive/u/1/folders/13MkeOTBgDPfwtX9C9xKaOF1cH7xR4BWC.
  The world folder contains the script and the original SDF with just the ARUCO poles.
  

When adding new Gazebo models, we recommend the following:

*   **Best Source:** Use **Gazebo Fuel** ([https://app.gazebosim.org/fuel/models](https://app.gazebosim.org/fuel/models)).
    *   Many third-party model sources can be unreliable due to inconsistent folder structures or missing files required for Gazebo simulation.
    *   Models from organizations **OpenRobotics** and **GoogleDeepmind** on Gazebo Fuel are generally well-structured and require minimal modification.
*   **Included Models:** Some models are provided in the models folder of the google drive . You can add more using the method above.

*This script and model integration approach were tested on ROS 2 Humble with Gazebo Fortress.*

## Configuration

To use the script, you'll need to modify its Python source code:

1.  **Define Original Poses:**
    *   Update the `poses`  with the original `[x, y, z, roll, pitch, yaw]` coordinates for each landmark you want to randomize.
2.  **Specify Target Landmarks:**
    *   Update the `landmarks`  with the names of the landmark models (as they appear in your SDF) that the script should modify.
3.  **Set File Paths:**
    *   Modify the path to your **original input `.sdf` file** (e.g., `mars_yard.sdf`).
    *   Specify the **output directory** where new `.sdf` files will be saved.

After configuration, run the Python script.
Make sure that you export the path to your models 
##Improvements 
  We are testing compatibility with ROS2 Jazzy and will update ASAP
  Right now because of the uneven terrain  as there is no heightmap and a confirmed way to determine the z coordinate sometimes the models are not full visible so adding more poses to the list of pose in the script  is more challenging 
