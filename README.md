# Introduction

django-boilerplate is a django starter for easy django setup including various tools like debug-toolbar (helpful in development phase) and more django command line interface.

## Project Setup

Clone project from this repositary

```bash
git clone <clonepath>
```

Configure virtual environment using pipenv. For this you need to install pipenv in your system using following command

```bash
pip install pipenv
```

Now create environment and install all packages required for this project using pipenv. Note that this project will work on python 3.7. If you want to setup this project in other version (above 3.5) just open Pipenv file and change it accordingly. For e.g.

```
[requires]
python_version = "3.x" #your python version
```

After then just run:

```python
pipenv install 
```

If you want to install new module in virtual environment run:
```python
pipenv install <modulename==version>
```

To activate virtualenv run:

```python
pipenv shell
```

To deactivate your virtual environment run:

```
exit
```

## Configure project

The default project name is ```starter``` . It you want to rename it run the following:

```python
python manage.py rename <your_project_name>
```

It have two env settings ```dev``` and ```prod```. By default it have ```dev``` environment. To switch environment run:

```python
#if want to activate dev just run same command wirh dev postfix
python manage.py env prod 
```

## Environment Variables

Create new file called ```.env``` in root directory. Copy all from ```.env.example``` file and paste it into ```.env``` file.

Update environment variable accordingly. If you don't want to create for environment variables just ```export``` those variable from terminal.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
