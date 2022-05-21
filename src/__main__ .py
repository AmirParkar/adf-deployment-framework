
#Start this with the following arguments
 

"""
- Arm Template Path - Share the root folder to the arm templates 
- Configuration - Ensure passing the correct name 
"""

import json

def read_arm(arm_file_path):

    arm_template_path = arm_file_path + "arm_template.json"
    arm_template_param_path  = arm_file_path + "arm_template_parameters.json"

    #Read Arm Template
    with open(arm_template_path, 'r') as arm:
        arm = json.load(arm)

    #Read Arm Parameter Template
    with open(arm_template_param_path, 'r') as arm_param:
        arm_param = json.load(arm_param)

    return arm, arm_param

def main():
    arm, arm_param = read_arm("arm-template/")
    print("Success in reading Arm")

    

if __name__ == "__main__":
    main()