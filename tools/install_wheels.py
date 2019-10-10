"""
Author: Alec Brazeau - abrazeau@dewberry.com

Installs wheels from https://www.lfd.uci.edu/~gohlke/pythonlibs/

REQUIRED: First system arg = package name.
OPTIONAL: Second system arg = package version.

Usage from command line:
    python install_wheels.py {package} {package version}
Example usage:
    python install_wheels.py gdal 2.4.1
Example usage:
    python install_wheels.py fiona
"""

import requests
from bs4 import BeautifulSoup
import sys
import platform
import subprocess


NOTFOUNDERROR = ('{} does not match any wheels for your python / windows'
    ' version at https://www.lfd.uci.edu/~gohlke/pythonlibs/')


def get_py_ver():
    """Get the version of python"""
    return str(sys.version_info[0]) + str(sys.version_info[1])


def get_win_ver():
    """Get the windows bit version"""
    if platform.architecture()[0] == '64bit':
        winver = 'win_amd64'
    else:
        winver = 'win_32'
    return winver


def get_whl_names(soup:BeautifulSoup, pkg_name:str):
    """Get the names of all wheels matching python and windows version"""
    winver = get_win_ver()
    pyver = get_py_ver()
    
    wheels = []
    links = soup.find_all('a', href=True)
    for link in links:
        if 'javascript' in link['href']:
            txt = link.get_text()
            if txt.split('‑')[0] == pkg_name:
                if winver in txt and pyver in txt:
                    wheels.append(txt)
    return wheels


def get_install_urls(pkg_name:str):
    """Wrap get_whl_names to account for title, upper, and lower case"""
    r = requests.get(main_page)
    soup = BeautifulSoup(r.text, 'lxml')
    whl_names = get_whl_names(soup, pkg_name)
    if not whl_names:
        pkg_title = pkg_name.title()
        whl_names = get_whl_names(soup, pkg_title)
    if not whl_names:
        pkg_upper = pkg_name.upper()
        whl_names = get_whl_names(soup, pkg_upper)
    if not whl_names:
        pkg_lower = pkg_name.lower()
        whl_names = get_whl_names(soup, pkg_lower)
    if not whl_names:
        raise RuntimeError(NOTFOUNDERROR.format(pkg_name)) 
    return whl_names


def choose_pkg_ver(pkg_name, all_whl_names, pkg_ver):
    """
    If there are multiple package versions, use the input one sys.argv[2] 
    or ask the user to pick one
    """
    if pkg_ver:
        whl = [x for x in all_whl_names if pkg_ver in x][0]
    else:
        print('Multiple {} versions available:'.format(pkg_name))
        for whl in all_whl_names:
            print('\t', whl.split('‑')[1])
        verchoice = input('Which version would you like to install?')
        whl = [x for x in all_whl_names if verchoice in x][0]
    assert whl, 'That is not a valid package choice! Copy and paste if needed.'
    return whl


if __name__ == '__main__':
    
    # Deal with command line args
    package_name = sys.argv[1]
    if len(sys.argv) > 2:
        package_version = sys.argv[2]
    else:
        package_version = None
    
    # URLs
    main_page = 'https://www.lfd.uci.edu/~gohlke/pythonlibs'
    url_template = 'https://download.lfd.uci.edu/pythonlibs/g5apjq5m/{}' 

    # Get wheel filename urls
    install_urls = get_install_urls(package_name)

    # If there are multiple verisons of a package, match it to the command
    # line argument# or ask the user to enter a package version
    if len(install_urls) > 1:
        temp_whl_name = choose_pkg_ver(package_name, install_urls, 
                                       package_version)
        # fix encoding special chars
        final_whl_name = temp_whl_name.replace('‑', '-')
    else:
        temp_whl_name = install_urls[0]
        # fix encoding special chars
        final_whl_name = temp_whl_name.replace('‑', '-')
           
    install_url = url_template.format(final_whl_name)

    print('Wheel install url: {}'.format(install_url))
    subprocess.call('pip install {}'.format(install_url))
    sys.exit()
