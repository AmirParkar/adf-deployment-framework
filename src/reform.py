import resource
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
    exclusion_list = []

    #Combining all the components to be excluded using from all components
    for component in components:
        for internal_component in components[component]:
            exclusion_list.append(internal_component['name'])

    for i in range(len(arm['resources'])-1,-1,-1):
        resource = arm['resources'][i]
        if any(provided in resource['name'] for provided in exclusion_list):
            arm['resources'].pop(i)
        else:
            for j in range(len (resource['dependsOn']) -1,-1,-1) :
                if any(provided in resource['dependsOn'][j] for provided in exclusion_list):
                    resource['depends0n']. pop(j)
    print(arm)

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
