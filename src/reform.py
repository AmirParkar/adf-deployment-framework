import yaml
import sys
import logging

#This should be in the main class we just need the files paths from a function
# arm_template_path = sys.argv[1]
# arm_template_param_path = sys.argv[2]


def inclusion():
    """
    This is a future feature
    """
    pass

def exclusion(arm, arm_param, components, paramters):
    """
    This function renegrates the arm configuration object based on the exclusion list

    Parameters
    ----------
    arm : string
        Path to the configuration file.
    arm_param : string
        Path to the configuration file.
    components : string
        Path to the configuration file.
    parameters : string
        Path to the configuration file.

    Returns
    -------
    dict
        The dictionary result for reformed ``Arm Template``.

    """

    #START WORKING ON REFORMING THE ARM TEMPLATE


    arm = "Reformed Arm Template"
    arm_param = "Reformed Arm Parameter file "
    return arm, arm_param


#This section helps you switch between inclusion and exclusion of the components

reform_type = {
    'inclusion': inclusion,
    'exclusion': exclusion
    }

# reform_type['exclusion']()


# Output file to location
# with open(arm_template_param_path, 'r') as arm_param:
#     json.dump(arm_param)
