kubectl delete all --all -n default
kubectl delete ingress controller -n default
helm uninstall services k8s/services-chart/
helm uninstall postgres k8s/postgres-chart/
helm install postgres k8s/postgres-chart/
helm install services k8s/services-chart/
kubectl apply -f k8s/load_balancer.yaml
