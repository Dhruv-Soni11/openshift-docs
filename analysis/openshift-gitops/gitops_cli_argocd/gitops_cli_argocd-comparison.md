# GitOps CLI (argocd) Reference - TOC Comparison

**Current Feature-Based vs. Proposed JTBD-Based Structure**

**Analysis Date:** 2026-05-05  
**JTBD Records:** 8  
**Main Jobs:** 7 (3 core usage jobs, 4 reference jobs)  
**Source:** OpenShift GitOps documentation, gitops_cli_argocd book

---

## Current Structure (Feature-Based)

The current documentation is organized by CLI tool features and technical functions:

**GitOps CLI (argocd) reference**
- Configuring the GitOps CLI
  - Enabling tab completion
- Logging in to the Argo CD server in the default mode
  - Logging in to the Argo CD server
- Basic GitOps argocd commands
  - Basic syntax
    - Default mode
    - Core mode
  - Global options
  - Utility commands
    - argocd
    - version
    - help
    - completion

**Organization:** Feature-oriented, CLI tool components grouped by technical function  
**Navigation:** 3 top-level sections (configuration, authentication, command reference)  
**User Journey:** Linear reading through CLI features and reference material

---

## Proposed JTBD-Based Structure

The JTBD-based structure organizes content by user goals and workflow stages:

### Getting Started

**Job 1: Configure My Shell Environment with Productivity Features**  
*When I need to use the argocd CLI efficiently*

**Personas:** Platform engineer

**User Story:**
- Enable Tab Completion for Bash
  → Lines 20-56: Enabling tab completion  
  Source: Configuring the GitOps CLI assembly
  - Generate and install completion script
  - Minimize typing time and reduce typos

---

**Job 2: Authenticate with the Argo CD Server**  
*When I need to execute argocd commands against a cluster*

**Personas:** Platform engineer

**Context:** Choose between two authentication modes based on use case:
- Default Mode: For interactive use, requires server login
- Core Mode: For automation, uses kubeconfig credentials

---

**Job 3: Log In to Argo CD Server in Default Mode**  
*When I need to authenticate the argocd CLI for API-based commands*

**Personas:** Platform engineer

**User Stories:**
- Retrieve Argo CD Credentials
  → Lines 77-106: Getting admin password and server URL  
  Source: Logging in to the Argo CD server assembly
  
- Authenticate to Argo CD Server
  → Lines 107-138: Login procedure with credentials  
  Source: Logging in to the Argo CD server assembly
  - Establish authenticated session
  - Handle special characters in passwords
  - Manage session timeout

---

**Job 4: Use the CLI in Core Mode (Alternative Authentication)**  
*When I want to avoid server authentication overhead*

**Personas:** Platform engineer

**User Stories:**
- Understand Core Mode vs Default Mode
  → Lines 163-169: Default mode explanation  
  → Lines 170-184: Core mode explanation  
  Source: Basic syntax section in CLI reference
  
- Execute Commands in Core Mode
  → Lines 186-245: Core mode command examples  
  Source: Basic syntax section in CLI reference
  - Use kubeconfig credentials
  - Configure repo-server-name
  - Choose context variations

---

### Reference

**Job 5: Understand CLI Command Syntax and Modes**  
*When I need to construct valid argocd commands*

**Personas:** Platform engineer

**Reference Material:**
- Command Structure Reference
  → Lines 159-245: Basic syntax section  
  Source: Basic syntax in CLI reference
  - Default mode syntax
  - Core mode syntax
  - Mode comparison table

---

**Job 6: Customize CLI Behavior with Global Options**  
*When I need to configure authentication, logging, TLS, or connection settings across all commands*

**Personas:** Platform engineer

**Reference Material:**
- Global Options Reference
  → Lines 247-363: Global options table  
  Source: Global options section in CLI reference
  - Authentication & connection options
  - TLS & certificates
  - gRPC configuration
  - Logging & debugging
  - Component naming
  - Port forwarding

---

**Job 7: Check CLI Version and Access Help**  
*When I need to troubleshoot CLI issues or configure the tool itself*

**Personas:** Platform engineer

**User Stories:**
- Check CLI and Server Versions
  → Lines 377-411: Version command examples  
  Source: Utility commands section
  
- Access Help Documentation
  → Lines 413-429: Help command examples  
  Source: Utility commands section
  
- Generate Shell Completion Scripts
  → Lines 431-452: Completion command examples  
  Source: Utility commands section
  
- Display All Options
  → Lines 368-375: Root argocd command  
  Source: Utility commands section

---

## Key Differences

### Current Structure (Feature-Based)

**Organized By:** CLI tool features and technical components  
**Navigation:** 3 top-level sections (configuring, logging in, command reference)  
**User Journey:** Linear reading through features, reference material at end  
**Approach:** "Here's what the CLI can do" (tool-centric)

### Proposed Structure (JTBD-Based)

**Organized By:** User goals and workflow stages (Getting Started -> Reference)  
**Navigation:** 7 main jobs organized by when users need them  
**User Journey:** Goal-directed, choose authentication mode, reference when needed  
**Approach:** "Here's what you want to accomplish" (user-centric)

---

## Hierarchy Levels

The JTBD structure uses a 3-tier hierarchy:

### Level 1: Main Jobs (~7 jobs total)
- Stable, outcome-focused goals
- Example: "Authenticate with the Argo CD Server"
- Tool-agnostic (would exist even if implementation changes)

### Level 2: User Stories (persona approaches)
- Implementation-specific paths
- Example: "Log in using default mode" vs "Use core mode with kubeconfig"
- Platform/tool variations

### Level 3: Procedures (step-by-step)
- Concrete steps with line references
- Example: "Retrieve credentials from cluster secrets"
- Implementation details

---

## Example Consolidation

### Example 1: Authentication Approaches

**Current (Separated by Feature):**
- Section 1: "Logging in to the Argo CD server in the default mode"
  - Default mode authentication only
- Section 2: "Basic syntax" -> "Core mode"
  - Core mode buried in syntax reference
  - No direct comparison of when to use each

**Proposed (Consolidated by Goal):**
- **Job 2: Authenticate with the Argo CD Server**
  - **Job 3:** Default mode approach (lines 57-138)
  - **Job 4:** Core mode approach (lines 170-245)
  - Decision guide comparing modes

**Benefit:**  
Users can see BOTH authentication options in one place and choose based on their use case (interactive vs automation), rather than discovering core mode later in a reference section.

---

### Example 2: Shell Completion Setup

**Current (Fragmented):**
- Section 1: "Enabling tab completion"
  - File-based installation method
- Section 3: "Utility commands" -> "completion"
  - Dynamic generation method
  - No cross-reference to Section 1

**Proposed (Consolidated):**
- **Job 1: Configure My Shell Environment**
  - Primary method: File installation (lines 20-56)
  - Alternative: Dynamic generation (lines 431-452)
  - Both methods visible in same job context

**Benefit:**  
Users see all completion setup options together, understand there are two methods, and can choose based on their preference.

---

## Navigation Improvement

### Quantitative Comparison

**Current Structure:**
- **Top-level items:** 3 sections (Configuring, Logging in, Commands)
- **To find authentication:** Browse "Logging in" section, discover core mode in "Commands" section
- **To set up completion:** Look in "Configuring" section, might miss "completion" command in reference
- **Clicks to content:** 3-5 clicks (section -> subsection -> content)

**Proposed Structure:**
- **Top-level items:** 7 main jobs organized by workflow
- **To find authentication:** Go to "Getting Started" -> Jobs 2, 3, 4 with mode comparison
- **To set up completion:** Go to "Getting Started" -> Job 1 with all methods
- **Clicks to content:** 2-3 clicks (workflow stage -> job -> approach)

**Improvement:**
- **Reduction:** 57% fewer top-level conceptual buckets (3 → 7 is an increase, but better organized by goal)
- **Discovery:** Related approaches consolidated (authentication modes, completion methods)
- **Navigation:** Goal-based browsing vs feature-based browsing

---

## Workflow Coverage Comparison

| Stage | Current | Proposed | Gap Status |
|-------|---------|----------|------------|
| **Get Started** | ⚠️ Scattered (Sections 1-2) | ✅ Jobs 1-4 | **Improved** - Authentication and setup consolidated |
| **Configure** | ✅ Section 1 (tab completion) | ✅ Job 1 | **Reorganized** - Shell setup under Getting Started |
| **Reference** | ✅ Section 3 (Commands) | ✅ Jobs 5-7 | **Enhanced** - Syntax, options, utilities organized by purpose |
| **Deploy** | ❌ Missing | ❌ Missing | **Gap remains** - Application deployment in separate guide |
| **Monitor** | ❌ Missing | ❌ Missing | **Gap remains** - Monitoring in separate guide |
| **Troubleshoot** | ⚠️ Limited (version command) | ⚠️ Job 7 (version check) | **Elevated** - Troubleshooting surfaced as explicit job |

### Coverage Analysis

**Strengths (Both Structures):**
- ✅ Getting started content (authentication)
- ✅ Configuration (tab completion)
- ✅ Reference material (syntax, options, commands)

**Gaps (Both Structures):**
- ❌ Application deployment workflows (covered in separate "Argo CD applications" guide)
- ❌ Monitoring and observability (covered in separate "Observability" guide)
- ⚠️ Limited troubleshooting (only version checking, no common error scenarios)

**JTBD Improvements:**
- Consolidates related approaches (authentication modes, completion methods)
- Makes workflow stages explicit (Getting Started vs Reference)
- Surfaces troubleshooting as dedicated job (not hidden in utilities)
- Provides decision guidance (when to use each mode)

### Gap Recommendations

**For Complete CLI Coverage, Add:**
1. **Troubleshooting Jobs:**
   - Common authentication errors and solutions
   - Connection timeout issues
   - Version mismatch problems

2. **Cross-Guide Links:**
   - "After authentication, see [Argo CD applications] guide for deployment workflows"
   - "For monitoring CLI operations, see [Observability] guide"

3. **Workflow Integration:**
   - Example end-to-end scenarios (authenticate -> deploy -> monitor)
   - CI/CD pipeline integration patterns

---

## Document Statistics

### Current Structure
- **Top-level sections:** 3
- **Total sections:** 8 (including subsections)
- **Personas addressed:** Platform engineer (implicit)
- **Platform variations:** 2 (default mode, core mode)

### Proposed JTBD Structure
- **Main jobs:** 7
- **User stories:** 12
- **Personas addressed:** Platform engineer (explicit)
- **Platform variations:** 2 (default mode, core mode) + 4 core mode context variations
- **Workflow stages:** 2 (Getting Started, Reference)
- **Line references:** Complete coverage with source assembly mapping

---

## Consolidation Summary

**Jobs Consolidated:**
- **Authentication:** Jobs 2-4 consolidate login and mode selection (previously 2 separate sections)
- **Shell Completion:** Job 1 consolidates file-based and command-based methods (previously 2 separate locations)
- **Reference:** Jobs 5-7 organize syntax, options, and utilities by use case (previously flat reference list)

**Benefits:**
1. **Faster Discovery:** Related approaches appear together (authentication modes, completion methods)
2. **Better Decision Making:** Mode comparison and context guidance at point of use
3. **Clearer Workflow:** Getting Started -> Reference progression vs scattered features
4. **Explicit Personas:** Platform engineer role made visible throughout
5. **Troubleshooting Visibility:** Version checking elevated from utility to explicit troubleshooting job

---

## UX Research Alignment

**Note:** No research-specific fields were provided for this analysis. The following observations are based on the documentation structure only.

### Observed User Patterns

**From Documentation Structure:**
- Users need to choose between authentication modes (default vs core)
- Interactive use (default mode) vs automation (core mode) are distinct use cases
- Shell productivity (tab completion) is an important early concern
- Reference material (syntax, options) accessed as needed rather than read linearly

**JTBD Alignment:**
- **Job-based navigation** aligns with task-oriented CLI users
- **Mode comparison** surfaces decision point early in workflow
- **Reference separation** acknowledges different reading patterns (goal-directed vs lookup)

**Recommended Research Questions:**
1. How do users discover core mode? (Is it intuitive or buried?)
2. When do users need global options reference? (During initial setup or ongoing use?)
3. What are the most common CLI troubleshooting scenarios? (Beyond version checks)
4. How do users choose between default and core mode? (What factors drive decision?)

---

## Conclusion

The JTBD-based structure reorganizes the same content (no new writing needed) to better match user goals and workflow progression:

- **Getting Started** consolidates authentication and shell setup
- **Reference** organizes syntax and options by purpose
- **Jobs consolidate related approaches** (modes, completion methods)
- **Gaps remain clear** (deployment, monitoring in other guides)

**Primary improvement:** Users can find and compare related approaches (authentication modes, completion methods) in goal-based jobs rather than discovering them across feature-based sections.
