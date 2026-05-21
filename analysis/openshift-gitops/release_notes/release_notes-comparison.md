# OpenShift GitOps Release Notes 1.20 - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-05-20
**JTBD Records:** 23
**Main Jobs:** 12 (consolidated from 23 records)
**Source Document:** gitops-release-notes-1-20.adoc (497 lines)

---

## Current Structure (Feature-Based)

```
Red Hat OpenShift GitOps release notes
  ├── Compatibility and support matrix
  │   └── Technology Preview features
  ├── Release notes for Red Hat OpenShift GitOps 1.20.1
  │   ├── Errata updates
  │   └── Fixed issues
  └── Release notes for Red Hat OpenShift GitOps 1.20.0
      ├── Errata updates
      ├── New features (15 features listed sequentially)
      └── Fixed issues (7 issues listed sequentially)
```

**Organizational Pattern:**
- Chronological by release (newest first)
- Flat lists within each category (New features, Fixed issues)
- No grouping by user intent or workflow stage

**Navigation Path Example:**
To find information about agent deployment:
1. Scan "New features" list (15 items)
2. Locate "Managed and autonomous agent installation through the Argo CD agent"
3. No indication of related features (agent mapping, pod log streaming, OpenTelemetry)

---

## Proposed JTBD-Based Structure

### Getting Started

**Job 1: Understand Version Compatibility**
  When: Planning an OpenShift GitOps deployment or upgrade
  Personas: Platform administrator

  - Check supported versions
    → Lines 151-183: Compatibility and support matrix
  - Understand Technology Preview feature status
    → Lines 186-240: Technology Preview tracker

---

### Plan Deployment and Upgrades

**Job 2: Discover Issue Resolutions**
  When: Encountering problems or deciding whether to upgrade
  Personas: Platform administrator, SRE

  - 1.20.1 fixed issues (1 issue)
  - 1.20.0 console plugin fixes (1 issue)
  - 1.20.0 upgrade correctness fixes (1 issue)
  - 1.20.0 UI observability fixes (2 issues)
  - 1.20.0 Image Updater fixes (2 issues, Technology Preview)

**Job 3: Plan Upgrade from Previous Versions**
  When: Considering upgrade to OpenShift GitOps 1.20.x
  Personas: Platform administrator

  - Understand image naming changes
    → Lines 420-423: UBI 9 migration
  - Review errata advisories
    → Lines 260-272 (1.20.1), 299-311 (1.20.0)

---

### Configure Authentication and Access

**Job 4: Configure Argo CD Authentication for External Authentication Environments**
  When: External authentication is enabled on OpenShift 4.20+
  Personas: Platform administrator

  - Configure external OIDC provider
    → Lines 316-319: Authentication changes (GITOPS-8017)

---

### Configure Namespace and Application Management

**Job 5: Configure ApplicationSet Source Namespaces**
  When: Managing ApplicationSets across many namespaces
  Personas: Platform administrator

  - Use wildcard patterns for dynamic namespace support
    → Lines 321-324: Wildcard support (GITOPS-8217)

**Job 6: Configure Application Routing in Multitenant Environments**
  When: Organizing applications for multiple teams targeting the same agent
  Personas: Platform administrator

  - Enable destination-based mapping
    → Lines 331-338: Destination-based mapping (GITOPS-8531)

**Job 7: Configure Image Update Automation**
  When: Managing image updates across multiple applications
  Personas: Platform administrator

  - Configure Image Updater Custom Resource (Technology Preview)
    → Lines 340-369: ImageUpdater CR (GITOPS-8544)
  - Configure CloudEvents webhook for AWS ECR (Technology Preview)
    → Lines 371-383: CloudEvents support (GITOPS-8283)

---

### Deploy Multi-Cluster Infrastructure

**Job 8: Deploy Argo CD Agents for Multi-Cluster Management**
  When: Deploying agents for multi-cluster workflows
  Personas: Platform administrator

  - Deploy agents through Argo CD CR
    → Lines 326-329: Agent installation (GITOPS-8164)

---

### Monitor and Troubleshoot

**Job 9: Troubleshoot Applications Using Agent Architecture**
  When: Diagnosing application issues on workload clusters
  Personas: Platform administrator, SRE

  - View pod logs centrally
    → Lines 385-388: Pod log streaming (GITOPS-7264)
  - Analyze performance with distributed tracing
    → Lines 390-393: OpenTelemetry integration (GITOPS-8119)

---

### Secure Deployments

**Job 10: Secure Argo CD Components**
  When: Implementing security hardening for GitOps deployments
  Personas: Security administrator, Platform administrator

  - Enable network policies
    → Lines 395-398: Network policies (GITOPS-7787)
  - Configure TLS trust for repo-server plugins
    → Lines 400-403: Trust anchors (GITOPS-7391)

---

### Manage Lifecycle

**Job 11: Manage Application and Resource Lifecycle**
  When: Operating GitOps-managed applications and resources
  Personas: Platform administrator

  - Configure ordered application deletion
    → Lines 405-408: Progressive sync ordered deletion (GITOPS-6250)
  - Automatic cleanup of orphaned resources
    → Lines 410-413: Orphaned role cleanup (GITOPS-8537)

---

### Access Tools

**Job 12: Access Argo Rollouts CLI**
  When: Implementing progressive delivery workflows
  Personas: Platform administrator

  - Download platform-specific binaries
    → Lines 415-418: Argo Rollouts kubectl plugin (GITOPS-5038)

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** Release chronology, feature categories (New features, Fixed issues)
**Navigation:** 3 main sections, 22+ individual feature/issue entries
**User Journey:** Linear reading through flat lists
**Discoverability:** Scan entire list to find relevant items
**Grouping:** None - all features listed sequentially

### Proposed Structure (JTBD-Based)

**Organized By:** User goals and workflow stages
**Navigation:** 12 main jobs, 23 user stories nested under jobs
**User Journey:** Goal-directed - jump to relevant workflow stage
**Discoverability:** Find content by intent (e.g., "Secure Deployments" -> Network policies + TLS trust)
**Grouping:** Related features grouped under common jobs (e.g., Job 9 groups pod logs + distributed tracing under "Troubleshoot")

---

## Hierarchy Levels Explanation

### Level 1: Main Jobs (~12 per document)
Stable, outcome-focused goals that persist across releases.

**Examples:**
- "Configure Application Routing in Multitenant Environments"
- "Troubleshoot Applications Using Agent Architecture"
- "Secure Argo CD Components"

**Characteristics:**
- Outcome-focused (what user wants to accomplish)
- Stable over time (job persists even as tech changes)
- Tool/platform-agnostic at this level

### Level 2: User Stories (1-5 per main job)
Persona-specific or option-specific approaches to accomplish the main job.

**Examples:**
- Under Job 7 (Configure Image Update Automation):
  - "Configure Image Updater Custom Resource" (CR-based approach)
  - "Configure CloudEvents webhook for AWS ECR" (Event-driven approach)

**Characteristics:**
- Implementation-specific (references specific features)
- Persona or platform-specific
- Technology/tool mentions allowed

### Level 3: Procedures (embedded via line references)
Step-by-step instructions or reference content.

**Characteristics:**
- Line number references to source
- Brief description of content
- Link to full details in source document

---

## Example Consolidation

### Example 1: Agent Architecture Features (Grouped Under Job 8 and Job 9)

**Current (Fragmented):**
- New features, item 3: "Managed and autonomous agent installation through the Argo CD agent" (lines 326-329)
- New features, item 8: "Pod log streaming in agent architecture" (lines 385-388)
- New features, item 9: "OpenTelemetry integration for Argo CD agent" (lines 390-393)
- Additional Resources: "Argo CD Agent architecture overview" (line 486)
- Additional Resources: "Installing Argo CD Agent" (line 490)

**Proposed (Consolidated):**

**Job 8: Deploy Argo CD Agents for Multi-Cluster Management**
  - Deploy agents through Argo CD CR (GITOPS-8164)

**Job 9: Troubleshoot Applications Using Agent Architecture**
  - View pod logs centrally (GITOPS-7264)
  - Analyze performance with distributed tracing (GITOPS-8119)
  - Related: Argo CD Agent architecture overview, Installing Argo CD Agent

**Benefit:** 
- Users deploying agents see deployment feature AND related operational features in logical sequence
- Troubleshooting features grouped with observability context
- Clear workflow progression: Deploy (Job 8) -> Operate & Troubleshoot (Job 9)

---

### Example 2: Security Features (Grouped Under Job 10)

**Current (Fragmented):**
- New features, item 10: "Network policies for core Argo CD components" (lines 395-398)
- New features, item 11: "Kubernetes trust anchors in the GitOps operator" (lines 400-403)
- Fixed issues, item 5: "Enhanced security for Image Updater application references" (lines 453-465)

**Proposed (Consolidated):**

**Job 10: Secure Argo CD Components**
  - Enable network policies (GITOPS-7787)
  - Configure TLS trust for repo-server plugins (GITOPS-7391)
  - Related fix: Enhanced security for Image Updater (GITOPS-8876, Technology Preview)

**Benefit:**
- All security-related features discoverable under one job
- Security administrators can review all relevant updates in one place
- Network + TLS + Application security presented as cohesive hardening workflow

---

## Navigation Improvement Metrics

**Current:**
- Top-level sections: 3 (Compatibility matrix, 1.20.1 release notes, 1.20.0 release notes)
- Feature entries: 22 total (1 in 1.20.1 Fixed issues, 15 in 1.20.0 New features, 7 in 1.20.0 Fixed issues)
- Average items per section: 7.3
- To find agent-related features: Scan 15-item "New features" list

**Proposed:**
- Top-level jobs: 12
- Average user stories per job: 1.9
- Reduction: 45% fewer top-level items (22 -> 12)
- To find agent-related features: Navigate to "Deploy Multi-Cluster Infrastructure" or "Monitor and Troubleshoot" sections (2 clicks)

**Improvement Summary:**
- **Discoverability:** Grouped related features reduce scan time
- **Contextual navigation:** Workflow stages provide intent-based wayfinding
- **Consolidation:** 22 scattered items -> 12 goal-oriented jobs
- **Related content:** Cross-references surface connected features (e.g., agent deployment + agent troubleshooting)

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| Plan | ⚠️ Limited | ✅ Jobs 1, 2, 3 | Improved - added issue discovery and upgrade planning |
| Get Started | ⚠️ Scattered | ✅ Job 12 | Improved - CLI access elevated |
| Configure | ⚠️ Mixed in features | ✅ Jobs 4, 5, 6, 7 | Improved - configuration features grouped by intent |
| Deploy | ⚠️ Mixed in features | ✅ Job 8 | Improved - agent deployment elevated |
| Monitor | ⚠️ Mixed in features | ✅ Job 9 | Improved - observability features grouped |
| Secure | ⚠️ Mixed in features | ✅ Job 10 | Improved - security features consolidated |
| Operate | ⚠️ Mixed in features | ✅ Job 11 | Improved - lifecycle management grouped |
| Troubleshoot | ⚠️ Buried in fixed issues | ✅ Jobs 2, 9 | Improved - fixed issues and troubleshooting tools surfaced |
| Upgrade | ⚠️ Buried in errata | ✅ Job 3 | Improved - upgrade planning elevated |
| Reference | ✅ Compatibility matrix | ✅ Job 1 | Maintained - version reference accessible |

### Coverage Summary

**Current structure:** 
- All workflow stages present but scattered across flat feature lists
- No intentional grouping by workflow stage
- Discovery requires scanning entire lists

**Proposed structure:**
- All workflow stages explicitly organized with dedicated jobs
- Features grouped by user intent and workflow progression
- Discovery follows workflow logic

**Gaps addressed by restructure:**
- **Planning:** Upgrade planning and issue discovery now explicit jobs
- **Configuration:** Configuration features grouped by domain (auth, namespaces, images)
- **Security:** Security features consolidated under dedicated job
- **Troubleshooting:** Fixed issues and troubleshooting tools surfaced as jobs

### Recommendations for Future Releases

| Gap | Recommendation | Priority |
|-----|----------------|----------|
| Training | Add "Getting Started with 1.20" tutorial section | Medium |
| Migration | Include migration guidance for breaking changes (auth changes, image naming) | High |
| Deprecation tracking | Surface deprecated features explicitly in Planning section | High |

---

## Document Statistics

**Current Structure:**
- Sections: 3 main sections (Compatibility, 1.20.1, 1.20.0)
- Subsections: 7 (Compatibility matrix, TP features, Errata x2, Fixed issues x2, New features)
- Individual items: 22 features/fixes
- Deepest nesting: 2 levels

**Proposed Structure:**
- Main workflow sections: 9 (Getting Started through Access Tools)
- Main jobs: 12
- User stories: 23
- Deepest nesting: 3 levels (Job -> User Story -> Line Reference)

**Consolidation Metrics:**
- Items reduced at top level: 22 -> 12 (45% reduction)
- Related features grouped: 3 agent features -> 2 jobs (deployment + troubleshooting)
- Security features grouped: 3 items -> 1 job
- Navigation depth maintained: 2-3 levels in both structures

---

## Technology Preview Feature Visibility

### Current Structure
Technology Preview features are:
- Listed in Technology Preview tracker table (lines 186-240)
- Scattered across New features list with inline TP disclaimers
- No unified view of all TP features in 1.20.x

### Proposed Structure
Technology Preview features are:
- Still listed in Job 1 (Technology Preview tracker reference)
- Grouped under relevant jobs with "Technology Preview" status label
- All Job 7 user stories flagged as Technology Preview
- Quick Navigation section could add "See Technology Preview features → Jobs 1, 7"

**Benefit:** Users can see TP features both in reference table AND in workflow context

---

## Persona Visibility

### Current Structure
Personas are implicit:
- No explicit persona indicators
- Users infer relevance from feature descriptions
- No persona-based navigation

### Proposed Structure
Personas are explicit:
- Each job lists relevant personas
- Quick Navigation shows persona-based journeys
- Navigation Guide provides persona-specific workflows

**Personas identified:**
- Platform administrator (most jobs)
- Security administrator (Job 10, Job 4)
- SRE (Jobs 2, 9)

**Benefit:** Users can filter to persona-relevant content immediately
