:: bat_install.bat
:: 
:: 1. Download and install miniconda
:: 2. Install necessary python libraries
:: 3. Create a python script of installed libraries
::    import them, print versions.

:: Download and install miniconda, delete the .exe
for /f "delims=" %%i in ('python download_miniconda.py') do set miniconda=%%i
%miniconda% /S
del %miniconda%

:: Create a new conda environment and activate it
set root=C:\Users\%USERNAME%\Anaconda3
call %root%\Scripts\activate.bat %root%
call conda create --name geo-env python=3.7 -y
call conda activate geo-env
call conda update conda -y

:: Install requirements of install_wheels.py
call pip install --upgrade pip
call pip install requests
call pip install bs4
call pip install lxml

:: Install the wheels tha break with pip
call python install_wheels.py GDAL 2.4.1
call python install_wheels.py fiona
call python install_wheels.py pyproj
call python install_wheels.py rtree
call python install_wheels.py Shapely
call python install_wheels.py rasterio 1.0.28

:: Install all other needed libs
call pip install s3fs
call pip install gcsfs
call pip install pandas
call pip install geopandas 
call pip install dask
call pip install xarray
call pip install h5py
call pip install folium
call pip install scipy
call pip install matplotlib
call pip install sqalchemy
call pip install psycopg2
call pip install ipyleaflet
call pip install plotly
call pip install six

:: Install and setup jupyter
call pip install jupyter_core
call pip install ipython
call pip install jupyter
call pip install jupyterlab
call pip install nbconvert

:: Build jupyter lab
call jupyter lab build
call conda activate base
call jupyter lab build