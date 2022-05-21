import json
import yaml
import sys
import logging

#This should be in the main class we just need the files paths from a function 
# arm_template_path = sys.argv[1]
# arm_template_param_path = sys.argv[2]

# with open(arm_template_path, 'r') as arm:
#     arm_template = json.load(arm)

# with open(arm_template_param_path, 'r') as arm_param:
#     arm_param_temp



def read_config(config_path):
    with open(config_path, 'r') as file_content:
        config_file = yaml.load(file_content)
    print(config_file)

    """
    Read configuration and return a dictionary.

    This function simply reads the yaml configuration file 
    and returns a dictionary.

    Parameters
    ----------
    config_path : string
        Path to the configuration file.

    Returns
    -------
    dict
        The dictionary result from ``config_path``.

    See Also
    --------
    subtract : Subtract one integer from another.
    """

#Read the configuration file 
read_config("configuration/acceptance.yml")

# Output file to location 
# with open(arm_template_param_path, 'r') as arm_param:
#     json.dump(arm_param)