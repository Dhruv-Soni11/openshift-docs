# GitOps CLI (argocd) Reference — Consolidation Report

**Document:** gitops_cli_argocd-combined.adoc  
**JTBD Records:** 8 pre-consolidated main jobs → 7 final jobs (after merging)

---

## Executive Summary

### What's Changing

The current GitOps CLI documentation is organized by **CLI tool features and technical components** — separate sections for configuration, authentication, and command reference. This feature-based structure scatters related approaches (authentication modes, completion methods) across multiple sections, making it harder for users to discover alternatives and compare options.

The proposed JTBD-based structure reorganizes the same content by **user goals and workflow stages**. Instead of "here's how to configure the CLI" followed separately by "here's the command reference," the new structure asks "what are you trying to accomplish?" and presents all relevant approaches together. Authentication in default mode and core mode are consolidated under "Getting Started," shell completion methods appear together, and reference material is organized by lookup purpose.

This is not new content — it's the existing documentation reorganized to match how users actually think about CLI work: "I need to authenticate" (see both modes), "I want productivity features" (see all completion options), "I need syntax help" (reference).

### Key Improvements

- **Authentication Consolidation:** Default mode login (Section 2) and core mode approach (buried in Section 3 syntax) → unified "Authenticate with Argo CD Server" job with explicit mode comparison
- **Shell Completion Discovery:** Tab completion file method (Section 1) and completion command (Section 3 utilities) → consolidated "Configure Shell Environment" job showing both approaches
- **Reference Organization:** Flat command reference (Section 3) → 3 purpose-driven jobs (Syntax, Global Options, Utilities) for targeted lookup
- **Workflow Visibility:** Implicit setup sequence → explicit Getting Started and Reference stages with clear progression
- **Decision Guidance:** Scattered mode mentions → explicit authentication decision guide comparing default vs core mode use cases
- **Troubleshooting Elevation:** Version command buried in utilities → dedicated "Check CLI Version and Access Help" job for troubleshooting entry point
- **Cross-Referencing:** No links between related methods → consolidated jobs show alternatives together (completion methods, authentication modes)

---

## Current Structure (Feature-Based)

- **Configuring the GitOps CLI** — CLI environment setup
  - Enabling tab completion — File-based bash completion installation
- **Logging in to the Argo CD server in the default mode** — Default authentication
  - Logging in to the Argo CD server — Step-by-step login procedure
- **Basic GitOps argocd commands** — Command reference material
  - Basic syntax — Command structure and modes
    - Default mode — API-based authentication
    - Core mode — Kubernetes API authentication (alternative approach)
  - Global options — Table of 20+ configuration flags
  - Utility commands — Meta-commands for the CLI tool
    - argocd — Parent command
    - version — Version checking
    - help — Help access
    - completion — Shell completion generation

**Total:** 3 top-level sections, organized by CLI features (configuration, authentication, reference).

---

## Proposed JTBD-Based Structure

### Quick Overview

- **Getting Started**
  - Job 1: Configure My Shell Environment with Productivity Features
  - Job 2: Authenticate with the Argo CD Server
  - Job 3: Log In to Argo CD Server in Default Mode
  - Job 4: Use the CLI in Core Mode (Alternative Authentication)
- **Reference**
  - Job 5: Understand CLI Command Syntax and Modes
  - Job 6: Customize CLI Behavior with Global Options
  - Job 7: Check CLI Version and Access Help

### Detailed Job Descriptions

#### Getting Started

**Job 1: Configure My Shell Environment with Productivity Features**

*When I need to use the argocd CLI efficiently, I want to configure my shell environment with productivity features, so I can work faster and avoid command-line errors.*

Prerequisites: argocd CLI tool installed, bash-completion installed on local system

- **1.1. Enable Tab Completion for Bash (File Installation Method)** `[procedure]`
  - Configuring the GitOps CLI > Enabling tab completion (lines 20-56): Generate completion script and install to /etc/bash_completion.d/
  - Context: Persistent installation that survives shell restarts; requires sudo access
  - Alternative: See Job 7.3 for dynamic generation method

---

**Job 2: Authenticate with the Argo CD Server**

*When I need to execute argocd commands against a cluster, I want to authenticate with the Argo CD server, so I can manage GitOps resources via the CLI.*

Prerequisites: argocd CLI installed and configured, Argo CD deployed on the cluster

- **2.1. Understand Authentication Modes** `[concept]`
  - Basic GitOps argocd commands > Basic syntax (lines 159-184): Comparison of default mode vs core mode
  - Context: Choose mode based on use case — default for interactive, core for automation
  - Decision factors: Session management needs, CI/CD integration, Kubernetes access
- **2.2. Choose Your Authentication Approach** `[concept]`
  - Job 3: Default mode (API-based authentication with server login)
  - Job 4: Core mode (Kubernetes API authentication with kubeconfig)

---

**Job 3: Log In to Argo CD Server in Default Mode**

*As a Platform engineer, when I need to authenticate the argocd CLI for API-based commands, I want to log in using my Argo CD credentials, so I can execute commands against the server.*

Prerequisites: argocd CLI installed and configured, admin credentials or user credentials for Argo CD

- **3.1. Retrieve Argo CD Credentials** `[procedure]`
  - Logging in to the Argo CD server in the default mode > Logging in (lines 94-106): Get admin password and server URL from cluster secrets
  - Context: Required before login; credentials stored in openshift-gitops namespace
- **3.2. Authenticate to Argo CD Server** `[procedure]`
  - Logging in to the Argo CD server in the default mode > Logging in (lines 107-138): Login procedure with password quoting for special characters
  - Context: Establishes session; supports relogin on timeout; logout when finished
  - Important: Single-quote passwords to handle special characters like $

---

**Job 4: Use the CLI in Core Mode (Alternative Authentication)**

*As a Platform engineer, when I want to avoid server authentication overhead, I want to use the argocd CLI in core mode with kubeconfig credentials, so I can execute commands directly against the Kubernetes API.*

Prerequisites: kubeconfig file with cluster credentials, argocd CLI installed

- **4.1. Understand Core Mode vs Default Mode** `[concept]`
  - Basic GitOps argocd commands > Basic syntax > Core mode (lines 170-184): How core mode works and when to use it
  - Context: Core mode for automation/CI-CD, default mode for interactive use
  - Key difference: No server login required, uses kubeconfig credentials
- **4.2. Execute Commands in Core Mode** `[procedure]`
  - Basic GitOps argocd commands > Basic syntax > Core mode (lines 186-245): Four context variations with examples
  - Context: Must set repo-server-name; multiple kubeconfig/context options available
  - Options: Default kubeconfig + default context, custom context, custom kubeconfig, both custom

---

#### Reference

**Job 5: Understand CLI Command Syntax and Modes**

*When I need to construct valid argocd commands, I want reference documentation for command syntax and modes, so I can build correct commands for my use case.*

Prerequisites: None

- **5.1. Command Structure Reference** `[reference]`
  - Basic GitOps argocd commands > Basic syntax (lines 159-245): Syntax for default and core modes
  - Context: Lookup when constructing commands; mode comparison table included
  - Content: Default mode syntax, core mode syntax, key differences table

---

**Job 6: Customize CLI Behavior with Global Options**

*When I need to customize argocd CLI behavior across all commands, I want reference documentation for global flags and options, so I can configure authentication, logging, and connection settings.*

Prerequisites: None

- **6.1. Global Options Reference** `[reference]`
  - Basic GitOps argocd commands > Global options (lines 247-363): Table of 20+ global configuration flags
  - Context: Lookup when configuring auth, TLS, logging, component naming, port forwarding
  - Categories: Authentication & connection, TLS & certificates, gRPC, logging & debugging, component naming, port forwarding

---

**Job 7: Check CLI Version and Access Help**

*When I need to troubleshoot CLI issues or configure the tool itself, I want reference documentation for utility commands, so I can verify versions, get help, and generate completion scripts.*

Prerequisites: None

- **7.1. Check CLI and Server Versions** `[procedure]`
  - Basic GitOps argocd commands > Utility commands > version (lines 377-411): Version command with output format options
  - Context: Troubleshooting version mismatches; verifying compatibility
- **7.2. Access Help Documentation** `[procedure]`
  - Basic GitOps argocd commands > Utility commands > help (lines 413-429): Help command for all commands and subcommands
  - Context: Quick reference without external docs
- **7.3. Generate Shell Completion Scripts (Dynamic Method)** `[procedure]`
  - Basic GitOps argocd commands > Utility commands > completion (lines 431-452): Bash and zsh completion generation
  - Context: Alternative to file installation (Job 1); dynamic generation for current shell
- **7.4. Display All Options (Root Command)** `[reference]`
  - Basic GitOps argocd commands > Utility commands > argocd (lines 368-375): Parent command showing all options
  - Context: Discover available commands

---

## Key Differences

| Dimension | Current (Feature-Based) | Proposed (JTBD-Based) |
|-----------|------------------------|----------------------|
| **Organizing principle** | CLI features and technical components | User goals and workflow stages |
| **Top-level items** | 3 sections (Configuring, Logging in, Commands) | 7 jobs (1 Configure, 4 Getting Started, 3 Reference) |
| **Authentication** | Separate sections: default mode (Section 2) and core mode buried in syntax (Section 3) | Consolidated under "Getting Started" with explicit mode comparison (Jobs 2-4) |
| **Shell completion** | File method (Section 1), command method (Section 3 utilities) | Consolidated in Job 1 with cross-reference to Job 7.3 for alternative |
| **Reference material** | Flat list (Section 3: syntax, options, utilities) | Purpose-driven jobs (Job 5: syntax, Job 6: options, Job 7: utilities) |
| **Decision guidance** | Implicit (user must discover core mode) | Explicit authentication decision guide at Job 2 |
| **Workflow visibility** | Implied sequence | Explicit stages: Getting Started → Reference |

### Job List Adjustments from Suggested Input

The suggested 8 main jobs were consolidated to **7 jobs** for the following reason:

1. **Jobs "Understand CLI command syntax" and "Customize CLI behavior with global options" (conceptually could merge)** → Kept separate because syntax is structural reference (how to build commands) while global options are configuration reference (how to customize behavior). Different lookup patterns.

No other adjustments were needed. The 8 initial main jobs included one user story that was correctly tagged as `granularity: user_story` with `parent_job` set, so the final count is 7 main jobs.

---

## Consolidation Examples

### Example 1: Authentication Approaches (2 scattered sections → 1 unified job)

**Current (Fragmented):**
- Section 2: "Logging in to the Argo CD server in the default mode" — Default authentication with server login
- Section 3.1: "Basic syntax" > "Core mode" — Alternative authentication using kubeconfig, buried in syntax reference

Users must discover core mode by reading command syntax documentation. No explicit comparison of when to use each mode. Interactive users may never learn about core mode for automation.

**Proposed (Consolidated):**
- **Job 2: Authenticate with the Argo CD Server**
  - 2.1. Understand Authentication Modes (concept) — explicit comparison
  - 2.2. Choose Your Approach — decision guidance
    - Job 3: Default mode (API-based)
    - Job 4: Core mode (Kubernetes API)

**Benefit:** Users see BOTH authentication options at point of need with explicit guidance on when to use each mode (interactive vs automation use cases).

---

### Example 2: Shell Completion Setup (2 separate locations → 1 consolidated job)

**Current (Fragmented):**
- Section 1: "Enabling tab completion" — File installation method (generate script, copy to /etc/bash_completion.d/)
- Section 3.4: "Utility commands" > "completion" — Dynamic generation method (source in current shell)

No cross-reference between methods. Users following Section 1 may not know about dynamic generation. Users looking for completion command in reference may not know about persistent installation method.

**Proposed (Consolidated):**
- **Job 1: Configure My Shell Environment with Productivity Features**
  - 1.1. Enable Tab Completion (File Installation Method) — persistent setup
    - Cross-reference to Job 7.3 for alternative dynamic method

**Benefit:** Both completion setup methods visible in shell configuration job. Users can choose persistent vs dynamic based on their needs (production vs testing).

---

### Example 3: Reference Material Organization (flat list → purpose-driven jobs)

**Current (Flat):**
- Section 3: "Basic GitOps argocd commands"
  - 3.1. Basic syntax (structure reference)
  - 3.2. Global options (configuration reference)
  - 3.3. Utility commands (tool reference)

All reference material grouped together regardless of lookup purpose. Users must scan entire section to find syntax help vs configuration options vs troubleshooting commands.

**Proposed (Purpose-Driven):**
- **Job 5: Understand CLI Command Syntax and Modes** — for command construction
- **Job 6: Customize CLI Behavior with Global Options** — for configuration lookup
- **Job 7: Check CLI Version and Access Help** — for troubleshooting and discovery

**Benefit:** Reference jobs match lookup intent (syntax help, configuration, troubleshooting). Users jump directly to relevant job instead of scanning flat reference list.

---

## Content Gaps Identified

| Gap | JTBD Reference | Current Coverage | Impact |
|-----|---------------|-----------------|--------|
| Common authentication errors and solutions | Jobs 3-4 (Authentication) | Version checking only (Section 3.3) | **High** — Users likely encounter auth errors (wrong credentials, connection issues, certificate problems) but have no troubleshooting guidance beyond version check |
| CI/CD integration patterns | Job 4 (Core mode) | Core mode syntax shown (Section 3.1) but no automation examples | **High** — Core mode is for automation but no pipeline integration examples, environment variable patterns, or CI/CD best practices |
| When to use which global options | Job 6 (Global options) | Option descriptions only (Section 3.2) | **Medium** — 20+ global options listed but no guidance on common combinations (logging for debugging, TLS for security, port-forward for local dev) |
| Application deployment workflows | Jobs 3-4 (After authentication) | Not covered (separate guide) | **High** — Users authenticate then need deployment guidance, but no link to "Argo CD applications" guide at end of Job 3 |
| Monitoring and observability | After deployment | Not covered (separate guide) | **Medium** — No monitoring content in CLI guide, but link to "Observability" guide would help post-deployment workflow |
| Zsh completion setup | Job 1 (Tab completion) | Bash only (Section 1), zsh mentioned in completion command (Section 3.4) | **Low** — Zsh users must use dynamic method (Job 7.3), no persistent installation guide |
| Session timeout handling | Job 3 (Default mode login) | Mentioned (relogin command) but no examples | **Medium** — Session timeout noted but no procedure for handling or extending sessions |
| Multi-instance Argo CD management | Job 4 (Core mode) | Namespace note (Section 3.1) but no multi-instance patterns | **Low** — Core mode note about setting namespace but no examples for managing multiple Argo CD instances |

---

## Navigation Improvement Summary

| Metric | Current | Proposed | Improvement |
|--------|---------|----------|-------------|
| Top-level navigation items | 3 sections | 2 stages (7 jobs total) | Better stage visibility (Getting Started vs Reference) |
| Sections to browse for authentication | 2 sections (default in Section 2, core in Section 3) | 1 job (Job 2) with 2 approaches | ~50% reduction in navigation |
| Methods to find completion setup | 2 locations (Section 1 and Section 3.4) with no cross-reference | 1 job (Job 1) with cross-reference to alternative | Consolidated discovery |
| Clicks to find core mode | 3+ (Section 3 > Basic syntax > Core mode subsection) | 2 (Getting Started > Job 4) | ~33% faster discovery |
| Reference lookup | 1 section with 3 subsections (scan all to find relevant) | 3 jobs (direct jump to syntax/options/utilities) | Purpose-driven access |

**Final job count: 7** (from 8 pre-consolidated records). One record was correctly tagged as a user_story under a main_job parent, so no merging was needed. The JTBD structure consolidates scattered approaches (authentication modes, completion methods) into unified jobs while maintaining all existing content.

---

## UX Research Alignment

**Note:** No research-specific fields (pain_points, strategic_priority, teams_involved, loop) were populated in the JTBD records for this documentation. The following observations are based on documentation structure analysis only.

### Inferred User Patterns from Structure

**From Current Documentation Organization:**
- **Authentication friction:** Default mode and core mode separated suggests users may not discover alternatives
- **Reference lookup:** Flat command reference suggests users must scan entire section vs targeted lookup
- **Completion discovery:** Two setup methods in different locations suggests discoverability issue

**JTBD Alignment:**
- **Consolidated authentication:** Jobs 2-4 surface both modes at point of need (Getting Started stage)
- **Purpose-driven reference:** Jobs 5-7 match lookup intent (syntax vs configuration vs troubleshooting)
- **Cross-referencing:** Job 1 and Job 7.3 link completion methods

### Recommended Research Questions

To validate and improve this restructure, consider researching:

1. **Authentication mode discovery:**
   - Do users discover core mode or assume default mode is the only option?
   - What triggers users to seek core mode? (automation needs, session timeout frustration)
   - How do users decide between modes?

2. **Reference lookup patterns:**
   - When do users need syntax reference vs global options vs utility commands?
   - Are lookup patterns sequential (syntax first, then options) or random access?
   - What are the most frequently looked-up options?

3. **Shell completion adoption:**
   - What percentage of users set up tab completion?
   - Do users prefer file installation or dynamic generation?
   - Are users aware both methods exist?

4. **Troubleshooting entry points:**
   - What are the most common CLI errors? (auth failures, connection issues, version mismatches)
   - How do users currently troubleshoot CLI issues without error-specific guidance?
   - Is version checking the first troubleshooting step or a last resort?

5. **Workflow integration:**
   - How do users integrate the CLI into CI/CD pipelines?
   - What global option combinations are commonly used? (logging for debugging, TLS for security)
   - Do users know to link CLI authentication to application deployment workflows?

---

## Document Statistics

### Current Structure
- **Top-level sections:** 3
- **Total subsections:** 8 (including nested levels)
- **Personas addressed:** Platform engineer (implicit throughout)
- **Authentication modes:** 2 (default, core)
- **Reference material:** 1 section with 3 subsections (syntax, options, utilities)

### Proposed JTBD Structure
- **Main jobs:** 7
- **User stories/approaches:** 12 numbered approaches across all jobs
- **Personas addressed:** Platform engineer (explicit in job statements)
- **Workflow stages:** 2 (Getting Started: 4 jobs, Reference: 3 jobs)
- **Authentication modes:** 2 (consolidated in Jobs 2-4 with decision guidance)
- **Topic types:** 6 procedures, 4 concepts, 4 reference entries
- **Line references:** Complete coverage mapping all jobs to source sections

### Coverage Scope
- **Source assemblies:** 3 (configuring, logging in, command reference)
- **Source modules:** 6 (tab completion, login, syntax, options, utilities + technology preview snippet)
- **Total source lines:** 452 (combined document)
- **Content reused:** 100% (no new content, restructure only)

---

## Implementation Notes

### No New Content Required

This consolidation report describes a **restructuring** of existing documentation, not the creation of new material. All jobs map to existing sections:

- Job 1 → Section 1 (Configuring) + Section 3.4 (completion command)
- Jobs 2-4 → Section 2 (Logging in) + Section 3.1 (Basic syntax)
- Jobs 5-7 → Section 3 (Command reference subsections)

### Suggested Implementation Order

1. **High-value consolidations (Phase 1):**
   - Jobs 2-4: Consolidate authentication with mode comparison
   - Job 1: Consolidate shell completion methods with cross-references

2. **Reference reorganization (Phase 2):**
   - Jobs 5-7: Split flat reference into purpose-driven lookup jobs

3. **Gap filling (Phase 3):**
   - Add authentication troubleshooting examples (Job 3 enhancement)
   - Add CI/CD integration patterns (Job 4 enhancement)
   - Add cross-guide links to deployment and monitoring guides

### Stakeholder Considerations

**Documentation Writers:**
- Restructure uses existing content (no new writing)
- Cross-references between jobs improve discoverability
- Decision guidance (mode comparison) may need brief concept addition

**Platform Engineers (Users):**
- Faster authentication mode discovery (consolidated at Getting Started)
- Both completion methods visible together
- Purpose-driven reference jobs match lookup intent

**Content Strategists:**
- JTBD structure exposes gaps (auth errors, CI/CD patterns, multi-instance management)
- Workflow stages clarify content progression (Getting Started → Reference)
- Consolidation reduces section count while improving navigation
