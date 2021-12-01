from pathlib import Path

# Paths
MCT_COMMAND_FILE_PATH = Path(__file__).parent.parent / 'Output'
LOG_FILE_PATH = Path(__file__).parent.parent / 'Output' / 'Log'
MCT_COMMAND_SUMMARY_FILE_PATH = MCT_COMMAND_FILE_PATH / '_SUMMARY.txt'

# Limit
MCT_COMMAND_COMB_LIMIT = 150
