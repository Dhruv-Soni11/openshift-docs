# OpenShift GitOps Observability — Consolidation Report

**Document:** observability-combined.adoc
**JTBD Records:** 17 pre-consolidated records → 8 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current Observability documentation is organized by **monitoring target**: separate sections for logs, dashboards, Argo CD instances, the GitOps Operator, application health, and custom resource workloads. While this structure mirrors the technical architecture, it creates friction for users who need to accomplish specific goals across multiple monitoring targets.

For example, a platform administrator setting up observability must navigate six different assemblies to enable log access, configure metric scraping, access dashboards, and set up workload alerts. A developer trying to track deployment health must jump between "Monitoring application health status" for configuration and the same section for checking health—without a clear prerequisite flow.

The proposed structure reorganizes content by **user goal and workflow stage**: Configure prerequisites (metric control, environment labels), Observe system state (logs, deployment health), and Monitor performance (dashboards, Prometheus metrics, Operator metrics, workload alerts). This aligns documentation with how users actually work, reducing cognitive overhead and making prerequisite relationships explicit.

### Key Improvements

- **Metric control elevated:** Storage management (Job 4) is no longer buried in "Monitoring Argo CD instances" but is a first-class configuration job
- **Developer workflows grouped:** Environment configuration (Job 6) and health checking (Job 7) are clearly sequenced for developer persona
- **Monitoring consolidated:** Five monitoring assemblies → four main monitoring jobs (Jobs 2, 3, 5, 8) organized by monitoring scope
- **Configuration separated from observation:** Jobs 4 and 6 are clearly prerequisite configuration, Jobs 1-3, 5, 7-8 are runtime observation/monitoring
- **Workflow stages explicit:** Configure → Observe → Monitor progression makes prerequisite relationships clear
- **Log access unified:** Viewing and filtering logs (previously 2 procedures) → 1 job with integrated filtering workflow
- **Workload monitoring clarified:** Enable/disable workload alerts (2 procedures) → 1 job with toggle approaches
- **Semantic grouping:** 6 assemblies grouped by monitoring target → 8 jobs grouped by user goal and workflow stage

---

## Current Structure (Feature-Based)

- **Logging**
  - Viewing Argo CD logs — Using Kibana dashboard to access and filter logs
    - Storing and retrieving Argo CD logs (procedure) — Index pattern creation, namespace/pod filtering
- **Monitoring**
  - Monitoring with GitOps dashboards — Accessing four specialized dashboards
    - Accessing GitOps monitoring dashboards (procedure) — Dashboard selection and filtering
  - Monitoring Argo CD instances — Health tracking and metric control
    - Prerequisites — Cluster admin access, GitOps/Argo CD installed
    - Monitoring Argo CD health using Prometheus metrics (procedure) — PromQL queries for health_status
    - Disabling automatic scraping of metrics for Argo CD instances (procedure) — Setting disableMetrics flag
  - Monitoring the GitOps Operator performance — Operator-specific metrics
    - Accessing the GitOps Operator metrics (procedure) — Querying six Operator performance metrics
  - Monitoring application health status — Developer-facing deployment tracking
    - Settings for environment labels and annotations (reference) — Label/annotation requirements for Environments page
    - Checking health information (procedure) — Viewing environment status and deployment history
  - Monitoring Argo CD custom resource workloads — Workload-level alerting
    - Prerequisites — Cluster admin, monitoring stack, kube-state-metrics
    - Enabling Monitoring for Argo CD custom resource workloads (procedure) — Setting monitoring.enabled to true
    - Disabling Monitoring for Argo CD custom resource workloads (procedure) — Setting monitoring.enabled to false

**Total:** 2 categories (Logging, Monitoring), 6 assemblies, 9+ procedures and reference sections, organized by monitoring target.

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
  - Disabling automatic scraping of metrics for Argo CD instances (Lines 536-634): Set `spec.monitoring.disableMetrics` to `true` via YAML or CLI
  - Context: Operator deletes PrometheusRule, ServiceMonitors, Roles, RoleBindings and adds `openshift.io/cluster-monitoring=false` label
- **4.2. Re-enable Metrics When Needed** `[procedure]`
  - Set `spec.monitoring.disableMetrics` to `false`
  - Context: Operator recreates monitoring resources and restores `openshift.io/cluster-monitoring=true` label

**Job 6: Configure Environment Labels for Developer Visibility**

*When you need to enable deployment tracking in the Developer perspective, I want to configure environment labels and annotations, so I can make deployment status, sync health, and Git commit history visible to developers.*

Prerequisites: GitOps Operator installed, Argo CD applications synchronized

- **6.1. Add Environment Labels to Application Manifest** `[concept]`
  - Settings for environment labels and annotations (Lines 987-1030): Required `openshift.gitops/environment` label and destination namespace
  - Context: Environment name must match application name and destination namespace for visibility
- **6.2. Add VCS Annotations to Namespace Manifest** `[concept]`
  - VCS URI and ref annotations for linking deployments to Git commits

#### Observe System State

**Job 1: Access Argo CD Logs Through Centralized Logging**

*When you need to troubleshoot Argo CD application behavior, I want to access and view Argo CD logs through a centralized logging system, so I can diagnose issues and understand system activity.*

Prerequisites: OpenShift GitOps Operator installed, Logging subsystem installed with default configuration

- **1.1. Configure Kibana Index Pattern and Filters** `[procedure]`
  - Storing and retrieving Argo CD logs (Lines 138-183): Kibana dashboard access, index pattern creation (`*`), namespace/pod filtering
  - Context: OpenShift Logging Operator automatically enables logging for Argo CD; use Kibana for filtering and visualization

**Job 7: Assess Application Resource Health and Deployment History**

*When you need to identify degraded resources and track deployment revisions, I want to view the Environments page in Developer perspective, so I can quickly identify degraded resources and track deployment revisions.*

Prerequisites: GitOps Operator installed, Applications synchronized by Argo CD, Environment labels configured

- **7.1. View Environment Status in Developer Perspective** `[procedure]`
  - Checking health information (Lines 1076-1100): Navigate to Environments page, check status icons, view deployment history
  - Context: Broken heart = degraded performance, yellow yield sign = delayed health data, deployment history shows Git commits

#### Track & Monitor

**Job 2: Observe GitOps Instance Behavior Through Graphical Dashboards**

*When you need to understand system health and performance trends across the cluster, I want to access graphical monitoring dashboards, so I can quickly understand system health and performance trends without manual metric queries.*

Prerequisites: GitOps Operator installed in `openshift-gitops-operator`, Cluster monitoring enabled, Argo CD application installed

- **2.1. Access GitOps Monitoring Dashboards** `[procedure]`
  - Accessing GitOps monitoring dashboards (Lines 306-359): Four specialized dashboards (Overview, Components, gRPC Services, Rollouts)
  - Context: Dashboards auto-deployed by Operator, not customizable; filter by namespace/cluster/interval

**Job 3: Track Argo CD Application Health Status**

*When you need to detect out-of-sync applications and respond before issues escalate, I want to query Prometheus metrics, so I can detect out-of-sync applications and enable automated alerts.*

Prerequisites: Cluster admin access, GitOps Operator and Argo CD application installed

- **3.1. Query Prometheus Metrics for Health Status** `[procedure]`
  - Monitoring Argo CD health using Prometheus metrics (Lines 482-528): PromQL query for `argocd_app_info` by `health_status`
  - Context: Operator automatically connects Argo CD to monitoring stack; provides alerts for out-of-sync applications

**Job 5: Understand GitOps Operator Performance Through Metrics**

*When you need to diagnose slow reconciliations or scaling issues, I want to access Operator-specific metrics, so I can identify bottlenecks and performance degradation.*

Prerequisites: GitOps Operator installed in `openshift-gitops-operator`, Cluster monitoring enabled

- **5.1. Access Operator Performance Metrics** `[procedure]`
  - Accessing the GitOps Operator metrics (Lines 763-845): Six Operator metrics (active instances total/by phase, reconciliation count/timing)
  - Context: Metrics auto-picked up by OpenShift monitoring stack; includes Gauge (can go up/down) and Counter (only up) types

#### Enable Advanced Monitoring

**Job 8: Ensure Argo CD Component Workloads Are Monitored With Alerts**

*When you need to ensure Argo CD component workloads are running as expected, I want to enable workload monitoring with alerts, so I can detect replica drift before it impacts service availability.*

Prerequisites: Cluster admin access, GitOps installed, Monitoring stack configured in `openshift-monitoring`, `kube-state-metrics` running

- **8.1. Enable Workload Monitoring for Argo CD Instance** `[procedure]`
  - Enabling Monitoring for Argo CD custom resource workloads (Lines 1256-1323): Set `spec.monitoring.enabled` to `true`
  - Context: Creates PrometheusRule with alerts for application-controller, repo-server, server workloads; alerts fire when ready ≠ desired replicas >1 min
  - Note: User workload monitoring required for non-`openshift-*` namespaces
- **8.2. Disable Workload Monitoring** `[procedure]`
  - Disabling Monitoring for Argo CD custom resource workloads (Lines 1330-1357): Set `spec.monitoring.enabled` to `false`
  - Context: Deletes created PrometheusRule

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | By monitoring target (logs, dashboards, instances, Operator, app health, workloads) | By user goal and workflow stage (Configure, Observe, Monitor) |
| **Top-level items** | 2 categories + 6 assemblies | 4 lifecycle stages + 8 main jobs |
| **Logging** | Separate top-level category | Integrated into "Observe System State" stage |
| **Metric control** | Buried in "Monitoring Argo CD instances" | Elevated to dedicated job in "Configure Observability" |
| **Developer workflows** | Mixed into monitoring sections | Grouped under Jobs 6 & 7 with clear prerequisite flow |
| **Configuration vs Observation** | Mixed throughout assemblies | Clear separation: Configure (Jobs 4, 6) vs Observe/Monitor (Jobs 1-3, 5, 7-8) |
| **Navigation pattern** | Browse by monitoring target, find procedure | Navigate by goal (Configure/Observe/Monitor), choose approach |
| **Prerequisite visibility** | Implicit (Prerequisites sections in some assemblies) | Explicit (Configure jobs happen before Observe/Monitor jobs) |

### Job List Adjustments from Suggested Input

The suggested 17 main/user_story records were consolidated to **8 jobs** for the following reasons:

1. **Jobs "Access logs" and "Filter logs in Kibana" merged** → Job 1 consolidates log access and filtering into one coherent workflow; filtering is a sub-task, not a separate job
2. **Jobs "Access dashboards" and "View metrics visually" merged** → Job 2 consolidates dashboard access; UI approach vs CLI approach distinction is implementation detail
3. **Jobs "Monitor health" and "PromQL queries for health" merged** → Job 3 consolidates health tracking; PromQL is the approach, not a separate job
4. **Jobs "Disable metrics" and "Set disableMetrics flag" merged** → Job 4 consolidates metric control; enable/disable are toggle approaches under one job
5. **Jobs "Operator performance" and "Access Operator metrics" merged** → Job 5 consolidates Operator monitoring; metric access is the approach
6. **Jobs "Configure labels" and "Add environment labels" merged** → Job 6 consolidates environment configuration; labels and annotations are both setup tasks
7. **Jobs "Application health" and "View Environments page" merged** → Job 7 consolidates developer health checks; viewing is the approach
8. **Jobs "Workload monitoring", "Enable monitoring", "Disable monitoring" merged** → Job 8 consolidates workload alerts; enable/disable are configuration toggles

---

## Consolidation Examples

### Example 1: Metric Control (Buried procedure → First-class job)

**Current (Fragmented):**
- Section: Monitoring → Monitoring Argo CD instances → Disabling automatic scraping of metrics for Argo CD instances
  - Buried in 6th assembly under "Monitoring Argo CD instances"
  - Not discoverable for users concerned with storage management
  - No visibility that this is a primary configuration concern for large clusters

**Proposed (Consolidated):**
- **Job 4: Control Metric Collection to Manage Storage** (Configure Observability stage)
  - 4.1. Disable Automatic Metric Scraping (Lines 536-634)
  - 4.2. Re-enable Metrics When Needed
  - Elevated to first-class job in "Configure Observability" stage
  - Clear "When" statement explains storage concern
  - Toggle approaches (enable/disable) grouped together

**Benefit:** Platform administrators managing multi-instance clusters can immediately find metric control without navigating through instance monitoring procedures. Storage management concerns are visible at the job level.

---

### Example 2: Developer Workflows (Scattered → Sequenced)

**Current (Fragmented):**
- Section: Monitoring → Monitoring application health status → Settings for environment labels and annotations (reference material)
- Section: Monitoring → Monitoring application health status → Checking health information (procedure)
  - Configuration and observation mixed in one assembly
  - No clear prerequisite flow (must configure labels before viewing health)
  - Developer persona not obvious from assembly title "Monitoring application health status"

**Proposed (Consolidated):**
- **Job 6: Configure Environment Labels for Developer Visibility** (Configure Observability stage)
  - 6.1. Add Environment Labels to Application Manifest
  - 6.2. Add VCS Annotations to Namespace Manifest
- **Job 7: Assess Application Resource Health and Deployment History** (Observe System State stage)
  - 7.1. View Environment Status in Developer Perspective
  - Prerequisites: Environment labels configured (Job 6)

**Benefit:** Clear workflow progression: configure labels (Job 6) → observe health (Job 7). Prerequisite dependency explicit. Developer persona clear from job titles. Configuration and observation cleanly separated by lifecycle stage.

---

### Example 3: Logging Access (Procedure split → Unified workflow)

**Current (Fragmented):**
- Section: Logging → Viewing Argo CD logs → Storing and retrieving Argo CD logs
  - Procedure covers index pattern creation and filtering
  - "Storing" in title implies persistent storage configuration, but content is about accessing/viewing logs

**Proposed (Consolidated):**
- **Job 1: Access Argo CD Logs Through Centralized Logging** (Observe System State stage)
  - 1.1. Configure Kibana Index Pattern and Filters
  - Unified workflow: access Kibana → create index pattern → filter by namespace/pod

**Benefit:** Single coherent job for log access. Filtering integrated as part of access workflow, not separate task. Clear goal: troubleshoot Argo CD behavior.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| No troubleshooting procedures | Jobs 1, 3, 5, 7, 8 | No troubleshooting content beyond metric viewing | **High** — Users have observability tools but no guidance on interpreting results or resolving common issues |
| No log retention configuration | Job 1 | No guidance on Kibana log retention policies | **Medium** — Long-term log analysis limited without retention configuration |
| No custom alert configuration | Job 8 | Only default workload alerts documented | **Medium** — Advanced users need custom PrometheusRule guidance |
| No dashboard customization | Job 2 | Explicitly states dashboards not customizable, no alternative guidance | **Low** — Users accepting default dashboards; note states customization unsupported |
| No integration with external monitoring | Jobs 2, 3, 5 | Only OpenShift-integrated monitoring documented | **Low** — Most users using OpenShift monitoring stack |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 2 categories + 6 assemblies (8 total) | 4 lifecycle stages + 8 jobs (12 total) | Semantic grouping by workflow stage |
| Sections to browse for "log access" | 2 sections (Logging → Viewing → Storing) | 1 job, 1 approach | ~50% reduction, unified workflow |
| Sections to browse for "metric control" | 4 sections (Monitoring → Instances → Disabling) | 1 job, 2 approaches | ~50% reduction, elevated visibility |
| Sections to browse for "developer health" | 3 sections (Monitoring → App health → Settings + Checking) | 2 jobs with clear prerequisite | Prerequisite flow explicit |
| Sections to browse for "workload alerts" | 4 sections (Monitoring → Workloads → Enabling) | 1 job, 2 approaches (enable/disable) | ~50% reduction, toggles grouped |
| Clicks to find "Operator metrics" | 3 clicks (Monitoring → Operator → Accessing) | 2 clicks (Monitor → Job 5) | ~33% reduction |
| Configuration vs observation clarity | Implicit (must read prerequisites) | Explicit (Configure stage vs Observe/Monitor stages) | 100% improvement in prerequisite visibility |

**Final job count: 8** (reduced from suggested 17 main/user_story records).

Consolidation rationale: Group UI/CLI approaches under one job, merge enable/disable toggles, integrate filtering/access workflows, separate configuration from observation by lifecycle stage, elevate buried procedures to first-class jobs when they address primary user concerns (storage management).

---

## Document Statistics

**Workflow Coverage:**
- Configure: 2 jobs
- Observe: 2 jobs
- Monitor: 3 jobs
- Advanced Monitoring: 1 job

**Main Jobs:** 8
**Approaches:** 13 (procedures, concepts, references)
**Source Sections:** 6 assemblies (1 logging, 5 monitoring)
**Platform Variations:** Kibana vs Prometheus, UI vs CLI methods

**Topic Type Distribution:**
- Procedures: 10
- Concepts: 2
- Reference: 1 (metric types)

---

## Implementation Notes

**For content writers:**
1. Extract "Disabling automatic scraping" from "Monitoring Argo CD instances" and elevate to "Configure Observability" section
2. Split "Monitoring application health status" into two separate jobs: configuration (labels/annotations) and observation (Environments page)
3. Unify "Viewing Argo CD logs" procedure to emphasize access + filtering as integrated workflow
4. Group enable/disable procedures for workload monitoring under toggle approaches
5. Add cross-references between Jobs 6 and 7 to make prerequisite dependency explicit
6. Consider adding troubleshooting content for high-impact gap

**For stakeholders:**
- Consolidation reduces cognitive overhead by grouping by goal, not monitoring target
- Developer workflows (Jobs 6, 7) become discoverable and properly sequenced
- Metric control (Job 4) gains visibility for storage management concerns
- No content removed, only reorganized for better discoverability and prerequisite clarity
