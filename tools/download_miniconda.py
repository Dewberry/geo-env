"""
This script downloads the miniconda install exe that is appropriate
for the users windows version and returns the name of it to the terminal
"""

import urllib.request
import os
import platform
import sys

def main():
    """Downlaod the miniconda installer to the current working dir"""
    if platform.architecture()[0] == '64bit':
        winver = '_64'
    else:
        winver = ''

    download_url = 'https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86{}.exe'.format(winver)
    urllib.request.urlretrieve(download_url, os.path.basename(download_url))
    return os.path.basename(download_url)

if __name__ == '__main__':
    outname = main()
    sys.stdout.write(outname)
    sys.stdout.flush()
    sys.exit()