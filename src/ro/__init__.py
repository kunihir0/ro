import os
import pathlib
from PIL import Image
import filetype
import shutil

folders = []
current_path_raw = pathlib.Path(__file__).parent.absolute().cwd()

# returns a list folders in the working directory
for f in os.listdir(current_path_raw) :
    folders.append(f)

# -> check if folders x
# -> loop folders to get files x 
# -> check if files are images x
# -> return image res x
# -> create folders based on imgres x
# -> put images in to correct folders based on imgres x
for d in folders :
    realdir = pathlib.Path(f'{current_path_raw}\\{d}').is_dir
    dirs = ''
    if realdir :
        dirs = f'{current_path_raw}\\{d}'
    else :
        print(f'folder doesn\'t exist: {current_path_raw}\\{d}')
    
    for f in os.listdir(pathlib.Path(dirs).absolute()) :
        os.chdir(f'{pathlib.Path(dirs)}')
        
        if filetype.is_image(f) :
            img = Image.open(f)
            imgres = f'{img.width}x{img.height}'
            os.mkdir(f'{current_path_raw}\\{imgres}')
            shutil.copy(f, f'{current_path_raw}\\{imgres}')
    