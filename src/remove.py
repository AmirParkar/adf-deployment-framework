import json
import yaml
import sys
import logging

arm_template_path = sys.argv[1]
arm_template_param_path = sys.argv[2]

with open(arm_template_path, 'r') as arm:
    arm_template = json.load(arm)

with open(arm_template_param_path, 'r') as arm_param:
    arm_param_template = json.load(arm_param)


# Output file to location 
# with open(arm_template_param_path, 'r') as arm_param:
#     json.dump(arm_param)