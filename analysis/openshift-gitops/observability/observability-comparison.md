# OpenShift GitOps Observability — TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-05-05
**JTBD Records:** 17
**Main Jobs:** 8 (consolidated from 17 user stories)
**Coverage:** Standard schema (no research extensions)

---

## Current Structure (Feature-Based)

**Observability**
- **Logging**
  - Viewing Argo CD logs
    - Storing and retrieving Argo CD logs (procedure)
- **Monitoring**
  - Monitoring with GitOps dashboards
    - Accessing GitOps monitoring dashboards (procedure)
  - Monitoring Argo CD instances
    - Prerequisites
    - Monitoring Argo CD health using Prometheus metrics (procedure)
    - Disabling automatic scraping of metrics for Argo CD instances (procedure)
  - Monitoring the GitOps Operator performance
    - Accessing the GitOps Operator metrics (procedure)
  - Monitoring application health status
    - Settings for environment labels and annotations (reference)
    - Checking health information (procedure)
  - Monitoring Argo CD custom resource workloads
    - Prerequisites
    - Enabling Monitoring for Argo CD custom resource workloads (procedure)
    - Disabling Monitoring for Argo CD custom resource workloads (procedure)

**Total:** 2 top-level categories (Logging, Monitoring), 6 assemblies, 11+ procedures and reference sections, organized by monitoring target (logs, dashboards, instances, Operator, application health, custom resource workloads).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Configure Observability**
  - Job 4: Control Metric Collection to Manage Storage
  - Job 6: Configure Environment Labels for Developer Visibility
- **Observe System State**
  - Job 1: Access Argo CD Logs Through Centralized Logging
  - Job 7: Assess Application Resource Health and Deployment History
- **Track & Monitor**
  - Job 2: Observe GitOps Instance Behavior Through Graphical Dashboards
  - Job 3: Track Argo CD Application Health Status
  - Job 5: Understand GitOps Operator Performance Through Metrics
- **Enable Advanced Monitoring**
  - Job 8: Ensure Argo CD Component Workloads Are Monitored With Alerts

### Detailed Job Descriptions

#### Configure Observability

**Job 4: Control Metric Collection to Manage Storage**

*When metric scraping for multiple Argo CD instances causes excessive storage usage, I want to selectively disable metric collection, so I can control storage costs while maintaining visibility for critical instances.*

Prerequisites: Access to modify ArgoCD custom resources

- **4.1. Disable Automatic Metric Scraping** `[procedure]`
  - Lines 536-634 (Monitoring Argo CD instances): Set `spec.monitoring.disableMetrics` to `true` via YAML or CLI
  - Context: Operator deletes PrometheusRule, ServiceMonitors, and related resources when disabled
- **4.2. Re-enable Metrics When Needed** `[procedure]`
  - Set `spec.monitoring.disableMetrics` to `false` to restore monitoring

**Job 6: Configure Environment Labels for Developer Visibility**

*When you need to enable deployment tracking in the Developer perspective, I want to configure environment labels and annotations, so I can enable the Environments page to display sync status and deployment history.*

Prerequisites: GitOps Operator installed, Argo CD applications synchronized

- **6.1. Add Environment Labels to Application Manifest** `[concept]`
  - Lines 987-1030 (Monitoring application health status): Label and annotation requirements
  - Context: Requires `openshift.gitops/environment` label and matching namespace
- **6.2. Add VCS Annotations to Namespace Manifest** `[concept]`
  - VCS URI and ref annotations for Git commit tracking

#### Observe System State

**Job 1: Access Argo CD Logs Through Centralized Logging**

*When you need to troubleshoot Argo CD application behavior, I want to access and view Argo CD logs through a centralized logging system, so I can diagnose issues and understand system activity.*

Prerequisites: OpenShift GitOps Operator installed, Logging subsystem installed

- **1.1. Configure Kibana Index Pattern and Filters** `[procedure]`
  - Lines 138-183 (Viewing Argo CD logs): Kibana dashboard access, index pattern creation, namespace/pod filtering
  - Context: OpenShift Logging Operator automatically enables logging for Argo CD

**Job 7: Assess Application Resource Health and Deployment History**

*When you need to identify degraded resources and track deployment revisions, I want to view the Environments page in Developer perspective, so I can quickly identify degraded resources and track deployment revisions.*

Prerequisites: GitOps Operator installed, Applications synchronized, Environment labels configured

- **7.1. View Environment Status in Developer Perspective** `[procedure]`
  - Lines 1076-1100 (Monitoring application health status): Environments page navigation, icon interpretation, deployment history
  - Context: Visual indicators for degraded (broken heart) or delayed (yield sign) resource status

#### Track & Monitor

**Job 2: Observe GitOps Instance Behavior Through Graphical Dashboards**

*When you need to understand system health and performance trends across the cluster, I want to access graphical monitoring dashboards, so I can quickly understand system health and performance trends.*

Prerequisites: GitOps Operator installed in openshift-gitops-operator, Cluster monitoring enabled

- **2.1. Access GitOps Monitoring Dashboards** `[procedure]`
  - Lines 306-359 (Monitoring with GitOps dashboards): Four specialized dashboards (Overview, Components, gRPC Services, Rollouts)
  - Context: Dashboards auto-deployed by Operator, not customizable

**Job 3: Track Argo CD Application Health Status**

*When you need to detect out-of-sync applications and respond before issues escalate, I want to query Prometheus metrics, so I can detect out-of-sync applications and automated alerts.*

Prerequisites: Cluster admin access, GitOps Operator and Argo CD application installed

- **3.1. Query Prometheus Metrics for Health Status** `[procedure]`
  - Lines 482-528 (Monitoring Argo CD instances): PromQL query for `argocd_app_info` by health_status
  - Context: Operator automatically connects Argo CD to monitoring stack

**Job 5: Understand GitOps Operator Performance Through Metrics**

*When you need to diagnose slow reconciliations or scaling issues, I want to access Operator-specific metrics, so I can diagnose slow reconciliations or scaling issues.*

Prerequisites: GitOps Operator installed, Cluster monitoring enabled

- **5.1. Access Operator Performance Metrics** `[procedure]`
  - Lines 763-845 (Monitoring the GitOps Operator performance): Six Operator metrics (instances, reconciliation count/timing)
  - Context: Metrics auto-picked up by OpenShift monitoring stack

#### Enable Advanced Monitoring

**Job 8: Ensure Argo CD Component Workloads Are Monitored With Alerts**

*When you need to ensure Argo CD component workloads are running as expected, I want to enable workload monitoring with alerts, so I can detect replica drift before it impacts service availability.*

Prerequisites: Cluster admin access, GitOps installed, Monitoring stack configured, kube-state-metrics running

- **8.1. Enable Workload Monitoring for Argo CD Instance** `[procedure]`
  - Lines 1256-1323 (Monitoring Argo CD custom resource workloads): Set `spec.monitoring.enabled` to `true`
  - Context: Creates PrometheusRule with alerts for application-controller, repo-server, server workloads
- **8.2. Disable Workload Monitoring** `[procedure]`
  - Lines 1330-1357 (Monitoring Argo CD custom resource workloads): Set `spec.monitoring.enabled` to `false`
  - Context: Deletes PrometheusRule

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By monitoring target (logs, dashboards, instances, Operator, app health, workloads) | By user goal and workflow stage (Configure, Observe, Monitor) |
| **Top-level items** | 2 categories (Logging, Monitoring) + 6 assemblies | 4 lifecycle stages + 8 main jobs |
| **Logging** | Separate top-level category | Integrated into "Observe System State" stage |
| **Metric control** | Buried in "Monitoring Argo CD instances" | Elevated to dedicated job (Job 4) |
| **Developer workflows** | Mixed into monitoring sections | Grouped under Jobs 6 & 7 for developer persona |
| **Configuration vs Observation** | Mixed throughout | Clear separation: Jobs 4, 6 (Configure) vs Jobs 1, 7 (Observe) |
| **Navigation pattern** | Browse by monitoring target, then find relevant procedure | Navigate by goal (What do I want to accomplish?), then choose approach |

### Job List Adjustments from Suggested Input

The suggested 17 records were consolidated to **8 jobs** for the following reasons:

1. **Records for "Viewing Argo CD logs" and "Filtering logs in Kibana" merged** → Job 1 consolidates log access and filtering into one coherent workflow
2. **Records for "Accessing dashboards" and "Viewing metrics visually" merged** → Job 2 consolidates dashboard access
3. **Records for "Monitoring health" and "PromQL queries" merged** → Job 3 consolidates health tracking
4. **Records for "Disabling metrics" and "Setting disableMetrics flag" merged** → Job 4 consolidates metric control
5. **Records for "Operator performance" and "Accessing Operator metrics" merged** → Job 5 consolidates Operator monitoring
6. **Records for "Environment labels" and "Setting labels" merged** → Job 6 consolidates environment configuration
7. **Records for "Application health" and "Viewing Environments page" merged** → Job 7 consolidates developer health checks
8. **Records for "Workload monitoring", "Enabling monitoring", "Disabling monitoring" merged** → Job 8 consolidates workload alert configuration

---

## Hierarchy Levels Explanation

### Main Jobs (~8 jobs)
Stable, outcome-focused goals that would exist even if technology changes. Examples: "Access logs", "Track health status", "Control metric collection"

### User Stories (approaches)
Persona-specific or approach-specific implementation paths. Examples: "Configure Kibana filters" (UI approach), "Query Prometheus" (CLI approach)

### Procedures (reference)
Step-by-step instructions referenced by line numbers and source sections.

---

## Example: Content Consolidation

### Example 1: Metric Control (Fragmented → Unified)

**Current (Fragmented):**
- Section "Monitoring Argo CD instances" / "Disabling automatic scraping" (procedure buried in monitoring section)
- No visibility that metric control is a primary configuration concern

**Proposed (Consolidated):**
- **Job 4: Control Metric Collection to Manage Storage**
  - 4.1. Disable Automatic Metric Scraping (Lines 536-634)
  - 4.2. Re-enable Metrics When Needed

**Benefit:** Elevates metric control from a buried procedure to a first-class job, making storage management concerns visible to administrators.

---

### Example 2: Developer Workflows (Scattered → Grouped)

**Current (Fragmented):**
- Section "Monitoring application health status" / "Settings for environment labels" (reference material)
- Section "Monitoring application health status" / "Checking health information" (procedure)

**Proposed (Consolidated):**
- **Job 6: Configure Environment Labels for Developer Visibility** (Configure stage)
  - 6.1. Add Environment Labels
  - 6.2. Add VCS Annotations
- **Job 7: Assess Application Resource Health** (Observe stage)
  - 7.1. View Environment Status in Developer Perspective

**Benefit:** Clear workflow: configure labels first (Job 6), then observe health (Job 7). Persona-aligned for developers.

---

## Navigation Improvement Metrics

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 6 assemblies | 8 jobs grouped in 4 stages | 25% reduction + semantic grouping |
| Sections to browse for "log access" | 2 sections (Logging -> Viewing -> Storing) | 1 job, 1 approach | ~50% reduction |
| Sections to browse for "metric control" | 4 sections (Monitoring -> Instances -> Disabling) | 1 job, 2 approaches | ~50% reduction |
| Sections to browse for "developer health checks" | 3 sections (Monitoring -> App health -> Settings + Checking) | 2 jobs (Configure + Observe) | Clear prerequisite chain |
| Clicks to find "workload alerts" | 3 clicks (Monitoring -> Workloads -> Enabling) | 2 clicks (Advanced Monitoring -> Job 8) | ~33% reduction |

**Final job count: 8** (reduced from suggested 17 main/user_story records). Consolidation focused on grouping UI/CLI approaches, enable/disable toggles, and related procedures under coherent job goals.

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Configure | ⚠️ Scattered | ✅ Jobs 4, 6 | Improved |
| Observe | ✅ Logging, App health | ✅ Jobs 1, 7 | Reorganized |
| Monitor | ✅ All 5 monitoring assemblies | ✅ Jobs 2, 3, 5, 8 | Consolidated |
| Troubleshoot | ❌ Missing | ❌ Missing | Gap remains |
| Reference | ⚠️ Environment labels only | ✅ Metric types appendix | Improved |

### Coverage Summary

**Current structure gaps:** Troubleshooting content
**Proposed structure gaps:** Troubleshooting content
**Gaps addressed by restructure:** None (troubleshooting gap persists)

### Recommendations for Gap Closure

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Troubleshoot | Link to troubleshooting guide or add common issue resolution procedures | High |
| Log retention | Add procedure for configuring Kibana log retention | Medium |
| Custom alerts | Document how to create custom PrometheusRules beyond default workload alerts | Low |

---

## Success Criteria

A good JTBD-based structure should:

- User can immediately identify their goal (Configure, Observe, Monitor) without knowing GitOps internals
- User can distinguish between prerequisite configuration (Jobs 4, 6) and runtime observation (Jobs 1, 2, 3, 5, 7)
- User can find metric control (Job 4) without digging through monitoring procedures
- Developer workflows (Jobs 6, 7) are clearly separated from platform admin workflows (Jobs 1-5, 8)
- Content is simpler to navigate: 8 jobs vs 6 assemblies with scattered procedures
- Stakeholders understand the consolidation rationale: group by goal, not by monitoring target
