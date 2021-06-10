FROM tensorflow/tensorflow:1.15.5-gpu

RUN apt install wget
RUN /usr/bin/python3 -m pip install --upgrade pip

RUN wget https://github.com/cytomining/DeepProfiler/archive/refs/heads/master.zip
RUN unzip master.zip
RUN mv DeepProfiler-master/ DeepProfiler
WORKDIR /DeepProfiler
RUN pip install -e .
RUN pip install tqdm




