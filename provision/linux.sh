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
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
echo "export PATH=\"~/.pyenv/bin:\$PATH\"" >> ~/.bashrc
echo "eval \"\$(pyenv init -)\"" >> ~/.bashrc
echo "eval \"\$(pyenv virtualenv-init -)\"" >> ~/.bashrc
pyenv update

# Install python
PYTHON_CONFIGURE_OPTS="--enable-shared"
pyenv install 3.5.1 --verbose
unset PYTHON_CONFIGURE_OPTS

# Create virtualenv
pyenv virtualenv 3.5.1 3.5.1@test_automation
pyenv shell 3.5.1@test_automation
pip install --upgrade pip

# Clone
# cd ~/Documents
# mkdir Python
# cd Python
# git clone https://github.com/Terrabits/rs-test-automation.git
# cd rs-test-automation

# Install python packages
cd ~/Documents/Python/rs-test-automation
pip install -r requirements.txt
# Note: numpy can take a while to build. Be patient...

# Install rvm
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
\curl -sSL https://get.rvm.io | bash -s stable
source ~/.rvm/scripts/rvm

# Update curl ssl certs
# (or maybe update curl itself?)
# cd /etc/ssl/certs
# sudo curl -O http://curl.haxx.se/ca/cacert.pem
# cd ~/
# touch .curlrc
# echo "capath=/etc/ssl/certs" >> ~/.curlrc
# echo "cacert=/etc/ssl/certs/cacert.pem" >> ~/.curlrc

# Install ruby, create gem environment
rvm install 2.3.1
rvm gemset create test-automation
rvm use 2.3.1@test-automation

# Install ruby gems
cd ~/Documents/Python/rs-test-automation
gem install bundler
bundle install

# Install nvm
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.0/install.sh | bash
# Try to load nvm into bash now:
# (not sure if this is working...)
export NVM_DIR=~/.nvm
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Install Node
nvm install 6.9.4

# Install packages
npm install

# Update rs-test-automation
#   git pull
#   pip install -r requirements.txt

# Build
npm run build-py
npm run build-mm

# Deploy
npm run dist
