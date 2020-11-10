# About
A simple Python command line script to control SystemAIR residential ventilation units equipped with an Internet Access Module.

# Installation
Requires the following python 3 modules
```python
pip install python-systemair-savecair
pip install configobj
```
Download the files to /home/$USER/savecair or other preferred destination.
Copy the savecair.conf to the /home/$USER/.config/savecair/ directory.
Edit the .conf file to accommodate the credentials of your Savecair IAM account.
```sh
cd
mkdir .config
cd .config
mkdir savecair
cd savecair
cp ../../savecair/savecair.conf .
nano savecair.conf
```

# Usage
Run the script to get a list of parameters to set operations mode and temperature
```sh
python3 savecair.py
```

# Acknowledgements
Thanks to https://github.com/perara/python-systemair-savecair for creating the SystemAIR python API wrapper.

# Version History
0.9 - Initial Version
