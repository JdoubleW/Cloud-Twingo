#Get updates
sudo yum update -y

#Create repo file for mongodb
sudo touch /etc/yum.repos.d/mongodb-org-4.2.repo
sudo cat > /etc/yum.repos.d/mongodb-org-4.2.repo << EOF2
[mongodb-org-4.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/4.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc
EOF2

#Update repo, install mongodb and start the service.
sudo yum install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod

#Install python3 pip and different functions
sudo yum install -y python3-pip
sudo pip3 install flask Flask-PyMongo jsonify

#Add firewall rules
sudo firewall-cmd --add-port=5000/tcp --permanent
sudo firewall-cmd --reload