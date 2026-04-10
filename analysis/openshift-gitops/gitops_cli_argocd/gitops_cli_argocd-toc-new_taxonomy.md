# GitOps CLI (argocd) Reference
**Jobs-To-Be-Done Oriented Table of Contents**

*Organized by user goals and workflow stages*

---

## Guide Overview

**Purpose:** Enable platform engineers to configure, authenticate, and use the OpenShift GitOps argocd CLI tool to manage GitOps resources from the command line.

**Personas:** Platform engineer

**Main Jobs:** 5 core jobs across 3 workflow stages (Configure, Get Started, Reference)

---

## Quick Navigation

**I want to:**
- Improve my CLI productivity with tab completion -> Job 1 (Configure)
- Authenticate to Argo CD from the CLI -> Job 2, Job 3 (Get Started)
- Use the CLI without logging into the server -> Job 3 (Get Started)
- Understand CLI command syntax and modes -> Job 4 (Reference)
- Find available global options and flags -> Job 5 (Reference)
- Check CLI version or get help -> Job 6 (Reference)

---

# Table of Contents

## Set Up & Configure

### Job 1: Configure My Shell Environment with Productivity Features
*When I need to use the argocd CLI efficiently*

**Personas:** Platform engineer

**Prerequisites:**
- argocd CLI tool installed
- bash-completion installed on local system

#### 1.1 Enable Tab Completion for Bash

**Goal:** Set up automatic command completion to work faster and avoid errors.

→ Lines 20-56: Enabling tab completion  
  Source: Configuring the GitOps CLI assembly

**Procedure:**

- **Task:** Generate completion script
  ```bash
  argocd completion bash > argocd_bash_completion
  ```

- **Task:** Install completion script globally
  ```bash
  sudo cp argocd_bash_completion /etc/bash_completion.d/
  ```
  
  **Alternative:** Save to local directory and source from `.bash_profile`

- **Outcome:** Tab completion enabled when you open a new terminal

**Benefits:**
- Minimize time spent typing commands
- Reduce likelihood of typos in command names
- Discover command options without consulting documentation

**Note:** Tab completion only available for Bash shell (not zsh via this method)

---

## Getting Started

### Job 2: Authenticate with the Argo CD Server
*When I need to execute argocd commands against a cluster*

**Personas:** Platform engineer

**Prerequisites:**
- argocd CLI installed and configured
- Argo CD deployed on the cluster

**Why:** Authentication establishes the CLI session needed for all subsequent argocd commands in default mode.

#### Choose Your Authentication Mode

**Two modes are available:**

- **Default Mode:** CLI communicates with Argo CD server via API (requires login)
  - Best for: Interactive use, manual operations
  - Use Job 3 for the login procedure

- **Core Mode:** CLI communicates directly with Kubernetes API (no login needed)
  - Best for: Automated workflows, CI/CD pipelines, avoiding authentication overhead
  - Use Job 3 for core mode configuration

---

### Job 3: Log In to Argo CD Server in Default Mode
*When I need to authenticate the argocd CLI for API-based commands*

**Personas:** Platform engineer

**Prerequisites:**
- argocd CLI installed and configured
- Admin credentials or user credentials for Argo CD

→ Lines 77-138: Logging in to the Argo CD server  
  Source: Logging in to the Argo CD server in the default mode assembly

#### 3.1 Retrieve Argo CD Credentials (Preparation Step)

**Goal:** Obtain the admin password and server URL from the cluster.

- **Task:** Get admin password from cluster secret
  ```bash
  ADMIN_PASSWD=$(oc get secret openshift-gitops-cluster -n openshift-gitops \
    -o jsonpath='{.data.admin\.password}' | base64 -d)
  ```

- **Task:** Get Argo CD server URL
  ```bash
  SERVER_URL=$(oc get routes openshift-gitops-server -n openshift-gitops \
    -o jsonpath='{.status.ingress[0].host}')
  ```

#### 3.2 Authenticate to Argo CD Server

**Goal:** Establish an authenticated CLI session.

- **Task:** Log in with admin credentials
  ```bash
  argocd login --username admin --password ${ADMIN_PASSWD} ${SERVER_URL}
  ```

**Important:** Enclose password in single quotes to handle special characters:
  ```bash
  argocd login --username admin --password '<password>' \
    openshift-gitops.openshift-gitops.apps-crc.testing
  ```

**Expected Output:**
```
'admin:login' logged in successfully
Context '<server_url>' updated
```

**Session Management:**
- Session may timeout during extended work
- Use `relogin` command to re-authenticate
- Use `logout` command when finished

**Desired Outcomes:**
- Establish authenticated session with Argo CD server
- Avoid exposing credentials to shell history or logs
- Ensure session persists throughout work period

---

### Job 4: Use the CLI in Core Mode (Alternative Authentication)
*When I want to avoid server authentication overhead*

**Personas:** Platform engineer

**Prerequisites:**
- kubeconfig file with cluster credentials
- argocd CLI installed

→ Lines 170-245: Core mode description and examples  
  Source: Basic syntax section in CLI reference

#### 4.1 Understand Core Mode vs Default Mode

**Goal:** Choose the right authentication mode for your workflow.

**Default Mode:**
- CLI communicates with Argo CD server component through API requests
- Requires login with Argo CD credentials
- Session-based authentication (can timeout)
- Command syntax: `argocd [command] [options] [arguments...]`

**Core Mode:**
- CLI communicates directly with Kubernetes API server
- Uses credentials from kubeconfig file
- No login required (Kubernetes authentication only)
- Must specify repo-server-name
- Command syntax: `argocd --core [command] [options] [arguments...]`

#### 4.2 Execute Commands in Core Mode

**Goal:** Run argocd commands using Kubernetes credentials instead of server login.

**Required Configuration:**
- Set `--repo-server-name` option OR `ARGOCD_REPO_SERVER_NAME` environment variable
- If multiple Argo CD instances exist, set default namespace to the instance namespace

**Options for Core Mode Execution:**

- **Option 1: Default kubeconfig, Default context**
  ```bash
  argocd --core app list --repo-server-name openshift-gitops-repo-server
  ```
  
  Or with environment variable:
  ```bash
  ARGOCD_REPO_SERVER_NAME=openshift-gitops-repo-server argocd --core app list
  ```

- **Option 2: Default kubeconfig, Custom context**
  ```bash
  argocd --core --kube-context kubeadmin-local app list \
    --repo-server-name openshift-gitops-repo-server
  ```

- **Option 3: Custom kubeconfig, Default context**
  ```bash
  KUBECONFIG=~/.kube/custom_config argocd --core app list \
    --repo-server-name openshift-gitops-repo-server
  ```

- **Option 4: Custom kubeconfig, Custom context**
  ```bash
  KUBECONFIG=~/.kube/custom_config argocd --kube-context kubeadmin-local \
    --core app list --repo-server-name openshift-gitops-repo-server
  ```

**Desired Outcomes:**
- Execute commands without logging in to Argo CD server
- Minimize authentication friction for automated workflows
- Ensure commands target the correct Argo CD instance namespace

---

## Reference

### Job 5: Understand CLI Command Syntax and Modes
*When I need to construct valid argocd commands*

**Personas:** Platform engineer

→ Lines 159-245: Basic syntax section  
  Source: Basic syntax in CLI reference

#### Command Structure Reference

**Default Mode Syntax:**
```
argocd [command or options] [arguments...]
```

**Core Mode Syntax:**
```
KUBECONFIG=~/.kube/config argocd --core [command or options] [arguments...]
```

**Key Differences:**

| Aspect | Default Mode | Core Mode |
|--------|--------------|-----------|
| Authentication | Argo CD server login required | Kubernetes kubeconfig credentials |
| Communication | Argo CD API server | Kubernetes API server directly |
| Session | Login/logout/relogin commands | No session management |
| Repo server | Auto-detected | Must specify via --repo-server-name |

**When to Use Each Mode:**
- **Default mode:** Interactive sessions, manual operations
- **Core mode:** Automation, CI/CD pipelines, avoiding login overhead

---

### Job 6: Customize CLI Behavior with Global Options
*When I need to configure authentication, logging, TLS, or connection settings across all commands*

**Personas:** Platform engineer

→ Lines 247-363: Global options table  
  Source: Global options section in CLI reference

#### Global Options Reference

**Global options apply to ALL argocd subcommands.**

**Authentication & Connection:**
- `--auth-token <string>` - Authentication token
- `--server <string>` - Argo CD server address
- `--insecure` - Skip server certificate and domain verification
- `--kube-context <string>` - Direct command to given kube context

**TLS & Certificates:**
- `--client-crt <string>` - Client certificate file
- `--client-crt-key <string>` - Client certificate key file
- `--server-crt <string>` - Server certificate file
- `--plaintext` - Disable TLS protocols

**gRPC Configuration:**
- `--grpc-web` - Enable gRPC-Web protocol (for proxies without HTTP/2)
- `--grpc-web-root-path <string>` - Set web root for gRPC-Web

**Logging & Debugging:**
- `--logformat <string>` - Set format to `text` or `json` (default: `text`)
- `--loglevel <string>` - Set level: `debug`, `info`, `warn`, `error` (default: `info`)
- `--http-retry-max <integer>` - Max retries for HTTP connection to server

**Component Naming:**
- `--controller-name <string>` - Argo CD Application Controller name (default: `argocd-application-controller`)
- `--server-name <string>` - Argo CD API server name (default: `argocd-server`)
- `--repo-server-name <string>` - Repo server name (default: `argocd-repo-server`)
- `--redis-name <string>` - Redis deployment name (default: `argocd-redis`)
- `--redis-haproxy-name <string>` - Redis HA Proxy name (default: `argocd-redis-ha-haproxy`)

**Note:** Component naming options are needed when labels differ from defaults (e.g., Helm chart installations). Set via flag or corresponding environment variable (e.g., `ARGOCD_REPO_SERVER_NAME`).

**Port Forwarding:**
- `--port-forward` - Connect via port forwarding to random Argo CD server port
- `--port-forward-namespace <string>` - Namespace for port forwarding

**Other Options:**
- `--config <string>` - Path to Argo CD config file (default: `/home/user/.config/argocd/config`)
- `--core` - Communicate directly with Kubernetes API instead of Argo CD server
- `-H, --header <string>` - Add custom header to all requests (repeatable, supports comma-separated)
- `-h, --help` - Help for argocd CLI

**Desired Outcomes:**
- Discover available global options for my use case
- Understand how to configure TLS, authentication, and logging
- Know which environment variables can replace command-line flags

---

### Job 7: Check CLI Version and Access Help
*When I need to troubleshoot CLI issues or configure the tool itself*

**Personas:** Platform engineer

→ Lines 365-452: Utility commands  
  Source: Utility commands section in CLI reference

#### 7.1 Check CLI and Server Versions

**Goal:** Verify client and server version compatibility.

**Command Syntax:**
```
argocd version [flags]
```

**Examples:**

- **Print full version of client and server:**
  ```bash
  argocd version
  ```

- **Print client version only (no server connection):**
  ```bash
  argocd version --client
  ```

- **Print server version only:**
  ```bash
  argocd version --server <server_url>
  ```

- **Output in JSON format:**
  ```bash
  argocd version -o json
  ```

- **Output core version strings only in YAML:**
  ```bash
  argocd version --short -o yaml
  ```

#### 7.2 Access Help Documentation

**Goal:** Get command-specific help without external documentation.

**Command Syntax:**
```
argocd help [command] [flags]
```

**Examples:**

- **Get help for all commands:**
  ```bash
  argocd help
  ```

- **Get help for specific subcommand:**
  ```bash
  argocd help admin
  ```

#### 7.3 Generate Shell Completion Scripts

**Goal:** Create completion scripts for bash or zsh shells.

**Command Syntax:**
```
argocd completion SHELL [flags]
```

**For Bash:**
```bash
# Access completion in current shell:
source <(argocd completion bash)
```

**For Zsh:**
```bash
# Add to ~/.zshrc:
source <(argocd completion zsh)
compdef _argocd argocd
```

**Note:** This is an alternative to the installation method in Job 1. This generates the script dynamically vs saving to a file.

#### 7.4 Display All Options (Root Command)

**Goal:** See all available argocd commands and options.

**Command:**
```bash
argocd
```

**Desired Outcomes:**
- Verify CLI and server versions match
- Access help text without external documentation
- Generate shell completion scripts for bash or zsh

---

## Appendices

### A. Workflow Coverage Analysis

| Stage | Coverage | Jobs | Notes |
|-------|----------|------|-------|
| Get Started | ✅ | Jobs 2, 3, 4 | Authentication and initial setup |
| Configure | ✅ | Job 1 | Shell productivity features |
| Reference | ✅ | Jobs 5, 6, 7 | Syntax, options, and utility commands |
| Deploy | ❌ | - | No deployment content (separate guide) |
| Monitor | ❌ | - | No monitoring content (separate guide) |
| Troubleshoot | ⚠️ Limited | Job 7 (version check) | Basic version troubleshooting only |

### Gaps Identified

| Stage | Gap | Recommendation |
|-------|-----|----------------|
| Deploy | No application deployment | Link to "Argo CD applications" guide |
| Monitor | No monitoring/observability | Link to "Observability" guide |
| Troubleshoot | Limited troubleshooting | Add common CLI error scenarios |

---

### B. Authentication Mode Decision Guide

| Mode | Best For | Authentication | Prerequisites |
|------|----------|----------------|---------------|
| **Default** | Interactive use, manual operations | Argo CD server login | argocd credentials |
| **Core** | Automation, CI/CD, scripted workflows | Kubernetes kubeconfig | kubeconfig with cluster access |

**Choose Default Mode when:**
- Working interactively from command line
- Using Argo CD user accounts (not cluster admin)
- Server-side features require API server communication

**Choose Core Mode when:**
- Integrating into CI/CD pipelines
- Avoiding session timeout issues
- Working with multiple kubeconfig files/contexts
- Need direct Kubernetes API access

---

### C. Quick Reference

**Tab Completion Setup (Bash):**
```bash
argocd completion bash > argocd_bash_completion
sudo cp argocd_bash_completion /etc/bash_completion.d/
```

**Login (Default Mode):**
```bash
ADMIN_PASSWD=$(oc get secret openshift-gitops-cluster -n openshift-gitops \
  -o jsonpath='{.data.admin\.password}' | base64 -d)
SERVER_URL=$(oc get routes openshift-gitops-server -n openshift-gitops \
  -o jsonpath='{.status.ingress[0].host}')
argocd login --username admin --password "${ADMIN_PASSWD}" ${SERVER_URL}
```

**Core Mode (No Login):**
```bash
ARGOCD_REPO_SERVER_NAME=openshift-gitops-repo-server argocd --core app list
```

**Check Version:**
```bash
argocd version
```

**Get Help:**
```bash
argocd help
argocd help <command>
```

---

## Navigation Guide

### By User Journey

**First-time CLI user setting up for daily use:**
1. Job 1: Configure tab completion for productivity
2. Job 2 + Job 3: Authenticate with Argo CD server in default mode
3. Job 5: Understand CLI syntax and command structure
4. Job 6: Explore global options for common customization

**Platform engineer setting up CLI for CI/CD pipeline:**
1. Job 2: Understand authentication modes
2. Job 4: Configure core mode with kubeconfig credentials
3. Job 6: Review global options for automation (logging, retries)
4. Job 7: Verify client/server version compatibility

**Troubleshooting CLI issues:**
1. Job 7.1: Check CLI and server versions
2. Job 6: Review logging options (`--loglevel`, `--logformat`)
3. Job 3: Re-authenticate if session expired
4. Job 7.2: Access help for specific commands

---

## Document Statistics

**Workflow Coverage:**
- Get Started: 3 jobs (authentication and modes)
- Configure: 1 job (tab completion)
- Reference: 3 jobs (syntax, options, utilities)
- **Gaps:** Deploy (separate guide), Monitor (separate guide), Troubleshoot (limited)

**Main Jobs:** 7
**User Stories/Paths:** 12
**Source Sections:** 3 assemblies (configuring, logging in, reference)
**CLI Modes Covered:** 2 (default mode, core mode)

**Technology Preview Notice:** The argocd CLI tool is a Technology Preview feature. Not supported for production use.
