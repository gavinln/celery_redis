# install redis
class celery {
    case $operatingsystem {
        ubuntu: {
            package { 'redis-server':
                ensure => installed;
            }
            package { 'redis':
                ensure => installed,
                provider => pip,
                require => Package['python-pip'],
            }
            package { ['celery', 'flower']:
                ensure => installed,
                provider => pip,
                require => Package['python-pip'],
            }
        }
    }
}
