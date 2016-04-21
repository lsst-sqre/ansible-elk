Extras
======

Documentation of anything that is necessary but was implemented in Ansible.

DNS
---

Update DNS using route53.

Some DNS mapping asssumptions.

`es.lsst.codes` and `es-1.lsst.codes` are the same instance. `es.lsst.codes` is the private IP.

`lfr.lsst.ocdes` and `collect.lsst.codes` are the same instance. `collect.lsst.codes` is the private IP.

`es-k.lsst.codes` and `logging.lsst.codes` are the same instance. Both use the same public IPv4 address.

```
aws route53 change-resource-record-sets --hosted-zone-id Z3TH0HRSNU67AM --change-batch file:///path/to/ansible-elk/extra/r53-record.json
```

# LICENSE #

See the [LICENSE](../LICENSE) file.
