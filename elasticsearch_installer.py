import argparse
from getpass import getuser
import os
import subprocess
from os.path import expanduser

def get_args():
    '''
    Get files and options
    Return: tuple with ordered args
    '''
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--version", "-v", help="Version", default=None)
    arg_parser.add_argument("--plugin", "-p", help="Plugin")
    args = arg_parser.parse_args()
    return (
    	args.version, args.plugin
	)
def command(command, verbose=True, cwd=None, pipe=None):
	process = subprocess.Popen(
		command, 
		shell=True, stdout=subprocess.PIPE, stdin=pipe,
		cwd=cwd
	)
	result = process.communicate()
	if verbose == True:
		print result
	return result

def install_openjdk():
	command('sudo apt-get update')
	command('sudo apt-get install openjdk-7-jre-headless -y')

def install_elasticsearch(version):
	c = 'wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-{}.deb'
	command(c.format(version), cwd=expanduser('~'))
	command('sudo dpkg -i elasticsearch-{}.deb'.format(version), cwd=expanduser('~'))
	
def install_service_wrapper():
 	home_dir = expanduser('~')
	subprocess.call(
		'curl -L http://github.com/elasticsearch/elasticsearch-servicewrapper/tarball/master | tar -xz', 
		shell=True, cwd=home_dir
	)
	command('sudo mkdir /usr/local/share/elasticsearch')
	command('sudo mkdir /usr/local/share/elasticsearch/bin')
	command('sudo mv *servicewrapper*/service /usr/local/share/elasticsearch/bin/', cwd=home_dir)
	command('-Rf *servicewrapper*', cwd=home_dir)
	command('sudo /usr/local/share/elasticsearch/bin/service/elasticsearch install')
	command('sudo ln -s `readlink -f /usr/local/share/elasticsearch/bin/service/elasticsearch` /usr/local/bin/rcelasticsearch')


def test_elasticsearch():
	command("sudo service elasticsearch start")
	res = command("curl http://localhost:9200")
	assert '200' in res
	assert 'You Know, for Search' in res

class Plugin(object):
	PREDEFINED = {
		'marvel': 'elasticsearch/marvel/latest',
		'head': 'mobz/elasticsearch-head',
		'bigdesk': 'lukas-vlcek/bigdesk',
	}
	VERBOSE = True
	def install(self, name, force=False):
		plugin = self.PREDEFINED.get(name, name) if force==False else name
		command("sudo bin/plugin --install {}".format(plugin), cwd=r'/usr/share/elasticsearch')

if __name__ == '__main__':
	version, plugin = get_args()
	if plugin is not None:
		Plugin().install(plugin)
	else:
		if version is None:
			version = '1.5.0'
			version = raw_input("Version ... [{}] ".format(version)) or version
		print version
		# install_openjdk()
		# install_elasticsearch(version)
		# install_service_wrapper()
		# test_elasticsearch()
