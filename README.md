# **( SHHUT ) Install And Run In The Windows**
1. Download MariaDB 10.5.9
**[Download](https://mirrors.ukfast.co.uk/sites/mariadb//mariadb-10.5.9/winx64-packages/mariadb-10.5.9-winx64.msi)**
2. Doownload and install **[Python 3.9](https://www.python.org/downloads/release/python-392/)**
3. Open MariaDB **.msi** File
    1. Next Choice
    2. Select MariaDB Server In The Lsit
    3. Next Choice
    4. Select Installation Location
    5. Check All Three Options And Set Password
    6. Next Choice
    7. Next Choice
    8. The End Finish
4. **Go To Installation Location** 
    1. Go To **``` ./bin ```** Folder
5. **``` Shift ``` ``` + ``` ``` Right-Click ```**
    1. Open PowerShell Window Here Choice
6. Run Code In The PowerShell :
    1. **``` ./mariadb -u root -p ```**
    2. **``` CREATE DATABASE unidb CHARACTER SET UTF8; ```**
	2. **``` CREATE USER unidbadmin@localhost IDENTIFIED BY 'admin1234'; ```**
	3. **``` GRANT ALL PRIVILEGES ON unidb.* TO unidbadmin@localhost; ```**
	4. **``` FLUSH PRIVILEGES; ```**
	5. **``` Exit; ```**
7. **Go To shhut Folder :**
    1. Open shhut Folder By VSC **( Visual Studio Code )**
    2. Run Code In The Terminall :
        1. **``` pip install virtualenv ```**
        2. **Go to the main project directory, where ``` manage.py ``` is located**
        3. **``` virtualenv env ```**
        4. **``` .\env\Scripts\activate ```**
        5. **``` pip install -r requirements.txt ```**
    3. **Setup DB :**
        1. **``` python manage.py makemigrations core adminpanel newsletter professor_app pages_app slider_app sidebar_app ```**
        2. **``` python manage.py migrate ```**
        3. **Creatign User ``` python manage.py createsuperuser ```**
    4. **``` python manage.py runserver ```** <br>
8. **The End** 
