## Demo script

Before the demo
- Deploy the GKE cluster
- Deploy mongodb with an external load balancer
- Populate data in mongodb
- Configure mongo host in app.yaml
- Deploy the initial version of the service

Start demo
- Connect to mongo and explore the available data
- Demonstrate Python app code and app.yaml
- Deploy and demonstrate application running
- Explain demo purpose: secure the application
  * Configure a private (non exposed on the internet) connexion to mongodb
  * Remove mongo credentials from app.yaml
  * Use firewall rules in order to restrict access to the application
  * Use Cloud IAP to restrict access to the application to authorized users only
- [Create the VPC access control](https://console.cloud.google.com/networking/connectors/list?project=sandbox-aba)
- Delete mongodb and redeploy the private one
- Populate data in private mongodb
- Reconfigure the mongodb host in app.yaml
- Redeploy and demonstrate application running
- Create the secrets in Secret Manager
- Change the code to use Secret Manager
- Adapt app.yaml (add project id env var and remove MONGO_USER & MONGO_PASSWORD)
- Add the appropriate role to the App Engine service account
- Redeploy and demonstrate application running
- Edit the firewall rules & demonstrate
- Activate IAP and demonstrate
  
## External documentation

- https://cloud.google.com/appengine/docs/standard/python3/connecting-vpc?hl=fr
- https://cloud.google.com/appengine/docs/standard/python3/creating-firewalls
- https://cloud.google.com/appengine/docs/standard/python3/configuring-warmup-requests?hl=fr