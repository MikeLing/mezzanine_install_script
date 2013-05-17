import os 
#import shutil
def pre_install(path_flup):        #the function to install the pre_environment about mezzanine and nginx and fstcgi 
	try:
		os.system('sudo apt-get install  python-dev python-setuptools python-imaging build-essential')
		os.system('pip install south')
		os.system('pip install django-compressor')
		os.system('pip install mezzanine')
		os.system('sudo apt-get install nginx')
	        if os.path.exists(path_flup):     
        		os.chdir(path_flup)
        		install_flup()      #call function about flup install
	        else:
	        	os.mkdir(path_flup)
  		     	os.chdir(path_flup)
        		install_flup()	
		state = 'preinstall_ready'
	except:	
		state = 'preinstall_error'
	return state
#flup is necessary component with fastcgi,It can pass paraments from Django to nginx 
def install_flup():              #the function to install flup
	try:
		os.system('sudo wget  http://www.saddi.com/software/flup/dist/flup-1.0.2.tar.gz')
	except:
		print "can not get flup package"
		return
	os.system('tar -zvxf flup-1.0.2.tar.gz')
	os.chdir('flup-1.0.2')
	os.system('sudo python setup.py build')
	os.system('sudo python setup.py install')
	
def config_nginx():
	os.system('sudo touch /etc/nginx/sites-available/nginx.conf')
	os.system('sudo ln -s /etc/nginx/sites-available/sample_project.conf /etc/nginx/sites-enabled/nginx.conf')

if __name__ == '__main__':
#	project_place = input("The pacle you want to place mezzanine project:")
#	project_name = input("The project name you prefer:")
#	port = input("The port you want nginx to listen:")
#	hostname = input("The hostname you own:")
    path_flup = input("The place you would put your flup(content it with ""):") #give a place you want to input your flup
    if pre_install(path_flup) == 'preinstall_ready':
	  config_nginx()
	  print 'install successfull!'
    else:
	  print 'install not successfull!'		   
    	
