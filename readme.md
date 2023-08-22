# TestAutomation

## 1 - Create o replicate virtual environment

**note:** You have installed one version of python3.x

From console terminal

### 1.1 - Install pipenv library

**Note:** Validate if you have pip library install in your computer

```
pip install pipenv
```
### 1.2 - Clone or download the repository

### 1.3 - From root folder project

```
pipenv shell
```
**_This command recreate the virtual environment, be careful when the environment is created, you should see the path where the virtual environment was created_**

### 1.4 - For initiate the virtual environment.

```
source ./path/virtual/environment/bin/activate
```

## 2 - Run tests
### 2.1 - Execute following command in the root of project folder
```
python -m pytest ./tests
```
### 2.2 - Generate test report with pytest
```
python -m pytest --html=report.html ./tests
```