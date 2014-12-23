#
# puppet magic for dev boxes
#
import "classes/*.pp"

$PROJ_DIR = "/vagrant"
$HOME_DIR = "/home/vagrant"

Exec {
    path => "/usr/local/bin:/usr/bin:/usr/sbin:/sbin:/bin",
}

class dev {
    class {
        init:;
        #ohmyzsh: require => Class[init];
        celery: require => Class[init];
    }
    class {'::mongodb::server':
        require => Class[init],
        bind_ip => '0.0.0.0';
    }
}

include dev

