<!--
Sync Impact Report:
- Version change: Template → 1.0.0 (Initial ratification)
- Modified principles: All placeholders filled with project-specific values
- Added sections: Phase Constraints, Technology Stack Requirements
- Removed sections: None
- Templates requiring updates:
  ✅ plan-template.md (reviewed - Constitution Check section aligns)
  ✅ spec-template.md (reviewed - requirements structure aligns)
  ✅ tasks-template.md (reviewed - phase organization aligns)
- Follow-up TODOs: None
-->

# AI-Native Todo Application Constitution

## Core Principles

### I. Spec-First Development (NON-NEGOTIABLE)

**No implementation without written specification.** Every feature, enhancement, or architectural change MUST be documented in a spec file before any code is written. Specifications are the single source of truth for all functionality.

**Rationale**: Prevents scope creep, ensures traceability, enables informed decision-making, and maintains alignment across all phases of the multi-phase evolution.

**Rules**:
- All functionality MUST be derived from explicit requirements in spec files
- Breaking changes MUST require spec updates before implementation
- No "quick fixes" or "small changes" bypass this requirement
- Specs MUST be version-controlled and reviewed

### II. Phase Isolation & Progressive Complexity

**Each phase builds strictly on prior phases.** Technology choices are fixed per phase and later-phase technologies MUST NOT leak into earlier phases. Phases cannot be skipped.

**Rationale**: Ensures incremental learning, maintains architectural clarity, prevents premature optimization, and allows independent validation of each evolutionary step.

**Rules**:
- Phase I (Python Console) → Phase II (Full-Stack Web) → Phase III (AI-Powered) → Phase IV (Local K8s) → Phase V (Cloud)
- Each phase MUST be fully functional before proceeding to the next
- Technology stack per phase is immutable unless explicitly revised in spec
- No cloud dependencies in local phases; no web dependencies in console phase

### III. Traceability & Explicit State

**All state must be explicitly modeled and traceable.** No hidden state, no implicit behavior. Every feature MUST map to a spec file and phase.

**Rationale**: Enables debugging, auditing, and understanding of system behavior across all phases. Critical for AI features where behavior must be explainable.

**Rules**:
- All in-memory or persisted state MUST be explicitly documented
- Every feature MUST reference its originating spec file
- State transitions MUST be logged and traceable
- No magic numbers, no undocumented assumptions

### IV. Deterministic-First, AI-Auditable

**Deterministic behavior in early phases, probabilistic behavior only in AI phases.** When AI is introduced (Phase III+), all AI behavior MUST be prompt-defined, auditable, and reproducible where possible.

**Rationale**: Establishes predictable foundation before introducing non-deterministic AI components. Ensures AI features remain controllable and debuggable.

**Rules**:
- Phases I-II MUST be fully deterministic
- AI (Phase III+) MUST NOT bypass business rules from earlier phases
- All AI actions MUST map to explicit backend operations
- Prompt logic MUST be versioned and documented
- AI behavior MUST be auditable through logs and traces

### V. Technology Stack Discipline

**Technology choices are fixed per phase and explicitly documented.** Deviations require spec amendment and architectural justification.

**Rationale**: Prevents technology sprawl, maintains focus, ensures team can master each stack before adding complexity.

**Phase-Specific Stacks**:
- **Phase I**: Python (console, in-memory only)
- **Phase II**: Next.js, FastAPI, SQLModel, Neon PostgreSQL
- **Phase III**: OpenAI ChatKit, Agents SDK, Official MCP SDK
- **Phase IV**: Docker, Minikube, Helm, kubectl-ai, kagent
- **Phase V**: DigitalOcean DOKS, Kafka, Dapr

**Rules**:
- Technology substitutions MUST be documented in spec with rationale
- No experimental or unproven technologies without explicit approval
- Dependencies MUST be pinned and documented

### VI. Separation of Concerns

**Clear boundaries between UI, logic, storage, AI, and infrastructure.** Each layer MUST have well-defined responsibilities and interfaces.

**Rationale**: Enables independent testing, parallel development, and clean phase transitions. Prevents coupling that would make evolution difficult.

**Rules**:
- UI layer MUST NOT contain business logic
- Business logic MUST NOT contain storage implementation details
- AI layer MUST NOT directly access storage (must go through business logic)
- Infrastructure concerns MUST be isolated from application code
- API contracts MUST be explicitly defined at layer boundaries

## Phase Constraints

### Phase Execution Rules

1. **No Phase Skipping**: Each phase MUST be completed and validated before proceeding
2. **Phase Completion Criteria**:
   - All specs for the phase are implemented
   - All tests pass (where applicable)
   - System is deployable in the phase's target environment
   - No regressions from previous phases
3. **Phase Isolation**: Later-phase code MUST NOT be introduced prematurely
4. **Backward Compatibility**: Each phase MUST maintain functionality from all prior phases

### Phase-Specific Requirements

**Phase I (In-Memory Python Console)**:
- MUST run entirely in-memory (no files, no databases)
- MUST be console-based (no GUI, no web interface)
- MUST implement CRUD for todos, status management, listing/filtering
- MUST be fully deterministic
- Testing: Manual or lightweight scripted tests only

**Phase II (Full-Stack Web Application)**:
- MUST define explicit API contracts before implementation
- MUST replace in-memory state with persistent storage
- MUST maintain all Phase I functionality
- MUST use specified stack: Next.js, FastAPI, SQLModel, Neon

**Phase III (AI-Powered Todo Chatbot)**:
- MUST NOT bypass business rules from Phases I-II
- MUST map all AI actions to explicit backend operations
- MUST version and document all prompt logic
- MUST maintain deterministic core with AI as enhancement layer

**Phase IV (Local Kubernetes Deployment)**:
- MUST be fully reproducible locally
- MUST NOT require cloud dependencies
- MUST demonstrate operational understanding (monitoring, logging, debugging)
- MUST use specified stack: Docker, Minikube, Helm

**Phase V (Advanced Cloud Deployment)**:
- MUST define infrastructure as code
- MUST implement observability (metrics, logs, traces)
- MUST demonstrate scalability and resilience
- MUST use specified stack: DigitalOcean DOKS, Kafka, Dapr

## Development Workflow

### Specification Process

1. **Feature Request**: User provides natural language description
2. **Spec Creation**: Use `/sp.specify` to create formal specification
3. **Clarification**: Use `/sp.clarify` to resolve ambiguities (max 5 questions)
4. **Planning**: Use `/sp.plan` to create architectural plan
5. **Task Breakdown**: Use `/sp.tasks` to generate dependency-ordered tasks
6. **Implementation**: Use `/sp.implement` to execute tasks
7. **Validation**: Verify against acceptance criteria in spec

### Quality Gates

**Before Implementation**:
- [ ] Spec file exists and is complete
- [ ] Phase assignment is clear
- [ ] Technology stack matches phase requirements
- [ ] No phase isolation violations
- [ ] Acceptance criteria are testable

**During Implementation**:
- [ ] All changes reference spec file
- [ ] No hidden state introduced
- [ ] Separation of concerns maintained
- [ ] Phase constraints respected
- [ ] Traceability maintained (logs, comments, commit messages)

**After Implementation**:
- [ ] All acceptance criteria met
- [ ] No regressions in prior phases
- [ ] Documentation updated
- [ ] PHR (Prompt History Record) created
- [ ] ADR created for significant architectural decisions

### Testing Requirements

**Phase I**: Manual testing acceptable; focus on correctness
**Phase II+**: Automated tests required for:
- API contract compliance
- Business logic correctness
- Integration between layers
- Regression prevention

**AI Features (Phase III+)**: Additional requirements:
- Prompt behavior must be reproducible
- AI actions must be auditable
- Fallback behavior for AI failures
- Business rule enforcement tests

## Governance

### Amendment Process

1. **Proposal**: Document proposed change with rationale
2. **Impact Analysis**: Identify affected specs, code, and phases
3. **Review**: Evaluate against core principles
4. **Approval**: Explicit user consent required
5. **Migration**: Update constitution, templates, and dependent artifacts
6. **Version Bump**: Follow semantic versioning (MAJOR.MINOR.PATCH)

### Versioning Policy

- **MAJOR**: Backward-incompatible governance changes, principle removals/redefinitions
- **MINOR**: New principles added, materially expanded guidance
- **PATCH**: Clarifications, wording improvements, non-semantic refinements

### Compliance

- All PRs and reviews MUST verify compliance with this constitution
- Complexity MUST be justified (see plan-template.md Complexity Tracking section)
- Violations MUST be documented with rationale or rejected
- Constitution supersedes all other practices and conventions

### Architectural Decision Records (ADRs)

When significant architectural decisions are made (typically during planning), document them using `/sp.adr <decision-title>`. Significant decisions meet ALL criteria:
- **Impact**: Long-term consequences (framework, data model, API, security, platform)
- **Alternatives**: Multiple viable options were considered
- **Scope**: Cross-cutting and influences system design

ADRs are stored in `history/adr/` and MUST include: context, decision, consequences, alternatives considered.

### Prompt History Records (PHRs)

Every user interaction that results in work (implementation, planning, debugging, spec creation) MUST be recorded as a PHR in `history/prompts/` with appropriate routing:
- Constitution changes → `history/prompts/constitution/`
- Feature-specific work → `history/prompts/<feature-name>/`
- General work → `history/prompts/general/`

PHRs ensure traceability and learning from all development activities.

---

**Version**: 1.0.0 | **Ratified**: 2026-01-06 | **Last Amended**: 2026-01-06
