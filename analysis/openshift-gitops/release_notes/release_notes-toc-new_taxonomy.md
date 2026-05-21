# OpenShift GitOps Release Notes 1.20
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and information needs*

---

## Guide Overview

**Purpose:** Help users understand what's new, what's fixed, version compatibility, and plan upgrades for OpenShift GitOps 1.20.x releases.

**Personas:** Platform administrator, Security administrator, SRE

**Main Jobs:** 9 core information needs across planning, configuration, upgrade, and troubleshooting stages

---

## Quick Navigation

**I want to:**
- Check version compatibility → Job 1 (Plan)
- See new features in 1.20.0 → Jobs 4-8 (Configure, Deploy, Monitor, Secure, Operate)
- Find fixed issues → Jobs 2, 9 (Troubleshoot, Upgrade)
- Understand Technology Preview status → Job 1 (Plan)
- Plan upgrade from 1.19.x → Jobs 1, 3 (Plan, Upgrade)

---

# Table of Contents

## Understand Compatibility and Support

### Job 1: Understand Version Compatibility
*When planning an OpenShift GitOps deployment or upgrade*

**Personas:** Platform administrator

#### Check Supported Versions

→ Lines 151-183: Compatibility and support matrix
  Source: Section "Compatibility and support matrix"
  - OpenShift GitOps 1.20.0, 1.19.0, 1.18.0 component versions
  - Supported OpenShift Container Platform versions (4.14, 4.16-4.21)
  - Argo CD, Argo Rollouts, Dex, Helm, Kustomize versions
  - Important deprecations (Keycloak-based authentication removed in 1.18+)

#### Understand Technology Preview Feature Status

→ Lines 186-240: Technology Preview features
  Source: Section "Technology Preview features"
  - Features in Technology Preview (TP): argocd CLI tool, ApplicationSets in non-control plane namespaces, round-robin sharding, dynamic sharding, ApplicationSet Progressive Sync Strategy
  - Features graduated to GA: Argo CD Agent (1.19.0), Argo Rollouts (1.13.0), Multiple sources (1.15.0), Applications in non-control plane namespaces (1.13.0)
  - Permanent TP features (no GA planned): argocd CLI tool, ApplicationSets in non-control plane namespaces, round-robin sharding, dynamic sharding, ApplicationSet Progressive Sync Strategy

**Related:** Job 3 (Plan upgrade path), Job 2 (Assess production readiness)

---

## Discover Fixed Issues

### Job 2: Discover Issue Resolutions
*When encountering problems or deciding whether to upgrade*

**Personas:** Platform administrator, SRE

#### 1.20.1 Fixed Issues

→ Lines 277-280: Prevent unintended AppProjects deletion during resync
  Source: Release notes 1.20.1 - Fixed issues
  - **Issue:** AppProjects managed by autonomous agents could be deleted during resync when destination names didn't match agent name
  - **Resolution:** Reconciliation logic now preserves AppProjects during resync and restarts
  - **Jira:** GITOPS-9200

#### 1.20.0 Fixed Issues - Console Plugin

→ Lines 433-436: Fixed console plugin Applications page rendering error
  Source: Release notes 1.20.0 - Fixed issues
  - **Issue:** Applications page crashed with JavaScript error for invalid/ill-formed Applications
  - **Resolution:** Plugin gracefully handles malformed application data
  - **Jira:** GITOPS-8773

#### 1.20.0 Fixed Issues - Upgrade Correctness

→ Lines 438-441: Fixed incorrect ownerReferences apiVersion in config maps
  Source: Release notes 1.20.0 - Fixed issues
  - **Issue:** ownerReferences used v1alpha1 even after Argo CD CR upgraded to v1beta1
  - **Resolution:** ownerReferences updated during upgrade to match correct apiVersion
  - **Jira:** GITOPS-8001

#### 1.20.0 Fixed Issues - UI Observability

→ Lines 443-446: Fixed Progressive Sync status display in UI
  Source: Release notes 1.20.0 - Fixed issues
  - **Issue:** ApplicationSet-generated apps showed "Unknown" for Progressive Sync status
  - **Resolution:** UI displays correct Progressive Sync state; hides field when disabled
  - **Jira:** GITOPS-7797

→ Lines 448-451: Fixed incorrect application links across Argo CD instances
  Source: Release notes 1.20.0 - Fixed issues
  - **Issue:** Cluster-scoped Argo CD UI generated wrong links to namespaced instance applications
  - **Resolution:** UI generates correct links for applications managed by different instances
  - **Jira:** GITOPS-1505

#### 1.20.0 Fixed Issues - Image Updater (Technology Preview)

→ Lines 453-465: Enhanced security for Image Updater application references
  Source: Release notes 1.20.0 - Fixed issues
  - **Issue:** Users could reference applications across namespaces, bypassing AppProject restrictions
  - **Resolution:** Image Updater enforces namespace boundaries and AppProject configurations
  - **Jira:** GITOPS-8876
  - **Status:** Technology Preview feature

→ Lines 467-479: Fixed Image Updater Git process exhaustion
  Source: Release notes 1.20.0 - Fixed issues
  - **Issue:** Image Updater accumulated thousands of Git processes when retrieving tokens
  - **Resolution:** Image Updater properly releases Git processes after use
  - **Jira:** GITOPS-8875
  - **Status:** Technology Preview feature

**Related:** Job 3 (Plan upgrade to resolve issues)

---

## Plan Upgrade Path

### Job 3: Plan Upgrade from Previous Versions
*When considering upgrade to OpenShift GitOps 1.20.x*

**Personas:** Platform administrator

**Timing:** Review compatibility (Job 1) and fixed issues (Job 2) BEFORE planning upgrade

#### Understand Image Naming Changes

→ Lines 420-423: Operator base image migration to UBI 9 Minimal
  Source: Release notes 1.20.0 - New features
  - **Change:** Operator and operand images migrated from UBI 8 to UBI 9 Minimal
  - **Impact:** Image suffix changes from `rhel8` to `rhel9`
  - **Action Required:** Update external automation or scripts referencing operator images
  - **Benefit:** Reduced CVE exposure, improved security posture
  - **Jira:** GITOPS-8107

#### Review Errata Advisories

→ Lines 260-272: OpenShift GitOps 1.20.1 errata updates
  Source: Release notes 1.20.1 - Errata updates
  - Advisory: RHEA-2026:6378 (issued 2026-04-01)
  - View container images: `oc describe deployment gitops-operator-controller-manager -n openshift-gitops-operator`

→ Lines 299-311: OpenShift GitOps 1.20.0 errata updates
  Source: Release notes 1.20.0 - Errata updates
  - Advisory: RHEA-2026:5819 (issued 2026-03-25)
  - View container images: `oc describe deployment gitops-operator-controller-manager -n openshift-gitops-operator`

**Related:** Job 1 (Check version compatibility), Job 2 (Review fixed issues)

---

## Configure New Authentication Features

### Job 4: Configure Argo CD Authentication for External Authentication Environments
*When external authentication is enabled on OpenShift 4.20+*

**Personas:** Platform administrator

**Why:** External authentication changes how Argo CD login is configured

#### Configure External OIDC Provider

→ Lines 316-319: Changes to Argo CD authentication with external authentication enabled
  Source: Release notes 1.20.0 - New features
  - **Behavior Change:** When external authentication is enabled in OCP 4.20+, GitOps Operator no longer configures OpenShift OAuth for Argo CD
  - **Action Required:** Configure external identity provider via `.spec.oidc` field in ArgoCD CR
  - **Example Provider:** Red Hat Build of Keycloak (RHBK)
  - **Fallback:** If external authentication not enabled, GitOps continues using Dex with OpenShift OAuth
  - **Jira:** GITOPS-8017

**Related:** Configuring SSO for Argo CD using external OIDC providers (see Additional Resources in source)

---

## Configure Namespace and Application Management

### Job 5: Configure ApplicationSet Source Namespaces
*When managing ApplicationSets across many namespaces*

**Personas:** Platform administrator

#### Use Wildcard Patterns for Dynamic Namespace Support

→ Lines 321-324: Enhanced wildcard support for ApplicationSet source namespaces
  Source: Release notes 1.20.0 - New features
  - **Feature:** Wildcard characters (`*`) now supported in `.spec.applicationSet.sourceNamespaces` field
  - **Use Case:** Enable ApplicationSets in any namespace feature for dynamic namespace groups
  - **Benefit:** Single pattern instead of maintaining static namespace lists
  - **Jira:** GITOPS-8217

**Related:** Job 6 (Configure agent mapping for multitenant environments)

---

### Job 6: Configure Application Routing in Multitenant Environments
*When organizing applications for multiple teams targeting the same agent*

**Personas:** Platform administrator

**Requires:** Deployed Argo CD agents, multitenant architecture understanding

#### Enable Destination-Based Mapping

→ Lines 331-338: Mapping Applications to managed agents by using the destination field
  Source: Release notes 1.20.0 - New features
  - **Feature:** Destination-based mapping routes applications to agents using `.spec.destination.name` instead of application namespace
  - **Use Case:** Teams organize applications in separate namespaces while targeting same agent
  - **Configuration:** Set `destinationBasedMapping` field in Argo CD CR for principal and agent components
  - **Optional:** Set `createNamespace` field on agent to enable automatic namespace creation on spoke cluster
  - **Benefit:** Applications retain original namespace on spoke cluster
  - **Jira:** GITOPS-8531

**Related:** Argo CD Agent Mapping modes documentation (see Additional Resources in source)

---

### Job 7: Configure Image Update Automation
*When managing image updates across multiple applications*

**Personas:** Platform administrator

**Status:** Technology Preview features

#### Configure Image Updater Custom Resource (Technology Preview)

→ Lines 340-369: Image Updater custom resource with legacy annotation reading
  Source: Release notes 1.20.0 - New features
  - **Feature:** Custom resource (CR) targeting multiple ApplicationSet-generated applications
  - **Backward Compatibility:** Reads existing annotations (`argocd-image-updater.argoproj.io/*`)
  - **Benefit:** Centralized configuration without migrating existing annotations
  - **Scope:** Single ImageUpdater CR manages multiple applications
  - **Jira:** GITOPS-8544
  - **Status:** Technology Preview

#### Configure CloudEvents Webhook for AWS ECR (Technology Preview)

→ Lines 371-383: CloudEvents webhook support for AWS ECR in Image Updater
  Source: Release notes 1.20.0 - New features
  - **Feature:** CloudEvents v1.0 webhook handler for AWS ECR push events through AWS EventBridge
  - **Benefit:** Standard event format instead of registry-specific handlers
  - **Integration:** AWS EventBridge converts native ECR events to CloudEvents
  - **Result:** Automated image updates when new images pushed to ECR registries
  - **Jira:** GITOPS-8283
  - **Status:** Technology Preview

**Related:** Argo CD Image Updater upstream documentation (see Additional Resources in source)

---

## Deploy and Manage Agents

### Job 8: Deploy Argo CD Agents for Multi-Cluster Management
*When deploying agents for multi-cluster workflows*

**Personas:** Platform administrator

**Requires:** Argo CD agent architecture understanding, multi-cluster environment

#### Deploy Agents Through Argo CD CR

→ Lines 326-329: Managed and autonomous agent installation through the Argo CD agent
  Source: Release notes 1.20.0 - New features
  - **Feature:** Configure and deploy managed/autonomous agents directly through Argo CD CR
  - **Benefit:** Operator-managed lifecycle simplifies deployment workflows
  - **Deployment Types:** Managed agents, Autonomous agents
  - **Jira:** GITOPS-8164

**Related:** Installing Argo CD Agent (see Additional Resources in source), Argo CD Agent architecture overview (see Additional Resources in source)

---

## Monitor and Troubleshoot

### Job 9: Troubleshoot Applications Using Agent Architecture
*When diagnosing application issues on workload clusters*

**Personas:** Platform administrator, SRE

**Requires:** Argo CD agent architecture deployed

#### View Pod Logs Centrally

→ Lines 385-388: Pod log streaming in agent architecture
  Source: Release notes 1.20.0 - New features
  - **Feature:** View pod logs from workload clusters in control plane
  - **Benefit:** Centralized troubleshooting without direct cluster access
  - **Jira:** GITOPS-7264

#### Analyze Performance with Distributed Tracing

→ Lines 390-393: OpenTelemetry integration for Argo CD agent
  Source: Release notes 1.20.0 - New features
  - **Feature:** OpenTelemetry integration for distributed tracing
  - **Scope:** Agent and principal components
  - **Benefit:** Deeper visibility into system behavior and performance
  - **Jira:** GITOPS-8119

**Related:** Job 2 (Discover fixed issues)

---

## Secure Deployments

### Job 10: Secure Argo CD Components
*When implementing security hardening for GitOps deployments*

**Personas:** Security administrator, Platform administrator

#### Enable Network Policies

→ Lines 395-398: Network policies for core Argo CD components
  Source: Release notes 1.20.0 - New features
  - **Feature:** Kubernetes Network Policy resources for all Argo CD workload pods
  - **Default:** Enabled (prevent unnecessary ingress/egress traffic)
  - **Purpose:** Mitigate risks identified in OCP threat model, ensure least-privilege network posture
  - **Opt-out:** Set `spec.networkPolicy.enabled` to `false`
  - **Jira:** GITOPS-7787

#### Configure TLS Trust for Repo-Server Plugins

→ Lines 400-403: Kubernetes trust anchors in the GitOps operator
  Source: Release notes 1.20.0 - New features
  - **Feature:** Configure system CA trust for repo-server through Argo CD CR
  - **Use Case:** Plugin sidecars trusting TLS hosts (kustomize, file fetching over TLS)
  - **Benefit:** Simplified certificate management vs manual `argocd-tls-certs-cm` ConfigMap editing
  - **Jira:** GITOPS-7391

**Related:** Job 4 (Configure authentication)

---

## Manage Lifecycle

### Job 11: Manage Application and Resource Lifecycle
*When operating GitOps-managed applications and resources*

**Personas:** Platform administrator

#### Configure Ordered Application Deletion

→ Lines 405-408: Argo CD progressive sync with ordered deletion
  Source: Release notes 1.20.0 - New features
  - **Feature:** Configure deletion order for Progressive Sync applications
  - **Previous Behavior:** Parallel deletion of all applications
  - **Benefit:** Avoid dependency issues and service disruptions
  - **Jira:** GITOPS-6250

#### Automatic Cleanup of Orphaned Resources

→ Lines 410-413: Automatic cleanup of orphaned roles and role bindings
  Source: Release notes 1.20.0 - New features
  - **Feature:** Operator identifies and cleans up orphaned roles when namespaces removed from sourceNamespaces
  - **Trigger:** Namespace removed from `.spec.sourceNamespaces` or `.spec.applicationSet.sourceNamespaces`
  - **Benefit:** Consistent resource management, no manual cleanup
  - **Jira:** GITOPS-8537

---

## Access CLI Tools

### Job 12: Access Argo Rollouts CLI
*When implementing progressive delivery workflows*

**Personas:** Platform administrator

#### Download Platform-Specific Binaries

→ Lines 415-418: Argo Rollouts kubectl plugin binaries
  Source: Release notes 1.20.0 - New features
  - **Availability:** Binaries built and released through Konflux for multiple platforms
  - **Format:** Standalone executables (not RPM packages)
  - **Download:** See Additional Resources for download links
  - **Jira:** GITOPS-5038

**Download Link:** See Argo Rollouts kubectl plugin binaries link in Additional Resources (source lines 497)

---

## Appendices

### A. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Plan | ✅ | Jobs 1, 3 | Version compatibility, upgrade planning |
| Configure | ✅ | Jobs 4, 5, 6, 7 | Authentication, namespaces, agents, image updates |
| Deploy | ✅ | Job 8 | Agent deployment |
| Monitor | ✅ | Job 9 | Observability, troubleshooting |
| Secure | ✅ | Job 10 | Network policies, TLS trust |
| Operate | ✅ | Job 11 | Lifecycle management |
| Troubleshoot | ✅ | Job 2, 9 | Fixed issues, centralized logs, tracing |
| Upgrade | ✅ | Job 3 | Upgrade planning, errata advisories |
| Get Started | ✅ | Job 12 | CLI tool access |
| Reference | ✅ | Job 1 | Component version matrix |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Training | No training content | Release notes focus on features/fixes, not tutorials |
| Migrate | No migration content | Link to main documentation for migration guides |

**Note:** Release notes intentionally focus on "What's New" and "What's Fixed" rather than comprehensive workflow coverage. For full workflow documentation, see the main OpenShift GitOps documentation.

---

## Document Statistics

**Workflow Coverage:**
- Plan: 2 jobs
- Configure: 4 jobs
- Deploy: 1 job
- Monitor: 1 job
- Secure: 1 job
- Operate: 1 job
- Troubleshoot: 2 jobs (overlaps with Monitor)
- Upgrade: 1 job
- Get Started: 1 job
- Reference: 1 job (overlaps with Plan)

**Main Jobs:** 12
**User Stories/Paths:** 23 total JTBD records extracted
**Source Sections:** 3 main sections (Compatibility matrix, 1.20.1 release notes, 1.20.0 release notes)
**Releases Covered:** 2 (1.20.0, 1.20.1)

**Technology Preview Features:**
- Argo CD Image Updater CR (GITOPS-8544)
- CloudEvents webhook for AWS ECR (GITOPS-8283)
- Image Updater security enhancements (GITOPS-8876)
- Image Updater Git process fixes (GITOPS-8875)

---

## Navigation Guide

### By User Journey

**Platform administrator evaluating upgrade to 1.20.x:**
1. Job 1: Understand version compatibility
2. Job 2: Review fixed issues
3. Job 3: Plan upgrade path
4. Job 4-12: Review new features relevant to your use cases

**Platform administrator deploying multi-cluster setup:**
1. Job 1: Check supported versions
2. Job 8: Deploy Argo CD agents
3. Job 6: Configure application routing
4. Job 9: Set up centralized troubleshooting

**Security administrator hardening GitOps deployment:**
1. Job 10: Enable network policies and configure TLS trust
2. Job 4: Configure external authentication
3. Job 2: Review security-related fixes (GITOPS-8876)

**SRE troubleshooting production issues:**
1. Job 2: Check if issue is fixed in 1.20.x
2. Job 9: Use pod log streaming and distributed tracing
3. Job 3: Plan upgrade if fix is available
