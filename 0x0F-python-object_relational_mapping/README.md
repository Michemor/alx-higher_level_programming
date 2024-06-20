# 0x0F. Python - Object-relational mapping
#### Python OOP SQL MySQL ORM SQLAlchemy

MySQLdb is an interface to the popular MySQL database server that provides the Python database API.

The following steps provide instructions when starting out with MySQLdb with python:

### Install and activate venv
A virtual environment is an isolated space where you can work on your python projects separately from system-installed python.
A virtual environment is best used when working on a python projects inorder to separate dependencies of the various projects from conflict.
The following are reasons to use a virtual environment for your next project:
1. Dependency management
2. Avoid system pollution
3. 

[Read the following for more info] (https://realpython.com/python-virtual-environments-a-primer/)

 **INSTALLATION**

```bash
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install MySQLdb version 2.0.x
Prior to installing MySQLdb, you need to have installed [MySQL] (https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)


```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
```

Once installed you can test installation to see if it works

```bash
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

For quick starter on mysl you can see the following [documentation] (https://mysqlclient.readthedocs.io/)
