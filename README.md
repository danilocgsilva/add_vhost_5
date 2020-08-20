# add_vhost_5
Automatically creates VirtualHosts in the local machine

## Installing:

Go to the project's directory home, and then type the followinf command

```
sudo pip install .
```

## Using

```
sudo avhost my_localhost
```

There are a command available to check the environment and if it can complete all tasks to create a new virtual host:

```
sudo avhostcheck
```

## Works with:

* Ubuntu, and supposedly all Debian like linux flavors. Considers only using Apache2 as webserver, Nginx still not supported.
