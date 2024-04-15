FROM python:3.9
ADD main.py .
RUN pip3 install requests
CMD ["python3", "main.py"]
