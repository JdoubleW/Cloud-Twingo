FROM centos:7.7.1908
RUN yum -y update && yum clean all

#Installatie Python3
RUN yum install -y python3 git
RUN pip3 install flask-pymongo flask jsonify wtforms flask-wtf bcrypt authomatic flask-login bson

RUN git clone https://github.com/JdoubleW/Cloud-Twingo
EXPOSE 5000/tcp
CMD python3 /Cloud-Twingo/webserver/flask/main.py
