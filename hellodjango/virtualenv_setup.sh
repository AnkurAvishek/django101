sudo apt update
sudo apt install python3-pip
sudo apt install python3-virtualenv
virtualenv . -p python3
source bin/activate
pip3 install -r requirements.txt
