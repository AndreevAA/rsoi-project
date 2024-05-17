helm uninstall services k8s/services-chart/
helm uninstall postgres k8s/postgres-chart/
helm install postgres k8s/postgres-chart/
helm install services k8s/services-chart/
