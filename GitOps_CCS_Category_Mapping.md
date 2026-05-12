# Red Hat OpenShift GitOps 1.19 Documentation
# Category Mapping to CCS Framework

**Analysis Date:** May 12, 2026  
**Documentation Version:** OpenShift GitOps 1.19  
**Reference:** Product documentation categories.docx (CCS Framework)

---

## Overview

This document maps the existing Red Hat OpenShift GitOps documentation structure to the CCS (Customer Communication Services) approved documentation categories. Each mapping includes rationale and implementation notes.

---

## CCS-Approved Categories Reference

According to the Product documentation categories.docx, the approved categories are:

1. **What's new** - Learn what has changed in the current release
2. **Discover** - Orient me to what the product is and when to use it
3. **Get started** - Perform simplest first tasks to become productive
4. **Plan** - Choose the right architecture and topology before installing
5. **Install** - Install the product in a supported and repeatable way
6. **Upgrade** - Move to a newer version safely
7. **Migrate** - Move from one system or platform to another
8. **Administer** - Operate and manage the product on an ongoing basis
9. **Develop** - Build, modify, or maintain applications or automation
10. **Configure** - Adjust system or product settings to meet desired behavior
11. **Secure** - Implement security controls and ensure compliance
12. **Observe** - Monitor, trace, and understand system behavior
13. **Integrate** - Connect to external systems, platforms, or services
14. **Optimize** - Right size deployment and tune software installations
15. **Extend** - Add capabilities or optional components
16. **Troubleshoot** - Diagnose and resolve issues
17. **Reference** - Access authoritative details, parameters, and APIs
18. **Download PDF** - Access documentation in PDF format

---

## Category Mapping Table

| # | Existing GitOps Category | Recommended CCS Category | Mapping Type | Rationale | Notes/Exceptions |
|---|--------------------------|-------------------------|--------------|-----------|------------------|
| 1 | **Release notes** | **What's new** | Direct match | Release notes content directly aligns with "what has changed in the current release" | Already correctly positioned at top of TOC |
| 2 | **Understanding OpenShift GitOps** | **Discover** | Direct match | Contains "What is GitOps?", "About OpenShift GitOps" - classic orientation content | Move to position #2 in TOC per CCS guidelines |
| 3 | **Managing cluster configuration** | **Configure** | Functional grouping | Focuses on configuring OpenShift clusters using GitOps patterns | Could also fit under Administer; context suggests Configure |
| 4 | **Installing GitOps** | **Install** | Direct match | Core installation procedures for the GitOps Operator | Already correctly named and positioned |
| 5 | **Argo CD instance** | **Configure** | Functional grouping | "Setting up a new Argo CD instance" and CR properties are configuration tasks | Post-installation configuration activities |
| 6 | **Access control and user management** | **Secure** | Direct match | RBAC, SSO, authentication - all security-focused activities | Rename to "Security and access control" for clarity |
| 7 | **Managing resource use** | **Optimize** | Direct match | Resource quotas, requests, limits align with "right sizing deployment" | CCS Optimize category fits perfectly |
| 8 | **Argo CD applications** | **Develop** | Functional grouping | Creating and deploying applications is development activity | Mix of Develop and Configure; primary focus is app creation |
| 9 | **Argo CD application sets** | **Develop** | Functional grouping | ApplicationSets are development/automation tools | Extension of application development workflow |
| 10 | **Multitenancy** | **Configure** | Functional grouping | Configuring multi-tenant architecture and isolation | Could also be Secure; primarily configuration focused |
| 11 | **Declarative cluster configuration** | **Configure** | Functional grouping | Declarative config patterns and RBAC customization | Core configuration methodology |
| 12 | **Argo CD Agent architecture** | **Discover** | Subcategory | Architecture overview content for agent model | Should be under Discover as conceptual content |
| 13 | **Argo CD Agent installation** | **Install** | Subcategory | Installation procedure for optional agent component | Could also be Extend; placing under Install for consistency |
| 14 | **Argo Rollouts** | **Extend** | Direct match | Optional component that adds progressive delivery capabilities | Perfect fit for "add capabilities or optional components" |
| 15 | **Security** | **Secure** | Direct match | Redis security, secrets management, masking - all security topics | Already correctly named; consolidate with #6 |
| 16 | **GitOps CLI (argocd) reference** | **Reference** | Direct match | CLI command reference and parameters | Move to bottom section per CCS guidelines |
| 17 | **Observability** | **Observe** | Direct match | Logging and monitoring content | Split into Observe (top-level category) |
| 18 | **GitOps workloads on infrastructure nodes** | **Optimize** | Functional grouping | Performance and placement optimization | Could also be Configure; Optimize better fits intent |
| 19 | **Troubleshooting issues** | **Troubleshoot** | Direct match | Problem diagnosis and resolution | Move to bottom section per CCS guidelines |
| 20 | **Removing GitOps** | **Install** | Subcategory | Uninstallation is part of installation lifecycle | CCS Install includes "uninstalling procedures" |

---

## Detailed Mapping Analysis

### 1. Release notes → What's new
**Mapping:** ✅ Direct match  
**Current Position:** Top of TOC  
**Recommended Action:** No change needed

**Rationale:** The "Release notes" category perfectly aligns with the CCS "What's new" category definition: "Learn what has changed in the current release."

---

### 2. Understanding OpenShift GitOps → Discover
**Mapping:** ✅ Direct match  
**Current Position:** #2 in TOC  
**Recommended Action:** Rename to "Discover OpenShift GitOps" or keep as-is

**Rationale:** 
- Contains "What is GitOps?" - orientation content
- Contains "About OpenShift GitOps" - product overview
- Aligns with CCS Discover: "Orient me to what the product is, what it does, and when I should use it"

**Current Topics:**
- What is GitOps?
- About OpenShift GitOps  
- Gathering diagnostic information for support *(Note: Last topic might belong in Troubleshoot)*

---

### 3. Managing cluster configuration → Configure
**Mapping:** 🟡 Functional grouping  
**Current Position:** #3 in TOC  
**Recommended Action:** Keep under Configure; consider renaming to "Configure cluster settings"

**Rationale:**
- "Managing" is often associated with Administer, but content focus is on configuration
- CCS Configure: "Adjust system or product settings to meet desired behavior"
- The job is to configure OpenShift clusters declaratively using GitOps

**Alternative Consideration:** Could be Administer if content evolves to operational management

---

### 4. Installing GitOps → Install
**Mapping:** ✅ Direct match  
**Current Position:** #4 in TOC  
**Recommended Action:** No change needed; excellent alignment

**Rationale:** Perfect match with CCS Install category: "Set up the product so it's running in my environment"

**Current Topics:**
- Preparing to install OpenShift GitOps
- Installing OpenShift GitOps
- Installing the GitOps CLI

---

### 5. Argo CD instance → Configure
**Mapping:** 🟡 Functional grouping  
**Current Position:** After Install  
**Recommended Action:** Merge into Configure section or keep as subsection

**Rationale:**
- "Setting up a new Argo CD instance" is post-installation configuration
- "Argo CD custom resource and component properties" is reference-style configuration
- Not core installation, but configuration of instances

**Alternative:** Could be split - setup procedure stays in Configure, CR properties move to Reference

---

### 6. Access control and user management → Secure
**Mapping:** ✅ Direct match  
**Current Position:** Middle of TOC  
**Recommended Action:** Consolidate with "Security" category (#15)

**Rationale:**
- RBAC configuration, SSO, OIDC, local user management are all security controls
- CCS Secure: "Protect my system and data, and meet security requirements"
- Authentication and authorization are core security topics

**Consolidation Plan:** Merge with category #15 to create comprehensive "Secure OpenShift GitOps" section

---

### 7. Managing resource use → Optimize
**Mapping:** ✅ Direct match  
**Current Position:** Middle of TOC  
**Recommended Action:** Rename to "Optimize resource usage" or "Optimize performance"

**Rationale:**
- Resource quotas, requests, and limits are optimization activities
- CCS Optimize: "Right size the deployment for my environment and tune existing software installations"
- Perfect semantic alignment

**Current Topics:**
- Configuring Resource Quota
- Configure resource requests and limits for GitOps plugin components

---

### 8. Argo CD applications → Develop
**Mapping:** 🟡 Functional grouping  
**Current Position:** Middle of TOC  
**Recommended Action:** Rename to "Develop with Argo CD" or "Create applications"

**Rationale:**
- Creating applications, deploying apps, managing app resources = development activities
- CCS Develop: "Create software or automation that uses this product's capabilities"
- Users are building GitOps-managed applications

**Alternative Consideration:** Some topics like "Managing application resources" could be Configure, but primary focus is application development

**Current Topics:**
- Deploying a Spring Boot application with Argo CD
- Creating an application by using the GitOps CLI
- Managing the application resources in non-control plane namespaces
- Managing application links

---

### 9. Argo CD application sets → Develop
**Mapping:** 🟡 Functional grouping  
**Current Position:** After Argo CD applications  
**Recommended Action:** Merge into "Develop" section as subsection or keep separate

**Rationale:**
- ApplicationSets are automation tools for creating multiple applications
- CCS Develop: "Build, modify, or maintain applications or automation"
- Natural extension of application development

**Consideration:** Could potentially be Extend (as it extends Argo CD capabilities), but Develop is more accurate as it's about building automation

**Current Topics:**
- Managing application set resources in non-control plane namespaces
- Using Progressive Sync in OpenShift GitOps *(Note: Progressive Sync is part of Argo Rollouts, consider moving)*

---

### 10. Multitenancy → Configure
**Mapping:** 🟡 Functional grouping  
**Current Position:** Middle of TOC  
**Recommended Action:** Keep under Configure; could also be subsection of Secure

**Rationale:**
- Multitenancy is about configuring namespace isolation and tenant boundaries
- CCS Configure: "Set up or tune the product to behave the way I need"
- Could also fit Secure (isolation for security), but primary job is configuration

**Current Topics:**
- Multitenancy support in GitOps

**Recommendation:** Consider expanding this section or merging with related configuration topics

---

### 11. Declarative cluster configuration → Configure
**Mapping:** 🟡 Functional grouping  
**Current Position:** Middle of TOC  
**Recommended Action:** Rename to "Configure clusters declaratively" and consolidate with #3

**Rationale:**
- Declarative configuration is a configuration methodology
- Topics cover configuring clusters and customizing permissions
- CCS Configure fits the intent

**Current Topics:**
- Configuring an OpenShift cluster by deploying an application with cluster configurations
- Customizing permissions by creating user-defined cluster roles
- Customizing permissions by creating aggregated cluster roles
- Sharding clusters across Argo CD Application Controller replicas *(Note: Sharding could be Optimize)*

**Consolidation Opportunity:** Merge with "Managing cluster configuration" (#3) to create comprehensive cluster configuration section

---

### 12. Argo CD Agent architecture → Discover
**Mapping:** 🔵 Subcategory  
**Current Position:** Middle of TOC  
**Recommended Action:** Move to Discover section as conceptual/architectural content

**Rationale:**
- "Introduction to the Argo CD Agent architecture" is orientation content
- CCS Discover includes "conceptual diagrams (not architectural choices)"
- Should appear early in documentation to help users understand the agent model

**Current Topics:**
- Introduction to the Argo CD Agent architecture

**Recommendation:** Either merge into main Discover section or create a subsection "Architecture" under Discover

---

### 13. Argo CD Agent installation → Install
**Mapping:** 🔵 Subcategory  
**Current Position:** After Agent architecture  
**Recommended Action:** Keep under Install or move to Extend

**Rationale:**
- Installation procedure for the agent component
- CCS Install includes procedures for optional components
- However, could also be Extend since agent is an optional architectural enhancement

**Decision Factors:**
- If agent is a core supported deployment option → **Install**
- If agent is an optional add-on that extends capabilities → **Extend**

**Recommendation:** Based on documentation structure, appears to be optional, so **Extend** may be better fit

---

### 14. Argo Rollouts → Extend
**Mapping:** ✅ Direct match  
**Current Position:** Middle of TOC  
**Recommended Action:** No change needed; excellent alignment

**Rationale:**
- Argo Rollouts is an optional component that adds progressive delivery capabilities
- CCS Extend: "Enhance the product's functionality by adding supported extensions or plug-ins"
- Perfect semantic match - Rollouts extends GitOps with progressive delivery

**Current Topics:**
- Argo Rollouts overview
- Using Argo Rollouts for progressive deployment delivery
- Getting started with Argo Rollouts
- Routing traffic by using Argo Rollouts
- Various configuration and enablement topics

**Note:** "Progressive delivery" mentioned in original question is covered by this Argo Rollouts section

---

### 15. Security → Secure
**Mapping:** ✅ Direct match  
**Current Position:** Later in TOC  
**Recommended Action:** Consolidate with "Access control and user management" (#6)

**Rationale:**
- Security topics like secrets management, secure communication align perfectly with CCS Secure
- CCS Secure: "Protect my system and data, and meet security requirements"

**Current Topics:**
- Configuring secure communication with Redis
- Managing secrets securely using Secrets Store CSI driver
- Masking sensitive annotations in the Argo CD Web UI

**Consolidation Plan:** 
Merge with #6 to create comprehensive "Secure OpenShift GitOps" section:
- Access control and RBAC
- Authentication and SSO
- Secrets management
- Secure communications

---

### 16. GitOps CLI (argocd) reference → Reference
**Mapping:** ✅ Direct match  
**Current Position:** Later in TOC  
**Recommended Action:** Move to bottom section per CCS guidelines; expand coverage

**Rationale:**
- CLI commands and reference material align perfectly with CCS Reference
- CCS Reference: "Look up exact details so I can configure or automate accurately"
- Should be positioned near bottom of TOC per CCS recommendations

**Current Topics:**
- Configuring the GitOps CLI
- Logging in to the Argo CD server
- Basic GitOps argocd commands

**Recommendation:** Consider expanding to include:
- Complete CLI command reference
- API reference
- Custom Resource Definitions (CRD) specifications

---

### 17. Observability → Observe
**Mapping:** ✅ Direct match  
**Current Position:** Later in TOC  
**Recommended Action:** No change needed; excellent alignment

**Rationale:**
- Logging and monitoring content aligns perfectly with CCS Observe
- CCS Observe: "See what's happening in my system so I can understand or troubleshoot it"

**Current Topics (Subsections):**
- **Logging:**
  - Viewing Argo CD logs
- **Monitoring:**
  - Monitoring with GitOps dashboards
  - Monitoring Argo CD instances
  - Monitoring the GitOps Operator performance
  - Monitoring application health status
  - Monitoring Argo CD custom resource workloads

**Structure:** Already well-organized with Logging and Monitoring subsections

---

### 18. GitOps workloads on infrastructure nodes → Optimize
**Mapping:** 🟡 Functional grouping  
**Current Position:** Later in TOC  
**Recommended Action:** Merge into Optimize section

**Rationale:**
- Running workloads on infrastructure nodes is about performance and resource optimization
- CCS Optimize: "Right size the deployment for my environment"
- Placement optimization is a form of tuning

**Current Topics:**
- Running GitOps control plane workloads on infrastructure nodes

**Alternative:** Could be Configure, but Optimize better captures the performance/efficiency intent

**Recommendation:** Consolidate with "Managing resource use" (#7) under Optimize

---

### 19. Troubleshooting issues → Troubleshoot
**Mapping:** ✅ Direct match  
**Current Position:** Near bottom of TOC  
**Recommended Action:** Move to bottom section; expand coverage

**Rationale:**
- Perfect alignment with CCS Troubleshoot
- CCS Troubleshoot: "Fix a problem so the system works again"
- Already correctly positioned near bottom per CCS guidelines

**Current Topics:**
- Auto-reboot during Argo CD sync with machine configurations

**Gap Analysis:** Only 1 topic currently - significant opportunity to expand with:
- Common error messages and solutions
- Diagnostic procedures
- Known issues and workarounds
- Log analysis guidance

**Recommendation:** Significant expansion needed; move diagnostic gathering from Discover (#2) to here

---

### 20. Removing GitOps → Install
**Mapping:** 🔵 Subcategory  
**Current Position:** Bottom of TOC  
**Recommended Action:** Move under Install section as "Uninstalling OpenShift GitOps"

**Rationale:**
- CCS Install category explicitly includes "uninstalling procedures"
- Uninstallation is part of the installation lifecycle
- Per CCS definition: "Installation procedures... and uninstalling procedures"

**Current Topics:**
- Uninstalling OpenShift GitOps

**Recommendation:** Move this as a subsection under Install rather than standalone category

---

## Categories That Don't Cleanly Map

### Issue: "Progressive delivery"
**Status:** ✅ Resolved  
**Mapping:** This is covered under **Argo Rollouts** → **Extend**

**Rationale:** 
- Progressive delivery is implemented via Argo Rollouts (optional component)
- Topics like "Using Progressive Sync in OpenShift GitOps" are in the ApplicationSets section
- "Using Argo Rollouts for progressive deployment delivery" is in Argo Rollouts section

**Recommendation:** Consolidate all progressive delivery content under Argo Rollouts (Extend category)

---

### Issue: "Manage" / "Managing"
**Status:** 🟡 Requires mapping decision  
**Categories Affected:**
- Managing cluster configuration → Configure
- Managing resource use → Optimize
- Managing applications → Develop
- Managing secrets → Secure

**Analysis:** 
"Manage" is not a CCS-approved category. The CCS framework uses **Administer** for operational management.

**Mapping Rules:**
1. **Managing configuration** → **Configure** (setting up behavior)
2. **Managing resources/sizing** → **Optimize** (tuning deployment)
3. **Managing security/secrets** → **Secure** (protecting system)
4. **Managing applications** → **Develop** (building/maintaining apps)
5. **Managing operations** → **Administer** (ongoing operational tasks)

**Recommendation:** 
Replace "Managing" with the appropriate CCS verb based on context:
- "Managing cluster configuration" → "Configure cluster settings"
- "Managing resource use" → "Optimize resource usage"
- "Managing secrets" → "Secure secrets"

---

### Issue: Multiple "Security" sections
**Status:** ⚠️ Needs consolidation  
**Affected Categories:**
- Access control and user management (#6)
- Security (#15)

**Recommendation:** **Consolidate into single "Secure" category**

**Proposed Structure:**
```
Secure
├── Access control and RBAC
│   ├── Configuring Argo CD RBAC
│   └── Customizing permissions
├── Authentication and SSO
│   ├── Configuring SSO for Argo CD using Dex
│   ├── Configuring SSO using external OIDC providers
│   └── Managing local users in Argo CD
├── Secrets management
│   └── Managing secrets securely using Secrets Store CSI driver
└── Secure communications
    ├── Configuring secure communication with Redis
    └── Masking sensitive annotations in the Argo CD Web UI
```

---

## Missing CCS Categories

The following CCS-approved categories have **no current coverage** in GitOps 1.19 documentation:

### 1. Get started
**CCS Definition:** "Quickly learn how to do something meaningful with the product after installation"

**Gap:** No quick-start tutorial or "hello world" workflow

**Recommendation:** Create a "Get started with GitOps" guide including:
- Deploy your first application with GitOps
- Basic GitOps workflow tutorial
- Simple end-to-end example

---

### 2. Plan
**CCS Definition:** "Design and size the right deployment for my environment before committing to installation"

**Gap:** No architecture planning, sizing, or requirements guidance

**Recommendation:** Create "Plan your GitOps deployment" section:
- Architecture options and decision factors
- Sizing and capacity planning
- System requirements
- Deployment topology choices

**Note:** Some content in "Preparing to install" might belong here

---

### 3. Upgrade
**CCS Definition:** "Update the product without disrupting my environment"

**Gap:** No upgrade procedures or version migration guidance

**Recommendation:** Create "Upgrade OpenShift GitOps" section:
- Upgrade paths and procedures
- Version compatibility
- Migration considerations
- Rollback procedures

---

### 4. Migrate
**CCS Definition:** "Shift my data, apps, or clusters to a different environment"

**Gap:** No migration guides

**Recommendation:** Evaluate if needed; if yes, create:
- Migrating from other GitOps tools
- Moving GitOps configurations between clusters
- Backup and restore procedures

---

### 5. Integrate
**CCS Definition:** "Make this product work with other products, cloud services, or enterprise systems"

**Gap:** Integration patterns not explicitly documented as a category

**Recommendation:** Create "Integrate with external systems":
- CI/CD integration patterns
- Notification and webhook integration
- External secret management integration
- Service mesh integration

**Note:** Some integration content exists (Argo Rollouts with Service Mesh) but not organized as Integration category

---

### 6. Download PDF
**CCS Definition:** "Access the product documentation in PDF for disconnected environments"

**Gap:** Not applicable to topic map structure

**Recommendation:** Add as TOC entry at bottom per CCS guidelines

---

## Recommended TOC Reorganization

Based on CCS framework, the recommended TOC order is:

### Top Section (Fixed Order)
1. **What's new** *(Release notes)*
2. **Discover** *(Understanding OpenShift GitOps + Agent architecture)*
3. **Get started** *(NEW - create quick-start content)*
4. **Plan** *(NEW - create sizing and architecture planning)*

### Middle Section (Flexible Order)
5. **Install** *(Installing GitOps + Removing GitOps as subsection)*
6. **Upgrade** *(NEW - create upgrade procedures)*
7. **Migrate** *(NEW - if applicable)*
8. **Administer** *(NEW - operational management tasks)*
9. **Develop** *(Argo CD applications + Application sets)*
10. **Configure** *(Cluster configuration + Argo CD instances + Multitenancy)*
11. **Secure** *(CONSOLIDATED: Access control + Security)*
12. **Observe** *(Observability: Logging + Monitoring)*
13. **Integrate** *(NEW - integration patterns)*
14. **Optimize** *(CONSOLIDATED: Resource use + Infrastructure nodes)*
15. **Extend** *(Argo Rollouts + Agent installation)*

### Bottom Section (Fixed Order)
16. **Troubleshoot** *(Troubleshooting issues - EXPAND)*
17. **Reference** *(GitOps CLI reference - EXPAND)*
18. **Download PDF** *(Add TOC entry)*

---

## Summary of Mapping Types

| Mapping Type | Count | Categories |
|--------------|-------|------------|
| **Direct match** | 9 | Release notes, Understanding, Installing, Security, GitOps CLI, Observability, Argo Rollouts, Troubleshooting, Managing resource use |
| **Functional grouping** | 8 | Cluster configuration, Applications, Application sets, Multitenancy, Declarative config, Workloads on infra nodes |
| **Subcategory** | 3 | Argo CD instance, Agent architecture, Removing GitOps |
| **Requires consolidation** | 2 | Access control (merge with Security), Agent installation (decide Install vs Extend) |

---

## Implementation Priorities

### Priority 1: Quick Wins (Direct Renames)
1. "Release notes" → "What's new" ✅
2. "Managing resource use" → "Optimize" ✅
3. "Security" + "Access control" → "Secure" (consolidate)
4. Position Reference and Troubleshoot at bottom ✅

### Priority 2: Reorganization
5. Move "Removing GitOps" under Install
6. Move "Agent architecture" to Discover
7. Consolidate cluster configuration topics under Configure
8. Consolidate optimization topics under Optimize

### Priority 3: New Content
9. Create "Get started" quick-start guide
10. Create "Plan" deployment planning guide
11. Create "Upgrade" procedures
12. Expand "Troubleshoot" with more scenarios
13. Expand "Reference" with API and CRD docs

---

## Conclusion

The OpenShift GitOps 1.19 documentation has **strong coverage in 9 categories** with direct CCS alignment. The main work required is:

1. **Consolidation** of security topics
2. **Reorganization** of configuration and optimization topics  
3. **Creation** of missing foundational categories (Get started, Plan, Upgrade)
4. **Expansion** of underdeveloped categories (Troubleshoot, Reference)

The "Progressive delivery" content is appropriately covered under Argo Rollouts (Extend), and "Managing" categories map cleanly to Configure, Optimize, Develop, and Secure based on context.

---

**Document Version:** 1.0  
**Last Updated:** May 12, 2026  
**Status:** Ready for review and implementation
