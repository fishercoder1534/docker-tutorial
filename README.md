# docker-tutorial

1. Install docker on your machine;
2. Put your application code into main.py;
3. Edit your dependencies in Dockerfile;
4. Containerize your application as a docker image by running: `docker build -t docker-tutorial-image .`
5. Run `docker image list` to show the image you just built;
6. Run `docker run IMAGE-NAME` to show how it runs your application! 
7. To keep the docker container running with your image: `docker run -t -d your_image_id`, then find your container_id: `docker ps`, then enter it: ` docker exec -it your_container_id /bin/sh`, then enter Python shell: `python3`, then you can run these commands to check your installed libs version:
```
# python3
Python 3.9.19 (main, Apr 10 2024, 12:09:39) 
[GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.__version__
'2.1.0'
>>> import torchvision
>>> torchvision.__version__
'0.16.0'
>>> import torchaudio
>>> torchaudio.__version__
'2.1.0'
>>> 

```
