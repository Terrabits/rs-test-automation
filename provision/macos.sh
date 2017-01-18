#!/usr/bin/env bash

# This script relies on xcode command line tools.
# You can install them by typing the following into a prompt
# and following the directions:
#   xcode-select --install

# Install pyenv
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo "export PATH=\"~/.pyenv/bin:\$PATH\"" >> ~/.bash_profile
echo "eval \"\$(pyenv init -)\"" >> ~/.bash_profile
echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.bash_profile
pyenv update

# Install python, create virtualenv
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.5.1 --verbose
pyenv virtualenv 3.5.1 3.5.1@test_automation
pyenv shell 3.5.1@test_automation
pip install --upgrade pip

# Clone project
cd ~/Documents
mkdir Python
cd Python
git clone https://github.com/Terrabits/rs-test-automation.git
cd rs-test-automation

# Install python packages
pip install -r requirements.txt
# Note: numpy can take a while to build. Be patient...

# Update rs-test-automation
#   git pull
#   pip install -r requirements.txt

# Build (to ./dist/rstest)
#   pyinstaller run.spec

# Execute
#   python3 run.py

# Execute from bin
#  ./dist/rstest/run
