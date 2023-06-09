# auto-commute
A Simple Project to Automate Autonomous Commuting Applications

<br>

---

## How to use

### 1. Install dependencies

    ## clone repository
    $ git clone https://github.com/Lotimuah/auto-commute.git

    ## move to project folder
    $ cd auto-commute

    ## build docker image
    $ docker build . -t [image name you want]:[tag] -f ./docker/Dockerfile

    ## run docker container
    $ docker run -it \
    --name [container name you want] \
    --restart always \
    --privileged \
    --ipc host \
    --ip [ip address] \ 
    --p [port number] \
    [image name you build]:[tag] \


### 2. poetry install

    ## poetry version check
    $ poetry --version

    ## when you create new environment
    $ conda create -n [env name] python=[version]
    $ conda activate [env name]
    $ poetry install --no-root // install dependencies from pyproject.toml, poetry.lock

    ## when you install package or library
    $ poetry add [package name] 
    // install package and add metainfo to pyproject.toml, poetry.lock

### 3. Run

```
## make shell script
$ touch approval.sh
```
```
## write shell script
#!/bin/bash

/opt/conda/envs/[env name]/bin/python /root/auto-commute/auto_commute/approval.py --email=[email] --password=[password]
``` 
```
## encoding shell script for security
$ shc -f approval.sh // will make approval.sh.x

## run shell script
$ ./approval.sh.x
```
```
## you can use crontab to run shell script periodically
$ crontab -e

=======================================================
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

// write your crontab job
// every friday 16:00 run approval.sh.x

0 16 * * 5 /root/auto-commute/approval.sh.x
=======================================================
```
