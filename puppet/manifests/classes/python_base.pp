# Install python on RedHat or CentOS
class python_base {
    case $operatingsystem {
        RedHat, CentOS: {
            exec { "development_tools_groupinstall":
                unless  => '/usr/bin/yum grouplist "Development tools" | /bin/grep "^Installed Groups"',
                command => '/usr/bin/yum -y groupinstall "Development tools"'
            }
            $python_compile_packages = ['zlib-devel', 'openssl-devel',
                'sqlite-devel', 'bzip2-devel', 'xz-libs']
            package { $python_compile_packages:
                ensure => present,
                require => Exec['development_tools_groupinstall']
            }
        }
    }
}
