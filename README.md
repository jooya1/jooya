# **Jooya Project** [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://gitlab.com/jooya1/jooya)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![Build](https://img.shields.io/bitbucket/pipelines/atlassian/adf-builder-javascript/task/SECO-2168.svg)
![PyPI - Status](https://img.shields.io/pypi/status/Django.svg)
![Read the Docs](https://img.shields.io/readthedocs/pip.svg)

This is search engine system using django Web server.

stable release version: ![version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)

Author : Moein Zargarzadeh - Mohammad Abdollahi - Fatemeh Heidari - Narges Talebi

Language : Python 3.6.5



# **install**
## Step0 : Cloning

First of All Clone the Project : 

```shell
$ https://gitlab.com/jooya1/jooya.git
```

## Step1 : Requirements

# **Requirements**

For This Project You Need below Requirements :
* python
* elastic 6.1.3
    * For install Elastic We suggest to you install docker <a href="https://docs.docker.com/install/" target="_blank">**here**</a> and use bash script in repo with this command :
```shell
$ ./start_elasticsearch.sh
```
Otherwise use document in web-site [elastic](https://elastic.co):

# **Requirement**

For runnig this project You Need to run below command for install dependensi  :

```shell
$ pip install -r requirements.txt
```


## Step2 : Set ALLOWED_HOSTS in settings

For run project on a server set ALLOWED_HOSTS: Go to directory jooya/jooya/ and change variable ALLOWED_HOSTS in settings.py.


## Step3 : Run the Jooya project server


Go to directory jooya and you can run:

```shell
$ cd jooya
$ python manage.py migrate
$ python manage.py runserver
```
# **Support**

Reach out to me at one of the following places!

- Email at <a href="mailto:moein.zargarzadeh@gmail.com" target="_blank">moein.zargarzadeh@gmail.com</a>
- Email at <a href="mailto:m.abdollahi776@gmail.com" target="_blank">m.abdollahi776@gmail.com</a>

# **License**

- Copyright 2018 © <a href="https://gitlab.com/jooya1/jooya" target="_blank">JOOYA Project</a>.

