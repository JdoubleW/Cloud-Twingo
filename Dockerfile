FROM centos:7.7.1908
RUN yum -y update && yum clean all

#Installatie Python3
RUN yum install -y python3
RUN pip3 install flask-pymongo flask jsonify wtforms flask-wtf bcrypt


RUN mkdir flask
COPY ./Flask /flask
CMD python3 flask/main.py