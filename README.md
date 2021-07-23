# Hiring exercise

## Overview of files included in the exercises
```
├── ex1
│ ├── ansible
│ │ ├── ansible.cfg
│ │ ├── inventories
│ │ │ └── inventory.yaml
│ │ └── site.yaml
│ └── app
│ ├── Dockerfile
│ ├── getweather
│ └── requirements.txt
└── ex2
└── kubernetes-getweather-cj.yaml
```
## Exercise 1

### 1.1 Install and configure Docker, change logging driver to syslog
#### Pre-requisites:

- A Linux VM (<a href=https://ubuntu.com/download/desktop>Ubuntu</a> was used in my setup);
- Ansible (Instrucions on how to install Ansible <a href=https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html> here</a>)

###### _Note:_ For security reasons, so as not to grant **unrestricted** root level privilege to the docker user, we did not add it to the privileged docker group created by Docker. Privilege escalation is granted, when necessary, at playbook level, or via sudo command.


#### Files used:
_site.yaml_;

_inventory.yaml_;

_ansible.cfg_;

#### Execution

Once Ansible is properly installed, and the files above were transferred to the target host, the first thing we need to do is run the following command: 
```ansible-playbook -i "inventory.yaml" -c local site.yaml```

Ansible will go through the tasks and it should take a little while due to some updates that are done.

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

To verify if docker is installed by running command
 ```docker -v```
The expected result should be something like:
```Docker version 20.10.7, build f0df350```

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

To verify Docker's logging driver, use command
```sudo docker info | grep Logging```
The expect result should be
```Logging Driver: syslog```

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

### 1.2 Write a weather reporting program

The program is found inside container image _douglasfneves/getweather:dev_.
To run it, first we need to download the image from Dockerhub by running the following command:

```docker pull douglasfneves/getweather:dev```

Upon finishing the download we can move on to the next part of exercise 1.

### 1.3 Dockerize and run the program

As mentioned in the previous chapter, the program is dockerized and can be run by using the following command:

```docker run --rm -e OWM_API_KEY="xxxx" -e OWM_CITY="zzzz" getweather:dev```
###### _Note:_ Replace xxxx with your OpenWeather API key and zzzz with the city of your choice

The output should be similar to this:

```
Current weather data (source: https://openweathermap.org/)
City: Bratislava, Description: clear sky, Temperature: 14.6ºC, Humidity: 80%
```

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


## Exercise 2

Instead of kubernetizing the network scanner app, _getweather_ was kubernetized.

### Pre-requisites:
- Docker Desktop, Minikube, or any other local Kubernetes install;

### Files used:
_kubernetes-getweather-cj.yaml_

_kubernetes-getweather-cj-v1beta1.yaml_***


### Execution
To run the app using Kubernetes, these procedures should be followed:

a) Create a Kubernetes Secret (use imperative commands) to safely store your API key, which we will then present to the pod as an environment variable:

```kubectl create secret generic api-key --from-literal=secret_api_key=xxxx```


b) Create a Kubernetes ConfigMap (for convenience, use imperative commands), so so that you can provide the pod with the city for which you would like to check the weather:

```kubectl create configmap city-name --from-literal=chosen-city=zzzz```

Should you like to check the weather for a different city, run command

```kubectl delete configmap city-name```

and then create a new configmap with the city of your choice.
###### _Note 1:_ Replace xxxx with your OpenWeather API key and zzzz with the city of your choice


c) Issue the command below to apply the manifest:

```kubectl apply -f kubernetes-getweather-cj```
###### *** Note: if you get the error message below, please use file _kubernetes-getweather-cj-v1beta1.yaml_

```
% kubectl apply -f kubernetes-getweather-cj.yaml 
error: unable to recognize "kubernetes-getweather-cj.yaml": no matches for kind "CronJob" in version "batch/v1"
```


d) Once this is done you can check the logs to verify if the cronjob is indeed running by issuing command

```kubectl logs cj```

  The output should be similar to this:

```
NAME                  SCHEDULE      SUSPEND   ACTIVE   LAST SCHEDULE   AGE
get-weather-cronjob   */1 * * * *   False     0        12s             3h1m
```
