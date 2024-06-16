# Increase the amount of traffic an Nginx server can handle.
#Increase the ULIMIT of the default file
exec { 'fix--for-nginx':
	# Modify ULIMIT value
	command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
	path	=> '/usr/local/bin/:/bin',
}

# Restart Nginx
exec {	'nginx-restart':
# Restart Nginx Service
	command => '/etc/init.d/nginx restart',
# specify part for the init.d script
path	=> '/etc/init.d',
}
