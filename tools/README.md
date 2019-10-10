# :wrench: tools :straight_ruler:
---
## [install_wheels.py](install_wheels.py)

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