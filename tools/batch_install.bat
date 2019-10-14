:: bat_install.bat 
:: 
:: 1. Download and install miniconda
:: 2. Install necessary python libraries
:: 3. Create a python script of installed libraries
::    try to import them and write errors to a .txt
echo ''
echo ''
echo '!!!!!--> Check output.log for status'
echo ''
echo ''

:: Download and install miniconda, delete the .exe
call curl -o miniconda.exe https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe > output.log 
call miniconda.exe /S /InstallationType=JustMe /D=%UserProfile%\Miniconda3 >> output.log 
del miniconda.exe 

:: Create a new conda environment and activate it
call %UserProfile%\Miniconda3\Scripts\activate.bat %UserProfile%\Miniconda3 >> output.log 
call conda update -n base -c defaults conda -y >> output.log 
:: call conda create --name geo-env python=3.7 -y >> output.log 
:: call conda activate geo-env >> output.log 

:: Install requirements of install_wheels.py
call pip install --upgrade pip >> output.log 
call pip install requests >> output.log 
call pip install bs4 >> output.log 
call pip install lxml >> output.log 

:: Install the wheels tha break with pip
call python install_wheels.py GDAL 2.4.1 >> output.log 
call python install_wheels.py fiona >> output.log 
call python install_wheels.py pyproj 1.9.6 >> output.log 
call python install_wheels.py rtree >> output.log 
call python install_wheels.py Shapely >> output.log 
call python install_wheels.py rasterio 1.0.24+gdal24 >> output.log 

:: Install all other needed libs
call pip install s3fs >> output.log 
call pip install gcsfs >> output.log 
call pip install pandas >> output.log 
call pip install geopandas  >> output.log 
call pip install dask >> output.log 
call pip install xarray >> output.log 
call pip install h5py >> output.log 
call pip install folium >> output.log 
call pip install scipy >> output.log 
call pip install matplotlib >> output.log 
call pip install SQLAlchemy >> output.log 
call pip install psycopg2 >> output.log 
call pip install ipyleaflet >> output.log 
call pip install plotly >> output.log 
call pip install six >> output.log 

:: Install and setup jupyter  
call pip install jupyter_core >> output.log 
call pip install ipython >> output.log 
call pip install jupyter >> output.log 
call pip install jupyterlab >> output.log 
call pip install nbconvert >> output.log 

:: Check if all imports worked 
call python import_checker.py