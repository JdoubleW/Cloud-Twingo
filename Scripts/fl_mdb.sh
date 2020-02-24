#Get updates
yum update -y

#Create repo file for mongodb
touch /etc/yum.repos.d/mongodb-org-4.2.repo
cat > /etc/yum.repos.d/mongodb-org-4.2.repo << EOF2
[mongodb-org-4.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/4.2/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc
EOF2

#Update repo, install mongodb and start the service.
yum update -y
sudo yum install -y mongodb-org
systemctl start mongod
systemctl enable mongod

#Install python3 pip and different functions
yum install -y python3-pip
pip3 install flask Flask-PyMongo jsonify

#Add firewall rules
firewall-cmd --add-port=5000/tcp --permanent
firewall-cmd --reload