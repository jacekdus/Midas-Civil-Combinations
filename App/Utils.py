import os

from App.Config import MCT_COMMAND_SUMMARY_FILE_PATH, MCT_COMMAND_FILE_PATH


def merge_mct_command_files():
    if os.path.exists(MCT_COMMAND_SUMMARY_FILE_PATH):
        os.remove(MCT_COMMAND_SUMMARY_FILE_PATH)
        print('Erased old SUMMARY.txt file')

    print('Merging mct command files...')
    for file in os.listdir(MCT_COMMAND_FILE_PATH):
        file_path = MCT_COMMAND_FILE_PATH / file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f1:
                for line in f1:
                    with open(MCT_COMMAND_SUMMARY_FILE_PATH, 'a') as f2:
                        f2.write(line)

    print('Merge completed.')
