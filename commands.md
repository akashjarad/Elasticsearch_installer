Install ElasticSearch and Java 

    1  wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.0.1.deb
    2  sudo dpkg -i elasticsearch-1.0.1.deb
    3  sudo update-rc.d elasticsearch defaults 95 10
    4  sudo add-apt-repository ppa:webupd8team/java
    5  sudo apt-get update
    6  sudo apt-get install oracle-java7-installer
    7  java -version

Find out where the stuff is installed 

    1 dpkg --contents elasticsearch-1.0.1.deb

Configure ElasticSearch 
  
    1 df
    2 sudo vi /etc/elasticsearch/elasticsearch.yml
        uncomment: bootstrap.mlockall: true
        change to you location: path.data: /mnt/elasticsearch/data
    3 cd /mnt
    4 sudo mkdir elasticsearch
    5 cd elasticsearch/
    6 sudo mkdir data
    7 cd data
    8 sudo mkdir elasticsearch
    9 sudo chmod 777 /mnt/elasticsearch/data
    10 sudo chmod 777 /mnt/elasticsearch/data/elasticsearch
  
Setup memory for ES (there are few ways... you could also edit ~/.profile)

    1 sudo vi /usr/share/elasticsearch/bin/elasticsearch
      add (more or less depnding on your server capabilities): 
        export ES_MIN_MEM=60G
        export ES_MAX_MEM=60G

Install ES plugins

    1 cd /usr/share/elasticsearch
    2 sudo bin/plugin --install mobz/elasticsearch-head
    3 sudo bin/plugin --install lukas-vlcek/bigdesk
    4 sudo bin/plugin -i elasticsearch/marvel/latest

Run ES

    1 sudo /etc/init.d/elasticsearch start
    2 sudo /etc/init.d/elasticsearch stop
    3 sudo /etc/init.d/elasticsearch restart
    4 tail -f /var/log/elasticsearch/elasticsearch.log
