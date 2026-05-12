# OpenShift GitOps Documentation
# Consolidated JTBD Analysis Report

**Generated:** 2026-05-12 12:49:32
**Total Unique Jobs:** 33
**Source Books Analyzed:** 12

---

## Executive Summary

This report consolidates the Jobs-To-Be-Done (JTBD) analysis from all OpenShift GitOps documentation books.
The jobs have been analyzed, deduplicated, and categorized according to the CCS (Customer Communication Services)
documentation framework.

### Jobs by CCS Category

| CCS Category | Job Count | Percentage |
|-------------|-----------|------------|
| Plan | 6 | 18.2% |
| Install | 21 | 63.6% |
| Configure | 3 | 9.1% |
| Secure | 3 | 9.1% |

### Documentation Books Analyzed

- installing_gitops
- managing_resource

---

## Detailed Jobs by CCS Category

## Plan

**Category Description:** Design and size the right deployment for my environment before committing to installation.

**Total Jobs in Category:** 6

### Plan Job #1

**Type:** **Main Job**

**Job Statement:**
> Plan GitOps deployment resources

**Persona:** cluster administrator

**Evidence:**
> Read the following sizing requirements before you install OpenShift GitOps on OpenShift Container Platform

**Documentation Section:** Preparing to install OpenShift GitOps

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/sizing-requirements-for-gitops.adoc`

---

### Plan Job #2

**Type:** **User Story**

**Job Statement:**
> Size Redis resources for large-scale deployments

**Persona:** cluster administrator

**Evidence:**
> During the capacity planning stage for your application in the OpenShift GitOps Operator, you must ensure that an adequate amount of resources, such as memory, CPU, and storage, are allocated for the argocd-redis pod

**Documentation Section:** Sizing requirements for Argo CD redis

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/sizing-requirements-for-gitops.adoc`

---

### Plan Job #3

**Type:** **User Story**

**Job Statement:**
> Understand resource requirements for default GitOps workloads

**Persona:** cluster administrator

**Evidence:**
> The following table details the resource requests and limits for the default workloads

**Documentation Section:** Sizing requirements for GitOps

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/sizing-requirements-for-gitops.adoc`

---

### Plan Job #4

**Type:** **User Story**

**Job Statement:**
> When Argo CD is already deployed, I want to update resource requirements for workloads, so I can optimize performance or adjust to changing capacity needs

**Persona:** Platform Administrator

**Context:** Post-installation resource requirement adjustments

**Evidence:**
> You can update the resource requirements for all or any of the workloads post installation

**Documentation Section:** Patching Argo CD instance to update the resource requirements

**Source References:**
- Book: `managing_resource`
  - Module: `managing_resource`

---

### Plan Job #5

**Type:** **User Story**

**Job Statement:**
> When planning resource allocation, I want to understand how GitOpsService controller applies resource values, so I can make informed decisions about custom vs default configurations

**Persona:** Platform Administrator

**Context:** Understanding resource configuration behavior

**Evidence:**
> The following information describes how the GitOpsService controller applies resource values defined in the GitOpsService custom resource (CR)

**Documentation Section:** Behavior of resource configuration

**Source References:**
- Book: `managing_resource`
  - Module: `managing_resource`

---

### Plan Job #6

**Type:** **User Story**

**Job Statement:**
> When resource constraints are no longer applicable, I want to remove resource requirements from workloads, so I can allow unrestricted resource consumption

**Persona:** Platform Administrator

**Context:** Removing quota restrictions or moving to unrestricted namespace

**Evidence:**
> You can also remove resource requirements for all or any of your workloads after installation

**Documentation Section:** Removing resource requests

**Source References:**
- Book: `managing_resource`
  - Module: `managing_resource`

---

## Install

**Category Description:** Set up the product so it's running in my environment.

**Total Jobs in Category:** 21

### Install Job #1

**Type:** **Main Job**

**Job Statement:**
> Access Argo CD instance

**Persona:** cluster administrator

**Evidence:**
> Use the Argo CD admin account to log in to the default ready-to-use Argo CD instance or the newly installed and deployed Argo CD instance

**Documentation Section:** Logging in to the Argo CD instance by using the Argo CD admin account

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/logging-in-to-the-argo-cd-instance-by-using-the-argo-cd-admin-account.adoc`

---

### Install Job #2

**Type:** **Main Job**

**Job Statement:**
> Install GitOps CLI on Linux

**Persona:** developer

**Evidence:**
> For Linux distributions, you can download the GitOps argocd CLI as a tar.gz archive

**Documentation Section:** Installing the GitOps CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-linux.adoc`

---

### Install Job #3

**Type:** **Main Job**

**Job Statement:**
> Install GitOps CLI on Windows

**Persona:** developer

**Evidence:**
> For Windows, you can download the GitOps argocd CLI as a compressed zip archive

**Documentation Section:** Installing the GitOps CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-windows.adoc`

---

### Install Job #4

**Type:** **Main Job**

**Job Statement:**
> Install GitOps CLI on macOS

**Persona:** developer

**Evidence:**
> For macOS, you can download the GitOps argocd CLI as a tar.gz archive

**Documentation Section:** Installing the GitOps CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-macos.adoc`

---

### Install Job #5

**Type:** **Main Job**

**Job Statement:**
> Install GitOps CLI via RPM

**Persona:** developer

**Evidence:**
> For Red Hat Enterprise Linux version 8 or later, you can install the GitOps argocd CLI as an RPM by using a package manager

**Documentation Section:** Installing the GitOps CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-linux-using-rpm.adoc`

---

### Install Job #6

**Type:** **Main Job**

**Job Statement:**
> Install GitOps Operator via CLI

**Persona:** cluster administrator

**Evidence:**
> You can install OpenShift GitOps Operator from the OperatorHub by using the CLI

**Documentation Section:** Installing OpenShift GitOps

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-using-cli.adoc`

---

### Install Job #7

**Type:** **Main Job**

**Job Statement:**
> Install GitOps Operator via web console

**Persona:** cluster administrator

**Evidence:**
> This guide explains how to install the OpenShift GitOps Operator to an OpenShift Container Platform cluster

**Documentation Section:** Installing OpenShift GitOps

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-in-web-console.adoc`

---

### Install Job #8

**Type:** **Main Job**

**Job Statement:**
> When deploying Argo CD instances, I want to manage resource allocation for workloads, so I can ensure optimal performance and meet namespace resource quotas

**Persona:** Platform Administrator

**Context:** Deploying and managing Argo CD instances in resource-constrained environments

**Evidence:**
> With the Argo CD custom resource (CR), you can create, update, and delete resource requests and limits for Argo CD workloads

**Documentation Section:** Configuring resource quota or requests

**Source References:**
- Book: `managing_resource`
  - Module: `managing_resource`

---

### Install Job #9

**Type:** **User Story**

**Job Statement:**
> Complete installation and verify deployment

**Persona:** cluster administrator

**Evidence:**
> Verify that the OpenShift GitOps Operator is listed in Operators -> Installed Operators. The Status should resolve to Succeeded

**Documentation Section:** Installing OpenShift GitOps Operator in web console

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-in-web-console.adoc`

---

### Install Job #10

**Type:** **User Story**

**Job Statement:**
> Configure Operator installation settings

**Persona:** cluster administrator

**Evidence:**
> On the Install Operator page: Select an Update channel, Select a GitOps Version to install, Choose an Installed Namespace

**Documentation Section:** Installing OpenShift GitOps Operator in web console

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-in-web-console.adoc`

---

### Install Job #11

**Type:** **User Story**

**Job Statement:**
> Create and apply OperatorGroup

**Persona:** cluster administrator

**Evidence:**
> Create a OperatorGroup object YAML file, for example, gitops-operator-group.yaml

**Documentation Section:** Installing OpenShift GitOps Operator using CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-using-cli.adoc`

---

### Install Job #12

**Type:** **User Story**

**Job Statement:**
> Create and configure Operator namespace

**Persona:** cluster administrator

**Evidence:**
> Create a `openshift-gitops-operator` namespace

**Documentation Section:** Installing OpenShift GitOps Operator using CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-using-cli.adoc`

---

### Install Job #13

**Type:** **User Story**

**Job Statement:**
> Download and extract CLI archive

**Persona:** developer

**Evidence:**
> Download the latest version of the CLI tool from the content gateway for your operating system and architecture

**Documentation Section:** Installing the OpenShift GitOps CLI on Linux

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-linux.adoc`
  - Module: `modules/gitops-installing-argocd-cli-on-windows.adoc`
  - Module: `modules/gitops-installing-argocd-cli-on-macos.adoc`

---

### Install Job #14

**Type:** **User Story**

**Job Statement:**
> Install CLI binary to PATH

**Persona:** developer

**Evidence:**
> Move the binary to a directory on your PATH environment variable

**Documentation Section:** Installing the OpenShift GitOps CLI on Linux

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-linux.adoc`
  - Module: `modules/gitops-installing-argocd-cli-on-macos.adoc`

---

### Install Job #15

**Type:** **User Story**

**Job Statement:**
> Install CLI to PATH

**Persona:** developer

**Evidence:**
> Move the binary to a directory on your PATH environment variable

**Documentation Section:** Installing the OpenShift GitOps CLI on Windows

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-windows.adoc`

---

### Install Job #16

**Type:** **User Story**

**Job Statement:**
> Install and verify CLI package

**Persona:** developer

**Evidence:**
> Install the openshift-gitops-argocd-cli package

**Documentation Section:** Installing the OpenShift GitOps CLI on Linux using an RPM

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-linux-using-rpm.adoc`

---

### Install Job #17

**Type:** **User Story**

**Job Statement:**
> Navigate to OperatorHub and locate GitOps Operator

**Persona:** cluster administrator

**Evidence:**
> Open the Administrator perspective of the web console and go to Operators -> OperatorHub

**Documentation Section:** Installing OpenShift GitOps Operator in web console

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-in-web-console.adoc`

---

### Install Job #18

**Type:** **User Story**

**Job Statement:**
> Register system and enable GitOps repositories

**Persona:** developer

**Evidence:**
> Register with Red Hat Subscription Manager by running the following command

**Documentation Section:** Installing the OpenShift GitOps CLI on Linux using an RPM

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-linux-using-rpm.adoc`

---

### Install Job #19

**Type:** **User Story**

**Job Statement:**
> Subscribe namespace to GitOps Operator

**Persona:** cluster administrator

**Evidence:**
> Create a Subscription object YAML file to subscribe a namespace to the OpenShift GitOps Operator

**Documentation Section:** Installing OpenShift GitOps Operator using CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-using-cli.adoc`

---

### Install Job #20

**Type:** **User Story**

**Job Statement:**
> Verify CLI installation

**Persona:** developer

**Evidence:**
> After you install the GitOps argocd CLI, verify that it is available

**Documentation Section:** Installing the OpenShift GitOps CLI on Linux

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/gitops-installing-argocd-cli-on-linux.adoc`
  - Module: `modules/gitops-installing-argocd-cli-on-windows.adoc`
  - Module: `modules/gitops-installing-argocd-cli-on-macos.adoc`

---

### Install Job #21

**Type:** **User Story**

**Job Statement:**
> Verify GitOps pod deployment

**Persona:** cluster administrator

**Evidence:**
> After the installation is complete, verify that all the pods in the openshift-gitops namespace are running

**Documentation Section:** Installing OpenShift GitOps Operator using CLI

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/installing-gitops-operator-using-cli.adoc`

---

## Configure

**Category Description:** Set up or tune the product to behave the way I need.

**Total Jobs in Category:** 3

### Configure Job #1

**Type:** **Main Job**

**Job Statement:**
> When managing GitOps console components, I want to configure resource allocation for plugin and backend services, so I can control memory usage and ensure stable performance

**Persona:** Platform Administrator

**Context:** Managing OpenShift GitOps console plugin resource consumption

**Evidence:**
> You can configure CPU and memory resource requests and limits for the {gitops-shortname} console plugin and its backend cluster components

**Documentation Section:** Configure resource requests and limits for GitOps plugin components

**Source References:**
- Book: `managing_resource`
  - Module: `managing_resource`

---

### Configure Job #2

**Type:** **User Story**

**Job Statement:**
> When configuring GitOps plugin resources, I want to set specific requests and limits via GitOpsService CR, so I can address memory and performance issues in console components

**Persona:** Platform Administrator

**Context:** Configuring GitOps console plugin resource allocation

**Evidence:**
> To enable resource configuration for the {gitops-shortname} plugin components, specify the .spec.consolePlugin.backend.resources field for the backend component and the .spec.consolePlugin.gitopsPlugin.resources field

**Documentation Section:** Enabling the GitOpsService custom resource

**Source References:**
- Book: `managing_resource`
  - Module: `managing_resource`

---

### Configure Job #3

**Type:** **User Story**

**Job Statement:**
> When setting up a new Argo CD instance, I want to configure resource requests and limits for all workloads, so I can deploy in namespaces with resource quotas

**Persona:** Platform Administrator

**Context:** Initial Argo CD instance deployment in quota-restricted namespace

**Evidence:**
> You can create Argo CD custom resource workloads with resource requests and limits. This is required when you want to deploy the Argo CD instance in a namespace that is configured with resource quotas

**Documentation Section:** Configuring workloads with resource requests and limits

**Source References:**
- Book: `managing_resource`
  - Module: `managing_resource`

---

## Secure

**Category Description:** Protect my system and data, and meet security requirements.

**Total Jobs in Category:** 3

### Secure Job #1

**Type:** **User Story**

**Job Statement:**
> Authenticate with OpenShift credentials

**Persona:** cluster administrator

**Evidence:**
> To log in with your OpenShift Container Platform credentials, ensure you are a user of the cluster-admins group and then select the LOG IN VIA OPENSHIFT option

**Documentation Section:** Logging in to the Argo CD instance by using the Argo CD admin account

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/logging-in-to-the-argo-cd-instance-by-using-the-argo-cd-admin-account.adoc`

---

### Secure Job #2

**Type:** **User Story**

**Job Statement:**
> Authenticate with admin credentials

**Persona:** cluster administrator

**Evidence:**
> Use `admin` as the Username and the copied password as the Password to log in to the Argo CD UI

**Documentation Section:** Logging in to the Argo CD instance by using the Argo CD admin account

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/logging-in-to-the-argo-cd-instance-by-using-the-argo-cd-admin-account.adoc`

---

### Secure Job #3

**Type:** **User Story**

**Job Statement:**
> Navigate to Argo CD UI

**Persona:** cluster administrator

**Evidence:**
> Navigate to the menu -> OpenShift GitOps -> Cluster Argo CD. The login page of the Argo CD UI is displayed in a new window

**Documentation Section:** Logging in to the Argo CD instance by using the Argo CD admin account

**Source References:**
- Book: `installing_gitops`
  - Module: `modules/logging-in-to-the-argo-cd-instance-by-using-the-argo-cd-admin-account.adoc`

---

## Appendix

### CCS Category Framework

The following categories are prescribed by the Customer Communication Services (CCS) framework:

1. **Discover**: Understand whether this product solves my problem, what it can do, and how it conceptually works.
2. **Get started**: Quickly learn how to do something meaningful with the product after installation.
3. **Plan**: Design and size the right deployment for my environment before committing to installation.
4. **Install**: Set up the product so it's running in my environment.
5. **Upgrade**: Update the product without disrupting my environment.
6. **Migrate**: Shift my data, apps, or clusters to a different environment.
7. **Administer**: Keep the product healthy, secure, and performing well in production.
8. **Develop**: Create software or automation that uses this product's capabilities.
9. **Configure**: Set up or tune the product to behave the way I need.
10. **Secure**: Protect my system and data, and meet security requirements.
11. **Observe**: See what's happening in my system so I can understand or troubleshoot it.
12. **Integrate**: Make this product work with other products, cloud services, or enterprise systems.
13. **Troubleshoot**: Fix a problem so the system works again.
14. **Reference**: Look up exact details so I can configure or automate accurately.

### Recommended TOC Order

According to CCS guidelines, the following order is recommended:

**Fixed at Top:**
1. What's new
2. Discover
3. Get started
4. Plan

**Flexible Middle Section:**
- Install, Upgrade, Migrate, Administer, Develop, Configure, Secure, Observe, Integrate

**Fixed at Bottom:**
1. Troubleshoot
2. Reference
3. Download PDF
