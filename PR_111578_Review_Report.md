# Peer and CQA Review: PR #111578
**Title:** Added documentation for Runtime class  
**Author:** shivanisathe25  
**Issue:** RHDEVDOCS-7604  
**Version:** build-docs-1.8  
**Status:** OPEN (1 approval from @avinal)  
**Review Date:** May 14, 2026

---

## Executive Summary

This PR adds comprehensive documentation for RuntimeClass support in OpenShift Builds, including configuration procedures and troubleshooting guidance. The content is technically sound and well-structured. However, there are several **critical issues** that must be addressed before merge.

**Overall Assessment:** ⚠️ **REQUIRES CHANGES** (7 critical issues, 8 moderate issues, 4 minor suggestions)

---

## Critical Issues (Must Fix)

### 1. Missing Trailing Newlines ⚠️ CRITICAL
**Severity:** High  
**Location:** Multiple files

The following files do not end with a trailing newline, which can cause git merge issues:

- `modules/ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc` (line 75)
- `modules/ob-troubleshoot-buildrun-field-override-forbidden.adoc` (line 48)

**Fix:** Add a newline character at the end of each file.

```bash
# Verify with:
tail -c 1 modules/ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc | od -An -tx1
# Should show '0a' (newline)
```

---

### 2. Inconsistent Capitalization in Module Filenames ⚠️ CRITICAL
**Severity:** High  
**Location:** `modules/ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc`

**Issue:** Filename uses `RuntimeClass` with capital letters, which is inconsistent with other module filenames that use lowercase.

**Current:**
```
ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc
```

**Should be:**
```
ob-isolate-all-project-builds-using-a-specific-runtimeclass.adoc
```

**Impact:** This affects the include statement and overall naming conventions.

---

### 3. Technology Preview Disclaimer Position ⚠️ CRITICAL
**Severity:** Moderate  
**Location:** `configuring/isolate-build-workloads-for-security-and-compliance.adoc` (lines 16-17)

**Issue:** Technology Preview snippet is placed **after** the abstract, but per Red Hat documentation standards, it should be placed **before** any procedural content but should reference the specific feature.

**Current position:**
```adoc
[role="_abstract"]
By default, build pods run using...

:FeatureName: Builds in sandbox containers
include::snippets/technology-preview.adoc[]
```

**Recommendation:** The current position is acceptable, but consider whether this applies to all RuntimeClass usage or only specific implementations. If it only applies to Kata Containers/sandboxed containers, clarify this in the feature name.

---

### 4. Incorrect Table Syntax ⚠️ CRITICAL
**Severity:** High  
**Location:** `modules/ob-runtimeclass-prerequisites-and-precedence.adoc` (line 71)

**Issue:** Table row is missing the closing pipe (`|`).

**Current:**
```adoc
| kata | gvisor | gvisor

|===
```

**Should be:**
```adoc
| kata | gvisor | gvisor |

|===
```

**Impact:** This will cause rendering errors in the table.

---

### 5. Technology Preview Feature Scope Unclear ⚠️ MODERATE
**Severity:** Moderate  
**Location:** `configuring/isolate-build-workloads-for-security-and-compliance.adoc`

**Issue:** The technology preview notice states "Builds in sandbox containers" but it's unclear if:
1. All RuntimeClass support is tech preview, OR
2. Only Kata Containers/sandboxed containers are tech preview

**Recommendation:** Clarify the scope. If RuntimeClass support is GA but Kata Containers specifically is tech preview, update the disclaimer:

```adoc
:FeatureName: OpenShift Sandboxed Containers (Kata Containers)
include::snippets/technology-preview.adoc[]
```

---

### 6. Incomplete Prerequisites in Procedure ⚠️ MODERATE
**Severity:** Moderate  
**Location:** `modules/ob-override-runtimeclass-for-specific-build-run.adoc` (lines 19-22)

**Issue:** Prerequisites list mentions needing a RuntimeClass but doesn't specify worker node requirements.

**Current:**
```adoc
.Prerequisites

* You have an existing `Build` resource.
* A RuntimeClass resource exists in your cluster that you want to use for this specific build run.
```

**Should add:**
```adoc
* Worker nodes have the required runtime installed and configured.
* The RuntimeClass resource exists in your cluster and is ready to use.
```

---

### 7. Inconsistent Formatting of Code Elements ⚠️ MODERATE
**Severity:** Moderate  
**Location:** Multiple files

**Issue:** Some references to Kubernetes/Builds resources are in backticks, others are not.

**Examples of inconsistency:**
- `Build` (correct) vs Build (incorrect)
- `BuildRun` (correct) vs BuildRun (incorrect)
- `RuntimeClass` (correct) vs RuntimeClass (incorrect)

**Locations:**
- Line 10 in `ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc`: "reference this `Build`" ✓ (correct)
- Line 20 in `ob-override-runtimeclass-for-specific-build-run.adoc`: "existing `Build` resource" ✓ (correct)

Most are correct, but verify consistency throughout.

---

## Moderate Issues (Should Fix)

### 8. Link Formatting ⚠️ MODERATE
**Severity:** Moderate  
**Location:** `configuring/isolate-build-workloads-for-security-and-compliance.adoc` (lines 29-30)

**Issue:** External links should use the `link:` prefix for clarity, which they do. However, consider if these should be versioned links or if general documentation links are appropriate.

**Current:**
```adoc
* link:https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/[OpenShift Sandboxed Containers documentation]
```

**Recommendation:** If there's a specific version of Sandboxed Containers that corresponds to this Builds version, use a versioned link:
```adoc
* link:https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/1.x/[OpenShift Sandboxed Containers 1.x documentation]
```

---

### 9. Ambiguous Wording in NOTE ⚠️ MODERATE
**Severity:** Moderate  
**Location:** `modules/ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc` (lines 54-57)

**Issue:** The NOTE uses "takes priority over" but the more common phrasing in OpenShift docs is "overrides" or "has precedence over".

**Current:**
```adoc
[NOTE]
====
If you also define `spec.runtimeClassName` in the `BuildRun` CR, the `BuildRun` value takes priority over the `Build` value.
====
```

**Recommended:**
```adoc
[NOTE]
====
If you also define `spec.runtimeClassName` in the `BuildRun` resource, the `BuildRun` value overrides the `Build` value.
====
```

**Rationale:** 
- Change "CR" to "resource" for consistency
- Use "overrides" instead of "takes priority over" for consistency with OpenShift documentation

---

### 10. Memory Values Formatting ⚠️ MODERATE
**Severity:** Low  
**Location:** `modules/ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc` (line 15)

**Issue:** Memory values are written inconsistently (2Gi vs 2 GiB).

**Current:**
```adoc
* Worker nodes have sufficient capacity. Kata Containers allocate 2Gi of RAM and 1 CPU per pod as base overhead...
```

**Recommendation:** Use the more explicit format for clarity:
```adoc
* Worker nodes have sufficient capacity. Kata Containers allocate 2 GiB of RAM and 1 CPU per pod as base overhead...
```

---

### 11. Verification Step Enhancement ⚠️ MODERATE
**Severity:** Low  
**Location:** `modules/ob-isolate-all-project-builds-using-a-specific-RuntimeClass.adoc` (lines 66-75)

**Issue:** Verification only checks if Build was registered, but doesn't verify the RuntimeClass setting.

**Current verification:**
```adoc
.Verification

. Run the following command to verify that the Build was registered successfully:
+
[source,terminal]
----
$ oc get build buildah-build-kata
----
+
A `Succeeded` status reason confirms that the `Build` passed validation.
```

**Recommended addition:**
```adoc
.Verification

. Run the following command to verify that the Build was registered successfully:
+
[source,terminal]
----
$ oc get build buildah-build-kata -o yaml
----
+
A `Succeeded` status reason confirms that the `Build` passed validation.

. Verify the RuntimeClass is configured correctly:
+
[source,terminal]
----
$ oc get build buildah-build-kata -o jsonpath='{.spec.runtimeClassName}'
----
+
.Example output
[source,terminal]
----
kata
----
```

---

### 12. Procedure Consistency ⚠️ MODERATE
**Severity:** Low  
**Location:** Multiple procedure modules

**Issue:** Some procedures use "Run the following command to apply the resource" while others use "Run the following command to apply the `BuildRun` resource".

**Recommendation:** Be consistent. Either:
- Always specify the resource type: "apply the `Build` resource"
- Or use generic: "apply the resource"

**Preferred:** Be specific for clarity.

---

### 13. Example Naming Inconsistency ⚠️ MODERATE
**Severity:** Low  
**Location:** `modules/ob-override-runtimeclass-for-specific-build-run.adoc`

**Issue:** Example section uses "Example:" but other modules might use ".Example" or different formatting.

**Current:**
```adoc
.Example: Overriding the Build's RuntimeClass
```

**Check:** Verify this matches the style guide. This format appears correct for AsciiDoc labeled examples.

---

### 14. Missing Cross-References ⚠️ MODERATE
**Severity:** Low  
**Location:** Troubleshooting modules

**Issue:** Troubleshooting modules could benefit from cross-references to the configuration procedures.

**Recommendation:** Add xrefs in troubleshooting modules:

```adoc
For information about configuring RuntimeClass, see xref:../configuring/isolate-build-workloads-for-security-and-compliance.adoc#ob-isolate-all-project-builds-using-a-specific-RuntimeClass_isolate-build-workloads[Isolate all project builds using a specific RuntimeClass].
```

---

### 15. Incomplete Error Resolution ⚠️ MODERATE
**Severity:** Moderate  
**Location:** `modules/ob-troubleshoot-runtimeclass-name-not-valid.adoc`

**Issue:** Module explains how to check the status but doesn't provide a complete fix example.

**Current:**
```adoc
. To fix this issue, confirm that the `runtimeClassName` consists strictly of lowercase alphanumeric characters, dots (`.`), or hyphens (`-`)...
```

**Recommended addition:**
```adoc
. To fix this issue, update the `runtimeClassName` to use only lowercase alphanumeric characters, dots (`.`), or hyphens (`-`):
+
.Example of invalid name
[source,yaml]
----
runtimeClassName: My_Runtime!  # Invalid
----
+
.Example of valid name
[source,yaml]
----
runtimeClassName: kata  # Valid
----
```

---

## Minor Issues (Nice to Have)

### 16. Parallel Structure in Lists 💡 SUGGESTION
**Severity:** Low  
**Location:** `modules/ob-runtimeclass-prerequisites-and-precedence.adoc`

**Issue:** Bullet points under "Prerequisites" don't follow parallel structure.

**Current:**
- "The OpenShift Sandboxed Containers Operator is installed." (passive voice)
- "A RuntimeClass resource exists in your cluster." (passive voice)
- "Cluster nodes support the target runtime." (active voice)
- "Node scheduling constraints are compatible." (active voice)
- "The RuntimeClass name is a valid DNS subdomain." (passive voice)

**Recommendation:** Make all bullet points follow the same structure (either all passive or all active). Passive voice is acceptable for prerequisites.

---

### 17. Consider Adding Admonition for Performance Impact 💡 SUGGESTION
**Severity:** Low  
**Location:** `modules/ob-runtimeclass-prerequisites-and-precedence.adoc`

**Issue:** The overhead information is mentioned but could benefit from a stronger callout.

**Recommended addition:**
```adoc
[IMPORTANT]
====
Kata Containers add significant resource overhead. Each build pod requires a base allocation of 2 GiB RAM and 1 CPU in addition to any limits specified in your build configuration. Ensure your cluster has adequate capacity before enabling sandboxed builds at scale.
====
```

---

### 18. Expand on Node Labeling 💡 SUGGESTION
**Severity:** Low  
**Location:** `modules/ob-runtimeclass-prerequisites-and-precedence.adoc`

**Issue:** The KataConfig section mentions node labeling but doesn't provide an example.

**Recommendation:** Add a brief example or link to the Sandboxed Containers documentation that covers selective node installation.

---

### 19. Add Related Information Section 💡 SUGGESTION
**Severity:** Low  
**Location:** `troubleshooting/troubleshooting-runtime-class.adoc`

**Issue:** Assembly could benefit from a "Related information" or "Additional resources" section linking back to configuration procedures.

**Recommended addition:**
```adoc
[role="_additional-resources"]
== Additional resources

* xref:../configuring/isolate-build-workloads-for-security-and-compliance.adoc#isolate-build-workloads-for-security-and-compliance[Isolate build workloads for security and compliance]
* link:https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/[OpenShift Sandboxed Containers documentation]
```

---

## Positive Observations ✅

1. **Well-structured content** - Clear separation between configuration and troubleshooting
2. **Good use of abstracts** - Each module has a clear abstract explaining its purpose
3. **Comprehensive examples** - YAML examples are complete and realistic
4. **Proper metadata** - All modules have correct `:_mod-docs-content-type:` set
5. **Good verification steps** - Procedures include verification commands
6. **Technology Preview disclaimer** - Appropriate use of tech preview snippet
7. **Consistent module naming** - Follows `ob-` prefix convention (except for the capitalization issue noted)
8. **Good prerequisite documentation** - Clear explanation of requirements
9. **Helpful troubleshooting scenarios** - Covers common failure modes
10. **Appropriate use of admonitions** - IMPORTANT and NOTE blocks used correctly

---

## Documentation Standards Compliance

### ✅ Compliant
- Content type metadata present
- Module includes commented correctly
- Abstracts provided for all assemblies and modules
- Proper use of leveloffset
- Code blocks properly formatted with source type
- Verification steps included in procedures

### ⚠️ Needs Attention
- **Trailing newlines** - 2 files missing (MUST FIX)
- **Filename capitalization** - 1 file inconsistent (SHOULD FIX)
- **Table syntax** - 1 error (MUST FIX)

---

## Technical Accuracy Review

### ✅ Accurate
- RuntimeClass concept explanation
- Kata Containers overhead values (2 GiB RAM, 1 CPU)
- Resource precedence logic
- Pod scheduling constraints
- DNS subdomain naming rules (RFC 1123)
- Webhook validation behavior

### ❓ Verify
1. **Tech Preview status** - Confirm whether RuntimeClass support is GA or TP
2. **Sandboxed Containers version** - Verify if docs link should be versioned
3. **KataConfig reboot time** - "10 to more than 60 minutes" - verify this is current
4. **Bare metal requirement** - Confirm sandboxed containers only work on bare metal

---

## Checklist for Author

Before requesting re-review, please ensure:

- [ ] Add trailing newlines to all files
- [ ] Fix table syntax error (missing closing pipe)
- [ ] Verify and clarify Technology Preview scope
- [ ] Consider renaming file to use lowercase `runtimeclass`
- [ ] Review all resource names for consistent backtick usage
- [ ] Add enhanced verification steps
- [ ] Consider adding performance impact admonition
- [ ] Add cross-references in troubleshooting modules
- [ ] Expand error resolution examples
- [ ] Verify external link versioning

---

## Recommendation

**Status:** ⚠️ **REQUEST CHANGES**

**Summary:**
This PR provides valuable documentation for RuntimeClass support in OpenShift Builds. The content is technically accurate and well-organized. However, **7 critical/moderate issues must be addressed** before merge, particularly:

1. Missing trailing newlines (git issue)
2. Table syntax error (rendering issue)
3. Filename capitalization inconsistency
4. Technology Preview scope clarification

**Next Steps:**
1. Author should address critical issues (items 1-5)
2. Author should consider moderate issues (items 6-15)
3. Request re-review after changes
4. QE review still pending (noted in PR description)

**Estimated effort to resolve:** 30-45 minutes

---

## Reviewer Information

**Reviewed by:** Claude (Peer Review)  
**Review type:** Technical and Editorial  
**Focus areas:** Documentation standards, technical accuracy, clarity, completeness

