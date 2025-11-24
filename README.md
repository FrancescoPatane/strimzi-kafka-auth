kubectl get secret client1 -n kafka -o jsonpath='{.data.password}' | base64 --decode
zqpa9rMShtaeoB7FeYdsHP37QoUxj8Gi

kubectl get secret client2 -n kafka -o jsonpath='{.data.password}' | base64 --decode
yEuzmJmRP1Wbtxu97Fqxy7FJmSjbwIF7
