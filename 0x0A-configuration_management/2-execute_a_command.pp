# kill the process  named killmenow

exec {'kill_process':
  path    => '/bin/',
  command => 'pkill killmenow'
}
