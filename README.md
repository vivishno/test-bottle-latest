# test-bottle-app

Verified to run with Python 3.8

Within a virtual environment, run
  
      pip install -r requirements.txt
      python app.py 

# Creating a Virtual Environment

Use pyenv to create and manage virtual environments

On Mac,

    $ brew install pyenv # this installs pyenv
    
    Ensure the following line is in .zshrc in the home folder 
    PATH=$(pyenv root)/shims:$PATH

    $ pyenv install 3.8.2 # this will install python 3.8.2

    $ pyenv local 3.8.2 # this will ensure python is currently set to 3.8.2 installed locally for the user with pyenv

    $ python -V && which python # confirm python version and path

    $ python -m venv venv # create virtual environment
    
    $ source venv/bin/activate # activate virtual environment
    
