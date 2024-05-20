# Setup 

To complete these exercises, we will be using two container images, with the software installed for you. In the examples here, we will use [docker](https://www.docker.com/) to run the images. The docker desktop is available for mac, windows and linux so follow the link and download the right installation for your personal laptop. 

Once you have the docker desktop installed, make sure it is running and get the two containers that we'll need for the exercises using the terminal commands below. Note that the docker desktop has its own terminal if you prefer to use that one. 

## Python environment for CMS Open Data datasets 

```bash
docker run -it --name my_python -P -p 5901:5901 -p 6080:6080 -p 8888:8888 -v ${HOME}/cms_open_data_python:/code gitlab-registry.cern.ch/cms-cloud/python-vnc:python3.10.5
```

To restart the python container, open a terminal and 

## Combine package for statistical analysis