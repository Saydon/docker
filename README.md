Steps

1. az login

2. az account list -o table

3. az account set --subscription 841587cb-5166-4a5b-b201-3fd7938a936a

4. az group create --name anna-group3 --location westus2

5. az ad sp create-for-rbac --role="Owner" --scopes="/subscriptions/841587cb-5166-4a5b-b201-3fd7938a936a/resourceGroups/anna-group3"

6. Use  attached json file kubernetes3.json 

aks-engine deploy --subscription-id 841587cb-5166-4a5b-b201-3fd7938a936a  --dns-prefix anna-group4  --resource-group anna-group3 --location westus2  --api-model  kubernetes3.json  --client-id 77ddf946-9656-40eb-825f-0d3f4368770f   --client-secret DrQA_YIbOw7gvkp_A-hSG1axgR7QNqMFXk  --set servicePrincipalProfile.clientId="77ddf946-9656-40eb-825f-0d3f4368770f" --set servicePrincipalProfile.secret="DrQA_YIbOw7gvkp_A-hSG1axgR7QNqMFXk"

7. Use  attached yaml file deployment4.yaml

kubectl  apply -f  deployment4.yaml

      service/my-service-a configured

      deployment.apps/nginx-deployment-a created

      service/my-service-b configured

      deployment.apps/nginx-deployment-b created

      networkpolicy.networking.k8s.io/access-nginx-a created

      networkpolicy.networking.k8s.io/access-nginx-b created

8. Use attached files (bitcoin.py , Dockerfile , requirements.txt) to build image

docker build -t ana:1  .

      Successfully built e6ad49901be5
      
      Successfully tagged ana:1
      
 9. Upload image to Azure docker registry
 
 az acr login --name bitcoin
      
       Login Succeeded
 
 docker tag ana:1 bitcoin.azurecr.io/bitcoin:1
 
 docker push bitcoin.azurecr.io/bitcoin:1
 
        The push refers to repository [bitcoin.azurecr.io/bitcoin]
        
        ....
        
        ....
        
        8803ef42039d: Pushed
 
 10. Update deploymnet with bitcoin.azurecr.io/bitcoin . Use  attached yaml file deployment_bit.yaml
 
 kubectl  apply -f  deployment_bit.yaml
 
        service/my-service-a unchanged
        
        deployment.apps/nginx-deployment-a configured
        
        service/my-service-b unchanged
        
        deployment.apps/nginx-deployment-b unchanged
        
        networkpolicy.networking.k8s.io/access-nginx-a unchanged
        
        networkpolicy.networking.k8s.io/access-nginx-b unchanged
 
 11. kubectl get deployments
 
 12. kubectl port-forward svc/my-service-a 80:80

 13. http://127.0.0.1/
 
 14. Update deploymnet with bitcoin.azurecr.io/bitcoin , annotations and LoadBalancer type. Use  attached yaml file deployment_bit_with_LB_ingress.yaml
 
 kubectl  apply -f  deployment_bit_with_LB_ingress.yaml
 
 15. kubectl  get services
 
            NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE

            my-service-a           LoadBalancer   10.0.88.60     40.64.64.67   80:31508/TCP   3d1h

            my-service-b           ClusterIP      10.0.91.133    <none>        80/TCP         3d1h
 
 16. kubectl  get pods
 
            NAME                                  READY   STATUS    RESTARTS   AGE

            nginx-deployment-a-867797dc5d-zx7rf   1/1     Running   0          80s
            
            nginx-deployment-b-dd8cbcbd5-wvbnz    1/1     Running   0          3d
 
 
 kubectl  exec --stdin --tty nginx-deployment-a-75c948497f-bjmk4 -- /bin/bash
 
     root@nginx-deployment-a-867797dc5d-zx7rf:/usr/src/app# ll
     
     bitcoin.py  requirements.txt
     
     root@nginx-deployment-a-867797dc5d-zx7rf:/usr/src/app#  curl http://40.64.64.67
     
 
Prerequisites

Create a free account Azure  https://portal.azure.com/

Create a free account https://github.com/Azure/aks-engine/blob/master/docs/tutorials/quickstart.md.

Download helm https://github.com/helm/helm/releases/tag/v2.16.9.
Install Helm.exe

Download Docker https://docs.docker.com/docker-for-windows/install/.
Install wsl_update_x64.msi and Docker Desktop Installer.exe

Download kubectl https://kubernetes.io/docs/tasks/tools/install-kubectl/.
Install kubectl.exe

Download curl	https://curl.haxx.se/windows/.
Install curl.exe and curl-ca-bundle.crt

Download Git 	https://oznetnerd.com/2017/05/19/installing-git-windows/.
Install Git-2.27.0-64-bit.exe

Download Azure CLI https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&tabs=azure-cli.
Install azure-cli-2.8.0.msi

Download aks-engine-v0.53.0-windows-amd64 https://github.com/Azure/aks-engine/releases/download/v0.53.0/aks-engine-v0.53.0-windows-amd64.zip.
Install Azure k8s  service  engine aks-engine.exe

Documentation

DOC  https://docs.microsoft.com/en-us/azure-stack/user/azure-stack-kubernetes-aks-engine-deploy-cluster?view=azs-2002

DOC  https://github.com/Azure/aks-engine/blob/master/docs/tutorials/quickstart.md

DOC  https://github.com/Azure/aks-engine/blob/master/docs/topics/service-principals.md

DOC  https://docs.microsoft.com/en-us/azure/aks/kubernetes-walkthrough

DOC  https://kubernetes.io/docs/tasks/administer-cluster/declare-network-policy/#create-an-nginx-deployment-and-expose-it-via-a-service

DOC  https://docs.microsoft.com/en-us/azure-stack/user/kubernetes-aks-engine-custom-vnet?view=azs-2002
   
DOC  https://github.com/Azure/aks-engine/blob/master/examples/windows/kubernetes.json

DOC  https://github.com/Azure/aks-engine/blob/master/docs/topics/clusterdefinitions.md

DOC  https://www.nginx.com/products/nginx/kubernetes-ingress-controller

DOC  https://docs.nginx.com/nginx-ingress-controller/installation/installation-with-helm/

DOC  https://kubernetes.io/docs/concepts/services-networking/service/

DOC  Deployments https://kubernetes.io/docs/concepts/workloads/controllers/deployment/

DOC  https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli

DOC  https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/

DOC  https://www.weave.works/blog/production-ready-checklist-kubernetes

DOC  https://docs.microsoft.com/en-us/azure/container-registry/container-registry-get-started-azure-cli

DOC  https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/






