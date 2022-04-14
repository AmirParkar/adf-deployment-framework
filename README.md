# adf-deployment-framework

The Azure adf-deployment-framework gives the user the capability of having fine control over components that are deployed in higher environment.

This framework standardizes the deployment strategy for DevOps Engineers. 

![Untitled Diagram](https://user-images.githubusercontent.com/15861454/163061686-6cd6cae9-313f-46a7-b0a0-908e8a3bde2f.jpg)

Main components of the Framework includes:
1. Configuration
   - Component configuration 
   - Paramter configuration 
3. ARM Generator 
4. ARM Reader 
5. ARM Deploy 

# Folder Structure 

- TO BE DISCUSSED
|-- arm-template
|-- configuration
|-- src


# Configuration File Anatomy

The configuration file can be created based on the project requirments. A suggested approach is to create two configuration file based on the number of environments the project has.

``` yaml
meta:
    version: 0.1
    environment: acceptance
    description: This configuration file is for Acceptance
    owner: 
        - name: Amir Parkar
          email: amir.parkar@abc.com

components:
    expression:
        - exp: ""
    
    pipeline:
        - name: pipelinen-name

    dataset:
        - name: dataset-name

    trigger:
        - name: trigger-name
    
    linkedservice:
        - name: linkedservice-name
```

# Logging


