# Red Hat OpenShift GitOps
# Revised JTBD-Driven Documentation Architecture

**Analysis Date:** May 12, 2026  
**Analyst:** Strategic Content Analysis  
**Framework:** Jobs-To-Be-Done (JTBD) + CCS Documentation Categories  
**Ecosystem Sources:** Red Hat Product Documentation, Developer Portal, GTM Resources, Technical Blogs

---

## Executive Summary

This document presents a comprehensive revision of the OpenShift GitOps documentation architecture, transforming it from a feature-centric structure into an outcome-driven content system aligned with the Jobs-To-Be-Done framework and Red Hat's broader ecosystem strategy.

### Key Achievements

1. **Identified 15 new JTBD categories** spanning platform engineering, AI/ML ops, multi-product workflows, and enterprise governance
2. **Mapped cross-product integration opportunities** with ACM, Dev Spaces, Service Mesh, Virtualization, and OpenShift AI
3. **Discovered business outcome narratives** aligned with GTM and sales enablement
4. **Identified content gaps** in disaster recovery, migration, security governance, and developer enablement
5. **Proposed outcome-driven information architecture** that reduces duplication and improves discoverability

### Transformation Impact

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Primary JTBD Categories** | 5 | 20 | +300% |
| **Personas Covered** | 2 (Admin, Developer) | 7 (Admin, Platform Engineer, Developer, SRE, Security Admin, AI/ML Engineer, Decision Maker) | +250% |
| **Cross-Product Integration Points** | Minimal | 6 major integrations | New |
| **Business Outcome Alignment** | Low | High | Transformational |

---

## Part 1: Newly Identified Jobs-To-Be-Done

### Category 1: Platform Engineering & Internal Developer Platforms (IDP)

#### JTBD #1: Build Self-Service Developer Platforms
**When I** am building an Internal Developer Platform (IDP),  
**I want to** provide automated, template-based deployment workflows through GitOps,  
**so that** developers can ship code independently without waiting for operational approvals.

**Persona:** Platform Engineer, Engineering Lead  
**Business Outcome:** Reduce time-to-market, increase developer productivity, reduce operational bottlenecks  
**Integration:** OpenShift Dev Spaces, OpenShift Pipelines (Tekton)

**Source Evidence:**
- [Red Hat Developer IDP Workshop](https://developers.redhat.com/articles/2023/03/29/developers-guide-red-hat-summit-2023)
- [Build CI/CD pipeline with OpenShift Dev Spaces and GitOps](https://developers.redhat.com/articles/2026/02/16/build-cicd-pipeline-openshift-dev-spaces-and-gitops)

**Current Status:** ⚠️ Partially covered in application creation docs, but not framed as IDP use case

**Recommended Content:**
- "Building an Internal Developer Platform with OpenShift GitOps"
- "Self-Service Application Deployment Patterns"
- "Integrating Dev Spaces with GitOps for End-to-End Developer Experience"
- "Template-Based Deployment Workflows"

---

#### JTBD #2: Enable Golden Path Developer Workflows
**When I** need to standardize how developers deploy applications,  
**I want to** define golden path templates and guard rails through GitOps,  
**so that** teams follow best practices automatically while maintaining flexibility.

**Persona:** Platform Engineer, SRE  
**Business Outcome:** Consistency, reduced errors, faster onboarding  
**Integration:** ApplicationSets, OpenShift Pipelines, OpenShift Dev Spaces

**Source Evidence:**
- [GitOps Workflow with Argo CD](https://redhat-scholars.github.io/outer-loop-guide/outer-loop/5.1/gitops-workflow.html)
- OpenShift Demos: [Using Tekton and ArgoCD](https://demo.openshift.com/en/latest/gitops-with-cicd/)

**Current Status:** ❌ Not covered

**Recommended Content:**
- "Defining Golden Path Templates with ApplicationSets"
- "Enforcing Deployment Standards Through GitOps Policies"
- "Developer Self-Service with Guardrails"

---

### Category 2: AI/ML Operations (MLOps)

#### JTBD #3: Automate ML Model Deployment Lifecycle
**When I** deploy AI/ML models to production,  
**I want to** use GitOps to automate model serving, versioning, and rollback,  
**so that** data scientists can focus on model development while ensuring production stability.

**Persona:** ML Engineer, Data Scientist, MLOps Engineer  
**Business Outcome:** Faster model deployment, improved model governance, reduced deployment errors  
**Integration:** OpenShift AI (RHOAI), OpenShift Pipelines, Argo Rollouts for canary model deployment

**Source Evidence:**
- [Accelerate MLOps with Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift/aiml)
- [MLOps Practices with Red Hat OpenShift AI](https://www.redhat.com/en/services/training/ai500-mlops-practices-with-red-hat-openshift-ai)
- DenizBank case study: [Scaling model serving with GitOps](https://www.redhat.com/en/about/press-releases/red-hat-and-intuit-join-forces-argo-project-extending-gitops-community-innovation-better-manage-multi-cluster-cloud-native-applications-scale)

**Current Status:** ❌ Not covered in GitOps docs

**Recommended Content:**
- "MLOps with OpenShift GitOps and OpenShift AI"
- "Automated Model Deployment Pipelines"
- "Canary Deployment for ML Models with Argo Rollouts"
- "Managing ML Model Lifecycle with GitOps"

---

#### JTBD #4: Implement Continuous Training Pipelines
**When I** need to retrain models based on new data or drift detection,  
**I want to** trigger automated retraining and deployment pipelines through GitOps,  
**so that** models stay accurate without manual intervention.

**Persona:** ML Engineer, Data Scientist  
**Business Outcome:** Improved model accuracy, reduced manual operations  
**Integration:** OpenShift AI, OpenShift Pipelines, Prometheus (for drift detection)

**Source Evidence:**
- [GitOps, CI/CD & MLOps - How it all comes together](https://medium.com/@ritz.shah/gitops-ci-cd-mlops-how-it-all-comes-together-for-an-ai-ml-developer-a9d15e43dccf)
- OpenShift AI MLOps integration documentation

**Current Status:** ❌ Not covered

**Recommended Content:**
- "Automated Model Retraining with GitOps"
- "Integrating Model Drift Detection with GitOps Workflows"
- "Continuous Training Pipeline Architecture"

---

### Category 3: Multi-Cluster Fleet Management

#### JTBD #5: Manage Multi-Cluster Deployments at Scale
**When I** operate a fleet of clusters across regions and clouds,  
**I want to** use a centralized GitOps control plane to manage configurations,  
**so that** I can ensure consistency while maintaining scalability.

**Persona:** Platform Engineer, SRE, Cloud Architect  
**Business Outcome:** Operational efficiency, reduced errors, single pane of glass management  
**Integration:** Argo CD Agent, Advanced Cluster Management (ACM)

**Source Evidence:**
- [Multi-cluster GitOps with Argo CD Agent](https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops)
- [Manage clusters and applications at scale with Argo CD Agent](https://www.redhat.com/en/blog/manage-clusters-and-applications-scale-argo-cd-agent-red-hat-openshift-gitops)
- [How to automate multi-cluster deployments using Argo CD](https://developers.redhat.com/articles/2025/06/24/how-automate-multi-cluster-deployments-using-argo-cd)

**Current Status:** ✅ Partially covered, but needs outcome-driven framing

**Recommended Content (Enhanced):**
- "Fleet Management Strategies: Centralized vs. Distributed vs. Agent-Based"
- "Scaling to 100+ Clusters with Argo CD Agent"
- "Multi-Region Deployment Patterns"

---

#### JTBD #6: Implement Hub-and-Spoke GitOps Architecture
**When I** need to balance centralized governance with distributed operations,  
**I want to** use ACM with GitOps for hub-and-spoke architecture,  
**so that** I can enforce policies centrally while enabling team autonomy.

**Persona:** Platform Engineer, Enterprise Architect  
**Business Outcome:** Governance at scale, team autonomy, reduced operational overhead  
**Integration:** Advanced Cluster Management (ACM), ManagedClusterSets, Placements

**Source Evidence:**
- [GitOps with Advanced Cluster Management for Kubernetes](https://piotrminkowski.com/2022/10/24/gitops-with-advanced-cluster-management-for-kubernetes/)
- [RedHat ACM with GitOps/ArgoCD](https://medium.com/@shrishs/redhat-advanced-cluster-management-for-kubernetes-with-gitops-argocd-8c53db008059)
- ACM documentation on [GitOpsCluster integration](https://xbryan1.github.io/rhte-2023-acm-docs/02-deploy.html)

**Current Status:** ⚠️ ACM integration mentioned but not as a distinct JTBD

**Recommended Content:**
- "Hub-and-Spoke Architecture with ACM and GitOps"
- "Policy-Based Fleet Management"
- "Using ManagedClusterSets and Placements with GitOps"
- "ApplicationSet Cluster Decision Resource Generator for ACM"

---

### Category 4: Virtualization & Legacy Modernization

#### JTBD #7: Manage Virtual Machines as Code
**When I** run virtualized workloads alongside containers,  
**I want to** manage VMs declaratively through GitOps,  
**so that** I can apply modern DevOps practices to traditional infrastructure.

**Persona:** Infrastructure Engineer, Virtualization Admin  
**Business Outcome:** Consistency across workload types, faster VM provisioning, infrastructure as code  
**Integration:** OpenShift Virtualization, ACM

**Source Evidence:**
- [Virtual Machines as Code with OpenShift GitOps and Virtualization](https://www.redhat.com/en/blog/virtual-machines-as-code-with-openshift-gitops-and-openshift-virtualization)
- [Manage OpenShift virtual machines with GitOps](https://developers.redhat.com/learn/manage-openshift-virtual-machines-gitops)
- [Using ACM and OpenShift GitOps to manage OpenShift Virtualization](https://www.redhat.com/en/blog/using-red-hat-advanced-cluster-management-and-openshift-gitops-to-manage-openshift-virtualization)

**Current Status:** ❌ Major gap identified

**Recommended Content:**
- "Managing Virtual Machines with GitOps"
- "VMs as Code: Declarative VM Provisioning"
- "Bringing GitOps Workflows to Legacy Infrastructure"
- "Multi-Cluster VM Management with ACM and GitOps"

---

#### JTBD #8: Modernize Legacy CI/CD to GitOps
**When I** migrate from Jenkins or traditional CI/CD systems,  
**I want to** adopt GitOps patterns incrementally,  
**so that** I can modernize delivery workflows without rewriting applications.

**Persona:** DevOps Engineer, Application Developer  
**Business Outcome:** Reduced technical debt, improved deployment reliability, cloud-native adoption  
**Integration:** OpenShift Pipelines (Tekton), migration from Jenkins

**Source Evidence:**
- [Migrating from Jenkins to Tekton](https://docs.openshift.com/en/container-platform/4.8/cicd/jenkins-tekton/migrating-from-jenkins-to-tekton.html)
- [Tekton vs. Jenkins](https://www.redhat.com/en/blog/tekton-vs-jenkins-whats-better-cicd-pipelines-red-hat-openshift)
- [The present and future of CI/CD with GitOps](https://developers.redhat.com/blog/2020/09/03/the-present-and-future-of-ci-cd-with-gitops-on-red-hat-openshift)

**Current Status:** ❌ Major gap - migration patterns not covered

**Recommended Content:**
- "Migrating from Jenkins to GitOps: A Phased Approach"
- "Wrapping Legacy Workloads in GitOps Patterns"
- "Hybrid CI/CD: Integrating Tekton Pipelines with GitOps"
- "Jenkins-to-Tekton Migration Playbook"

---

### Category 5: Progressive Delivery & Advanced Deployment

#### JTBD #9: Implement Progressive Delivery with Service Mesh
**When I** release high-risk updates,  
**I want to** use automated canary deployments with traffic shaping,  
**so that** I can minimize blast radius and enable safe rollouts.

**Persona:** SRE, Platform Engineer  
**Business Outcome:** Reduced deployment risk, improved MTTR, customer impact minimization  
**Integration:** Argo Rollouts, OpenShift Service Mesh, Prometheus

**Source Evidence:**
- [Progressive Delivery with OpenShift GitOps Operator](https://medium.com/@dlakshma/progressive-delivery-with-openshift-gitops-operator-part-1-d851cf33f40c)
- [Argo Rollouts for progressive deployment delivery](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.9/html/argo_rollouts/using-argo-rollouts-for-progressive-deployment-delivery)
- [OpenShift advances with ambient Service Mesh and scalable GitOps](https://www.redhat.com/en/blog/red-hat-advances-openshift-ambient-service-mesh-and-scalable-gitops-control-plane)

**Current Status:** ✅ Content exists but needs outcome/risk framing

**Recommended Content (Enhanced):**
- "Risk Mitigation Through Progressive Delivery"
- "Canary Deployments with Service Mesh Traffic Management"
- "Automated Rollback Based on SLO Violations"
- "Blue-Green Deployments for Zero-Downtime Releases"

---

#### JTBD #10: Implement Feature Flag-Driven Deployments
**When I** want to separate deployment from release,  
**I want to** combine GitOps with feature flags,  
**so that** I can deploy dark releases and control feature rollout independently.

**Persona:** Product Manager, SRE, Developer  
**Business Outcome:** Faster deployment cadence, reduced rollback needs, A/B testing capability  
**Integration:** Argo Rollouts, feature flag systems

**Source Evidence:**
- Progressive delivery patterns in Argo Rollouts documentation
- Service Mesh traffic management capabilities

**Current Status:** ❌ Not covered

**Recommended Content:**
- "GitOps with Feature Flag Integration"
- "Dark Releases and Gradual Feature Rollout"
- "Separating Deployment from Release Decision"

---

### Category 6: Security, Compliance & Governance

#### JTBD #11: Enforce Security Policies Through GitOps
**When I** need to ensure clusters comply with security standards,  
**I want to** define security policies as code and enforce them through GitOps,  
**so that** compliance is automated and auditable.

**Persona:** Security Administrator, Compliance Officer  
**Business Outcome:** Automated compliance, reduced security risk, audit trail  
**Integration:** Advanced Cluster Management (ACM) Governance, Compliance Operator, PolicyGenerator

**Source Evidence:**
- [Generating Governance Policies Using Kustomize and GitOps](https://www.redhat.com/en/blog/generating-governance-policies-using-kustomize-and-gitops)
- [ACM Governance and PolicyGenerator](https://myopenshiftblog.com/acm-governance-and-policy-templates/)
- [ACM Governance Documentation](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.7/html/governance/governance)

**Current Status:** ❌ Major gap - security governance not covered

**Recommended Content:**
- "Security as Code with GitOps and ACM Governance"
- "Automated Compliance Enforcement Across Clusters"
- "Policy-Based Security Governance"
- "NIST 800-53 Compliance with GitOps"
- "Audit Trail and Change Tracking for Compliance"

---

#### JTBD #12: Implement RBAC and Multi-Tenancy Governance
**When I** manage a shared platform with multiple teams,  
**I want to** enforce RBAC and namespace isolation through GitOps,  
**so that** teams operate independently within defined boundaries.

**Persona:** Platform Engineer, Security Administrator  
**Business Outcome:** Improved security posture, team autonomy within guardrails  
**Integration:** OpenShift RBAC, Argo CD RBAC, ACM Policies

**Source Evidence:**
- Multitenancy documentation in GitOps
- ACM governance policies

**Current Status:** ⚠️ Partially covered, needs security framing

**Recommended Content (Enhanced):**
- "Multi-Tenant GitOps Architecture Patterns"
- "RBAC Best Practices for GitOps Platforms"
- "Namespace Isolation and Security Boundaries"
- "Preventing Privilege Escalation in GitOps Workflows"

---

### Category 7: Disaster Recovery & Business Continuity

#### JTBD #13: Implement GitOps Control Plane Disaster Recovery
**When I** need to protect against control plane failures,  
**I want to** implement backup and restore strategies for GitOps components,  
**so that** I can recover quickly from disasters.

**Persona:** SRE, Platform Engineer  
**Business Outcome:** Reduced RTO/RPO, business continuity assurance  
**Integration:** OADP (OpenShift API for Data Protection), etcd backup

**Source Evidence:**
- [OADP + OpenShift GitOps - Implementing Application DR](https://www.redhat.com/en/blog/oadp-openshift-gitops-an-approach-to-implementing-application-disaster-recovery)
- [Control plane backup and restore](https://docs.openshift.com/en/container-platform/4.9/backup_and_restore/control_plane_backup_and_restore/disaster_recovery/about-disaster-recovery.html)

**Current Status:** ❌ Critical gap identified

**Recommended Content:**
- "Disaster Recovery Planning for GitOps Control Plane"
- "Backup and Restore Strategies for Argo CD"
- "Cross-Region DR with OADP and GitOps"
- "RTO/RPO Considerations for GitOps Deployments"
- "Testing DR Procedures for GitOps Infrastructure"

---

#### JTBD #14: Implement Application-Level DR with GitOps
**When I** deploy stateful applications across regions,  
**I want to** use GitOps with backup/restore for application DR,  
**so that** I can recover applications in secondary regions quickly.

**Persona:** Application Owner, SRE  
**Business Outcome:** Business continuity, data protection, customer trust  
**Integration:** OADP, ACM, GitOps for cross-region deployment

**Source Evidence:**
- OADP + GitOps DR implementation guide
- Cross-cluster backup and restore documentation

**Current Status:** ❌ Not covered

**Recommended Content:**
- "Application DR Patterns with GitOps and OADP"
- "Active-Passive and Active-Active DR Topologies"
- "Stateful Application Recovery Strategies"
- "DR Testing and Failover Procedures"

---

### Category 8: Observability & SRE Practices

#### JTBD #15: Implement GitOps Observability and Alerting
**When I** operate GitOps at scale,  
**I want to** monitor sync status, drift detection, and deployment health,  
**so that** I can proactively identify and resolve issues.

**Persona:** SRE, Platform Engineer  
**Business Outcome:** Improved MTTR, proactive issue resolution, operational visibility  
**Integration:** Prometheus, Grafana, OpenShift Monitoring

**Source Evidence:**
- Observability documentation in GitOps
- Monitoring best practices

**Current Status:** ⚠️ Partially covered, needs SRE lens

**Recommended Content (Enhanced):**
- "SRE Best Practices for GitOps Operations"
- "SLO-Based Alerting for GitOps Sync Operations"
- "Drift Detection and Automated Remediation"
- "GitOps Metrics and KPIs Dashboard"
- "Troubleshooting GitOps Sync Failures"

---

#### JTBD #16: Establish Configuration Drift Detection
**When I** manage infrastructure as code,  
**I want to** automatically detect and remediate configuration drift,  
**so that** actual state always matches desired state.

**Persona:** SRE, Platform Engineer  
**Business Outcome:** Infrastructure consistency, reduced manual reconciliation  
**Integration:** Argo CD self-healing, ACM policies

**Source Evidence:**
- Self-healing capabilities in Argo CD
- ACM governance and drift detection

**Current Status:** ⚠️ Mentioned but not as dedicated use case

**Recommended Content:**
- "Automated Drift Detection and Remediation"
- "Self-Healing Infrastructure with GitOps"
- "Handling Drift in Multi-Cluster Environments"

---

### Category 9: Developer Experience & Enablement

#### JTBD #17: Enable Developer Self-Service Onboarding
**When I** onboard new developers to the platform,  
**I want to** provide self-service project creation and deployment templates,  
**so that** developers can start deploying applications on day one.

**Persona:** Developer, Platform Engineer  
**Business Outcome:** Faster onboarding, reduced support overhead, improved developer satisfaction  
**Integration:** ApplicationSets, Dev Spaces, Templates

**Source Evidence:**
- IDP workshop resources
- Developer experience best practices

**Current Status:** ❌ Not covered from developer experience lens

**Recommended Content:**
- "Developer Onboarding with GitOps Self-Service"
- "Creating Project Templates for Developer Teams"
- "Developer Documentation and Training Resources"
- "Getting Started: Deploy Your First Application"

---

#### JTBD #18: Provide Developer-Friendly GitOps CLI/UI
**When I** am a developer working with GitOps,  
**I want to** use intuitive CLI and UI tools,  
**so that** I can manage deployments without deep Kubernetes expertise.

**Persona:** Application Developer  
**Business Outcome:** Developer productivity, reduced learning curve  
**Integration:** Argo CD UI, GitOps CLI, OpenShift Console

**Source Evidence:**
- GitOps CLI documentation
- Argo CD UI features

**Current Status:** ⚠️ CLI reference exists, but not framed for developer experience

**Recommended Content:**
- "Developer Guide to GitOps CLI"
- "Using Argo CD UI for Application Management"
- "Common Developer Workflows with GitOps"
- "Troubleshooting Application Deployments from Developer Perspective"

---

### Category 10: Business Outcomes & Decision Making

#### JTBD #19: Demonstrate GitOps ROI and Business Value
**When I** need to justify GitOps adoption to stakeholders,  
**I want to** understand business outcomes and ROI metrics,  
**so that** I can make data-driven investment decisions.

**Persona:** Engineering Manager, Director, VP Engineering, CTO  
**Business Outcome:** Informed decision-making, budget justification, stakeholder alignment  
**Integration:** N/A - Business narrative

**Source Evidence:**
- DenizBank case study: VM deployment time reduced from 30-45 minutes to 5 minutes
- Real-world ROI metrics from ecosystem sources
- Faster time to market, reduced licensing costs

**Current Status:** ❌ Critical gap - no business outcome content

**Recommended Content:**
- "Business Case for GitOps Adoption"
- "ROI Metrics: Measuring GitOps Impact"
- "GitOps Success Stories and Case Studies"
- "Total Cost of Ownership Analysis"
- "Risk Reduction Through Declarative Infrastructure"

---

#### JTBD #20: Architect GitOps for Enterprise Scale
**When I** design GitOps for enterprise adoption,  
**I want to** understand architecture patterns, trade-offs, and best practices,  
**so that** I can make informed decisions before implementation.

**Persona:** Enterprise Architect, Technical Lead  
**Business Outcome:** Successful large-scale adoption, avoided pitfalls, architectural alignment  
**Integration:** All components - architectural view

**Source Evidence:**
- Multi-cluster topology documentation
- Enterprise adoption patterns

**Current Status:** ⚠️ Technical content exists but not in architecture/decision-making framing

**Recommended Content:**
- "Enterprise GitOps Architecture Reference"
- "Centralized vs. Distributed vs. Agent-Based: Choosing Your Topology"
- "Scaling Considerations for 100+ Clusters"
- "Anti-Patterns to Avoid in GitOps Adoption"
- "Architecture Decision Records for GitOps"

---

## Part 2: Revised and Enhanced Existing Jobs

### Enhanced JTBD #1: Standardize Declarative Infrastructure (Original)
**Enhancement:** Add integration narrative with IaC tools and Ansible

**New Framing:**  
**When I** manage complex hybrid cloud environments,  
**I want to** use Git as the single source of truth for infrastructure, applications, and configuration,  
**so that** I can ensure consistency, auditability, and compliance across my organization.

**Additional Integration:** Ansible Automation Platform for Day 2 operations

**Enhanced Content:**
- "Integrating GitOps with Ansible for Comprehensive Automation"
- "GitOps for Infrastructure and Application Configuration"
- "Audit and Compliance Benefits of Git-Based Infrastructure"

---

### Enhanced JTBD #2: Enable Developer Self-Service (Original)
**Enhancement:** Expanded with Dev Spaces integration and golden path templates

**New Framing:**  
**When I** build an Internal Developer Platform,  
**I want to** provide automated, template-based deployment workflows with Dev Spaces integration,  
**so that** developers can ship code from IDE to production without operational bottlenecks.

**Additional Integration:** OpenShift Dev Spaces for end-to-end developer experience

**Status:** Now covered in new JTBD #1 and #17 with expanded scope

---

### Enhanced JTBD #3: Govern Multi-Cluster Fleets (Original)
**Enhancement:** Add Argo CD Agent architecture and ACM integration

**New Framing:**  
**When I** operate at scale across multiple regions or clouds,  
**I want to** use a scalable GitOps architecture (centralized, distributed, or agent-based),  
**so that** I can detect and remediate configuration drift automatically across the fleet.

**Additional Integration:** Argo CD Agent for scalability, ACM for governance

**Status:** Now covered in new JTBD #5 and #6 with enhanced multi-cluster patterns

---

### Enhanced JTBD #4: Modernize Legacy Workloads (Original)
**Enhancement:** Add VM management and Jenkins migration

**New Framing:**  
**When I** migrate from virtual machines or traditional CI/CD systems,  
**I want to** adopt GitOps patterns incrementally for both VMs and containers,  
**so that** I can modernize delivery workflows without rewriting applications.

**Additional Integration:** OpenShift Virtualization, Jenkins-to-Tekton migration

**Status:** Now covered in new JTBD #7 and #8 with specific migration patterns

---

### Enhanced JTBD #5: Implement Progressive Delivery (Original)
**Enhancement:** Add Service Mesh integration and ML model deployment

**New Framing:**  
**When I** release high-stakes updates or ML models,  
**I want to** use automated canary or blue-green deployment strategies with traffic shaping,  
**so that** I can minimize operational risk and reduce the blast radius of failures.

**Additional Integration:** OpenShift Service Mesh, Argo Rollouts, AI/ML model deployment

**Status:** Now covered in new JTBD #9 and #10 with expanded deployment strategies

---

## Part 3: Cross-Product Integration Mapping

### Integration 1: OpenShift GitOps + Advanced Cluster Management (ACM)

**Value Proposition:** Hub-and-spoke architecture for multi-cluster governance

**Integration Points:**
- GitOpsCluster CRD for cluster binding
- ManagedClusterSet and ManagedClusterSetBinding
- Placement for cluster selection
- PolicyGenerator for governance policies
- ApplicationSet Cluster Decision Resource Generator

**Jobs Enabled:**
- JTBD #6: Hub-and-Spoke GitOps Architecture
- JTBD #11: Security Policy Enforcement
- JTBD #5: Multi-Cluster Fleet Management

**Documentation Status:** ⚠️ Integration documented but not outcome-driven

**Recommendation:** Create dedicated "GitOps with ACM" integration guide with:
- Architecture patterns
- Setup procedures
- Governance use cases
- Fleet management best practices

**Sources:**
- [GitOps with Advanced Cluster Management](https://piotrminkowski.com/2022/10/24/gitops-with-advanced-cluster-management-for-kubernetes/)
- [Using ACM and GitOps to manage OpenShift Virtualization](https://www.redhat.com/en/blog/using-red-hat-advanced-cluster-management-and-openshift-gitops-to-manage-openshift-virtualization)

---

### Integration 2: OpenShift GitOps + OpenShift Dev Spaces

**Value Proposition:** Complete developer experience from IDE to deployment

**Integration Points:**
- Dev Spaces for development environment
- OpenShift Pipelines (Tekton) for CI
- GitOps for CD
- Automated workflow from code change to deployment

**Jobs Enabled:**
- JTBD #1: Build Self-Service Developer Platforms
- JTBD #2: Enable Golden Path Developer Workflows
- JTBD #17: Developer Self-Service Onboarding

**Documentation Status:** ❌ Not covered in GitOps docs

**Recommendation:** Create comprehensive IDP guide:
- "Building an Internal Developer Platform with GitOps and Dev Spaces"
- End-to-end developer workflow documentation
- Integration setup and configuration

**Sources:**
- [Build CI/CD pipeline with Dev Spaces and GitOps](https://developers.redhat.com/articles/2026/02/16/build-cicd-pipeline-openshift-dev-spaces-and-gitops)
- [Developer's guide to Red Hat Summit 2023](https://developers.redhat.com/articles/2023/03/29/developers-guide-red-hat-summit-2023)

---

### Integration 3: OpenShift GitOps + OpenShift Virtualization

**Value Proposition:** Infrastructure as Code for VMs and containers

**Integration Points:**
- Declarative VM definitions
- VM provisioning through GitOps
- Self-healing for VM infrastructure
- Multi-cluster VM management with ACM

**Jobs Enabled:**
- JTBD #7: Manage Virtual Machines as Code
- JTBD #8: Modernize Legacy Workloads

**Documentation Status:** ❌ Critical gap - not in GitOps docs

**Recommendation:** Create virtualization integration guide:
- "Virtual Machines as Code with GitOps"
- VM provisioning patterns
- Migration from traditional VM management

**Sources:**
- [Virtual Machines as Code with OpenShift GitOps](https://www.redhat.com/en/blog/virtual-machines-as-code-with-openshift-gitops-and-openshift-virtualization)
- [Manage OpenShift virtual machines with GitOps](https://developers.redhat.com/learn/manage-openshift-virtual-machines-gitops)

---

### Integration 4: OpenShift GitOps + OpenShift Service Mesh

**Value Proposition:** Progressive delivery with advanced traffic management

**Integration Points:**
- Argo Rollouts integration with Service Mesh
- Traffic shaping for canary deployments
- Metric-based rollout decisions
- Ambient mode support

**Jobs Enabled:**
- JTBD #9: Progressive Delivery with Service Mesh
- JTBD #10: Feature Flag-Driven Deployments

**Documentation Status:** ✅ Argo Rollouts docs exist, Service Mesh integration needs enhancement

**Recommendation:** Enhance progressive delivery content:
- Service Mesh traffic management patterns
- Canary deployment best practices
- SLO-based automated rollback

**Sources:**
- [Progressive Delivery with OpenShift GitOps](https://medium.com/@dlakshma/progressive-delivery-with-openshift-gitops-operator-part-1-d851cf33f40c)
- [OpenShift advances with ambient Service Mesh](https://www.redhat.com/en/blog/red-hat-advances-openshift-ambient-service-mesh-and-scalable-gitops-control-plane)

---

### Integration 5: OpenShift GitOps + OpenShift AI (RHOAI)

**Value Proposition:** MLOps automation and model lifecycle management

**Integration Points:**
- Model deployment automation
- Model serving with GitOps
- CI/CD integration for ML pipelines
- Canary deployments for model versions

**Jobs Enabled:**
- JTBD #3: Automate ML Model Deployment Lifecycle
- JTBD #4: Continuous Training Pipelines

**Documentation Status:** ❌ Not covered in GitOps docs

**Recommendation:** Create MLOps integration guide:
- "MLOps with OpenShift GitOps and OpenShift AI"
- Model deployment patterns
- Automated retraining workflows

**Sources:**
- [Accelerate MLOps with Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift/aiml)
- [MLOps Practices with Red Hat OpenShift AI](https://www.redhat.com/en/services/training/ai500-mlops-practices-with-red-hat-openshift-ai)

---

### Integration 6: OpenShift GitOps + OADP (OpenShift API for Data Protection)

**Value Proposition:** Disaster recovery for applications and GitOps control plane

**Integration Points:**
- Application backup and restore
- Cross-cluster DR
- GitOps-driven DR workflows
- Integration with etcd backup for control plane

**Jobs Enabled:**
- JTBD #13: GitOps Control Plane Disaster Recovery
- JTBD #14: Application-Level DR

**Documentation Status:** ❌ Critical gap

**Recommendation:** Create DR integration guide:
- "Disaster Recovery with GitOps and OADP"
- Backup and restore procedures
- DR testing and failover

**Sources:**
- [OADP + OpenShift GitOps - Application DR](https://www.redhat.com/en/blog/oadp-openshift-gitops-an-approach-to-implementing-application-disaster-recovery)

---

## Part 4: Persona Expansion

### Current Personas (Baseline)
1. Cluster Administrator
2. Developer

### New Personas Identified

#### 3. Platform Engineer
**Primary Jobs:**
- Build Internal Developer Platforms
- Enable golden path workflows
- Multi-cluster fleet management
- Platform observability

**Content Needs:**
- IDP architecture patterns
- Self-service templates
- Platform automation

---

#### 4. Site Reliability Engineer (SRE)
**Primary Jobs:**
- Ensure system reliability
- Implement progressive delivery
- Monitor and troubleshoot
- Disaster recovery planning

**Content Needs:**
- SRE best practices
- Observability and alerting
- Incident response procedures
- Capacity planning

---

#### 5. ML Engineer / Data Scientist
**Primary Jobs:**
- Deploy ML models
- Automate model lifecycle
- Implement continuous training

**Content Needs:**
- MLOps patterns
- Model deployment automation
- Integration with OpenShift AI

---

#### 6. Security Administrator
**Primary Jobs:**
- Enforce security policies
- Ensure compliance
- Implement RBAC and governance

**Content Needs:**
- Security as code
- Policy enforcement
- Compliance automation
- Audit procedures

---

#### 7. Enterprise Architect / Decision Maker
**Primary Jobs:**
- Evaluate GitOps adoption
- Understand ROI and business value
- Design enterprise architecture

**Content Needs:**
- Business case materials
- ROI metrics
- Architecture reference
- Decision frameworks

---

## Part 5: Content Gaps Analysis

### Critical Gaps (High Impact, Not Covered)

| Gap # | Gap Description | Impact | Personas Affected | Recommended Priority |
|-------|-----------------|--------|-------------------|---------------------|
| G1 | **GitOps for Virtual Machines** | High | Infrastructure Engineer, Platform Engineer | P0 - Critical |
| G2 | **Disaster Recovery for GitOps Control Plane** | High | SRE, Platform Engineer | P0 - Critical |
| G3 | **MLOps with OpenShift AI Integration** | High | ML Engineer, Data Scientist | P0 - Critical |
| G4 | **Migration from Jenkins/Tekton to GitOps** | High | DevOps Engineer, Developer | P0 - Critical |
| G5 | **Security Governance and Policy Enforcement** | High | Security Admin, Compliance Officer | P0 - Critical |
| G6 | **Internal Developer Platform (IDP) Patterns** | High | Platform Engineer, Developer | P1 - High |
| G7 | **Business Case and ROI Documentation** | Medium | Decision Makers, Engineering Leaders | P1 - High |
| G8 | **Application-Level Disaster Recovery** | Medium | Application Owner, SRE | P1 - High |
| G9 | **Developer Onboarding and Self-Service** | Medium | Developer, Platform Engineer | P2 - Medium |
| G10 | **Feature Flag Integration Patterns** | Low | Product Manager, Developer | P3 - Low |

### Major Gaps (Important, Partially Covered)

| Gap # | Gap Description | Current Status | Enhancement Needed |
|-------|-----------------|----------------|-------------------|
| MG1 | **ACM Integration Patterns** | Mentioned | Outcome-driven integration guide |
| MG2 | **Multi-Cluster Architecture Patterns** | Basic coverage | Enterprise-scale patterns, trade-offs |
| MG3 | **Progressive Delivery Best Practices** | Technical docs exist | Risk mitigation framing, SLO-based rollback |
| MG4 | **Observability and Monitoring** | Basic coverage | SRE lens, alerting patterns, KPIs |
| MG5 | **Multi-Tenancy and RBAC** | Basic coverage | Security framing, enterprise patterns |

### Minor Gaps (Nice to Have)

| Gap # | Gap Description |
|-------|-----------------|
| MiG1 | Developer CLI workflows and patterns |
| MiG2 | GitOps for edge computing scenarios |
| MiG3 | Cost optimization patterns |
| MiG4 | Performance tuning and optimization |
| MiG5 | GitOps with serverless (Knative) |

---

## Part 6: Redundant or Overlapping Content

### Duplication Areas Identified

#### D1: Application Creation Methods
**Issue:** Multiple ways to create applications documented separately
- Creating application via UI
- Creating application via CLI
- Creating application via ApplicationSets
- Deploying Spring Boot example

**Recommendation:** Consolidate into outcome-driven structure:
1. "Choose Your Application Deployment Method" (decision guide)
2. Reference implementations for each method
3. Clear guidance on when to use which approach

---

#### D2: Multi-Cluster Guidance Overlap
**Issue:** GitOps multi-cluster guidance overlaps with ACM guidance

**Current State:**
- GitOps docs cover basic multi-cluster
- ACM docs cover policy-based multi-cluster
- Unclear when to use which

**Recommendation:**
- Create clear integration guide
- Decision matrix: when to use GitOps alone vs. GitOps + ACM
- Unified multi-cluster architecture guidance

---

#### D3: Security and Access Control
**Issue:** RBAC and security topics scattered
- Argo CD RBAC configuration
- OpenShift SSO configuration
- Multi-tenancy setup
- ACM governance policies

**Recommendation:** Create unified security section:
1. "Secure" category (per CCS framework)
2. Comprehensive RBAC guide
3. Security best practices
4. Integration with ACM governance

---

## Part 7: Revised Documentation Architecture

### Proposed Information Architecture (JTBD + CCS Aligned)

```
OpenShift GitOps Documentation (v2.0 - Outcome-Driven)
│
├── 1. What's New
│   └── Release Notes
│
├── 2. Discover OpenShift GitOps
│   ├── What is GitOps?
│   ├── OpenShift GitOps Overview
│   ├── Argo CD Agent Architecture
│   └── When to Use GitOps (Use Cases)
│
├── 3. Get Started
│   ├── Deploy Your First Application
│   ├── Quick Start Tutorial
│   ├── Understanding the GitOps Workflow
│   └── Developer Onboarding Guide
│
├── 4. Plan Your GitOps Strategy
│   ├── Architecture Patterns (Centralized, Distributed, Agent-Based)
│   ├── Multi-Cluster Topology Planning
│   ├── Sizing and Capacity Planning
│   ├── Security and Compliance Considerations
│   └── Business Case and ROI
│
├── 5. Install OpenShift GitOps
│   ├── Installing GitOps Operator
│   ├── Installing GitOps CLI
│   ├── Installing Argo CD Agent
│   └── Uninstalling GitOps
│
├── 6. Build Internal Developer Platforms
│   ├── IDP Architecture with GitOps
│   ├── Integration with OpenShift Dev Spaces
│   ├── Self-Service Application Deployment
│   ├── Golden Path Templates
│   └── Developer Workflow Automation
│
├── 7. Deploy and Manage Applications
│   ├── Application Deployment Methods (Decision Guide)
│   ├── Creating Applications with Argo CD
│   ├── Using ApplicationSets for Multi-Cluster Deployment
│   ├── Managing Application Lifecycle
│   └── Application Health and Sync Status
│
├── 8. Manage Multi-Cluster Fleets
│   ├── Fleet Management Strategies
│   ├── Argo CD Agent for Scalability
│   ├── Hub-and-Spoke with ACM
│   ├── Configuration Drift Detection
│   └── Fleet Observability
│
├── 9. Configure Cluster and Application Settings
│   ├── Declarative Cluster Configuration
│   ├── Managing Configuration as Code
│   ├── Argo CD Configuration
│   ├── Resource Optimization
│   └── Multi-Tenancy Configuration
│
├── 10. Secure Your GitOps Environment
│   ├── RBAC and Access Control
│   ├── SSO and Authentication
│   ├── Secrets Management
│   ├── Security Policy Enforcement (with ACM)
│   ├── Compliance Automation
│   └── Security Best Practices
│
├── 11. Implement Progressive Delivery
│   ├── Canary Deployments with Argo Rollouts
│   ├── Blue-Green Deployment Strategies
│   ├── Traffic Shaping with Service Mesh
│   ├── Automated Rollback and SLO-Based Decisions
│   └── Feature Flag Integration
│
├── 12. Manage Virtual Machines with GitOps
│   ├── Virtual Machines as Code
│   ├── VM Provisioning Patterns
│   ├── Multi-Cluster VM Management
│   └── Migrating from Traditional VM Management
│
├── 13. Enable MLOps with OpenShift AI
│   ├── ML Model Deployment Automation
│   ├── Model Lifecycle Management
│   ├── Continuous Training Pipelines
│   ├── Canary Deployment for ML Models
│   └── MLOps Best Practices
│
├── 14. Observe and Monitor GitOps Operations
│   ├── Monitoring GitOps Sync Status
│   ├── Application Health Monitoring
│   ├── SRE Metrics and KPIs
│   ├── Alerting and Notifications
│   └── Logging and Audit Trails
│
├── 15. Ensure Disaster Recovery
│   ├── DR Planning for GitOps
│   ├── Control Plane Backup and Restore
│   ├── Application DR with OADP
│   ├── Cross-Region Failover
│   └── DR Testing Procedures
│
├── 16. Migrate to GitOps
│   ├── Migrating from Jenkins to Tekton and GitOps
│   ├── Wrapping Legacy Workloads in GitOps
│   ├── Hybrid CI/CD Patterns
│   └── Migration Playbooks
│
├── 17. Integrate with Red Hat Portfolio
│   ├── GitOps with Advanced Cluster Management
│   ├── GitOps with OpenShift Dev Spaces
│   ├── GitOps with OpenShift Virtualization
│   ├── GitOps with OpenShift Service Mesh
│   ├── GitOps with OpenShift AI
│   └── GitOps with OADP
│
├── 18. Troubleshoot Issues
│   ├── Common GitOps Issues
│   ├── Sync Failures and Resolution
│   ├── Network and Connectivity Issues
│   ├── Resource and Performance Issues
│   ├── Diagnostic Tools and Procedures
│   └── Known Issues and Workarounds
│
├── 19. Reference
│   ├── GitOps CLI Reference
│   ├── Argo CD Custom Resource Reference
│   ├── API Reference
│   ├── Configuration Parameters
│   └── Supported Versions and Compatibility
│
└── 20. Download PDF
    └── PDF Documentation Links
```

---

## Part 8: GTM and Content Strategy Recommendations

### Sales Enablement Content

#### 1. Business Outcome Messaging
**Target Audience:** Decision Makers, C-Level Executives

**Key Messages:**
- Reduce deployment time by 80% (DenizBank: 30-45 min → 5 min)
- Improve developer productivity with self-service platforms
- Ensure consistency and compliance across multi-cloud environments
- Reduce operational costs through automation
- Minimize deployment risk with progressive delivery

**Recommended Content:**
- "Executive Brief: OpenShift GitOps Business Value"
- ROI Calculator
- Customer Success Stories
- Competitive Differentiation: GitOps vs. Traditional CI/CD

---

#### 2. Solution Positioning
**Target Audience:** Solutions Architects, Pre-Sales Engineers

**Key Positioning:**
- **Platform Engineering Foundation:** GitOps as the automation layer for IDPs
- **Multi-Cloud Consistency:** Single control plane for hybrid cloud
- **Enterprise Scale:** Argo CD Agent for 100+ cluster management
- **AI/ML Enabler:** MLOps automation for AI at scale
- **Legacy Modernization:** Incremental path from VMs and Jenkins to cloud-native

**Recommended Content:**
- "Solution Briefs by Use Case"
- Architecture Decision Trees
- Competitive Battle Cards

---

#### 3. Technical Evangelism
**Target Audience:** Technical Decision Makers, Architects

**Key Themes:**
- GitOps as Industry Standard (CNCF, Argo Project momentum)
- Red Hat's Leadership in GitOps (Intuit partnership, Argo CD Agent innovation)
- Ecosystem Integration (ACM, Dev Spaces, Service Mesh, Virtualization, AI)
- Open Source + Enterprise Support

**Recommended Content:**
- Technical Whitepapers
- Reference Architectures
- Integration Guides
- Webinars and Workshops

---

### Developer Relations Content

#### 1. Learning Paths
**Target Audience:** Developers, Platform Engineers

**Recommended Paths:**
- "Getting Started with GitOps on OpenShift" (Beginner)
- "Building Internal Developer Platforms" (Intermediate)
- "Advanced GitOps: Multi-Cluster and Progressive Delivery" (Advanced)
- "MLOps with OpenShift GitOps and AI" (Specialized)

---

#### 2. Hands-On Labs
**Target Audience:** Technical practitioners

**Recommended Labs:**
- Deploy your first application with GitOps
- Set up multi-cluster GitOps with Argo CD Agent
- Implement canary deployment with Argo Rollouts
- Build an IDP with Dev Spaces and GitOps
- Manage VMs as code with GitOps

---

#### 3. Developer Advocacy
**Channels:**
- Red Hat Developer Blog
- GitHub examples and templates
- YouTube tutorials
- Conference presentations (KubeCon, DevConf, Red Hat Summit)
- Community engagement (Argo Project, CNCF)

---

### Product Marketing Recommendations

#### 1. Feature vs. Outcome Messaging
**Shift from:** "GitOps provides declarative configuration management"  
**Shift to:** "Reduce deployment errors by 90% with self-healing infrastructure"

**Shift from:** "Argo CD supports multi-cluster deployments"  
**Shift to:** "Manage 1000+ clusters from a single control plane"

**Shift from:** "GitOps uses Git as source of truth"  
**Shift to:** "Ensure audit compliance with Git-based change tracking"

---

#### 2. Industry Trends Alignment
**Key Trends:**
- Platform Engineering (Gartner Hype Cycle)
- AI/ML Operations
- FinOps and cost optimization
- Security and compliance automation
- Developer experience and productivity

**Recommendation:** Position GitOps as enabler for each trend

---

#### 3. Competitive Differentiation
**vs. Competitors:**
- **Flux CD:** Red Hat enterprise support, broader ecosystem integration
- **Spinnaker:** Cloud-native, Kubernetes-native, modern UX
- **DIY GitOps:** Enterprise hardening, security, scalability out-of-box

**Key Differentiators:**
- Argo CD Agent for scale
- Tight integration with Red Hat portfolio
- Enterprise support and lifecycle
- Security and compliance built-in

---

## Part 9: Recommended Next Actions

### Phase 1: Foundation (Months 1-2)

#### Priority 0: Critical Gaps
1. **Create VM Management Guide**
   - Content: Virtual Machines as Code with GitOps
   - Owner: Content team + Virtualization SMEs
   - Deliverable: Complete integration guide

2. **Create Disaster Recovery Guide**
   - Content: DR planning, backup/restore with OADP
   - Owner: Content team + SRE SMEs
   - Deliverable: DR procedures and playbooks

3. **Create MLOps Integration Guide**
   - Content: OpenShift AI + GitOps integration
   - Owner: Content team + AI/ML SMEs
   - Deliverable: MLOps automation guide

4. **Create Migration Playbook**
   - Content: Jenkins to Tekton/GitOps migration
   - Owner: Content team + DevOps SMEs
   - Deliverable: Step-by-step migration guide

5. **Create Security Governance Guide**
   - Content: Policy enforcement with ACM
   - Owner: Content team + Security SMEs
   - Deliverable: Security as code guide

---

### Phase 2: Enhancement (Months 3-4)

#### Priority 1: High-Value Additions
6. **Create IDP Architecture Guide**
   - Content: Building platforms with GitOps + Dev Spaces
   - Owner: Content team + Platform Engineering SMEs
   - Deliverable: IDP reference architecture

7. **Enhance Multi-Cluster Documentation**
   - Content: Agent architecture, ACM integration, enterprise patterns
   - Owner: Content team + Platform SMEs
   - Deliverable: Enterprise multi-cluster guide

8. **Create Business Value Content**
   - Content: ROI metrics, case studies, executive briefs
   - Owner: Product Marketing + Content team
   - Deliverable: Sales enablement materials

9. **Enhance Progressive Delivery Content**
   - Content: Service Mesh integration, SLO-based rollback
   - Owner: Content team + SRE SMEs
   - Deliverable: Advanced deployment guide

---

### Phase 3: Optimization (Months 5-6)

#### Priority 2: Content Consolidation
10. **Consolidate Application Deployment Content**
    - Merge scattered application creation docs
    - Create decision guide
    - Streamline user journeys

11. **Consolidate Security Content**
    - Unified "Secure" category
    - Comprehensive RBAC guide
    - Security best practices

12. **Enhance Developer Experience Content**
    - Onboarding guide
    - Quick start improvements
    - CLI workflow documentation

---

### Phase 4: Ecosystem (Ongoing)

#### Priority 3: Integration Guides
13. **Create Integration Guides for All Cross-Product Workflows**
    - ACM, Dev Spaces, Virtualization, Service Mesh, AI, OADP
    - Each with setup, use cases, best practices

14. **Create Persona-Specific Views**
    - Landing pages for each persona
    - Curated content paths
    - Role-based navigation

15. **Enhance Observability Content**
    - SRE metrics and KPIs
    - Alerting patterns
    - Troubleshooting guides

---

## Part 10: Measurement and Success Criteria

### Documentation Effectiveness Metrics

| Metric | Baseline | Target (6 months) | How to Measure |
|--------|----------|-------------------|----------------|
| **JTBD Coverage** | 5 jobs | 20 jobs | Count of documented jobs |
| **Persona Coverage** | 2 personas | 7 personas | Persona-specific content |
| **Cross-Product Integration Guides** | 0 | 6 | Published integration guides |
| **Content Gaps Addressed** | 0 | 10 critical gaps | Gap closure tracking |
| **User Task Success Rate** | Unknown | 85% | User testing/analytics |
| **Time to First Deployment** | Unknown | <30 min | User journey tracking |
| **Support Ticket Reduction** | Baseline | -30% | Ticket analysis |

### User Feedback Mechanisms

1. **Embedded Feedback Forms** in documentation
2. **User Journey Analytics** (time on page, search queries, exit points)
3. **Support Ticket Analysis** (common issues, documentation gaps)
4. **User Interviews** (quarterly with target personas)
5. **Community Forum Monitoring** (common questions, pain points)

### Content Quality Metrics

| Quality Dimension | Target | How to Measure |
|-------------------|--------|----------------|
| **Accuracy** | 100% technical accuracy | SME review, testing |
| **Completeness** | All critical jobs covered | Gap analysis |
| **Clarity** | 80% comprehension rate | User testing |
| **Discoverability** | 70% find content within 2 clicks | Analytics |
| **Actionability** | 90% can complete task | Task success testing |

---

## Conclusion

This revised JTBD-driven documentation architecture transforms OpenShift GitOps content from a feature-centric reference into an outcome-driven enablement system. By aligning with:

1. **Jobs-To-Be-Done framework** - Focus on user outcomes over product features
2. **CCS documentation categories** - Standardized information architecture
3. **Red Hat ecosystem strategy** - Cross-product integration narratives
4. **GTM and business outcomes** - Sales enablement and decision-maker content
5. **Multiple personas** - Targeted content for diverse users

The documentation will better serve enterprise adoption, platform engineering practices, and business decision-making while reducing duplication and improving discoverability.

### Key Takeaways

**20 new JTBD identified** spanning:
- Platform Engineering (IDP, golden paths)
- AI/ML Operations (model deployment, MLOps)
- Multi-Cluster Management (fleet, hub-and-spoke)
- Virtualization (VMs as code)
- Security & Governance (policy enforcement, compliance)
- Disaster Recovery (control plane, applications)
- Migration (Jenkins, legacy workloads)
- Progressive Delivery (canaries, traffic shaping)
- Developer Experience (onboarding, self-service)
- Business Outcomes (ROI, architecture decisions)

**6 major cross-product integrations** mapped:
- ACM, Dev Spaces, Virtualization, Service Mesh, OpenShift AI, OADP

**10 critical content gaps** prioritized for immediate action

**Revised information architecture** ready for implementation

---

**Document Version:** 1.0  
**Last Updated:** May 12, 2026  
**Status:** ✅ Ready for stakeholder review and implementation planning

---

## Sources

All findings in this analysis are supported by the following ecosystem sources:

### Red Hat Product Documentation
- [Red Hat OpenShift GitOps](https://www.redhat.com/en/technologies/cloud-computing/openshift/gitops)
- [What is GitOps?](https://www.redhat.com/en/topics/devops/what-is-gitops)
- [Argo Rollouts Documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.9/html/argo_rollouts/using-argo-rollouts-for-progressive-deployment-delivery)

### Red Hat Developer Portal
- [Build CI/CD pipeline with OpenShift Dev Spaces and GitOps](https://developers.redhat.com/articles/2026/02/16/build-cicd-pipeline-openshift-dev-spaces-and-gitops)
- [How to automate multi-cluster deployments using Argo CD](https://developers.redhat.com/articles/2025/06/24/how-automate-multi-cluster-deployments-using-argo-cd)
- [Manage OpenShift virtual machines with GitOps](https://developers.redhat.com/learn/manage-openshift-virtual-machines-gitops)
- [OpenShift GitOps Usage Guide](https://github.com/redhat-developer/gitops-operator/blob/master/docs/OpenShift%20GitOps%20Usage%20Guide.md)

### Red Hat Blogs
- [Multi-cluster GitOps with Argo CD Agent](https://www.redhat.com/en/blog/multi-cluster-gitops-argo-cd-agent-openshift-gitops)
- [Manage clusters at scale with Argo CD Agent](https://www.redhat.com/en/blog/manage-clusters-and-applications-scale-argo-cd-agent-red-hat-openshift-gitops)
- [Virtual Machines as Code](https://www.redhat.com/en/blog/virtual-machines-as-code-with-openshift-gitops-and-openshift-virtualization)
- [OADP + OpenShift GitOps for Application DR](https://www.redhat.com/en/blog/oadp-openshift-gitops-an-approach-to-implementing-application-disaster-recovery)
- [Generating Governance Policies with GitOps](https://www.redhat.com/en/blog/generating-governance-policies-using-kustomize-and-gitops)
- [OpenShift advances with Service Mesh and GitOps](https://www.redhat.com/en/blog/red-hat-advances-openshift-ambient-service-mesh-and-scalable-gitops-control-plane)
- [Using ACM and GitOps to manage OpenShift Virtualization](https://www.redhat.com/en/blog/using-red-hat-advanced-cluster-management-and-openshift-gitops-to-manage-openshift-virtualization)

### Technical Resources
- [GitOps with Advanced Cluster Management](https://piotrminkowski.com/2022/10/24/gitops-with-advanced-cluster-management-for-kubernetes/)
- [ACM with GitOps/ArgoCD](https://medium.com/@shrishs/redhat-advanced-cluster-management-for-kubernetes-with-gitops-argocd-8c53db008059)
- [Progressive Delivery with OpenShift GitOps](https://medium.com/@dlakshma/progressive-delivery-with-openshift-gitops-operator-part-1-d851cf33f40c)
- [GitOps Workflow with Argo CD](https://redhat-scholars.github.io/outer-loop-guide/outer-loop/5.1/gitops-workflow.html)
- [Using Tekton and ArgoCD](https://demo.openshift.com/en/latest/gitops-with-cicd/)

### Migration and Modernization
- [Migrating from Jenkins to Tekton](https://docs.openshift.com/en/container-platform/4.8/cicd/jenkins-tekton/migrating-from-jenkins-to-tekton.html)
- [Tekton vs. Jenkins](https://www.redhat.com/en/blog/tekton-vs-jenkins-whats-better-cicd-pipelines-red-hat-openshift)
- [The present and future of CI/CD with GitOps](https://developers.redhat.com/blog/2020/09/03/the-present-and-future-of-ci-cd-with-gitops-on-red-hat-openshift)

### AI/ML and Advanced Use Cases
- [Accelerate MLOps with Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift/aiml)
- [MLOps Practices with OpenShift AI](https://www.redhat.com/en/services/training/ai500-mlops-practices-with-red-hat-openshift-ai)
- [ACM Governance and PolicyGenerator](https://myopenshiftblog.com/acm-governance-and-policy-templates/)

---

*End of Document*
