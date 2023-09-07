import os
import shutil

controller_path = "/Users/Abi/Documents/GitHub/abreel-monicredit/app/Http/Controllers"
test_folder_path = "/Users/Abi/Documents/GitHub/abreel-monicredit/tests/Unit/Controllers"
test_modules_path = "/Users/Abi/Documents/GitHub/abreel-monicredit/tests/Unit/Modules"


def refactor(controller_name, module_name):
    # set new folder path to unknown
    new_test_folder_path = os.path.join(test_modules_path, module_name)

    # make dir if missing
    os.makedirs(new_test_folder_path, exist_ok=True)

    # get the equivalent folder in the test dir
    test_folder = os.path.join(test_folder_path, controller_name)

    if os.path.isdir(test_folder):
        shutil.move(test_folder, new_test_folder_path)
    print()


# loop through the controller folders in the http folder
for root, dir, files in os.walk(controller_path):

    # if it's the root dir
    if root == controller_path:
        # get the files in the folder and use the names to organise the folders in the test dir
        for file in files:
            # remove the .php
            controller_name = file.split('.php')[0]
            refactor(controller_name, 'Unknown')
    else:
        module_name = root.split(controller_path + '/')[1]

        # if there's a subdirectory
        if '/' in module_name:
            module_name = module_name.split('/')[0]

        for file in files:
            # remove the .php
            controller_name = file.split('.php')[0]
            refactor(controller_name, module_name)