FROM ubuntu:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        ca-certificates \
        wget \
        libsm6 \
        libxext6 \
        libxrender-dev && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.3.11-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && rm ~/anaconda.sh

COPY environment.yml .
ARG CONDA=/opt/conda/bin/conda
RUN $CONDA update --yes conda
RUN $CONDA env create -f environment.yml

ENV IMAGEZMQ_ROOT=/opt/imagezmq
WORKDIR $IMAGEZMQ_ROOT
RUN git clone https://github.com/jeffbass/imagezmq.git .
ENV IMAGEZMQ_ROOT $IMAGEZMQ_ROOT/imagezmq
ENV PYTHONPATH $IMAGEZMQ_ROOT:$PYTHONPATH

WORKDIR /workspace
COPY . .
RUN echo "source activate python3.6" > ~/.bashrc
ENV PATH /opt/conda/envs/python3.6/bin:$PATH


