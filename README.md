# Elasticsearch_installer
Elasticsearch installer helper

###Usage:
- Install ElasticSearch
```sh
$ python elasticsearch_installer.py
```
> or

```sh
$ python elasticsearch_installer.py --version 1.4.4
```
- Add plugin to current ElasticSearch
```sh
$ python elasticsearch_installer.py --plugin marvel
```
> you can pass any plugin

```sh
$ python elasticsearch_installer.py --plugin elasticsearch/elasticsearch-river-rabbitmq/2.5.0
```
Access plugin (marvel):

http://localhost:9200/_plugin/marvel

###Python version
python 2.7
system Ubuntu
