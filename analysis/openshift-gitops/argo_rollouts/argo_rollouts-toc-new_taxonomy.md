# Argo Rollouts
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable teams to implement progressive deployment delivery using Argo Rollouts for safer, data-driven application releases in OpenShift.

**Personas:** Platform Engineer, Cluster Administrator, Application Developer, SRE, DevOps Engineer, Infrastructure Engineer, Platform Administrator

**Main Jobs:** 10 core jobs across 7 workflow stages (Get Started, Deploy, Monitor, Configure, Administer, Operate)

---

## Quick Navigation

**I want to:**
- Understand progressive delivery with Argo Rollouts -> Job 1 (Deploy)
- Install and configure Argo Rollouts -> Job 2 (Get Started)
- Create my first canary deployment -> Job 9 (Get Started)
- Route traffic between application versions -> Job 3 (Deploy)
- Validate deployments with automated metrics -> Job 4 (Monitor)
- Monitor and control rollout progress -> Job 5 (Monitor)
- Configure high availability for production -> Job 6 (Configure)
- Integrate with service mesh or ingress -> Job 7 (Configure)
- Manage multi-tenant rollout instances -> Job 8 (Administer)
- Centralize rollout management cluster-wide -> Job 10 (Operate)

---

# Table of Contents

## Get Started with Progressive Delivery

### Job 2: Install and Configure Argo Rollouts
*When setting up progressive delivery capabilities, I want to install and configure Argo Rollouts in my cluster*

**Personas:** Cluster Administrator

**Prerequisites:**
- OpenShift GitOps Operator installed
- Appropriate cluster permissions

#### 2.1 Create RolloutManager Custom Resource
**Goal:** Install Argo Rollouts controller and resources into target namespace.

-> Lines 321-441: Creating RolloutManager custom resources
-> Lines 442-725: Installing Argo Rollouts and CLI

**RolloutManager CR:**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: RolloutManager
metadata:
  name: argo-rollout
spec: {}
```

#### 2.2 Choose Installation Scope
**Decision:** Select cluster-scoped (default) or namespace-scoped mode based on requirements.

| Scope | Use Case | Access | Management |
|-------|----------|--------|------------|
| Cluster-scoped | Multi-tenant platform | All namespaces | Centralized |
| Namespace-scoped | Isolated tenants | Single namespace | Distributed |

-> Lines 2690-2969: Enabling namespace-scoped installation

#### 2.3 Install Argo Rollouts CLI (Optional)
**Goal:** Enable direct management of rollouts from command line.

-> Lines 292-306: Argo Rollouts CLI overview
-> Lines 442-725: Installing the Argo Rollouts CLI

**CLI capabilities:**
- Monitor rollout progress
- Promote or pause deployments
- Retry failed rollouts
- Modify rollout images

---

### Job 9: Create First Canary Deployment
*When creating my first canary deployment, I want to follow a complete example workflow*

**Personas:** Application Developer

**Prerequisites:**
- Argo Rollouts installed and operational
- Application container image available

#### 9.1 Understand Rollout Lifecycle
**Goal:** Learn the components and workflow of canary deployments.

-> Lines 726-846: Getting started overview
-> Lines 847-1515: Complete getting started guide

**Key Components:**
- `Rollout` CR (replaces Deployment)
- `Service` resources for traffic routing
- `AnalysisTemplate` for automated validation

#### 9.2 Deploy Sample Application
**Goal:** Deploy first application using Rollout resource with canary strategy.

-> Lines 847-1515: End-to-end canary deployment example

**Canary Strategy Steps:**
1. Deploy new version to subset of pods
2. Route percentage of traffic to canary
3. Run automated analysis
4. Promote or rollback based on metrics

---

## Deploy Applications Progressively

### Job 1: Reduce Deployment Risk with Progressive Delivery
*When I need to reduce deployment risk for application updates, I want to automate progressive delivery with canary or blue-green strategies*

**Personas:** Platform Engineer

**Context:** Progressive delivery exposes new versions incrementally, reducing blast radius of issues.

#### 1.1 Understand Progressive Delivery Benefits
**Goal:** Learn how Argo Rollouts reduces deployment risk.

-> Lines 4-124: Argo Rollouts overview
-> Lines 125-320: Architecture and components

**Benefits:**
- **Risk Reduction:** Expose updates to subset of users initially
- **Automated Validation:** Continuous analysis during rollout
- **Quick Rollback:** Automatic rollback on failure detection
- **Manual Control:** Pause and resume at any stage

#### 1.2 Choose Deployment Strategy
**Decision:** Select canary or blue-green strategy based on requirements.

| Strategy | Traffic Pattern | Use Case | Rollback |
|----------|----------------|----------|----------|
| Canary | Gradual percentage increase | Complex services, multiple metrics | Gradual |
| Blue-Green | Instant full cutover | Simpler services, fast validation | Instant |

-> Lines 125-320: Deployment strategies explanation

#### 1.3 Understand Architecture
**Goal:** Learn Argo Rollouts components and their roles.

-> Lines 221-285: Architecture overview
-> Lines 242-256: Component descriptions

**Components:**
- **Rollouts Controller:** Manages Rollout CR lifecycle
- **AnalysisRun Controller:** Executes metric analysis
- **Experiment Controller:** Runs short-lived tests
- **Service/Ingress Controllers:** Manage traffic routing

---

### Job 3: Route Traffic Between Application Versions
*When deploying applications with canary strategies, I want to route percentage-based traffic between versions*

**Personas:** Application Developer

**Prerequisites:**
- Rollout resource defined
- Service or Ingress resources configured

#### 3.1 Configure Traffic Routing with Services
**Goal:** Use Kubernetes Services for basic traffic splitting.

-> Lines 1516-1636: Routing traffic overview
-> Lines 1637-1997: Service-based traffic routing

**Traffic Routing Options:**
- Kubernetes `Service` resources
- OpenShift `Route` resources
- Ingress controllers
- Service mesh integration

#### 3.2 Integrate with OpenShift Service Mesh
**Goal:** Leverage service mesh for advanced traffic management.

-> Lines 1998-2118: Service Mesh routing overview
-> Lines 2119-2689: Service Mesh integration details

**Service Mesh Benefits:**
- Fine-grained traffic control
- mTLS between versions
- Advanced routing rules
- Traffic mirroring

---

## Monitor and Validate Deployments

### Job 4: Validate Deployment with Automated Analysis
*When validating deployment success, I want to define and run automated analysis against metrics*

**Personas:** SRE

**Prerequisites:**
- Prometheus or metrics provider configured
- Rollout resource deployed

#### 4.1 Define Analysis Templates
**Goal:** Create reusable metric queries for deployment validation.

-> Lines 237-241: Analysis mechanisms overview
-> Lines 275-284: AnalysisTemplate and AnalysisRun resources

**Analysis Types:**
- **Prometheus Metrics:** Query error rates, latency, throughput
- **Kubernetes Jobs:** Run validation jobs against new version
- **Custom Providers:** Integrate with other metrics sources

**AnalysisTemplate Structure:**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: success-rate
spec:
  metrics:
  - name: success-rate
    successCondition: result >= 0.95
    provider:
      prometheus:
        address: http://prometheus:9090
        query: |
          sum(requests{status="200"}) / sum(requests)
```

#### 4.2 Attach Analysis to Rollouts
**Goal:** Link AnalysisTemplates to rollout strategy steps.

-> Lines 275-284: Linking analysis to rollouts

**Analysis Triggers:**
- Background analysis during canary
- Post-promotion validation
- Pre-promotion gates

---

### Job 5: Monitor and Control Rollout Progress
*When managing Argo Rollouts deployments, I want to monitor rollout progress and control promotion steps*

**Personas:** DevOps Engineer

**Prerequisites:**
- Argo Rollouts CLI installed (optional but recommended)
- Active rollout in progress

#### 5.1 Monitor Rollout Status
**Goal:** Track deployment progress and current state.

-> Lines 292-306: CLI overview and capabilities

**CLI Commands:**
```bash
kubectl argo rollouts get rollout <name>
kubectl argo rollouts status <name>
kubectl argo rollouts list rollouts
```

**Dashboard UI:**
```bash
kubectl argo rollouts dashboard
```

#### 5.2 Control Rollout Progression
**Goal:** Manually pause, promote, or abort rollouts.

-> Lines 298-304: CLI operations

**Control Commands:**
```bash
kubectl argo rollouts promote <name>
kubectl argo rollouts pause <name>
kubectl argo rollouts abort <name>
kubectl argo rollouts retry <name>
```

---

## Configure for Production

### Job 6: Configure High Availability and Resource Isolation
*When scaling Argo Rollouts for production, I want to configure high availability and resource isolation*

**Personas:** Platform Engineer

**Prerequisites:**
- RolloutManager installed
- Production cluster configured

#### 6.1 Enable High Availability Mode
**Goal:** Configure controller replicas for fault tolerance.

-> Lines 3225-3345: HA support overview
-> Lines 3346-3452: Configuring HA for Argo Rollouts

**HA Configuration:**
- Multiple controller replicas
- Leader election
- Resource requests and limits

**RolloutManager HA Spec:**
```yaml
spec:
  env:
  - name: ARGO_ROLLOUTS_LEADER_ELECTION_ENABLED
    value: "true"
  replicas: 2
```

#### 6.2 Configure Resource Quotas
**Goal:** Set appropriate resource limits for controller and rollouts.

-> Lines 3346-3452: Resource configuration

**Resource Considerations:**
- Controller CPU/memory limits
- Per-rollout resource requirements
- Namespace quotas

---

### Job 7: Integrate with Traffic Management Infrastructure
*When integrating with service mesh or ingress controllers, I want to configure traffic management plugins*

**Personas:** Infrastructure Engineer

**Prerequisites:**
- Service mesh or ingress controller deployed
- RolloutManager installed

#### 7.1 Configure Traffic Management Plugins
**Goal:** Enable Argo Rollouts to work with existing networking infrastructure.

-> Lines 2970-3090: Traffic management overview
-> Lines 3091-3224: Configuring traffic and metric plugins

**Supported Traffic Routers:**
- **Istio/OpenShift Service Mesh:** VirtualService integration
- **NGINX Ingress:** Annotation-based routing
- **Traefik:** IngressRoute integration
- **AWS ALB:** TargetGroup weights
- **OpenShift Routes:** Route splitting

**Plugin Configuration:**
```yaml
spec:
  trafficRouterPlugins:
  - name: istio
    location: https://...
```

#### 7.2 Configure Metric Providers
**Goal:** Connect rollouts to observability infrastructure.

-> Lines 3091-3224: Metric plugin configuration

**Supported Metrics Providers:**
- Prometheus
- Datadog
- New Relic
- Wavefront
- Custom providers

---

## Manage Multi-Tenant Deployments

### Job 8: Configure Namespace-Scoped or Cluster-Scoped Instances
*When managing Argo Rollouts across multiple tenants, I want to configure namespace-scoped or cluster-scoped instances*

**Personas:** Platform Administrator

**Context:** Balance tenant isolation with operational efficiency.

#### 8.1 Decide on Scoping Model
**Decision:** Choose between cluster-scoped and namespace-scoped based on tenant isolation needs.

-> Lines 2690-2810: Namespace-scoped overview
-> Lines 2811-2969: Enabling namespace-scoped support

| Model | Isolation | Management | Resource Usage |
|-------|-----------|------------|----------------|
| Cluster-scoped | Shared controller | Centralized | Lower overhead |
| Namespace-scoped | Isolated per tenant | Distributed | Higher overhead |

#### 8.2 Enable Namespace-Scoped Mode
**Goal:** Configure RolloutManager to monitor single namespace only.

-> Lines 2811-2969: Namespace-scoped configuration

**RolloutManager Configuration:**
```yaml
spec:
  namespaceScoped: true
```

---

## Operate at Scale

### Job 10: Centralize Rollout Management Cluster-Wide
*When managing cluster-wide rollout resources, I want to use a cluster-scoped Argo Rollouts instance*

**Personas:** Platform Engineer

**Prerequisites:**
- Cluster-admin permissions
- RolloutManager installed in control namespace

#### 10.1 Configure Cluster-Scoped Instance
**Goal:** Enable single RolloutManager to manage rollouts across all namespaces.

-> Lines 3453-3573: Cluster-scoped overview
-> Lines 3574-3646: Using cluster-scoped instance

**Configuration:**
- Install RolloutManager in dedicated namespace (e.g., `argo-rollouts`)
- Grant cluster-level RBAC permissions
- Rollouts in any namespace are managed by central controller

**Benefits:**
- Single controller instance reduces overhead
- Consistent policy enforcement
- Centralized monitoring and operations

---

## Appendices

### A. Deployment Strategy Comparison

| Aspect | Canary | Blue-Green |
|--------|--------|------------|
| **Traffic Pattern** | Gradual percentage increase | Instant full cutover |
| **Validation Time** | Extended (hours to days) | Quick (minutes to hours) |
| **Rollback** | Gradual decrease | Instant switch |
| **Complexity** | Higher (traffic management, analysis) | Lower (simple swap) |
| **Best For** | High-risk changes, complex metrics | Low-risk changes, simple validation |
| **Resource Usage** | Lower (gradual replacement) | Higher (full duplicate environment) |

---

### B. Installation Scope Decision Matrix

**Choose cluster-scoped when:**
- Managing platform-wide rollouts
- Need centralized control and visibility
- Want to minimize controller resource usage
- Trust all tenants or have strong RBAC

**Choose namespace-scoped when:**
- Strict tenant isolation required
- Different teams manage their own rollouts
- Compliance requires isolated controllers
- Want to delegate rollout management

---

### C. Workflow Coverage Analysis

**Covered Stages:**
- ✅ Get Started: Installation, first deployment
- ✅ Deploy: Progressive delivery strategies
- ✅ Monitor: Rollout tracking, automated analysis
- ✅ Configure: HA, traffic management, plugins
- ✅ Administer: Multi-tenancy, scoping
- ✅ Operate: Cluster-wide management

**Gaps Identified:**
- ❌ Troubleshoot: No dedicated troubleshooting guide
- ❌ Upgrade: No upgrade procedures documented
- ❌ Migrate: No migration from standard Deployments

---

## Navigation Guide

### By User Journey

**Platform Engineer setting up progressive delivery:**
1. Job 1: Understand progressive delivery benefits and architecture
2. Job 2: Install and configure Argo Rollouts
3. Job 6: Configure HA and resource isolation for production
4. Job 10: Set up cluster-scoped management (if applicable)

**Application Developer deploying with canary:**
1. Job 9: Create first canary deployment (getting started)
2. Job 3: Configure traffic routing between versions
3. Job 5: Monitor and control rollout progress

**SRE validating deployment safety:**
1. Job 4: Define automated analysis templates
2. Job 5: Monitor rollout progress and metrics
3. Job 3: Understand traffic routing patterns

**Platform Administrator managing multi-tenant environment:**
1. Job 8: Choose and configure scoping model
2. Job 2: Install RolloutManagers per tenant or cluster-wide
3. Job 6: Configure HA and quotas

**Infrastructure Engineer integrating with existing systems:**
1. Job 7: Configure traffic management plugins (service mesh/ingress)
2. Job 7: Connect metric providers
3. Job 3: Validate traffic routing with existing infrastructure

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 2 jobs
- Deploy: 2 jobs
- Monitor: 2 jobs
- Configure: 2 jobs
- Administer: 1 job
- Operate: 1 job

**Main Jobs:** 10
**User Stories:** 0 (main jobs only in this version)
**Total Records:** 10
**Personas:** 7 unique personas identified
**Source Lines:** 3,645 lines of combined documentation
**Assemblies:** 9 original assembly files

**Coverage Notes:**
- Strong coverage of setup, deployment, and operations
- Missing troubleshooting and upgrade guidance
- No migration procedures from standard Deployments
- Good balance of getting started and production configuration
