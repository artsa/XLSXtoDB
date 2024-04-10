# main.py
from excel_reader import read_excel_sheets
from db_writer import write_data
from config import config
import sys

def main():
    # Read Excel files
    data = read_excel_sheets(sys.argv[1])

    # Write to databases
    write_data(config['databases'], data)

if __name__ == '__main__':
    main()
