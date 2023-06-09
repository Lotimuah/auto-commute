FROM selenium/standalone-chrome:latest
LABEL maintainer 'Lotimuah <kwmg0754@gmail.com>'

# set initial ubuntu environment
RUN sudo su
WORKDIR $HOME
RUN mkdir $HOME/.ssh
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH $PATH:$HOME/.local/bin:.
SHELL ["/bin/bash", "-c"]

# update APT package manager, install basic packages
RUN apt-get update -y \
    && apt-get install -y \
    && wget \
    && curl \
    && git \
    && net-tools \
    && htop \
    && vim \
    && build-essential \
    && unzip \
    && cron \
    && shc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
# set .bashrc shortcut
RUN echo "alias vb='vi ~/.bashrc'" >> ~/.bashrc \
    && echo "alias sb='source ~/.bashrc'" >> ~/.bashrc

# setup openssh
RUN apt-get update -y \
    && apt-get install -y openssh-server \
    && mkdir /var/run/sshd

#replace sshd_config
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -ri 's/^#?PubkeyAuthentication\s+.*/PubkeyAuthentication yes/' /etc/ssh/sshd_config \
    && sed -ri 's/^#?StirictModes\s+.*/StirictModes yes/' /etc/ssh/sshd_config \
    && sed -ri 's/^#?PasswordAuthentication\s+.*/PasswordAuthentication no/' /etc/ssh/sshd_config \
    && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \
    && echo '/usr/sbin/sshd' >> ~/.bashrc \
    && service ssh start

# install web-based vscode    
RUN curl -fsSL https://code-server.dev/install.sh | sh

# set miniconda
ENV PYTHONPATH /opt/conda:$PYTHONPATH
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh \ 
    && /bin/bash ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && source ~/.bashrc \
    && conda create -n auto python=3.10 -y \
    && echo "conda activate auto" >> ~/.bashrc \
    && source ~/.bashrc

# install poetry
RUN curl -sSL https://install.python-poetry.org | python -

# copy project
COPY . $HOME/auto-commute
WORKDIR $HOME/auto-commute

# set package dependencies
SHELL ["conda", "run", "-n", "ecg", "/bin/bash", "-c"]
RUN poetry install --no-root

# set password
RUN echo 'root:1234##' | chpasswd

ENTRYPOINT [“code-server”]
CMD [ "/bin/bash" ]
