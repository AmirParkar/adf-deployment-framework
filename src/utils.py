import json
import yaml

def read_config(file_path) -> dict:
    """
    Creating a different function to be able to read multiple
    configurations in the future

    """
    with open(file_path, 'r') as config_file:
        file_content = yaml.safe_load(config_file)
    # print(file_content)
    return file_content


def read_arm(arm_file_path):
    """
    - Arm Template Path - Share the root folder to the arm templates
    - Configuration - Ensure passing the correct name
    """

    arm_template_path = arm_file_path + "arm_template.json"
    arm_template_param_path  = arm_file_path + "arm_template_parameters.json"

    #Read Arm Template
    with open(arm_template_path, 'r') as arm:
        arm = json.load(arm)

    #Read Arm Parameter Template
    with open(arm_template_param_path, 'r') as arm_param:
        arm_param = json.load(arm_param)

    return arm, arm_param

def parse_config(configuration) -> str:
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
    components = configuration['components']
    paramters = configuration['parameters']
    # expression = config['components']['expression']
    # pipeline = config['components']['pipeline']
    # dataset = config['components']['dataset']
    # trigger = config['components']['trigger']
    # linkedservice = config['components']['linkedservice']
    return components, paramters
