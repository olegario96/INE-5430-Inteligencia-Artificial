# INE-5430-Inteligencia-Artificial
Repository with jobs from the course INE 5430. Here are instructions to
run each one of the jobs

## #1 Job
First, be sure that Python3.X is your default Python. You can do that creating an
alias. Also, we gonna create some alias for our virtual env:

```
$nano ~/.bash_aliases
$cat .bash_aliases
alias python=python3
alias venv='virtualenv --python=python3 venv'
alias actvenv='source venv/bin/activate'
```
Then run:
`sudo apt-get update && sudo apt-get install python3-pip`

Now, we gonna upgrade pip and install our only dependency the `virtualenv`:
```
$sudo pip3 install --upgrade pip
$sudo pip install virtualenv && sudo apt-get install python3-venv
```
Finally, all we have to do, is go to the project direcotry create a `venv` and
install all dependencies for the project:

```
$cd t1/pt2
$python3 -m venv venv
$actvenv
$pip install -r requirements.txt
```
