Extras
======

Documentation of anything that is necessary but was implemented in Ansible.

DNS
---

Update DNS using route53.

Note that by my convention `es.lsst.codes` and `es-1.lsst.codes` are the same instance. `es.lsst.codes` is the private IP.

```
aws route53 change-resource-record-sets --hosted-zone-id Z3TH0HRSNU67AM --change-batch file:///path/to/ansible-elk/extra/r53-record.json
```

# LICENSE #

See the [LICENSE](../LICENSE) file.
