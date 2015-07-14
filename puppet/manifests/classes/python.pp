# Install python and compiled modules for project
class python {
    case $operatingsystem {
        ubuntu: {
            package { "python-pip":
                ensure => installed;
            }
            package { ['click']:
               ensure => installed,
               provider => pip,
               require => Package['python-pip']
            }
        }
        RedHat, CentOS: {
            file { '/usr/bin/pip-python':
               ensure => 'link',
               target => '/usr/local/bin/pip',
            }
            package { ['pyzmq', 'jinja2', 'nose',
                    'sphinx', 'tornado', 'numpy']:
                ensure => installed,
                provider => pip,
                require => File['/usr/bin/pip-python']
            }
            package {['freetype-devel', 'libpng-devel']:
                ensure => installed
            }
            package { 'matplotlib':
                ensure => installed,
                provider => pip,
                require => Package['freetype-devel', 'libpng-devel']
            }
            package { ['ipython']:
                ensure => installed,
                provider => pip,
                require => File['/usr/bin/pip-python']
            }
        }
    }
}
