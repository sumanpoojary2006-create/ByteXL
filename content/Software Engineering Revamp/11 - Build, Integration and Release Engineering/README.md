# Unit 11 - Build, Integration and Release Engineering

Learning outcome: set up reproducible builds and CI, and prepare a versioned release with a rollback plan. Source: `Course Blueprint for Software Engineering.xlsx`, sheet `Syllabus`.

| # | Topic | Concepts |
| --- | --- | --- |
| 113 | Build Systems | Compile, link, package, build tools across ecosystems, deterministic builds |
| 114 | Dependency Management and Versioning | Lockfiles, semantic versioning, transitive dependencies, version conflicts |
| 115 | Continuous Integration | Integrate often, pipelines as code, quality gates, fast feedback |
| 116 | Continuous Delivery and Deployment | Release readiness, approval gates, deployment as a routine event |
| 117 | Branching Strategies and Feature Flags | Trunk-based development vs GitFlow, short-lived branches, decoupling deploy from release, flag lifecycle and clean-up |
| 118 | Containers for Development Environments | Reproducible dev environments, reading a Dockerfile, what containers do and do not solve |
| 119 | Configuration and Secrets Management | Environment-specific config, twelve-factor ideas, keeping secrets out of code |
| 120 | Release Management | Release notes, changelogs, hotfixes, rollback as a concept, deprecation policy |
| 121 | Developer Productivity | Fast local loops, slow-CI costs, internal tooling, onboarding scripts |

This unit is conceptual: it has no code snippets. Worked examples are given as tables and prose. Each image is introduced by a `Visual:` comment that records its brief.
