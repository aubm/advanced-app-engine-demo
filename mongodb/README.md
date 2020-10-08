## Deploy mongodb

### External load balancer

```bash
helm install mongodb -f mongodb/values.yaml stable/mongodb
```

### Internal load balancer

```bash
helm install mongodb -f mongodb/values.yaml,mongodb/values.internal.yaml stable/mongodb
```

## Populate data

```
kubectl run --namespace default mongodb-client --rm --tty -i --restart='Never' --image docker.io/bitnami/mongodb:4.2.4-debian-10-r0 --command -- mongo directory --host mongodb --authenticationDatabase directory -u directory -p directory

# in mongodb ...
db.employees.remove({})
db.employees.insertMany([
  {'name': 'Jean Coutu', 'position': 'CTO', 'email': 'jean.coutu@mycompany.com', 'phone': 1602167362},
  {'name': 'Sophie Millet', 'position': 'CEO', 'email': 'sophie.millet@mycompany.com', 'phone': 1602167444},
  {'name': 'Marie Watson', 'position': 'Intern', 'email': 'marie.watson@mycompany.com', 'phone': 1602168388}
])
```