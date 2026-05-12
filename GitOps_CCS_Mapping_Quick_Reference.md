# GitOps → CCS Category Mapping
## Quick Reference Guide

**Date:** May 12, 2026  
**Version:** OpenShift GitOps 1.19

---

## At a Glance: Mapping Summary

| Current Category | → | CCS Category | Action Required |
|-----------------|---|--------------|-----------------|
| Release notes | → | **What's new** | ✅ Direct match |
| Understanding OpenShift GitOps | → | **Discover** | ✅ Direct match |
| ~~Managing cluster configuration~~ | → | **Configure** | 🔧 Rename + Consolidate |
| Installing GitOps | → | **Install** | ✅ Direct match |
| Argo CD instance | → | **Configure** | 🔀 Merge into Configure |
| ~~Access control and user management~~ | → | **Secure** | ⚠️ CONSOLIDATE with Security |
| ~~Managing resource use~~ | → | **Optimize** | 🔧 Rename + Consolidate |
| Argo CD applications | → | **Develop** | 🔧 Rename (optional) |
| Argo CD application sets | → | **Develop** | 🔀 Merge into Develop |
| Multitenancy | → | **Configure** | 🔀 Keep or merge |
| ~~Declarative cluster configuration~~ | → | **Configure** | ⚠️ CONSOLIDATE with cluster config |
| Argo CD Agent architecture | → | **Discover** | 📍 Move to Discover |
| Argo CD Agent installation | → | **Extend** | 📍 Move to Extend |
| Argo Rollouts | → | **Extend** | ✅ Direct match |
| ~~Security~~ | → | **Secure** | ⚠️ CONSOLIDATE with Access control |
| GitOps CLI reference | → | **Reference** | 📍 Move to bottom |
| Observability | → | **Observe** | ✅ Direct match |
| GitOps workloads on infra nodes | → | **Optimize** | 🔀 Merge into Optimize |
| Troubleshooting issues | → | **Troubleshoot** | 📍 Move to bottom + 📈 Expand |
| Removing GitOps | → | **Install** | 🔀 Make subsection of Install |

**Legend:**
- ✅ No change needed
- 🔧 Rename recommended  
- 🔀 Merge/consolidate
- 📍 Reposition in TOC
- ⚠️ Requires action
- 📈 Expand content

---

## Special Cases Explained

### "Progressive delivery" → **Extend** (via Argo Rollouts)
Progressive delivery is **not a standalone category**.  
It's covered under **Argo Rollouts**, which correctly maps to **Extend**.

**Topics:**
- "Using Progressive Sync in OpenShift GitOps"
- "Using Argo Rollouts for progressive deployment delivery"

**Action:** Consolidate all progressive delivery content under Argo Rollouts

---

### "Manage" / "Managing" → **Context-dependent mapping**
"Manage" is **not a CCS-approved category**.

**Mapping rules:**
- "Managing configuration" → **Configure**
- "Managing resources/sizing" → **Optimize**  
- "Managing security/secrets" → **Secure**
- "Managing applications" → **Develop**
- "Managing operations" → **Administer**

**Action:** Replace "Managing X" with appropriate CCS verb based on what X is

---

### "Security" appears twice → **Consolidate to Secure**

**Current split:**
1. "Access control and user management" (RBAC, SSO, auth)
2. "Security" (Redis security, secrets, masking)

**Recommendation:** Merge into single **Secure** category

**Proposed structure:**
```
Secure
├── Access control and RBAC
├── Authentication and SSO  
├── Secrets management
└── Secure communications
```

---

## Direct Matches (No Changes Needed)

| Current | CCS Category |
|---------|--------------|
| Release notes | What's new ✅ |
| Understanding OpenShift GitOps | Discover ✅ |
| Installing GitOps | Install ✅ |
| Managing resource use | Optimize ✅ (rename recommended) |
| Argo Rollouts | Extend ✅ |
| Security | Secure ✅ (consolidate required) |
| GitOps CLI reference | Reference ✅ (reposition to bottom) |
| Observability | Observe ✅ |
| Troubleshooting issues | Troubleshoot ✅ (expand content) |

---

## Functional Groupings (Mapping Required)

| Current | CCS Category | Why |
|---------|--------------|-----|
| Managing cluster configuration | **Configure** | Configuring cluster settings |
| Argo CD instance | **Configure** | Post-install configuration |
| Argo CD applications | **Develop** | Creating apps = development |
| Application sets | **Develop** | Building automation |
| Multitenancy | **Configure** | Configuring tenant isolation |
| Declarative cluster config | **Configure** | Config methodology |
| GitOps workloads on infra nodes | **Optimize** | Performance optimization |

---

## Subcategories (Merge or Move)

| Current | CCS Category | Action |
|---------|--------------|--------|
| Argo CD instance | **Configure** | Merge into Configure |
| Agent architecture | **Discover** | Move to Discover section |
| Agent installation | **Extend** or **Install** | Move to appropriate section |
| Removing GitOps | **Install** | Make subsection (uninstall is part of install lifecycle) |

---

## Missing CCS Categories (Gaps)

| CCS Category | Status | Recommendation |
|--------------|--------|----------------|
| **Get started** | ❌ No coverage | CREATE quick-start tutorial |
| **Plan** | ❌ No coverage | CREATE sizing and architecture planning |
| **Upgrade** | ❌ No coverage | CREATE upgrade procedures |
| **Migrate** | ❌ No coverage | Evaluate if needed |
| **Administer** | ❌ No coverage | CREATE operational management content |
| **Integrate** | ⚠️ Minimal | CREATE integration patterns section |
| **Download PDF** | N/A | Add TOC entry |

---

## Recommended TOC (CCS-Compliant)

### Fixed Top Section
1. **What's new** ← Release notes
2. **Discover** ← Understanding + Agent architecture  
3. **Get started** ← NEW: Create content
4. **Plan** ← NEW: Create content

### Flexible Middle Section
5. **Install** ← Installing + Removing (subsection)
6. **Upgrade** ← NEW: Create content
7. **Migrate** ← NEW: If applicable
8. **Administer** ← NEW: Create content
9. **Develop** ← Applications + Application sets
10. **Configure** ← Cluster config + Argo CD instance + Multitenancy + Declarative config
11. **Secure** ← Access control + Security (CONSOLIDATED)
12. **Observe** ← Observability
13. **Integrate** ← NEW: Integration patterns
14. **Optimize** ← Resource use + Infra nodes (CONSOLIDATED)
15. **Extend** ← Argo Rollouts + Agent installation

### Fixed Bottom Section
16. **Troubleshoot** ← Troubleshooting (EXPAND)
17. **Reference** ← CLI reference (EXPAND)
18. **Download PDF** ← Add entry

---

## Implementation Checklist

### Phase 1: Quick Wins (Week 1)
- [ ] Rename "Release notes" to "What's new"
- [ ] Rename "Managing resource use" to "Optimize resource usage"
- [ ] Move "GitOps CLI reference" to bottom section
- [ ] Move "Troubleshooting issues" to bottom section

### Phase 2: Consolidation (Weeks 2-3)
- [ ] Consolidate "Security" + "Access control" → "Secure"
- [ ] Consolidate cluster configuration topics → "Configure"
- [ ] Consolidate optimization topics → "Optimize"
- [ ] Move "Removing GitOps" under "Install"
- [ ] Move "Agent architecture" to "Discover"

### Phase 3: New Content (Months 2-3)
- [ ] Create "Get started" quick-start guide
- [ ] Create "Plan" deployment planning content
- [ ] Create "Upgrade" procedures
- [ ] Expand "Troubleshoot" with more scenarios
- [ ] Expand "Reference" with API and CRD docs
- [ ] Create "Integrate" section for integration patterns

### Phase 4: Review and Polish (Month 4)
- [ ] Validate all mappings with stakeholders
- [ ] Test navigation and discoverability
- [ ] Update cross-references
- [ ] Final TOC review against CCS guidelines

---

## Key Decisions Made

### ✅ Progressive delivery → Extend
**Rationale:** Progressive delivery is implemented via Argo Rollouts, which is an optional component that extends GitOps capabilities. Maps to CCS Extend.

### ✅ Security topics → Consolidate to Secure
**Rationale:** Two separate security sections create fragmentation. Consolidate into single comprehensive Secure category.

### ✅ Managing X → Context-specific mapping
**Rationale:** "Manage" is not a CCS category. Map based on what's being managed (config, resources, apps, etc.)

### ⚠️ Agent installation → Extend (recommended)
**Rationale:** Agent is optional architectural enhancement. Could be Install if core deployment option, but Extend better fits optional nature.

### ✅ Removing → Install subsection
**Rationale:** CCS Install explicitly includes uninstalling procedures as part of installation lifecycle.

---

## Questions & Answers

**Q: Is "Progressive delivery" an approved CCS category?**  
A: No. Progressive delivery content lives under Argo Rollouts → **Extend**.

**Q: What about "Manage" category?**  
A: "Manage" is not CCS-approved. Use: Configure, Optimize, Secure, Develop, or Administer based on context.

**Q: Why consolidate Security sections?**  
A: CCS framework has one **Secure** category. Multiple security sections fragment the content and confuse users.

**Q: Where does "Removing GitOps" go?**  
A: Under **Install** as a subsection. CCS Install includes "uninstalling procedures."

**Q: Do we need all 18 CCS categories?**  
A: No. Only include categories where you have content. Don't add empty categories to the TOC.

---

## Contact

For questions about this mapping:
- Review: `GitOps_CCS_Category_Mapping.md` (detailed analysis)
- Spreadsheet: `GitOps_CCS_Mapping_Summary_Table.csv` (for tracking)
- CCS Reference: `Product documentation categories.docx`

---

**Version:** 1.0  
**Last Updated:** May 12, 2026  
**Status:** ✅ Ready for implementation
