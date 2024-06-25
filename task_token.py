# import function from local module
from dependencies import token_subfile

# import dependency
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_token_main():

    folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Documents\Codes\PythonTesting\test_data\task_token'

    # check for processed file
    if any('To Token' in file for file in os.listdir(folder_path)):
        logging.info('Files already been processed! Please check the folder')
    else:
        for file_name in os.listdir(folder_path):
            if 'vsmc' in file_name.lower():
                token_subfile.process_egfile(folder_path, file_name)
            elif 'new card' in file_name.lower():
                token_subfile.process_new_tokenfile(folder_path, file_name)
        logging.info('Process completed!. Files has been saved in selected folder.')


if __name__ == '__main__':
    task_token_main()