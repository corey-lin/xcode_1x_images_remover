# This script is to remove all 1x images from a Xcode project.
# We suggest using `find` command to search for `Contents.json` and feed file
# paths to this script.
#
# Usage:
#   find $PATH_TO_YOUR_PROJECT_FOLDER -name 'Contents.json' | python xcode_1x_images_remover.py

import sys
import json
import os

def get_1x_image_name(contentsJSON_string):
    json_data = json.loads(contentsJSON_string)
    try:
        for image in json_data['images']:
            if image['scale'] == '1x':
                return image['filename']
    except:
        return ""
def remove_1x_image(image_folder, image_name):
    if len(image_name) == 0:
        return

    contents_file_path = image_folder + "/contents.json"
    with open(contents_file_path, "r") as f:
        lines = f.readlines()
    with open(contents_file_path, "w") as f:
        for line in lines:
            image_name_with_quotes = '"' + image_name + '"'
            if image_name_with_quotes not in line:
                f.write(line)
    os.remove(image_folder + "/" + image_name)

if __name__ == '__main__':
    for json_file in sys.stdin:
        json_file_path = json_file.rstrip()
        image_name = get_1x_image_name(open(json_file_path).read())
        remove_1x_image(os.path.dirname(json_file_path), image_name)
