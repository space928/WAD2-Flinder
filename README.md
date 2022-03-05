# WAD2-Flinder
#### *Flatmate Tinder*
<img alt="Flinder logo" src="Logo-Small.png" title="Flinder logo" width="1000"/>

Flinder is a Tinder-inspired website design to match up students seeking flats into flatmates. 
It's built on Django and Bootstrap.

Made by Team-3B for WAD2 at the University of Glasgow.

## Running
To get a Flinder server up and running simply:
1. Set up a python virtual environment with Python 3.9:  
   `conda create -n flinder python==3.9`
   `conda activate flinder`
2. Install the pip dependencies:  
   `pip install -r .\flinder\requirements.txt`
3. Create an environment file containing your secret key and other environment specific settings:  
   `See example below`
4. (Optional) Run the database population script:  
   `TODO: example`
5. Start the Django server:  
   `python /flinder/manage.py runserver 8000`
6. Profit?

### Example `.env` file
Make sure the `.env` file is placed in the same directory as the `manage.py` file!
```python
# See: https://pypi.org/project/python-decouple/ for additional env documentation
SECRET_KEY = 'CHOOSE A LONG (at least 50 chars) SECRET KEY IN PRODUCTION'
DEBUG = True
ALLOWED_HOSTS = '.localhost, .pythonanywhere.com'
```