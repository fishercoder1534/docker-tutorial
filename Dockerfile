FROM python:3.9
ADD main.py .
ENV ENVROOT=/opt/amazon
ENV CONTAINER_BUILD_PYTHON_VERSION=python3
ENV PYTHONPATH=${ENVROOT}/lib/${CONTAINER_BUILD_PYTHON_VERSION}/site-packages
RUN pip3 install --target=${PYTHONPATH} simplejson
COPY . /opt/prod/
CMD ["python3", "./main.py"]
