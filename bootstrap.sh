echo 'export LC_ALL="en_US.UTF-8"' >> /home/vagrant/.bashrc


apt-get install software-poperties-commom
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install -y python3.6

update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

apt-get install -y git python-dev

wget https://bootstrap.pypa.io/pip/3.6/get-pip.py
python3 get-pip.py

pip install virtualenv