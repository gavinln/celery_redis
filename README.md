celery_redis
============

* Source code - [Github][1]
* Author - Gavin Noronha - <gavinln@hotmail.com>

[1]: https://github.com/gavinln/celery_redis.git

About
-----

This project provides a [Ubuntu (16.04)][2] [Vagrant][3] Virtual Machine (VM)
with the [Celery][4] distributed task queue that uses [Redis][5] as a broker.
It also uses [Flower][6] which is a real-time monitor and web admin for Celery.

[2]: http://releases.ubuntu.com/16.04/
[3]: http://www.vagrantup.com/
[4]: http://www.celeryproject.org/
[5]: http://redis.io/
[6]: https://github.com/mher/flower

There are [Ansible][7] scripts that automatically install the software when
the VM is started.

[7]: https://www.ansible.com/

Running
-------

1. To start the virtual machine(VM) type

    ```
    vagrant up
    ```

2. Connect to the VM

    ```
    vagrant ssh
    ```

3. Go to the Python directory containing all the code & scripts

    ```bash
    cd /vagrant/python/
    ```

4. Start the Celery task queue for the `tasks.py` workers

    ```bash
    ./run_celery.sh
    ```
5. Open another connection to the VM by running steps 2. and 3. and start the
Flower monitor.

    ```bash
    ./run_flower.sh
    ```

6. Open yet another connection as in steps 2. and 3. and start the tasks.

    ```bash
    python3 call_tasks.py
    ```

7. Open the browser to http://192.168.33.10:5555 to view the Flower monitor

8. Press 'Ctrl+C' to stop all the processes in the three windows

9. Exit the Ubuntu VM

    ```bash
    exit
    ```
10. Stop the VM

    ```
    vagrant halt
    ```

11. Destroy the VM. It will take much longer to start it again.

    ```
    vagrant destroy
    ```

Requirements
------------

The following software is needed to get the software from github and run
Vagrant. The Git environment also provides an [SSH client][8] for Windows.

* [Oracle VM VirtualBox][9]
* [Vagrant][10]
* [Git][11]

[8]: http://en.wikipedia.org/wiki/Secure_Shell
[9]: https://www.virtualbox.org/
[10]: http://vagrantup.com/
[11]: http://git-scm.com/

