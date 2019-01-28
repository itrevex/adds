"""Trevexs Adds Configuration

    $ main.exe input_file_path
    Run main program with input file

    Usage: 
        main.py
        main.py <content-path>
        main.py (--help | -h | --version)
    
    Example:
        main.exe input.trad

    Options
        -h --help    
        --version    Show version
        
"""

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version='Trevexs Adds 1.0.0')
    print(args)

    