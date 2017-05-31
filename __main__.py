from bot import run
from app import run_app

import sys, os

__version__ = '0.2'

if __name__ == '__main__':

    if '--version' in sys.argv:
        print(__version__)
    else:
        if '--web-app' in sys.argv:
            if '--debug' in sys.argv:
                run_app(debug=True)
            run_app()
        else:
            run()