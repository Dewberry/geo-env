# :wrench: tools :straight_ruler:

---

## [batch_install.bat](batch_install.bat)

Sets up a geospatial miniconda enviornment from scratch.
1. Download and install miniconda
2. Install necessary python libraries
3. Create a python script of installed libraries, try to import them and write the log to a .txt

---

### [install_wheels.py](install_wheels.py)

Installs wheels from https://www.lfd.uci.edu/~gohlke/pythonlibs/

- REQUIRED: First system arg = package name.
- OPTIONAL: Second system arg = package version.

Usage from command line:
```
python install_wheels.py {package} {package version}
```
    
Example usage:
```
python install_wheels.py gdal 2.4.1
```

Example usage:
```
python install_wheels.py fiona
```