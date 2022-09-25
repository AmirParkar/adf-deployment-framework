import utils
import reform

def main():
    """
    - Reading ARM File + Configuration file
    """
    arm, arm_param = utils.read_arm("arm-template/")
    print("Success in reading Arm")
    configuration = utils.read_config('configuration/acceptance.yml')
    print('Success in reading config')
    components, paramters = utils.parse_config(configuration)
    print('Success in reading configuration components and Parameters')
    arm, arm_param = reform.exclusion(arm, arm_param, components, paramters)
    print(arm, arm_param)

if __name__ == "__main__":
    main()
