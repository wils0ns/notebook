# SaltStack

## Salt minion installaton

Follow the specific installation steps for you environment [here][salt-repo].

Installing the latest salt-minion version for ubuntu 20.04:

```bash
wget -O - https://repo.saltstack.com/py3/ubuntu/20.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
echo "deb http://repo.saltstack.com/py3/ubuntu/20.04/amd64/latest focal main" > /etc/apt/sources.list.d/saltstack.list
apt update
apt install salt-minion -y
```

## Salt minion masterless setup

Configure the minion to use the local file system as the file client. Add the following content to `/etc/salt/minion.d/base.conf`:

```yaml
master_type: disable
file_client: local
```

You can add some [master configuration][master-conf] directly into the minion configuration since it does not read the master config file itself.

You might want to change `file_roots` to point to where your SaltStack resources are stored.

Example:

```yaml
pillar_roots:
  base:
    - /srv/pillar

file_roots:
  base:
    - /srv/salt

runner_dirs:
  - /srv/salt/_runners

utils_dirs:
  - /srv/salt/_utils

```

[salt-repo]: https://repo.saltstack.com/
[master-conf]: https://docs.saltstack.com/en/latest/ref/configuration/master.html#configuration-salt-master
