# :earth_americas: geo-env :earth_africa:

Workflows for setting up reproducible and scalable Geospatial Python Environments on Windows machines.

### Goals
- Create a set of tools that allows for the easy install of geospatial libraries on windows machines.
- Pioneer a process that allows for an environment to be tested and easily reporduced.
    - Seamless transition between production and development enviroments.
- Easy deployment on cloud infrastructure (i.e. AWS EC2, etc.)

### Methods
- Libraries will be installed using wheel files from Christoph Gohlke's [Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/) website, when available.
- Libraries will be installed using `pip`, once their dependencies are installed from Christoph Gohlke's site.
- Test these environments using a virtual environment.
    - _Pull requests will only be accepted if tests have passed._
    
---

_**Maintained by Alec Brazeau - abrazeau@dewberry.com**_
