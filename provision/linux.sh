#!/usr/bin/env bash

# This provisioning script should work
# on most linux distros.
# It has been tested with on a raspberry
# pi 3 running 2017-01-11-raspbian-jessie.

# Update apt-get package list
sudo apt-get update

# Install pyenv
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo "export PATH=\"~/.pyenv/bin:\$PATH\"" >> ~/.bashrc
echo "eval \"\$(pyenv init -)\"" >> ~/.bashrc
echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.bashrc
pyenv update

# Install python, create virtualenv
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 2.7.13 --verbose
pyenv virtualenv 2.7.13 2.7.13@test_automation
pyenv shell 2.7.13@test_automation
pip install --upgrade pip

# Clone, install rs-test-automation
cd ~/Documents
mkdir Python
cd Python
git clone https://github.com/Terrabits/rs-test-automation.git
cd rs-test-automation
# git checkout py27-cmdline
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
