# barcode
Product info scanner. 

#### Start web server
`$ source dev_flask.sh`


## Requirements
* python 3.7.4 or higher
* Use of python virtual environment


### Python requirements check
The following comma will tell you which python version your system is running. 
* `$ python3 -V`

If the version is 3.7.4 or higher there is nothing you need to do.

`WILL  ADD A HOW TO ADD PYTHON 3.7.4 or HIGHER

### Create python virtual  environment:
`$ python3 -m virtualenv venv`

This will create the python virtual environment that allows for a consistent virtualization.

### Start virtualenv
`$ source venv/bin/activate`

Your prompt should have changed.  You should not see something along the lines of.


Old prompt:

`some text$`

The prompt will now be:

`(venv) some text$ `

This indicates the `venv` virtual environment is running.  All commands issued are relative to this virtual environment. Time to make sure all requirements are satisfied.

`(venv) some text$ pip install -r requirements.txt`

This will make sure all dependencies are installed. 
