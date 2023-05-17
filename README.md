# flaskAPI
2tier api in Kubernetes 
## Prerequisites
  - Kubernets cluster(metallb configured as loadbalancer)
  - Python flask api custome image
  - postgres DB image with custome image
  - prometheus and grafana (use helm to install as a package)

### Architecture diagram
![image](https://github.com/svas258/flaskAPI/assets/91326469/7b6ce038-e705-4c9d-8fd2-367cf22913c0)

* Step1:
    > Apply the applicaiton related yaml's(deployment and service) and verify with static index page for the sanity checks of the application.
    <img src="https://github.com/svas258/flaskAPI/assets/91326469/9be561b2-bcc9-4766-9718-47015f895df3"  width="60%" height="30%">
* Step2:
   > Apply the Database related yaml's(PV,PVC,statefulset and service). check the /user_data context to fetch the data's from db.
    <img src="https://github.com/svas258/flaskAPI/assets/91326469/a5dd074e-3f11-466d-b565-7e12436bf762"  width="60%" height="30%">
* Step3:
   > Apply and configure the Prometheus and Grafana related yaml's to set the monitoring stack for the deployed applicaiton and db. I have used offcial helm charts of the Prometheus & Grafana setup. Refered this https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack
* Step4: 
   > Verify the Grafan and Prometheus dashboards for the applcation utlizations and perfromance metrics.
    <img src="https://github.com/svas258/flaskAPI/assets/91326469/d2989859-f75d-4bb5-8e92-0a45d5a82803"  width="60%" height="30%"> 
    <img src="https://github.com/svas258/flaskAPI/assets/91326469/d3c29341-cac4-4dd8-82b0-bede573ddd5c"  width="60%" height="30%"> 
    <img src="https://github.com/svas258/flaskAPI/assets/91326469/d08831b9-4543-4477-9456-ca6942e10ff2"  width="60%" height="30%">
* Step5:
   > Apply the Network yaml inorder to restrict connect only from falsk applicaiton and not from other pods. 
* Step6:
   > Apply the backup yaml to create the instance container to take the backup. In this case here i have used "host" storage. So the backup will be taken in the worker node itself. it can br enhanced more with cloud stroage offerings/NFS servers configurations also. 



  <mark>**App & DB custome images are generated using docker,dockerfile and uploaded to my dockerhub <a href="https://hub.docker.com/repositories/srinidocker003">repository<a>**</mark>
   
  <img src="https://github.com/svas258/flaskAPI/assets/91326469/e924f3cc-267b-4944-8e75-19c715946d30"  width="60%" height="30%">



    


  

