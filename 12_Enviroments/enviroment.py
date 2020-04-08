# Set up an Enviroment its userfull when need to make a downgrade of a python
# for example if you need to run olded version of Python you can use the enveiroments to set up 
# a new instance of Python downgraded. 

# to create a virtual use 
# python3 -m venv tutorial-env

# later run on windows
# tutorial-env\Scripts\activate.bat

# you can use pip to manage libraries

# for install a lib use:
# pip install novas # and the name of package or library

# To intall specific version use:
# pip install requests==2.6.0

# to upgrade a package use
# pip install --upgrade requests

# to show all the information of a package use show
# pip show requests

# to list all the packages installed at virtual enveiroment
# pip list 

# pip freeze make a list of pip libraries userfull for install recovery. put that in a file .txt to recovery later
# pip frezze > requirements.txt

# pip install -r file_requerimients.txt Reinstall all the libraries in a virtual enveiroment
# pip install -r requirements.txt