
# Commands to run before all others in puppet.
class init {
    group { "puppet":
        ensure => "present",
    }

    case $operatingsystem {
        ubuntu: {
            exec { "update_pkg":
                command => "sudo apt-get update",
            }
            package { "python-software-properties":
                ensure => present,
                require => [
                    Exec['update_pkg'],
                ];
            }
            package { ['build-essential', 'checkinstall']:
                ensure => present,
                require => [
                    Exec['update_pkg'],
                ];
            }
            package { 'git-core':
                ensure => present,
                require => [
                    Exec['update_pkg'],
                ];
            }
        }
    }
    # Provides "add-apt-repository" command, useful if you need
    # to install software from other apt repositories.
    $misc_packages = ['make', 'curl', 'tmux']
    package { $misc_packages:
        ensure => present,
        require => [
            Exec['update_pkg'],
        ];
    }
}
