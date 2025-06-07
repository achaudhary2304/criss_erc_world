# SDF Landmark Randomizer

This Python script facilitates the addition of landmarks to specified poses within an SDF (Simulation Description Format) file. It takes an existing SDF file, a list of predefined landmarks, and a list of possible poses, then generates a new SDF file with these landmarks placed at randomly selected poses, with slight random offsets.

## Overview

The primary purpose of this script is to automate the process of populating a simulated environment (defined by an SDF file) with various objects (landmarks) at different locations. This is particularly useful for generating variations of a world for robotics simulations, testing navigation algorithms, or creating diverse training environments.

## How it Works

The script operates based on three main components:

1.  **Poses List (`poses`):**
    *   This is a Python list of strings, where each string defines a base pose in the format `"x y z roll pitch yaw"`.
    *   Coordinates `x` and `y` should be compatible with the dimensions of your SDF world map.
    *   Example: `poses = ["0 0 0 0 0 0", "3 12 0 0 0 0"]`

2.  **Landmarks List (`landmarks`):**
    *   This is a Python list of strings, where each string is the exact model name of a landmark (e.g., as defined in your Gazebo models directory or a URI like `model://model_name`).
    *   Example: `landmarks = ["helmet", "antenna", "Squirrel"]`

3.  **Script Logic:**
    *   `generate_random_landmark_section(landmarks, poses)`:
        *   Randomly selects a unique pose from the `poses` list for each landmark in the `landmarks` list.
        *   For each selected pose, it applies a small random offset to the `x` and `y` coordinates. The offset is designed to place the landmark within a circle of radius 1 unit around the original (x, y) point.
        *   It then constructs an SDF `<include>` block for each landmark with its new, slightly randomized pose.
    *   `insert_landmarks_into_sdf(sdf_content, landmark_section)`:
        *   This function takes the original SDF file content and the generated landmark SDF blocks.
        *   It finds the closing `</world>` tag in the SDF content and inserts the landmark blocks just before it.
    *   `randomize_landmarks_in_sdf_file(input_filename, output_filename)`:
        *   This is the main function that orchestrates the process.
        *   It reads the content of the `input_filename` (your original SDF file).
        *   Calls `generate_random_landmark_section` to create the SDF snippets for the landmarks.
        *   Calls `insert_landmarks_into_sdf` to integrate these snippets into the original SDF content.
        *   Writes the modified SDF content to `output_filename`.

## Prerequisites

*   Python 3.x

## Usage

1.  **Configure Poses and Landmarks:**
    *   Open the `gen.py` script.
    *   Modify the `poses` list to include the desired base coordinates where landmarks can be placed. Ensure these coordinates are valid for your target SDF world.
    *   Modify the `landmarks` list to include the exact names of the Gazebo models you wish to use.

2.  **Set File Paths:**
    *   In the `if __name__ == "__main__":` block at the end of the script, update the file paths for `input_filename` and `output_filename`.
        ```python
        if __name__ == "__main__":
            # It's recommended to use absolute paths
            randomize_landmarks_in_sdf_file("path/to/your/original.sdf", "path/to/your/generated_world.sdf")
        ```

3.  **Run the Script:**
    *   Execute the script from your terminal:
        ```bash
        python gen.py
        ```
    *   This will generate a new SDF file (e.g., `generated_world.sdf`) with the landmarks included at randomized positions.

## Customization

*   **Adding More Poses:** Simply add more pose strings to the `poses` list.
*   **Adding More Landmarks:** Add more model names to the `landmarks` list. If the number of landmarks exceeds the number of unique poses, the script will raise an error because `random.sample` requires the population to be at least as large as the sample size. Ensure you have at least as many poses as landmarks.
*   **Adjusting Randomization:**
    *   The current randomization adds an offset within a 1-unit radius circle around the base (x, y) coordinate.
    *   You can modify the `rand_x_offset` and `rand_y_offset` generation logic within the `generate_random_landmark_section` function to change this behavior (e.g., change the range of `random.uniform` or the formula for `new_y`).

This script provides a straightforward way to introduce variability into your SDF worlds by programmatically placing landmarks.
