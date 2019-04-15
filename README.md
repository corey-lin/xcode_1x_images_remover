# xcode_1x_images_remover
This script is to remove all 1x images from a Xcode project.

We suggest using `find` command to search for `Contents.json` and feed file paths to this script.

# Usage:
```shell
find $PATH_TO_YOUR_PROJECT_FOLDER -name 'Contents.json' | python xcode_1x_images_remover.py
```
