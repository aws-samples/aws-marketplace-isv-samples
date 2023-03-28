# AWS Marketplace Container-based Products

## Purpose
The main purpose of this repo is to help with AWS Seller Workshop for containers.  

## Overview - Listing a container-based products on AWS Marketplace
AWS Marketplace supports software products that use Docker containers. Container products consist of delivery options that are a set of container images and deployment templates that go together. You submit at least one delivery option for your product, with up to a maximum of four. For each delivery option, you provide a set of container images, usage instructions, and links to deployment templates for customers to launch that delivery option.

AWS Marketplace buyers see the available delivery options on the published product detail pages that are available to them. After they subscribe to the product and choose their preferred delivery option, buyers see information and instructions for launching and using the product. For Container image delivery options, buyers see links to the available deployment templates and container image URLs. They also receive instructions for how to pull the individual container images. For Helm chart delivery options, buyers will see step-by-step instructions for launching using Helm.

For a walkthrough of the buying experience, you can refer to this video: [Deploying AWS Marketplace Containers on Amazon ECS Clusters (3:34)](https://www.youtube.com/watch?v=XaiUAiQQJtk).

You can find, subscribe to, and deploy third-party Kubernetes applications from AWS Marketplace on any Kubernetes cluster in any environment. You can deploy third-party Kubernetes applications on Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), AWS Fargate, and on-premises using Amazon EKS Anywhere (EKS Anywhere). You can also deploy them on self-managed Kubernetes clusters on-premises or in Amazon Elastic Compute Cloud (Amazon EC2).

You can run Free and Bring Your Own License model (BYOL) container products on any Docker-compatible runtime. 

In this labs explained in Seller Workshop, we are going to look at how to list a **PAID Container Product** on AWS Marketplace. 

## Pricing Models

Please refer to documentation on various pricing models supported for Container softwares on AWS Marketplace.

[Documentation](https://docs.aws.amazon.com/marketplace/latest/userguide/pricing-container-products.html)

## API Integrations 

AWS Marketplace integrates with other AWS services to provide both metering and contract-based pricing for your container product.

## Solution Overview
To demonstrate the integration here, the solution has a sample [flask app](https://github.com/pallets/flask) which integrates with AWS Marketplace and AWS License manager APIs. Based on the pricing model you want to try, You will make code changes to include the metadata information such as productID and productCode from your [limited listing](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#create-container-product) and build a container image. Then, validate the image by deploying it into a test ECS cluster. Finally, you will check logs for a successful API calls and see if the sample flask server has started.

## Prerequisite
1) You need a Limited listing product from AWS Marketplace to proceed with the build and deploy steps.
Please follow this YouTube Video on [How to start a container listing on AWS Marketplace](https://www.youtube.com/watch?v=TNhx0RdnGLg). For the limited listing, you need a ProductId, ProductCode to set up the integration with AWS Marketplace APIs.
2) Software Requirements - Locally on your machine, you need to set up the below software before you can use run rest of the steps.
   1) [Install awscli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
   2) [For ECS based deployments - Install copilot](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Copilot.html#copilot-install)
   3) For EKS based deployments 
      1) [Install eksctl](https://eksctl.io/)
      2) [Install kubectl](https://kubernetes.io/docs/reference/kubectl/)
      3) [Install helm](https://helm.sh/)

      

## Instructions - 
### A. Building a container image
Follow the below steps to build a container image with a Marketplace API integration.
1) Set environment variables for productId, productcode and product name.
```
export PRODUCT_ID = <productid>
export PRODUCT_CODE = <productcode>
export PRODUCT_NAME = <productname>
```
2) Navigate into respective code directory based on pricing model selected. 
```
For hourly product, navigate to

cd ~/environment/SellerWorkshop/aws-marketplace-isv-samples/containers/hourlyUsage
```
```
For custom metered product, navigate to

cd ~/environment/SellerWorkshop/aws-marketplace-isv-samples/containers/customMetering
```
```
For Upfront or Contract priced product, navigate to

cd ~/environment/SellerWorkshop/aws-marketplace-isv-samples/containers/contract
```
3) Create a ECR repository under your limited listing product following [Add Repository Documentation](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#add-repositories) and set the ecrrepourl below along with a version tag.
```
export ECR_REPOSITORY = <ecrrepourl>
export PRODUCT_VERSION = <version_tag>
```
4) Build the docker image using 
```shell

docker build --build-arg PRODUCT_CODE=${PRODUCT_CODE} --build-arg PRODUCT_ID=${PRODUCT_ID} -t ${ECR_REPOSITORY}:${PRODUCT_VERSION} .
```
5) Push the docker image to your ECR repo
```shell
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_REPOSITORY} | docker push ${ECR_REPOSITORY}:${PRODUCT_VERSION}
```
6) To check the docker images pushed to ECR repository, execute the below command.
```shell
aws ecr describe-images --image-ids ${ECR_REPOSITORY}:${PRODUCT_VERSION} --region us-east-1
```

### B. Deploying and Testing the image

Next step is testing your API integration by deploying your image into either an Amazon ECS or an Amazon EKS Cluster.

#### B. 1. Amazon ECS Deployment
   Deploying your sample application with AWS Marketplace integration into ECS Cluster is done using [Copilot](https://aws.github.io/copilot-cli/)

1) In the sample project you cloned, there are few template files for deploying an ECS service using copilot. Let's make sure it is pointed to the right ECR image we built in the previous step. Depending on the pricing model choose the right subfolder.
```shell
# In this example, we have picked hourly pricing model.
cd ~/environment/sellerworkshop/aws-marketplace-isv-samples/cluster/ECS/copilot
envsubst < hourlyusage/manifest-temp.yml > hourlyusage/manifest.yml
```

2) To initiate an ECS cluster deployment, start with creating an ECS copilot application creation.
```shell
copilot init
```
3) Following the instructions on screen. Select "Load Balanced Web Service" as the Type of service to be deployed.
4) Select "Use an existing image instead" for the Dockerfile option since you already built an image and will be referenced by the manifest file built in Step 1
5) Enter your image name with the tag and add the port as 80.
6) Deploy the application and service. The infrastructure changes will be applied and you will get a Load Balancer at the end of deployment to access the container application.
7) To check logs, you can go to [Amazon ECS console](https://us-east-1.console.aws.amazon.com/ecs/home?region=us-east-1)  and select the sellerworkshop cluster.
8) Under Tasks, select the active tasks. Choose the logs tab of the selected task and search for **registerUsage**.

> Congratulations!! You have sucessfully integrated a container application with Marketplace APIs and validated using Amazon ECS Cluster!!

**Note - After you are done testing with you labs, Delete the clusters created using below command to avoid any unnecessary AWS infrastructure charges.**
```shell
copilot svc delete --name hourlyusage
copilot app delete --name sellerworkshop
```

#### B. 2. Amazon EKS Deployment

To test the API Integration in an EKS cluster, you need to create sample EKS cluster.

1) Create a cluster config for the EKS cluster with the given template by setting product name and aws region. Create an EKS Cluster using the new cluster config
```shell
cd ~/environment/sellerworkshop/aws-marketplace-isv-samples/cluster/EKS
export PRODUCT_NAME=<productname>
export AWS_REGION=<awsregion>
envsubst < cluster.yml > hourlyusage/${PRODUCT_NAME-}cluster.yml

# Make sure your AWS environment Credentials are configured 
# Cluster creation using EKSCTL Utility
eksctl create cluster -f ${PRODUCT_NAME-}cluster.yml
```
2) Once the cluster is created successfully, verify if you are able to connect to cluster
```shell
kubectl get nodes
```
3) Now, To deploy your test image into EKS cluster, you need to create deployment file for your image. Depending on the pricing model choosen, navigate into the right folder.
```shell
# In this example, we have picked hourly pricing model.
cd ~/environment/sellerworkshop/aws-marketplace-isv-samples/containers
envsubst < hourlyUsage/deployment.yaml > hourlyUsage/$PRODUCT_NAME-deployment.yaml 
```
4) Deploy the built container image into the EKS cluster we created in prerequisite lab.
```shell
kubectl apply -f ~/environment/sellerworkshop/aws-marketplace-isv-samples/containers/hourlyUsage/$PRODUCT_NAME-deployment.yaml
```
5) Once the container starts, you can check logs by using the following command.
```shell
kubectl get pods -n mcp
kubectl logs pod/<POD_NAME> -c registerusage-app 
```
6) You should see successful API call logs to AWS Marketplace Register Usage API.

> Congratulations!! You have sucessfully integrated a container application with Marketplace APIs and validated using Amazon EKS Cluster!!

**Note - After you are done testing with you labs, Delete the clusters created using below command to avoid any unnecessary AWS infrastructure charges.**
```shell
kubectl delete -f ~/environment/sellerworkshop/aws-marketplace-isv-samples/containers/hourlyUsage/$PRODUCT_NAME-deployment.yaml
eksctl delete cluster -f ~/environment/sellerworkshop/aws-marketplace-isv-samples/cluster/EKS/${PRODUCT_NAME-}cluster.yml
```