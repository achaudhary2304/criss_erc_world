import random
import math
#add the poses to this list 
#pose is of the form "x y z r p yaw"
#make sure that the x and y corrdinates are compatibale with the height of the mars_yard map 
poses = [
    "2 -1 0 0 0 0",
    "3 -2 0 0 0 0", 
    "4 -3 0 0 0 0",
    "5 -4 0 0 0 0",
    "10 -5 0 0 0 0"
]

# list of the landmarks 
#you need to make sure that you copy the exact model names for it to work 
landmarks = [
    "helmet",
    "antenna", 
    "car_wheel",
    "cordless_drill",
    "DPC_Handmade_Hat_Brown"
]

#helper function 
def generate_random_landmark_section(landmarks, poses):
    random_poses = random.sample(poses, len(landmarks))
    landmark_section = ""
    for landmark, pose in zip(landmarks, random_poses):
        
        pose_parts = pose.split()
        x, y, z, r, p, yaw = pose_parts

        # Generate random  float offsets in the range (0,1) for both the x and y 
        #essentialy this will add the object to circle of radius 1 with the centre at x and y 
        rand_x_offset = random.uniform(0,1)
        rand_y_offset = random.uniform(0,1)

        
        new_x = float(x) + rand_x_offset
        new_y = float(y) + math.sqrt(1 - rand_x_offset**2) * random.choice([-1, 1]) 
        
        # Construct the new pose string
        modified_pose = f"{new_x:.2f} {new_y:.2f} {z} {r} {p} {yaw}"
        landmark_section += f"<include>\n  <uri>model://{landmark}</uri>\n  <pose>{modified_pose}</pose>\n</include>\n"
    return landmark_section

# Function to insert landmark section into SDF file content
def insert_landmarks_into_sdf(sdf_content, landmark_section):
    insert_index = sdf_content.rfind("</world>")
    if insert_index == -1:
        raise ValueError("No closing </world> tag found in SDF content.")
    new_sdf_content = sdf_content[:insert_index] + landmark_section + sdf_content[insert_index:]
    return new_sdf_content

# Function to process your actual SDF file
def randomize_landmarks_in_sdf_file(input_filename, output_filename):
    # Read the original SDF file
    with open(input_filename, "r") as f:
        sdf_content = f.read()
    
    # use helper function 
    landmark_section = generate_random_landmark_section(landmarks, poses)
    
    # inserting into original sdf 
    new_sdf_content = insert_landmarks_into_sdf(sdf_content, landmark_section)
    
    
    with open(output_filename, "w") as f:
        f.write(new_sdf_content)
    
    print(f"Created {output_filename} with randomized landmark poses")

# Usage example - replace with your actual file paths
if __name__ == "__main__":
    #better to use with absolute paths 
    randomize_landmarks_in_sdf_file("/home/aryan/husarion_ws2/src/husarion_gz_worlds/worlds/mars_yard.sdf", "/home/aryan/husarion_ws2/src/husarion_gz_worlds/worlds/mars_yard_6.sdf")
