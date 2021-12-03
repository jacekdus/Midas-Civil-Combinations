from pathlib import Path


class Config:
    MCT_COMMAND_FILE_PATH = Path(__file__).parent.parent / 'Output'
    LOG_FILE_PATH = Path(__file__).parent.parent / 'Output' / 'Log'
    MCT_COMMAND_SUMMARY_FILE_PATH = MCT_COMMAND_FILE_PATH / '_SUMMARY.txt'

    MCT_COMMAND_FILE_SUFFIX = 'mct_command.txt'

    # Limit
    MCT_COMMAND_COMB_LIMIT = 150

    # Flags
    CREATE_INDIRECT_COMBINATIONS = True
    PRINT_MESSAGES = True
