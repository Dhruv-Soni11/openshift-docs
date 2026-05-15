# Peer and CQA Review: PR #111506
**Title:** Release notes 1.8  
**Author:** shivanisathe25  
**Issue:** RHDEVDOCS-7522  
**Version:** build-docs-1.8  
**Status:** OPEN (1 review requesting changes from @avinal, 1 comment from @psrvere)  
**Review Date:** May 14, 2026

---

## Executive Summary

This PR adds release notes for OpenShift Builds 1.8, updates the compatibility matrix to show versions 1.7 and 1.8, and removes includes for older release notes (1.7 and 1.7.1). The content is well-written and covers key features and fixes. However, there are **3 critical issues** that must be fixed before merge.

**Overall Assessment:** ⚠️ **REQUIRES CHANGES** (3 critical issues, 5 moderate issues, 3 minor suggestions)

---

## Critical Issues (Must Fix)

### 1. Missing Trailing Newline ⚠️ CRITICAL
**Severity:** High  
**Location:** `modules/ob-release-notes-1-8.adoc` (line 31)

**Issue:** The file does not end with a trailing newline character, which can cause git merge issues.

**Current:** File ends with period (`.`) at line 31
```
...which improves resource mounting for users.
```

**Fix:** Add a newline character at the end of the file.

```bash
# Verify with:
tail -c 1 modules/ob-release-notes-1-8.adoc | od -An -tx1
# Should show '0a' (newline), currently shows '2e' (period)
```

---

### 2. Missing Trailing Newline ⚠️ CRITICAL
**Severity:** High  
**Location:** `release_notes/ob-openshift-builds-release-notes.adoc` (line 39)

**Issue:** The assembly file does not end with a trailing newline character.

**Current:** File ends with `]` at line 39

**Fix:** Add a newline character at the end of the file.

```bash
# Verify with:
tail -c 1 release_notes/ob-openshift-builds-release-notes.adoc | od -An -tx1
# Should show '0a' (newline), currently shows '5d' (closing bracket)
```

---

### 3. Version Placeholder Not Replaced ⚠️ CRITICAL
**Severity:** High  
**Location:** `modules/ob-release-notes-1-8.adoc` (line 8)

**Issue:** The OpenShift version uses placeholder "4.xx" which must be replaced with the actual version.

**Current:**
```adoc
{builds-shortname} 1.8 is now available on {ocp-product-title} 4.xx.
```

**Should be:**
```adoc
{builds-shortname} 1.8 is now available on {ocp-product-title} 4.17.
```

**Rationale:** Based on the compatibility matrix, version 1.8 supports OpenShift 4.17-4.21, so the initial release would be 4.17.

---

## Moderate Issues (Should Fix)

### 4. Technology Preview Snippet Placement ⚠️ MODERATE
**Severity:** Moderate  
**Location:** `modules/ob-release-notes-1-8.adoc` (lines 20-22)

**Issue:** The Technology Preview snippet is included as a list continuation within a definition list item. This placement may not render correctly or may be inconsistent with documentation standards.

**Current:**
```adoc
Support for custom runtime classes in builds::
With this update, you can define a `runtimeClassName` field...
+
:FeatureName: Builds in sandbox containers
include::snippets/technology-preview.adoc[]
```

**Recommendation:** Consider one of these alternatives:

**Option 1:** Move the tech preview notice outside the definition list
```adoc
Support for custom runtime classes in builds::
With this update, you can define a `runtimeClassName` field in the `Build` and `BuildRun` APIs to select specific container runtimes for the build pod. You can run builds in sandboxed environments, such as Kata Containers, for hypervisor-level isolation. This is useful when building from untrusted sources or when compliance policies require stronger workload isolation than the default container runtime provides.

:FeatureName: Builds in sandbox containers
include::snippets/technology-preview.adoc[]
```

**Option 2:** Use an inline NOTE within the description
```adoc
Support for custom runtime classes in builds::
With this update, you can define a `runtimeClassName` field in the `Build` and `BuildRun` APIs to select specific container runtimes for the build pod. You can run builds in sandboxed environments, such as Kata Containers, for hypervisor-level isolation. This is useful when building from untrusted sources or when compliance policies require stronger workload isolation than the default container runtime provides.
+
[NOTE]
====
:FeatureName: Builds in sandbox containers
include::snippets/technology-preview.adoc[]
====
```

**Action Required:** Verify with the documentation standards which placement is correct for tech preview features within release notes.

---

### 5. Inconsistent Version Ranges in Compatibility Matrix ⚠️ MODERATE
**Severity:** Low  
**Location:** `modules/ob-compatibility-support-matrix.adoc` (lines 27-28)

**Issue:** The Pipelines compatibility version ranges are formatted inconsistently.

**Current:**
```adoc
|1.8 | 0.19.0 (GA) | 0.19.0 (GA) | 1.20-1.22      | 4.17-4.21         | GA
|1.7 | 0.18.0 (GA) | 0.18.0 (GA) | 1.18-1.21 | 4.16-4.21         | GA
```

**Issue:** Row for 1.8 has extra spaces before the version range, while 1.7 doesn't.

**Recommended:**
```adoc
|1.8 | 0.19.0 (GA) | 0.19.0 (GA) | 1.20-1.22 | 4.17-4.21 | GA
|1.7 | 0.18.0 (GA) | 0.18.0 (GA) | 1.18-1.21 | 4.16-4.21 | GA
```

---

### 6. Large Version Jump in Compatibility Matrix ⚠️ MODERATE
**Severity:** Moderate (Requires Clarification)  
**Location:** `modules/ob-compatibility-support-matrix.adoc`

**Issue:** The PR removes versions 1.0, 1.1, and 1.2 and adds only 1.7 and 1.8. What about versions 1.3-1.6?

**Current state:**
- **Before:** Showed versions 1.0, 1.1, 1.2 (incomplete)
- **After:** Shows versions 1.7, 1.8 (missing 1.3-1.6)

**Questions:**
1. Are versions 1.3-1.6 EOL (End of Life)?
2. Should the matrix show all supported versions or only the most recent?
3. Is there a policy on how many versions to display in release notes?

**Recommendation:** If this is intentional (showing only currently supported versions), consider adding a note explaining this:

```adoc
[NOTE]
====
This table shows only the currently supported versions of {builds-shortname}. For information about older versions, see the archived release notes.
====
```

---

### 7. Removal of Previous Release Notes ⚠️ MODERATE
**Severity:** Moderate (Requires Clarification)  
**Location:** `release_notes/ob-openshift-builds-release-notes.adoc` (lines 31-33)

**Issue:** The PR removes includes for 1.7 and 1.7.1 release notes but doesn't specify where users can find this information.

**Current:**
```adoc
// Removed:
// include::modules/ob-release-notes-1-7-1.adoc[leveloffset=+1]
// include::modules/ob-release-notes-1-7.adoc[leveloffset=+1]

// Added:
include::modules/ob-release-notes-1-8.adoc[leveloffset=+1]
```

**Questions:**
1. Are the 1.7 and 1.7.1 release note files being archived/moved?
2. Should there be a link to archived release notes?
3. Is this consistent with the release notes policy for OpenShift Builds?

**Recommendation:** If older notes are archived, add a pointer in the abstract:

```adoc
[role="_abstract"]
Release notes contain information about new and deprecated features, breaking changes, and known issues. The following release notes apply for the most recent {builds-shortname} release on {ocp-product-title}.

For release notes of previous versions, see link:https://access.redhat.com/[archived {builds-shortname} documentation].
```

---

### 8. Verify Pipelines Compatibility Versions ⚠️ MODERATE
**Severity:** Moderate (Verification Required)  
**Location:** `modules/ob-compatibility-support-matrix.adoc` (line 27)

**Issue:** Please verify that the Pipelines compatibility versions are correct.

**Question:** Is OpenShift Builds 1.8 truly compatible with Pipelines 1.20-1.22?

**Action Required:** Confirm with the engineering or product team that these version ranges are accurate.

---

## Minor Issues (Nice to Have)

### 9. Consider Adding "Known Issues" Section 💡 SUGGESTION
**Severity:** Low  
**Location:** `modules/ob-release-notes-1-8.adoc`

**Issue:** The release notes only have "New features" and "Fixed issues" sections. Many release notes also include a "Known issues" section.

**Current sections:**
- New features
- Fixed issues

**Recommended addition:**
```adoc
[id="known-issues-1-8_{context}"]
== Known issues

// Add any known issues, or:

There are no known issues in this release.
```

**Rationale:** Even if there are no known issues, having the section provides consistency and sets expectations.

---

### 10. Add Bug Tracker References 💡 SUGGESTION
**Severity:** Low  
**Location:** `modules/ob-release-notes-1-8.adoc` (lines 27-31)

**Issue:** The fixed issues don't reference Jira tickets or bugzilla IDs.

**Current:**
```adoc
OpenShift Builds CLI version aligned with {builds-title-uppercase}::
Before this update, the shp CLI available for download...
```

**Recommended:**
```adoc
OpenShift Builds CLI version aligned with {builds-title-uppercase} (link:https://issues.redhat.com/browse/BUILD-xxx[BUILD-xxx])::
Before this update, the shp CLI available for download...
```

**Rationale:** Bug tracker references help users:
- Track the issue history
- Understand the context
- Verify the fix in their environment
- Reference in support cases

---

### 11. Enhance Fixed Issues Descriptions 💡 SUGGESTION
**Severity:** Low  
**Location:** `modules/ob-release-notes-1-8.adoc` (lines 27-31)

**Issue:** The fixed issues could be more concise and follow a tighter "Before/After/Consequence" structure.

**Current:**
```adoc
Memory leak fix for shared resource CSI Driver::
Before this update, unregistered callbacks for config maps and secrets in the shared resource CSI Driver caused high memory usage. As a consequence, shared resource mount failures occurred. With this update, the shared resource CSI Driver unregisters callbacks correctly. This fix reduces memory usage and prevents the `OOMKill` of shared resource CSI Driver pods, which improves resource mounting for users.
```

**Recommended (more concise):**
```adoc
Memory leak fix for shared resource CSI Driver::
Before this update, the shared resource CSI Driver did not unregister callbacks for ConfigMaps and Secrets, causing memory leaks that resulted in pod `OOMKill` events and mount failures. With this update, callbacks are properly unregistered, preventing memory leaks and improving resource mounting reliability. (link:https://issues.redhat.com/browse/BUILD-xxx[BUILD-xxx])
```

**Changes:**
- Removed redundant phrases
- Combined consequences
- More direct language
- Added hypothetical bug reference

---

## Positive Observations ✅

1. **Well-structured content** - Clear separation of new features and fixed issues
2. **Good abstracts** - Clear and concise module introduction
3. **Proper metadata** - Correct `:_mod-docs-content-type:` set to REFERENCE
4. **Good use of definition lists** - Features and fixes are well-organized
5. **Clear before/after explanations** - Fixed issues explain the problem, consequence, and solution
6. **Appropriate detail level** - Good balance between technical detail and readability
7. **Proper use of inline code** - API fields and resources properly formatted with backticks
8. **Technology Preview disclosure** - Appropriate use of tech preview snippet for sandbox containers
9. **Contextual anchors** - All sections have proper IDs with context variables
10. **Compatibility matrix updated** - Keeps documentation current with supported versions

---

## Documentation Standards Compliance

### ✅ Compliant
- Content type metadata present (REFERENCE)
- Module includes commented correctly
- Abstract provided
- Proper use of definition lists
- Code elements properly formatted with backticks
- Proper use of attributes ({builds-shortname}, {ocp-product-title})
- Section IDs follow naming convention with context

### ⚠️ Needs Attention
- **Trailing newlines** - 2 files missing (MUST FIX)
- **Version placeholder** - "4.xx" not replaced (MUST FIX)
- **Tech preview placement** - May need adjustment (VERIFY)

---

## Technical Accuracy Review

### ✅ Appears Accurate
- Resource overrides feature description
- RuntimeClass support description
- Kata Containers as example of sandboxed runtime
- Shared resource CSI Driver memory leak fix
- CLI version alignment issue

### ❓ Verify
1. **OpenShift version:** Confirm 1.8 releases on 4.17 (used to replace "4.xx")
2. **Pipelines compatibility:** Verify 1.8 works with Pipelines 1.20-1.22
3. **Tech preview status:** Confirm sandbox containers are tech preview in 1.8
4. **Version support policy:** Confirm only showing 1.7 and 1.8 is correct

---

## Content Quality Assessment

### Strengths
- **Clarity:** Technical features explained clearly for the target audience
- **Completeness:** Covers new features and bug fixes comprehensively
- **User focus:** Explains benefits and use cases ("useful when building from untrusted sources")
- **Consistency:** Follows established patterns from previous release notes

### Areas for Improvement
- **Conciseness:** Some fixed issue descriptions could be tighter
- **References:** Missing bug tracker links
- **Completeness:** No known issues section (even if empty)

---

## Checklist for Author

Before requesting re-review, please ensure:

### Must Fix (Critical)
- [ ] Add trailing newline to `modules/ob-release-notes-1-8.adoc`
- [ ] Add trailing newline to `release_notes/ob-openshift-builds-release-notes.adoc`
- [ ] Replace "4.xx" with the actual OpenShift version (likely 4.17)

### Should Fix (Moderate)
- [ ] Verify and clarify Technology Preview snippet placement
- [ ] Fix spacing inconsistency in compatibility matrix table
- [ ] Verify Pipelines compatibility versions (1.20-1.22) are correct
- [ ] Clarify policy on showing only recent versions in compatibility matrix
- [ ] Consider adding note about archived release notes for older versions

### Nice to Have (Minor)
- [ ] Consider adding "Known issues" section
- [ ] Consider adding bug tracker references to fixed issues
- [ ] Review and tighten fixed issue descriptions

---

## Recommendation

**Status:** ⚠️ **REQUEST CHANGES**

**Summary:**
This PR provides well-written release notes for OpenShift Builds 1.8 with clear feature descriptions and bug fix explanations. However, **3 critical issues must be addressed** before merge:

1. **Missing trailing newlines** (2 files) - Git issue
2. **Version placeholder** not replaced - Content incomplete
3. **Tech preview placement** - May need adjustment (requires verification)

**Next Steps:**
1. Author should address all critical issues (items 1-3)
2. Author should verify tech preview snippet placement with docs standards
3. Author should verify version numbers with engineering/product team
4. Request re-review after changes
5. QE review still pending (as noted in PR description)

**Estimated effort to resolve:** 15-20 minutes for critical issues, additional 10-15 minutes if tech preview placement needs adjustment

---

## Questions for Author/Reviewer

1. **Version support policy:** Is it correct to show only versions 1.7 and 1.8 in the compatibility matrix, or should more versions be displayed?
2. **Archived release notes:** Where can users find release notes for versions 1.0-1.7?
3. **OpenShift version:** What is the correct version to replace "4.xx" (assuming 4.17 based on compatibility matrix)?
4. **Tech preview placement:** Is the current placement of the tech preview snippet within a list continuation acceptable, or should it be moved?

---

## Reviewer Information

**Reviewed by:** Claude (Peer Review)  
**Review type:** CQA and Technical Editorial  
**Focus areas:** Documentation standards, technical accuracy, clarity, completeness, consistency

**Files reviewed:**
- `modules/ob-release-notes-1-8.adoc` (NEW)
- `modules/ob-compatibility-support-matrix.adoc` (MODIFIED)
- `release_notes/ob-openshift-builds-release-notes.adoc` (MODIFIED)

---

**Review Date:** May 14, 2026  
**Review Iteration:** 1
