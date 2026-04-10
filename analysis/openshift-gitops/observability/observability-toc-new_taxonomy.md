# OpenShift GitOps Observability
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform teams to monitor, observe, and troubleshoot OpenShift GitOps instances and Argo CD applications using integrated observability tools.

**Personas:** Platform Administrator, SRE, Developer

**Main Jobs:** 7 core jobs across 3 workflow stages (Configure, Observe, Monitor)

---

## Quick Navigation

**I want to:**
- View Argo CD logs for troubleshooting -> Job 1 (Observe)
- Access GitOps dashboards for visual monitoring -> Job 2 (Monitor)
- Track Argo CD application health status -> Job 3 (Monitor)
- Control metric collection to manage storage -> Job 4 (Configure)
- Monitor GitOps Operator performance -> Job 5 (Monitor)
- Make my environments visible in Developer perspective -> Job 6 (Configure)
- Check application deployment health and history -> Job 7 (Observe)

---

# Table of Contents

## Configure Observability

### Job 4: Control Metric Collection to Manage Storage
*When metric scraping for multiple Argo CD instances causes excessive storage usage*

**Personas:** Platform Administrator
**Why:** Prevent storage exhaustion while maintaining visibility for critical instances

#### 4.1 Disable Automatic Metric Scraping `[procedure]`
→ Lines 536-634: Disabling automatic scraping of metrics for Argo CD instances
Source: Monitoring Argo CD instances

**Context:** By default, GitOps Operator scrapes metrics from all Argo CD instances. For large clusters with many instances, this can lead to excessive storage usage.

- **Task:** Set `spec.monitoring.disableMetrics` to `true` in ArgoCD CR
  - **UI Path:** Operators -> Installed Operators -> Red Hat OpenShift GitOps -> Argo CD -> YAML tab
  - **CLI Path:** `oc patch argocd <name> -n <namespace> --type='json' -p='[{"op": "replace", "path": "/spec/monitoring/disableMetrics", "value": true}]'`
  - Operator deletes PrometheusRule, ServiceMonitors, Roles, and RoleBindings
  - Operator adds `openshift.io/cluster-monitoring=false` label to namespace

#### 4.2 Re-enable Metrics When Needed `[procedure]`
- **Task:** Set `spec.monitoring.disableMetrics` to `false`
  - Operator recreates monitoring resources
  - Restores `openshift.io/cluster-monitoring=true` label

---

### Job 6: Configure Environment Labels for Developer Visibility
*When you need to enable deployment tracking in the Developer perspective*

**Personas:** Developer
**Why:** Makes application deployment status, sync health, and Git commit history visible to developers without CLI expertise

#### 6.1 Add Environment Labels to Application Manifest `[concept]`
→ Lines 987-1030: Settings for environment labels and annotations
Source: Monitoring application health status

**Context:** The Environments page in Developer perspective requires specific labels and annotations to display applications.

- **Required Application Label:**
  ```yaml
  spec:
    labels:
      openshift.gitops/environment: <environment_name>
    destination:
      namespace: <environment_name>
  ```
  - Environment name must match application name and destination namespace
  
#### 6.2 Add VCS Annotations to Namespace Manifest `[concept]`
- **Required Namespace Annotations:**
  ```yaml
  metadata:
    annotations:
      app.openshift.io/vcs-uri: <repository_url>
      app.openshift.io/vcs-ref: <branch_name>
  ```
  - Links deployments to Git commits for revision tracking

---

## Observe System State

### Job 1: Access Argo CD Logs Through Centralized Logging
*When you need to troubleshoot Argo CD application behavior*

**Personas:** Platform Administrator
**Requires:** OpenShift GitOps Operator installed, Logging subsystem installed with default configuration

#### 1.1 Configure Kibana Index Pattern and Filters `[procedure]`
→ Lines 138-183: Storing and retrieving Argo CD logs
Source: Viewing Argo CD logs

**Context:** OpenShift Logging Operator automatically enables logging for Argo CD. Use Kibana to filter and visualize logs.

- **Task:** Access Kibana dashboard
  - Red Hat applications menu -> Observability -> Logging
  
- **Task:** Create index pattern
  - Define as `*` to display all indices
  - Set Time Filter field: `@timestamp`
  
- **Task:** Create namespace filter
  - Field: `kubernetes.namespace_name`
  - Operator: `is`
  - Value: `openshift-gitops` (or your target namespace)
  
- **Task:** Optional - Add pod-specific filter
  - Field: `kubernetes.pod_name`
  - Filter to specific pod name

---

### Job 7: Assess Application Resource Health and Deployment History
*When you need to identify degraded resources and track deployment revisions*

**Personas:** Developer
**Requires:** GitOps Operator installed, Applications synchronized by Argo CD, Environment labels configured

#### 7.1 View Environment Status in Developer Perspective `[procedure]`
→ Lines 1076-1100: Checking health information
Source: Monitoring application health status

**Context:** The Environments page consolidates deployment status, resource health, and Git commit history in one view.

- **Task:** Navigate to Environments page
  - Developer perspective -> Environments
  
- **Task:** Check environment status icons
  - Hover over icons to see sync status
  
- **Task:** View application details
  - Click application name to open Application environments page
  
- **Task:** Interpret resource health icons
  - **Broken heart:** Resource issues have degraded performance
  - **Yellow yield sign:** Resource issues have delayed health data
  
- **Task:** View deployment history
  - Click Deployment History tab
  - See: Last deployment, commit message, environment, author, revision

---

## Track & Monitor

### Job 2: Observe GitOps Instance Behavior Through Graphical Dashboards
*When you need to understand system health and performance trends across the cluster*

**Personas:** Platform Administrator
**Requires:** GitOps Operator installed in `openshift-gitops-operator`, Cluster monitoring enabled, Argo CD application installed

#### 2.1 Access GitOps Monitoring Dashboards `[procedure]`
→ Lines 306-359: Monitoring with GitOps dashboards and accessing dashboards
Source: Monitoring with GitOps dashboards

**Context:** Four specialized dashboards provide different views into GitOps performance. Dashboards are auto-deployed by Operator and cannot be customized.

- **Available Dashboards:**
  - **GitOps Overview:** All instances, application count, health/sync status, activity
  - **GitOps Components:** CPU/memory for application-controller, repo-server, server
  - **GitOps gRPC Services:** gRPC service activity between components
  - **GitOps Rollouts:** Active Rollouts, replica status, controller performance
  
- **Task:** Access dashboards
  - **UI Path:** Administrator perspective -> Observe -> Dashboards
  - Select desired dashboard from dropdown
  - Optional: Filter by namespace, cluster, interval

---

### Job 3: Track Argo CD Application Health Status
*When you need to detect out-of-sync applications and respond before issues escalate*

**Personas:** SRE
**Requires:** Cluster admin access, GitOps Operator and Argo CD application installed

#### 3.1 Query Prometheus Metrics for Health Status `[procedure]`
→ Lines 482-528: Monitoring Argo CD health using Prometheus metrics
Source: Monitoring Argo CD instances

**Context:** GitOps Operator automatically connects Argo CD to monitoring stack and provides alerts for out-of-sync applications.

- **Task:** Run health status query
  - **UI Path:** Developer perspective -> Observe -> Metrics -> Custom query
  - **Example PromQL:**
    ```
    sum(argocd_app_info{dest_namespace=~"<your_namespace>",health_status!=""}) by (health_status)
    ```
  - Replace `<your_namespace>` with target namespace (e.g., `openshift-gitops`)

---

### Job 5: Understand GitOps Operator Performance Through Metrics
*When you need to diagnose slow reconciliations or scaling issues*

**Personas:** Platform Administrator
**Requires:** GitOps Operator installed in `openshift-gitops-operator`, Cluster monitoring enabled

#### 5.1 Access Operator Performance Metrics `[procedure]`
→ Lines 763-845: Monitoring the GitOps Operator performance
Source: Monitoring the GitOps Operator performance

**Context:** Operator emits six metrics about active instances, reconciliation behavior, and timing. OpenShift monitoring stack automatically picks them up.

- **Available Metrics:**
  - `active_argocd_instances_total` (Gauge): Total active instances managed
  - `active_argocd_instances_by_phase` (Gauge): Instances by phase (pending, available)
  - `active_argocd_instance_reconciliation_count` (Counter): Total reconciliations per instance
  - `controller_runtime_reconcile_time_seconds_per_instance_bucket` (Counter): Reconciliations by duration
  - `controller_runtime_reconcile_time_seconds_per_instance_count` (Counter): Total observed reconciliations
  - `controller_runtime_reconcile_time_seconds_per_instance_sum` (Counter): Total time for reconciliations

- **Task:** Query metrics
  - **UI Path:** Administrator perspective -> Observe -> Metrics
  - Enter metric name in Expression field
  - Optional: Filter by properties (e.g., `active_argocd_instances_by_phase{phase="Available"}`)
  - Click Run queries

---

## Enable Advanced Monitoring

### Job 8: Ensure Argo CD Component Workloads Are Monitored With Alerts
*When you need to detect replica drift before it impacts service availability*

**Personas:** SRE
**Requires:** Cluster admin access, GitOps installed, Monitoring stack configured, `kube-state-metrics` running

#### 8.1 Enable Workload Monitoring for Argo CD Instance `[procedure]`
→ Lines 1256-1323: Enabling Monitoring for Argo CD custom resource workloads
Source: Monitoring Argo CD custom resource workloads

**Context:** Creates PrometheusRule with alert rules for application-controller, repo-server, and server workloads. Alerts fire when ready replicas ≠ desired replicas.

- **Task:** Set `spec.monitoring.enabled` to `true`
  - **Example ArgoCD CR:**
    ```yaml
    apiVersion: argoproj.io/v1beta1
    kind: ArgoCD
    metadata:
      name: example-argocd
    spec:
      monitoring:
        enabled: true
    ```
  - Operator creates PrometheusRule named `argocd-component-status-alert`
  - Alert example: `ApplicationSetControllerNotReady` fires when replica drift persists >1 minute

- **Note:** User workload monitoring must be enabled for Argo CD instances in non-`openshift-*` namespaces

#### 8.2 Disable Workload Monitoring `[procedure]`
→ Lines 1330-1357: Disabling Monitoring for Argo CD custom resource workloads
Source: Monitoring Argo CD custom resource workloads

- **Task:** Set `spec.monitoring.enabled` to `false`
  - Deletes created PrometheusRule
  - Removes workload monitoring alerts

---

## Appendices

### A. Metric Types Reference

| Type | Behavior | Examples |
|------|----------|----------|
| **Gauge** | Value can increase or decrease | active_argocd_instances_total |
| **Counter** | Value can only increase | active_argocd_instance_reconciliation_count |

### B. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Configure | ✅ | Jobs 4, 6 | Metric control, environment labels |
| Observe | ✅ | Jobs 1, 7 | Logs, deployment health |
| Monitor | ✅ | Jobs 2, 3, 5 | Dashboards, health, Operator metrics |
| Advanced Monitoring | ✅ | Job 8 | Workload-level alerts |
| Troubleshoot | ❌ | - | No troubleshooting procedures |

### C. Gaps Identified

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| No troubleshooting content | Link to troubleshooting guide or add common issue resolutions | High |
| No log retention configuration | Add procedure for configuring Kibana log retention | Medium |
| No custom alert configuration | Document how to create custom PrometheusRules | Low |

---

## Navigation Guide

### By User Journey

**Platform Administrator setting up observability:**
1. Job 4: Control metric collection (if managing storage)
2. Job 2: Access GitOps dashboards for visual monitoring
3. Job 5: Monitor Operator performance
4. Job 1: Access Argo CD logs when troubleshooting

**SRE monitoring production GitOps:**
1. Job 3: Track application health status via Prometheus
2. Job 8: Enable workload monitoring with alerts
3. Job 1: Access logs when investigating incidents

**Developer tracking application deployments:**
1. Job 6: Configure environment labels for visibility
2. Job 7: Check application health and deployment history

---

## Document Statistics

**Workflow Coverage:**
- Configure: 2 jobs
- Observe: 2 jobs
- Monitor: 3 jobs
- Advanced Monitoring: 1 job

**Main Jobs:** 8
**User Stories/Approaches:** 13
**Source Sections:** 6 assemblies (1 logging, 5 monitoring)
**Platform Variations:** Kibana vs Prometheus approaches, UI vs CLI methods
