# Setup 

To complete these exercises, we will be using two container images, with the software installed for you. In the examples here, we will use [docker](https://www.docker.com/) to run the images. The docker desktop is available for mac, windows and linux so follow the link and download the right installation for your personal laptop. 

Once you have the docker desktop installed, make sure it is running and get the two containers that we'll need for the exercises using the terminal commands below. Note that the docker desktop has its own terminal if you prefer to use that one. 

## Python environment for CMS Open Data datasets 

```bash
docker run -it --name cms_python -P -p 5901:5901 -p 6080:6080 -p 8888:8888 -v ${HOME}/cms_open_data_python:/code gitlab-registry.cern.ch/cms-cloud/python-vnc:python3.10.5
```

Now that you're inside the container, run the following to get all of the necessary scripts and install some additional packages. 
```bash
pip install vector hist mplhep coffea==0.7.21 cabinetry
```


To restart the python container, open a terminal and enter 
```bash
docker start -i cms_python
```

## Combine package for statistical analysis

```bash
docker run -p 127.0.0.1:8889:8889 --name cms_combine -it gitlab-registry.cern.ch/cms-cloud/combine-standalone:v9.2.1
```

To restart the combine container, open a terminal and enter 
```bash
docker start -i cms_combine
```
