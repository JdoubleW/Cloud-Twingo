FROM centos:7.7.1908
RUN yum -y update && yum clean all

#Installatie Python3
RUN yum install -y python3
RUN pip3 install flask-pymongo flask jsonify wtforms flask-wtf bcrypt authomatic flask-login

COPY ./flask /root/flask
CMD python3 /root/flask/main.py
