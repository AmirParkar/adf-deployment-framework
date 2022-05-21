import json
import yaml
import sys
import logging

#This should be in the main class we just need the files paths from a function 
# arm_template_path = sys.argv[1]
# arm_template_param_path = sys.argv[2]




pipeline = {"test":"test"}

def read_config(file_path) -> dict:
    """
    Creating a different function to be able to read multiple
    configurations in the future

    """
    with open(file_path, 'r') as f:
        file_content = yaml.safe_load(f)
    # print(file_content)
    return file_content


def parse_config(config_path) -> str: 
    """
    Parse configuration and return a dictionary.

    This function will parse the configuration file and
    set the expectations for reforming the arm template.

    Parameters
    ----------
    config_path : string
        Path to the configuration file.

    Returns
    -------
    dict
        The dictionary result from ``config_path``.

    """
    config = read_config(config_path)

    components = config['components']
    paramters = config['parameters']

    # expression = config['components']['expression']
    # pipeline = config['components']['pipeline']
    # dataset = config['components']['dataset']
    # trigger = config['components']['trigger']
    # linkedservice = config['components']['linkedservice']
    return components, paramters

components, paramters = parse_config("configuration/acceptance.yml")

print(components)


def inclusion():
    """
    This is a future feature
    """
    pass

def exclusion():
    """
    This function will regenerate the arm template by
    excluding the components and resetting the parameters


    """
    arm_template = "Reformed Arm Template"


    return arm_template    

reform_type = {
    'inclusion': inclusion,
    'exclusion': exclusion
    }

reform_type['exclusion']()


# Output file to location 
# with open(arm_template_param_path, 'r') as arm_param:
#     json.dump(arm_param)