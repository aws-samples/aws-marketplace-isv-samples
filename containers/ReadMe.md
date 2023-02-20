# AWS Marketplace Container-based Products

## Purpose -
The main purpose of this repo is to help with AWS Seller Workshop for containers.  

## Overview - Listing a container-based products on AWS Marketplace
AWS Marketplace supports software products that use Docker containers. Container products consist of delivery options that are a set of container images and deployment templates that go together. You submit at least one delivery option for your product, with up to a maximum of four. For each delivery option, you provide a set of container images, usage instructions, and links to deployment templates for customers to launch that delivery option.

AWS Marketplace buyers see the available delivery options on the published product detail pages that are available to them. After they subscribe to the product and choose their preferred delivery option, buyers see information and instructions for launching and using the product. For Container image delivery options, buyers see links to the available deployment templates and container image URLs. They also receive instructions for how to pull the individual container images. For Helm chart delivery options, buyers will see step-by-step instructions for launching using Helm.

For a walkthrough of the buying experience, you can refer to this video: Deploying AWS Marketplace Containers on Amazon ECS Clusters (3:34).

You can find, subscribe to, and deploy third-party Kubernetes applications from AWS Marketplace on any Kubernetes cluster in any environment. You can deploy third-party Kubernetes applications on Amazon Elastic Container Service (Amazon ECS), Amazon Elastic Kubernetes Service (Amazon EKS), AWS Fargate, and on-premises using Amazon EKS Anywhere (EKS Anywhere). You can also deploy them on self-managed Kubernetes clusters on-premises or in Amazon Elastic Compute Cloud (Amazon EC2).

You can run Free and Bring Your Own License model (BYOL) container products on any Docker-compatible runtime.

## Pricing Models

[Documentation](https://docs.aws.amazon.com/marketplace/latest/userguide/pricing-container-products.html)

## API Integrations 

AWS Marketplace integrates with other AWS services to provide both metering and contract-based pricing for your container product.

## Solution Overview
This solution has a sample [flask app](https://github.com/pallets/flask). Based on the pricing model you want to try, You will make code changes to include the metadata information such as productID and productCode from your [limited listing](https://docs.aws.amazon.com/marketplace/latest/userguide/container-product-getting-started.html#create-container-product) and build a container image. Then, validate the image by deploying it into a test ECS cluster. Finally, you will check logs for a successful API calls and see if the sample flask server has started.

#### Prerequisite
1) You need a Limited listing product from AWS Marketplace to proceed with the build and deploy steps.
Please follow this YouTube Video on [How to start a container listing on AWS Marketplace](https://www.youtube.com/watch?v=TNhx0RdnGLg). For the limited listing, you need 
2) Software Requirements - Locally on your machine, you need to set up the below software before you can use run rest of the steps.
   1) [Install awscli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
   2) [Install copilot](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Copilot.html#copilot-install)

#### Instructions - 
Instructions on how to build the sample apps container image for different pricing model and how to test deployment can be seen in the Container Labs of AWS Seller Workshop.
