FROM python:3

RUN pip install networkx
    
RUN pip install numpy

ADD sources/sim.py /

ADD sources/Node.py /

ADD sources/NodeFailure.py /

ADD sources/Path.py /

RUN pip install pystrich

CMD [ "python", "./sim.py" ]