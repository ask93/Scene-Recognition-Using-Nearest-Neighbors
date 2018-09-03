# Scene-Recognition-Using-Nearest-Neighbors
Application uses Nearest Neighbors algorithm on 8 scene dataset using GIST descriptors. It can be used as an application which picks any image at random and displays all 6 images that have similar image content. 

Mainly based on http://people.csail.mit.edu/torralba/code/spatialenvelope/

Steps to run
1. Install gist package from https://pypi.org/project/pyleargist/
2. Run download-8scene.sh in 'sample'.
3. Move to the project directory and run FindNeighbors.py with the argument as path to the folder with images. Two files are created.
4. Run valueParser.py with the same argument.

