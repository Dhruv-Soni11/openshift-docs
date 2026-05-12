# Peer and CQA Review Report
## PR #111485: Add documentation for optimizing build performance

**Reviewer:** Dhruv Soni  
**Date:** 2026-05-11  
**PR Link:** https://github.com/openshift/openshift-docs/pull/111485  
**Author:** Shivani Sathe (@shivanisathe25)  
**Jira:** RHDEVDOCS-7532  
**Target Version:** build-docs-1.8  

---

## Executive Summary

**Status:** ❌ **NEEDS REVISION**

This PR adds new documentation for optimizing build performance in OpenShift Builds, covering resource limit configuration at both Build and BuildRun levels. The content is technically sound and well-structured, but requires corrections to **critical issues** before approval.

**Files Changed:**
- `_topic_maps/_topic_map.yml` (2 additions)
- `work_with_builds/optimize-build-performance.adoc` (new assembly, 28 lines)
- `modules/adjust-resource-limits-for-a-build-configuration.adoc` (new module, 99 lines)
- `modules/override-resources-for-a-specific-build-run.adoc` (new module, 54 lines)
- `modules/verify-build-resource-limits.adoc` (new module, 62 lines)

**Total Changes:** +245 lines

---

## Critical Issues (Must Fix)

### Issue #1: Incorrect Module Header Reference
**File:** `modules/override-resources-for-a-specific-build-run.adoc`  
**Line:** 3  
**Severity:** 🔴 CRITICAL

**Current:**
```adoc
// Module included in the following assembly:
//
// * work_with_shared_resources/using-shared-resource-csi-driver.adoc
```

**Fix:**
```adoc
// Module included in the following assembly:
//
// * work_with_builds/optimize-build-performance.adoc
```

**Reason:** Copy-paste error from another module. Incorrect reference will confuse maintainers.

---

### Issue #2: Missing Trailing Newlines
**Files:** All new files  
**Severity:** 🔴 CRITICAL

**Affected Files:**
- `modules/adjust-resource-limits-for-a-build-configuration.adoc` (line 99)
- `modules/verify-build-resource-limits.adoc` (line 62)
- `work_with_builds/optimize-build-performance.adoc` (line 28)

**Fix:** Add a newline character at the end of each file.

**Reason:** Standard POSIX convention; may cause issues with git diff and some build tools.

---

### Issue #3: Incorrect Source Block Types
**Files:** All three module files  
**Severity:** 🔴 CRITICAL

**Problem:** Using `[source,yaml]` for shell commands instead of `[source,terminal]`.

**Occurrences:**

**File:** `adjust-resource-limits-for-a-build-configuration.adoc`

**Lines 51-53:**
```adoc
[source,yaml]
----
$ oc apply -f build.yaml
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc apply -f build.yaml
----
```

**Lines 59-61:**
```adoc
[source,yaml]
----
$ oc get buildrun <buildrun_name>
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc get buildrun <buildrun_name>
----
```

**Lines 71-73:**
```adoc
[source,yaml]
----
$ oc get buildrun buildah-buildrun-with-resources
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc get buildrun buildah-buildrun-with-resources
----
```

**Lines 88-90:**
```adoc
[source,yaml]
----
$ oc describe build <buildrun_name>
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc describe build <buildrun_name>
----
```

**File:** `override-resources-for-a-specific-build-run.adoc`

**Lines 50-52:**
```adoc
[source,yaml]
----
$ oc apply -f buildrun.yaml
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc apply -f buildrun.yaml
----
```

**File:** `verify-build-resource-limits.adoc`

**Lines 23-25:**
```adoc
[source,yaml]
----
$ oc get buildrun <buildrun_name>
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc get buildrun <buildrun_name>
----
```

**Lines 37-39:**
```adoc
[source,yaml]
----
$ oc get buildrun buildah-buildrun-with-resources
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc get buildrun buildah-buildrun-with-resources
----
```

**Lines 52-54:**
```adoc
[source,yaml]
----
$ oc describe build <buildrun_name>
----
```
**Fix:**
```adoc
[source,terminal]
----
$ oc describe build <buildrun_name>
----
```

**Reason:** YAML syntax highlighting is inappropriate for shell commands. Terminal is the correct source type for CLI commands.

---

### Issue #4: Incorrect Command in Error Checking
**Files:** `adjust-resource-limits-for-a-build-configuration.adoc` and `verify-build-resource-limits.adoc`  
**Lines:** ~88-90 and ~52-54  
**Severity:** 🔴 CRITICAL

**Current:**
```adoc
. If the SUCCEEDED column shows an error, run the following command to check `UndefinedStepResource` reason:
+
[source,yaml]
----
$ oc describe build <buildrun_name>
----
+
where:

<buildrun_name>:: Specifies the name of the `buildrun` resource.
```

**Fix Option 1 (Check BuildRun):**
```adoc
. If the SUCCEEDED column shows an error, run the following command to check `UndefinedStepResource` reason:
+
[source,terminal]
----
$ oc describe buildrun <buildrun_name>
----
+
where:

<buildrun_name>:: Specifies the name of the BuildRun resource.
```

**Fix Option 2 (Check Build):**
```adoc
. If the SUCCEEDED column shows an error, run the following command to check `UndefinedStepResource` reason:
+
[source,terminal]
----
$ oc describe build <build_name>
----
+
where:

<build_name>:: Specifies the name of the Build resource.
```

**Reason:** The command refers to `<buildrun_name>` but uses `oc describe build`. This is inconsistent. Either describe the BuildRun or describe the Build (and update the placeholder accordingly).

---

## Major Issues (Should Fix)

### Issue #5: Terminology Inconsistency
**File:** `work_with_builds/optimize-build-performance.adoc`  
**Line:** 15  
**Severity:** 🟡 MAJOR

**Current:**
```adoc
* Build runlevel: For one-time large builds (e.g., a major release).
```

**Fix:**
```adoc
* BuildRun level: For one-time large builds (e.g., a major release).
```

**Reason:** "BuildRun" is the proper Kubernetes custom resource name (capital B, capital R, one word). "runlevel" has different meaning in computing contexts.

---

### Issue #6: Placeholder Formatting Inconsistency
**Files:** Multiple  
**Severity:** 🟡 MAJOR

**Problem:** Inconsistent use of angle brackets in placeholders.

**Examples:**

In text (line 61):
```adoc
$ oc get buildrun <buildrun_name>
```

In where clause (line 67):
```adoc
<buildrun_name>:: Specifies the name of the `buildrun` resource.
```

**Recommendation:** 
1. Use angle brackets consistently: `<buildrun_name>` everywhere
2. OR use italics for better readability: `_buildrun_name_`

**Industry Standard:** Most OpenShift docs use angle brackets for placeholders.

---

### Issue #7: Verification Logic Improvement Needed
**File:** `adjust-resource-limits-for-a-build-configuration.adoc`  
**Lines:** 56-98  
**Severity:** 🟡 MAJOR

**Problem:** The verification section immediately checks BuildRun status, but the procedure configures a Build resource. Users need to create a BuildRun first.

**Current Flow:**
1. Edit Build YAML
2. Apply Build configuration
3. Check BuildRun status (but no BuildRun was created!)

**Suggested Improvement:**

Add step between current steps 3 and verification:

```adoc
. Apply the configuration to your cluster:
+
[source,terminal]
----
$ oc apply -f build.yaml
----

. Create a BuildRun to test the configuration:
+
[source,terminal]
----
$ oc create -f buildrun.yaml
----
+
Or trigger a build:
+
[source,terminal]
----
$ oc start-build my-app-build
----

.Verification

. Run the following command to check the status of the BuildRun:
+
[source,terminal]
----
$ oc get buildrun <buildrun_name>
----
```

**Reason:** Clearer workflow for users. Current version assumes a BuildRun exists.

---

### Issue #8: Duplicate Verification Content
**Files:** `adjust-resource-limits-for-a-build-configuration.adoc` and `verify-build-resource-limits.adoc`  
**Severity:** 🟡 MAJOR

**Problem:** Lines 56-98 in `adjust-resource-limits-for-a-build-configuration.adoc` contain nearly identical content to the entire `verify-build-resource-limits.adoc` module.

**Current Situation:**
- Verification section in adjustment procedure: ~43 lines
- Dedicated verification module: ~62 lines
- Significant overlap in content

**Suggested Approach:**

**Option A (Recommended):** Reference the verification module
```adoc
.Verification

See xref:../work_with_builds/optimize-build-performance.adoc#verify-build-resource-limits_optimize-build-performance[Verify build resource limits].
```

**Option B:** Make verification sections distinct
- In adjust procedure: Quick verification (check Build config applied)
- In verify module: Comprehensive verification (check BuildRun execution)

**Reason:** DRY principle. Reduces maintenance burden and prevents content drift.

---

## Minor Issues (Nice to Fix)

### Issue #9: Extra Whitespace
**Files:** `adjust-resource-limits-for-a-build-configuration.adoc` (line 85) and `verify-build-resource-limits.adoc` (line 48)  
**Severity:** 🟢 MINOR

**Current:**
```adoc
Verify that the SUCCEEDED column displays status as True. 
```
(Note the extra space before the period)

**Fix:**
```adoc
Verify that the SUCCEEDED column displays status as True.
```

---

### Issue #10: Attribute Usage Verification Needed
**File:** `verify-build-resource-limits.adoc`  
**Line:** 17  
**Severity:** 🟢 MINOR

**Current:**
```adoc
* You have installed the {builds-operator} and the `oc` CLI.
```

**Action Required:** Verify that the `{builds-operator}` attribute is defined in the build-docs-1.8 version.

**Fallback if not defined:**
```adoc
* You have installed the Builds for Red Hat OpenShift Operator and the `oc` CLI.
```

---

### Issue #11: Capitalization Consistency
**Files:** Multiple  
**Severity:** 🟢 MINOR

**Observations:**
- Sometimes: "BuildRun" (correct Kubernetes resource name)
- Sometimes: "buildrun" (lowercase in commands and descriptions)
- Sometimes: "build run" (two words)

**Recommendation:**
- Use "BuildRun" when referring to the resource type/kind
- Use "buildrun" in CLI commands (lowercase)
- Avoid "build run" (two words)

**Examples:**

✅ Good:
```adoc
Create a BuildRun resource YAML file...
$ oc get buildrun buildah-buildrun-with-resources
<buildrun_name>:: Specifies the name of the BuildRun resource.
```

❌ Avoid:
```adoc
Create a build run resource...
Specifies the name of the `buildrun` resource.
```

---

## Content Enhancement Suggestions

### Suggestion #1: Add Troubleshooting Section

Consider adding a troubleshooting section to the assembly or the verify module:

```adoc
== Troubleshooting

=== Build fails with "UndefinedStepResource"

*Symptom:* BuildRun fails with reason `UndefinedStepResource`.

*Cause:* The step name in `stepResources` doesn't match the actual step name in the BuildStrategy.

*Solution:*
. Check the strategy definition:
+
[source,terminal]
----
$ oc get clusterbuildstrategy buildah -o yaml
----

. Find the exact step names in the `spec.steps` section
. Update your Build or BuildRun YAML with the correct step names (case-sensitive)

=== Resource limits not applied

*Symptom:* Pod shows default resource limits instead of custom ones.

*Cause:* BuildRun overrides may be taking precedence over Build configuration.

*Solution:* Check the precedence order: BuildRun > Build > Strategy defaults.
```

---

### Suggestion #2: Add Example Use Cases

In the assembly introduction, add context for when to use each approach:

```adoc
.When to use Build-level configuration:
* Your application consistently needs more resources
* All builds of this application have similar requirements
* You want persistent configuration in version control

.When to use BuildRun-level overrides:
* One-time resource boost for a large release build
* Testing different resource allocations
* Temporary override without modifying Build configuration
* Emergency builds that need extra resources
```

---

### Suggestion #3: Add Resource Planning Guidance

```adoc
.Determining appropriate resource values:

* *CPU*: Start with `500m` (0.5 cores) for small builds, `1-2` cores for medium builds
* *Memory*: Start with `512Mi` for simple builds, `1-2Gi` for complex builds with large dependencies
* *Monitor*: Check actual resource usage with `oc adm top pods` during builds
* *Adjust*: Increase limits if builds are killed (OOMKilled) or throttled
```

---

## Documentation Standards Compliance

### ✅ Compliant Areas

- ✅ Proper module type declarations (`:_mod-docs-content-type: PROCEDURE`)
- ✅ Clear abstracts with `[role="_abstract"]`
- ✅ Proper assembly/module structure
- ✅ Prerequisites sections included
- ✅ Examples provided with context
- ✅ Proper use of context attribute
- ✅ Verification steps included
- ✅ AsciiDoc formatting generally correct

### ⚠️ Areas Needing Attention

- ❌ Module header references (1 incorrect)
- ❌ Source block types (8 instances)
- ❌ Trailing newlines (3 files)
- ❌ Command accuracy (2 instances)
- ⚠️ Terminology consistency
- ⚠️ Placeholder formatting
- ⚠️ Content duplication

---

## Detailed Fix Checklist for Author

### Priority 1: Must Fix Before Approval

- [ ] **Fix module header** in `override-resources-for-a-specific-build-run.adoc` line 3
- [ ] **Add trailing newlines** to all 3 new files
- [ ] **Change source blocks** from `[source,yaml]` to `[source,terminal]` for all 8 CLI command blocks
- [ ] **Fix commands** in error-checking steps: `oc describe build` → `oc describe buildrun` or update placeholder
- [ ] **Fix terminology**: "Build runlevel" → "BuildRun level"

### Priority 2: Should Fix

- [ ] **Make placeholder formatting consistent** throughout all files
- [ ] **Improve verification logic** in adjust-resource-limits module (add BuildRun creation step)
- [ ] **Address duplicate content** between modules (deduplicate or reference)
- [ ] **Remove extra spaces** before periods (2 instances)

### Priority 3: Nice to Have

- [ ] **Verify attribute** `{builds-operator}` is defined in build-docs-1.8
- [ ] **Standardize capitalization** of BuildRun/buildrun throughout
- [ ] **Consider adding** troubleshooting section
- [ ] **Consider adding** use case guidance
- [ ] **Consider adding** resource planning guidance

---

## Files Requiring Changes

### `modules/override-resources-for-a-specific-build-run.adoc`
- Line 3: Fix module header reference
- Line 50-52: Change source type to terminal
- Line 54: Add trailing newline

### `modules/adjust-resource-limits-for-a-build-configuration.adoc`
- Line 51-53: Change source type to terminal
- Line 59-61: Change source type to terminal
- Line 71-73: Change source type to terminal
- Line 85: Remove extra space
- Line 88-90: Change source type to terminal AND fix command/placeholder
- Line 99: Add trailing newline
- Lines 56-98: Consider refactoring verification section

### `modules/verify-build-resource-limits.adoc`
- Line 23-25: Change source type to terminal
- Line 37-39: Change source type to terminal
- Line 48: Remove extra space
- Line 52-54: Change source type to terminal AND fix command/placeholder
- Line 62: Add trailing newline

### `work_with_builds/optimize-build-performance.adoc`
- Line 15: Fix "Build runlevel" → "BuildRun level"
- Line 28: Add trailing newline

---

## Test Plan for Fixes

After making corrections, verify:

1. **Build the docs** and check for AsciiDoc errors
2. **Preview the rendered HTML** at the provided Netlify link
3. **Check syntax highlighting** appears correctly for all code blocks
4. **Verify all commands** are accurate and tested
5. **Check all xrefs and links** resolve correctly
6. **Verify placeholders** are consistent and clear
7. **Run through procedures** manually to ensure logical flow

---

## Approval Criteria

This PR can be approved when:

- ✅ All **Critical Issues** (#1-#4) are resolved
- ✅ All **Major Issues** (#5-#8) are addressed or acknowledged with plan
- ✅ Documentation builds without errors
- ✅ QE review is completed and approved
- ✅ Content is technically accurate per SME review

---

## Additional Notes

### Positive Aspects
- Well-structured content with clear hierarchy
- Good use of YAML examples showing realistic configurations
- Comprehensive coverage of both Build and BuildRun resource configuration
- Clear explanation of precedence order
- Good prerequisites sections

### Areas for Future Enhancement
- Could benefit from performance tuning guidance
- Could include more troubleshooting scenarios
- Could add links to related topics (quotas, limits, strategy documentation)
- Could include metrics/monitoring integration examples

---

## Reviewer Recommendation

**NEEDS REVISION** - The content is valuable and well-structured, but requires corrections to critical issues before approval. Once the Priority 1 items are addressed, this will be ready for QE review and final approval.

**Estimated effort to fix:** 30-45 minutes

**Follow-up needed:** Request re-review after author completes Priority 1 fixes.

---

## Contact

For questions about this review, contact:
- **Reviewer:** Dhruv Soni
- **Date:** 2026-05-11

---

**End of Review Report**
