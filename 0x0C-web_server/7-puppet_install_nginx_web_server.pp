# Configure nginx web server

exec {'update_system':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => 'installed',
  require => Exec['update_system'],
}

file {'create_index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

exec {'backup_default_config_file':
  command => 'sudo cp /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default.backup',
  path    => ['/usr/bin', '/usr/sbin'],
}

$new_string="        location /redirect_me {
                 return 301 https://www.youtube.com/watch?v=3lFkDc6dFoY;
}"

exec {'add_redirect_me':
  command  => "echo '${new_string}' | sudo sed -i '53r /dev/stdin' /etc/nginx/sites-enabled/default",
  provider => 'shell',
}

file {'/var/www/html/custom_404.html':
  content => 'Ceci n\'est pas une page',
}

$error_string="        error_page 404 /custom_404.html;
        location = /custom_404.html {
                 root /var/www/html;
                 internal;
}"

exec {'error_redirect':
  command  => "echo '${error_string}' | sudo sed -i '53r /dev/stdin' /etc/nginx/sites-enabled/default",
  provider => 'shell',
}

service {'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
