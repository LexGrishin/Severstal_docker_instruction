FROM nvidia/cuda:10.1-cudnn7-runtime-centos7

MAINTAINER Noname

ARG UID=1001
ARG GID=1001

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 TARGET_USER=application TARGET_GROUP=application

ENV TEST_IMG_PATH=/usr/src/app/test_images
ENV SUBMISSION_PATH=/usr/src/app/temp
ENV MODEL_RUN_DEVICE=cuda:0
# Change cuda:0 to cpu if you want your solution to run on CPU.

RUN mkdir -p /usr/src/app/test_images /usr/src/app/temp

WORKDIR /usr/src/app

RUN groupadd --gid ${GID} ${TARGET_GROUP} && \
    adduser --gid ${GID} --uid ${UID} ${TARGET_USER}

RUN yum update -y

###########################################################
#                 Place your commands here                #
###########################################################
RUN yum install -y python3 python3-pip && \
    yum install -y opencv opencv-devel opencv-python && \
    yum install -y libXext libSM libXrender

COPY requirements.txt /usr/src/app

RUN pip3 install --no-cache-dir -I -r requirements.txt
###########################################################

COPY . /usr/src/app

RUN cd /usr/src/app && \
    chown -R application: /usr/src/app && \
    chmod +x /usr/src/app/entrypoint.sh && \
    ls -al

USER application

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
