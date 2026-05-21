# OpenShift GitOps Release Notes 1.20 — Consolidation Report

**Document:** gitops-release-notes-1-20.adoc  
**JTBD Records:** 23 pre-consolidated records → 12 final jobs (after merging related features)

---

## Executive Summary

### What's Changing

OpenShift GitOps release notes currently organize content chronologically by release version (1.20.1, 1.20.0) with flat lists of features and fixes within each release. This structure forces users to scan sequentially through 22+ items to find relevant information, with no grouping by user intent or workflow context. Features that enable related workflows (agent deployment, agent troubleshooting, agent observability) are scattered across the "New features" list with no indication of their relationships.

The proposed JTBD-based restructure organizes the same content around 12 user goals and workflow stages. Related features are grouped under unified jobs (e.g., all agent architecture features under Jobs 8-9, all security features under Job 10), making it easier for users to discover what's relevant to their current work. The structure maintains chronological information in line references while prioritizing discoverability by user intent.

This change addresses a core pain point: release notes serve both as a "what's new" reference for existing users AND as upgrade planning guidance for decision-makers. Grouping by workflow stage enables both use cases without requiring users to mentally map feature names to their operational impact.

### Key Improvements

- **Agent Architecture Features Consolidated:** 5 scattered features (agent installation, pod log streaming, OpenTelemetry, destination-based mapping, agent mapping modes) grouped under 2 jobs (Deploy Agents, Troubleshoot with Agents)
- **Security Hardening Unified:** 3 security-related features (network policies, TLS trust anchors, Image Updater security fix) grouped under 1 job (Secure Argo CD Components)
- **Configuration Features Grouped by Domain:** 4 configuration features organized into distinct jobs (Authentication, Namespaces, Application Routing, Image Updates)
- **Troubleshooting Surfaced:** Fixed issues elevated from flat lists to dedicated troubleshooting job with grouped observability tools
- **Upgrade Planning Explicit:** Errata advisories and breaking changes (image naming, authentication) consolidated under upgrade planning job
- **Navigation Reduction:** 22 top-level feature/issue items reduced to 12 goal-oriented jobs (45% reduction)
- **Related Content Linked:** Cross-references between deployment features and operational features (e.g., agent deployment → agent troubleshooting)
- **Technology Preview Visibility:** TP features flagged in context while maintaining compatibility matrix reference

---

## Current Structure (Feature-Based)

- **Compatibility and support matrix** — Component version compatibility table
  - **Technology Preview features** — TP tracker showing feature maturity progression

- **Release notes for Red Hat OpenShift GitOps 1.20.1** — Patch release updates
  - **Errata updates** — Advisory information
  - **Fixed issues** — 1 issue fixed (AppProjects deletion during resync)

- **Release notes for Red Hat OpenShift GitOps 1.20.0** — Minor release updates
  - **Errata updates** — Advisory information
  - **New features** — 15 features listed sequentially:
    1. Changes to Argo CD authentication with external authentication enabled
    2. Enhanced wildcard support for ApplicationSet source namespaces
    3. Managed and autonomous agent installation through the Argo CD agent
    4. Mapping Applications to managed agents by using the destination field
    5. Image Updater custom resource with legacy annotation reading (TP)
    6. CloudEvents webhook support for AWS ECR in Image Updater (TP)
    7. Pod log streaming in agent architecture
    8. OpenTelemetry integration for Argo CD agent
    9. Network policies for core Argo CD components
    10. Kubernetes trust anchors in the GitOps operator
    11. Argo CD progressive sync with ordered deletion
    12. Automatic cleanup of orphaned roles and role bindings
    13. Argo Rollouts kubectl plugin binaries
    14. Operator base image migration to UBI 9 Minimal
    15. Reduced image size through package cleanup
  - **Fixed issues** — 7 issues listed sequentially:
    1. Fixed console plugin Applications page rendering error
    2. Fixed incorrect ownerReferences apiVersion in config maps
    3. Fixed Progressive Sync status display in UI
    4. Fixed incorrect application links across Argo CD instances
    5. Enhanced security for Image Updater application references (TP)
    6. Fixed Image Updater Git process exhaustion (TP)

- **Additional resources** — 7 external reference links

**Total:** 3 main sections, 7 subsections, 22+ individual feature/fix items, organized chronologically by release.

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Understand & Plan**
  - Job 1: Understand Version Compatibility
  - Job 2: Discover Issue Resolutions
  - Job 3: Plan Upgrade from Previous Versions

- **Set Up & Configure**
  - Job 4: Configure Argo CD Authentication for External Authentication Environments
  - Job 5: Configure ApplicationSet Source Namespaces
  - Job 6: Configure Application Routing in Multitenant Environments
  - Job 7: Configure Image Update Automation

- **Deploy & Serve**
  - Job 8: Deploy Argo CD Agents for Multi-Cluster Management

- **Track & Monitor**
  - Job 9: Troubleshoot Applications Using Agent Architecture

- **Secure**
  - Job 10: Secure Argo CD Components

- **Operate & Manage**
  - Job 11: Manage Application and Resource Lifecycle

- **Reference**
  - Job 12: Access Argo Rollouts CLI

---

### Detailed Job Descriptions

#### Understand & Plan

**Job 1: Understand Version Compatibility**

*When planning an OpenShift GitOps deployment or upgrade, I want to understand which component versions are compatible with my OpenShift cluster version, so I can ensure a supported configuration and avoid version conflicts.*

Prerequisites: None

- **1.1. Check supported versions** `[reference]`
  - Compatibility and support matrix (Lines 151-183): Component version table showing GitOps 1.20.0, 1.19.0, 1.18.0 with Argo CD, Argo Rollouts, Dex, Helm, Kustomize versions; supported OCP versions (4.14, 4.16-4.21)
  - Context: Use before deployment or upgrade planning

- **1.2. Understand Technology Preview feature status** `[reference]`
  - Technology Preview tracker (Lines 186-240): Table showing TP-to-GA progression for features; permanent TP features identified
  - Context: Critical for production readiness assessment

**Job 2: Discover Issue Resolutions**

*When encountering problems or deciding whether to upgrade, I want to know if the issue is fixed in the latest release, so I can decide whether to upgrade and resolve the problem.*

Prerequisites: None

- **2.1. Review 1.20.1 fixed issues** `[reference]`
  - Fixed issues section (Lines 277-280): GITOPS-9200 - AppProjects deletion during resync prevented
  - Context: Affects users with autonomous agents

- **2.2. Review 1.20.0 console plugin fixes** `[reference]`
  - Fixed issues section (Lines 433-436): GITOPS-8773 - Applications page rendering error fixed
  - Context: Affects users viewing invalid/ill-formed Applications

- **2.3. Review 1.20.0 upgrade correctness fixes** `[reference]`
  - Fixed issues section (Lines 438-441): GITOPS-8001 - ownerReferences apiVersion correction
  - Context: Affects users upgrading Argo CD CR from v1alpha1 to v1beta1

- **2.4. Review 1.20.0 UI observability fixes** `[reference]`
  - Fixed issues section (Lines 443-451): GITOPS-7797 (Progressive Sync status), GITOPS-1505 (application links across instances)
  - Context: Affects users monitoring ApplicationSets and using multiple Argo CD instances

- **2.5. Review 1.20.0 Image Updater fixes (TP)** `[reference]`
  - Fixed issues section (Lines 453-479): GITOPS-8876 (security enhancements), GITOPS-8875 (Git process exhaustion)
  - Context: Technology Preview features; affects multitenant Image Updater users

**Job 3: Plan Upgrade from Previous Versions**

*When considering upgrade to OpenShift GitOps 1.20.x, I want to understand breaking changes and upgrade procedures, so I can plan a smooth upgrade without surprises.*

Prerequisites: Review Job 1 (compatibility) and Job 2 (fixed issues)

- **3.1. Understand image naming changes** `[concept]`
  - New features section (Lines 420-423): GITOPS-8107 - UBI 9 migration changes image suffix from `rhel8` to `rhel9`
  - Context: Action required if external automation references operator images

- **3.2. Review errata advisories** `[reference]`
  - 1.20.1 errata (Lines 260-272): RHEA-2026:6378 advisory
  - 1.20.0 errata (Lines 299-311): RHEA-2026:5819 advisory
  - Context: View container images via `oc describe deployment` command

---

#### Set Up & Configure

**Job 4: Configure Argo CD Authentication for External Authentication Environments**

*When external authentication is enabled at the cluster level in OpenShift 4.20 and later, I want to configure an external identity provider for Argo CD login, so I can maintain login functionality and align with cluster security policies.*

Prerequisites: OpenShift 4.20+ with external authentication enabled, understand OIDC configuration

- **4.1. Configure external OIDC provider** `[concept]`
  - New features section (Lines 316-319): GITOPS-8017 - Behavior change requiring `.spec.oidc` field in ArgoCD CR; example: Red Hat Build of Keycloak
  - Context: Required when external authentication enabled; Dex fallback when not enabled

**Job 5: Configure ApplicationSet Source Namespaces**

*When managing ApplicationSets across many namespaces, I want to use wildcard patterns instead of maintaining a static namespace list, so I can reduce configuration overhead and enable dynamic namespace support.*

Prerequisites: Argo CD custom resource deployed, understand ApplicationSet namespace scoping

- **5.1. Use wildcard patterns for dynamic namespace support** `[procedure]`
  - New features section (Lines 321-324): GITOPS-8217 - Wildcard support in `.spec.applicationSet.sourceNamespaces` field
  - Context: Replaces static namespace lists with patterns

**Job 6: Configure Application Routing in Multitenant Environments**

*When organizing applications for multiple teams in multitenant environments, I want to route applications to agents using destination-based mapping, so I can support teams with separate namespaces targeting the same agent.*

Prerequisites: Deployed Argo CD agents, multitenant architecture understanding

- **6.1. Enable destination-based mapping** `[procedure]`
  - New features section (Lines 331-338): GITOPS-8531 - Configure `destinationBasedMapping` field in Argo CD CR; optional `createNamespace` for automatic namespace creation on spoke clusters
  - Context: Supports multitenant use cases; applications retain original namespace on spoke

**Job 7: Configure Image Update Automation**

*When managing image updates across multiple applications generated by ApplicationSets, I want to use a custom resource instead of per-application annotations, so I can centralize image update configuration and reduce duplication.*

Prerequisites: ApplicationSets deployed, understand Argo CD Image Updater

- **7.1. Configure Image Updater Custom Resource (TP)** `[procedure]`
  - New features section (Lines 340-369): GITOPS-8544 - ImageUpdater CR with backward compatibility for annotations
  - Context: Technology Preview; enables CR-based workflow without migrating existing configs

- **7.2. Configure CloudEvents webhook for AWS ECR (TP)** `[procedure]`
  - New features section (Lines 371-383): GITOPS-8283 - CloudEvents v1.0 webhook handler for AWS EventBridge integration
  - Context: Technology Preview; AWS ECR specific; requires EventBridge configuration

---

#### Deploy & Serve

**Job 8: Deploy Argo CD Agents for Multi-Cluster Management**

*When deploying Argo CD agents for multi-cluster management, I want to configure agent installation directly through the Argo CD CR, so I can simplify deployment workflows and use operator-managed lifecycle.*

Prerequisites: Understand Argo CD agent architecture, multi-cluster environment

- **8.1. Deploy agents through Argo CD CR** `[procedure]`
  - New features section (Lines 326-329): GITOPS-8164 - Managed and autonomous agent installation support
  - Context: Simplifies agent deployment vs manual installation

---

#### Track & Monitor

**Job 9: Troubleshoot Applications Using Agent Architecture**

*When troubleshooting applications on workload clusters, I want to view pod logs and trace performance from the control plane, so I can diagnose issues without direct access to each workload cluster.*

Prerequisites: Argo CD agent architecture deployed

- **9.1. View pod logs centrally** `[procedure]`
  - New features section (Lines 385-388): GITOPS-7264 - Pod log streaming in agent architecture
  - Context: Centralized troubleshooting without direct cluster access

- **9.2. Analyze performance with distributed tracing** `[procedure]`
  - New features section (Lines 390-393): GITOPS-8119 - OpenTelemetry integration for agent and principal components
  - Context: Performance visibility across distributed agent architecture

---

#### Secure

**Job 10: Secure Argo CD Components**

*When implementing security hardening for GitOps deployments, I want to apply network policies and configure TLS trust, so I can enforce least-privilege network access and simplify certificate management.*

Prerequisites: Understand Kubernetes Network Policies, security requirements defined

- **10.1. Enable network policies** `[concept]`
  - New features section (Lines 395-398): GITOPS-7787 - Network policies for all Argo CD workload pods; opt-out via `spec.networkPolicy.enabled`
  - Context: Enabled by default; mitigates OCP threat model risks

- **10.2. Configure TLS trust for repo-server plugins** `[procedure]`
  - New features section (Lines 400-403): GITOPS-7391 - Kubernetes trust anchors via Argo CD CR
  - Context: Replaces manual ConfigMap editing for plugin sidecars (kustomize, TLS hosts)

---

#### Operate & Manage

**Job 11: Manage Application and Resource Lifecycle**

*When operating GitOps-managed applications and resources, I want ordered deletion and automatic cleanup, so I can avoid dependency issues and ensure consistent resource management.*

Prerequisites: Use Progressive Sync or sourceNamespaces configuration

- **11.1. Configure ordered application deletion** `[procedure]`
  - New features section (Lines 405-408): GITOPS-6250 - Progressive sync ordered deletion support
  - Context: Prevents dependency violations during deletion; replaces parallel deletion

- **11.2. Automatic cleanup of orphaned resources** `[concept]`
  - New features section (Lines 410-413): GITOPS-8537 - Operator cleanup mechanism when namespaces removed from sourceNamespaces
  - Context: Triggered by namespace removal from `.spec.sourceNamespaces` or `.spec.applicationSet.sourceNamespaces`

---

#### Reference

**Job 12: Access Argo Rollouts CLI**

*When implementing progressive delivery workflows, I want standalone Argo Rollouts CLI binaries for my platform, so I can access the kubectl plugin without RPM packaging constraints.*

Prerequisites: None

- **12.1. Download platform-specific binaries** `[reference]`
  - New features section (Lines 415-418): GITOPS-5038 - Argo Rollouts kubectl plugin binaries built through Konflux
  - Additional resources (Line 497): Download link for binaries
  - Context: Standalone executables (not RPM); multi-platform support

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | Chronological (release version, then feature lists) | Workflow stage and user goal |
| **Top-level items** | 3 sections (Compatibility, 1.20.1, 1.20.0) with 22 flat feature/issue items | 12 jobs grouped into 7 lifecycle stages |
| **Agent architecture features** | Scattered across items 3, 4, 7, 8 in New features list + Additional resources | Consolidated under Jobs 8 (Deploy Agents) and 9 (Troubleshoot) |
| **Security features** | Items 9, 10 in New features + item 5 in Fixed issues | Consolidated under Job 10 (Secure Components) |
| **Configuration features** | Items 1, 2, 4, 5, 6 in New features | Grouped by domain: Jobs 4-7 (Authentication, Namespaces, Routing, Images) |
| **Fixed issues** | Flat list of 7 issues in 1.20.0, 1 issue in 1.20.1 | Integrated into relevant jobs (Job 2 groups all fixes, Jobs 9-10 link related fixes) |
| **Upgrade planning** | Errata sections + item 14 in New features | Consolidated under Job 3 (Plan Upgrade) |
| **Navigation path to find agent features** | Scan 15-item "New features" list | Navigate to "Deploy & Serve" or "Track & Monitor" sections |
| **Technology Preview visibility** | TP tracker + inline TP disclaimers | TP tracker in Job 1 + TP tags on Job 7 approaches |

### Job List Adjustments from Suggested Input

The suggested 23 JTBD records were consolidated to **12 jobs** for the following reasons:

1. **Records for Job 1 (main_job + user_story)** → Merged into single Job 1 with 2 approaches (compatibility check and TP status)
2. **Records for Job 2 (6 user stories)** → Consolidated into single Job 2 with 5 approaches (fixed issue categories)
3. **Records for Job 3 (2 user stories)** → Merged into single Job 3 with 2 approaches (breaking changes and errata)
4. **Records for Jobs 4-7 (1 main_job each)** → Retained as individual jobs (distinct configuration domains)
5. **Records for Jobs 9-10 (user stories under monitoring/security)** → Promoted to main jobs due to distinct personas and workflow stages
6. **Record for Job 11 (2 user stories under operate)** → Consolidated into single Job 11 with 2 approaches (lifecycle management)
7. **Record for Job 12 (consumption job)** → Retained as individual job (tool access)

**Rationale for consolidation:**
- **Issue discovery** (Job 2): All fixed issues serve the same job (discover resolutions) with different issue categories as approaches
- **Version compatibility** (Job 1): Compatibility check and TP status are approaches to the same planning job
- **Upgrade planning** (Job 3): Breaking changes and errata are both inputs to upgrade planning
- **Agent architecture**: Deployment (Job 8) and troubleshooting (Job 9) are distinct workflow stages, warranting separate jobs
- **Security hardening**: Network policies and TLS trust are both approaches to securing components (Job 10)

---

## Consolidation Examples

### Example 1: Agent Architecture Features (5 scattered items → 2 unified jobs)

**Current (Fragmented):**
- New features, item 3: "Managed and autonomous agent installation through the Argo CD agent" (lines 326-329)
- New features, item 4: "Mapping Applications to managed agents by using the destination field" (lines 331-338)
- New features, item 7: "Pod log streaming in agent architecture" (lines 385-388)
- New features, item 8: "OpenTelemetry integration for Argo CD agent" (lines 390-393)
- Additional resources: "Argo CD Agent architecture overview", "Installing Argo CD Agent" (lines 486, 490)

Users looking to deploy agents discover the installation feature but may miss the destination-based mapping configuration. Users troubleshooting applications may not realize pod log streaming and OpenTelemetry support are available. The relationship between deployment and operational features is not surfaced.

**Proposed (Consolidated):**
- **Job 8: Deploy Argo CD Agents for Multi-Cluster Management**
  - 8.1. Deploy agents through Argo CD CR (GITOPS-8164)
  - Related: Job 6 for destination-based mapping configuration
- **Job 9: Troubleshoot Applications Using Agent Architecture**
  - 9.1. View pod logs centrally (GITOPS-7264)
  - 9.2. Analyze performance with distributed tracing (GITOPS-8119)
  - Related: Additional resources for agent architecture overview

**Benefit:** Users deploying agents see both deployment AND routing configuration in logical sequence. Users troubleshooting applications find all observability features grouped together. The workflow progression (deploy → configure → troubleshoot) is explicit.

---

### Example 2: Security Features (3 scattered items → 1 unified job)

**Current (Fragmented):**
- New features, item 9: "Network policies for core Argo CD components" (lines 395-398)
- New features, item 10: "Kubernetes trust anchors in the GitOps operator" (lines 400-403)
- Fixed issues, item 5: "Enhanced security for Image Updater application references" (lines 453-465, TP)

Security administrators reviewing release notes must scan both the New features list AND the Fixed issues list to discover all security-related updates. Network policies and TLS trust are 7 items apart in the feature list with no indication they both serve security hardening.

**Proposed (Consolidated):**
- **Job 10: Secure Argo CD Components**
  - 10.1. Enable network policies (GITOPS-7787)
  - 10.2. Configure TLS trust for repo-server plugins (GITOPS-7391)
  - Related fix: Enhanced security for Image Updater (GITOPS-8876, TP)

**Benefit:** All security-related features discoverable under one job. Security administrators can review all relevant updates without scanning multiple lists. Network + TLS + application security presented as a cohesive hardening workflow.

---

### Example 3: Configuration Features (4 scattered items → 4 domain-specific jobs)

**Current (Fragmented):**
- New features, item 1: "Changes to Argo CD authentication with external authentication enabled" (lines 316-319)
- New features, item 2: "Enhanced wildcard support for ApplicationSet source namespaces" (lines 321-324)
- New features, item 4: "Mapping Applications to managed agents by using the destination field" (lines 331-338)
- New features, items 5-6: Image Updater features (lines 340-383, TP)

Configuration features appear as a flat sequential list with no indication of their distinct domains (authentication, namespaces, routing, images). Users configuring namespaces may not realize destination-based mapping is relevant to their multitenant use case.

**Proposed (Consolidated):**
- **Job 4: Configure Argo CD Authentication** → Item 1
- **Job 5: Configure ApplicationSet Source Namespaces** → Item 2
- **Job 6: Configure Application Routing** → Item 4
- **Job 7: Configure Image Update Automation** → Items 5-6

**Benefit:** Configuration features grouped by domain (auth, namespaces, routing, images) help users navigate to their specific configuration task. Related features surfaced via cross-references (e.g., Job 5 references Job 6 for multitenant routing).

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Migration guidance for authentication changes | Job 4 | Mentioned only as behavior change; no migration steps | **High** — Users on OCP 4.20+ with external auth need step-by-step migration from Dex to external OIDC |
| Rollback procedures for 1.20.x upgrades | Job 3 | No rollback guidance provided | **High** — Users encountering upgrade issues have no documented recovery path |
| Deprecation timeline for permanent TP features | Job 1 | TP tracker shows "NA" for GA but no deprecation timeline | **Medium** — Users need to know if permanent TP features will eventually be removed or supported indefinitely |
| Decision matrix for agent mapping modes | Jobs 6, 8 | Feature description only; no guidance on when to use namespace-based vs destination-based mapping | **Medium** — Users cannot determine which mapping mode fits their use case |
| Performance impact of network policies | Job 10 | Feature description only; no performance implications documented | **Medium** — Users may be concerned about opt-out necessity; need reassurance or metrics |
| Compatibility matrix for Image Updater TP features | Job 7 | Features listed but not in compatibility matrix | **Low** — TP features not in version table; unclear which GitOps versions support which Image Updater features |
| Breaking changes summary | Job 3 | Authentication change and image naming scattered; no consolidated summary | **High** — Users need a single "Breaking Changes" callout for upgrade risk assessment |
| Known issues for 1.20.x | Job 2 | No known issues section; only fixed issues | **Medium** — Users need to know outstanding issues before upgrading |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 22 features/fixes across 3 sections | 12 jobs across 7 lifecycle stages | 45% reduction in top-level items |
| Sections to browse for agent features | 4 items + 2 Additional Resources (scan 15-item list) | 2 jobs (Deploy Agents, Troubleshoot) | ~67% reduction in scan scope |
| Sections to browse for security features | 3 items (scan 22-item combined list) | 1 job (Secure Components) | ~67% reduction |
| Sections to browse for configuration features | 6 items (scan 15-item New features list) | 4 jobs (domain-specific) | 33% reduction with better domain clarity |
| Clicks to find upgrade planning info | 3 locations (errata x2 + item 14 in features) | 1 job (Plan Upgrade) | Consolidated into single location |
| Clicks to find fixed issues for specific topic | Scan 8 fixed issues across 2 releases | Navigate to Job 2, select issue category | Reduced to 2 clicks with categorization |
| Workflow stage visibility | Implicit (user infers from feature names) | Explicit (7 lifecycle stage headings) | Clear workflow progression |

**Final job count: 12** (reduced from suggested 23 JTBD records). Consolidation focused on grouping related features under unified jobs (agent architecture, security, issue discovery, upgrade planning) while maintaining domain-specific jobs for distinct configuration tasks. This balances navigability (fewer top-level items) with specificity (distinct configuration domains remain separate).

---

## Document Statistics

**Current Structure:**
- Sections: 3 main sections
- Subsections: 7 (Compatibility matrix, TP features, Errata x2, Fixed issues x2, New features)
- Individual items: 22 features/fixes
- Deepest nesting: 2 levels
- Personas: Implicit (inferred from feature descriptions)
- Technology Preview features: 5 (scattered across sections)

**Proposed Structure:**
- Lifecycle stages: 7 (Understand & Plan through Reference)
- Main jobs: 12
- Approaches: 23 (user stories/paths)
- Deepest nesting: 3 levels (Stage -> Job -> Approach)
- Personas: Explicit (Platform administrator, Security administrator, SRE)
- Technology Preview features: 5 (flagged in Job 1 + Job 7 approaches)

**Consolidation Metrics:**
- Top-level items reduced: 22 -> 12 (45% reduction)
- Agent architecture features grouped: 5 items -> 2 jobs
- Security features grouped: 3 items -> 1 job
- Configuration features organized by domain: 6 items -> 4 jobs
- Fixed issues categorized: 8 items -> 5 approaches under Job 2
- Navigation depth maintained: 2-3 levels in both structures

**Coverage:**
- Workflow stages covered: 7 of 10 common stages (Plan, Configure, Deploy, Monitor, Secure, Operate, Reference)
- Gaps: Training content, migration guidance, rollback procedures
- Technology Preview visibility: Maintained in both compatibility matrix (Job 1) and workflow context (Job 7)
