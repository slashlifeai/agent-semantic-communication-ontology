# ISO/IEC Standards and Regulatory Alignment

**Document Status:** Draft  
**Version:** 0.1

## 1. Introduction

This document provides a formal analysis of the alignment between the Semantic Agent Ontology and key international standards and regulations. Its purpose is to demonstrate how this ontology serves as a foundational technology to support compliance, interoperability, and governance as envisioned by major regulatory and standardization bodies, with a particular focus on the ISO/IEC JTC 1 landscape.

The core design principle of this ontology is to provide a machine-interpretable semantic layer that bridges high-level policy requirements with low-level technical implementation, thereby facilitating auditable and trustworthy AI systems.

## 2. High-Level Alignment Strategy

Our strategy is to ensure that the concepts defined within our ontology (e.g., Agent, Capability, Delegation, Accountability) provide concrete, implementable counterparts to the abstract requirements found in emerging standards. This enables organizations that adopt the ontology to build systems that are compliant-by-design.

## 3. Detailed Mapping

The following table outlines the specific relationships between our ontology's components and relevant standards.

| Ontology Concept | Related Standard / Regulation | Relationship and Rationale |
| :--- | :--- | :--- |
| **`core:Agent`** <br> **`agent:AgentIdentity`** | **ISO/IEC 42001 (AIMS)** <br> **EU AI Act** | Provides a precise, machine-readable definition of an "AI system" and its identity. This is fundamental for an **AI Management System (AIMS)**, as it allows for the clear scoping, cataloging, and risk assessment of AI assets within an organization, as required by ISO 42001 and the EU AI Act's conformity assessment procedures. |
| **`del:Delegation`** <br> **`cap:Capability`** | **ISO/IEC 23894 (Risk Management)** <br> **eIDAS 2.0 (EUDI Wallet)** | The `Delegation` and `Capability` model provides a formal mechanism for **access control and the management of rights**. This aligns with ISO 23894's risk treatment objectives by enabling fine-grained, auditable control over an AI system's operational scope. It also directly corresponds to the **Mandates** concept in the EUDI Wallet Architecture, providing a semantic framework for delegating rights from a person to an agent. |
| **`ledger:LedgerEvent`** <br> **`acc:AccountabilityEvent`** | **ISO/IEC 27001 (ISMS)** <br> **EU AI Act (Art. 13, 15, 20)** | Directly implements the requirements for **logging, traceability, and evidence collection**. The ledger-based approach creates an immutable audit trail, which is a cornerstone for an Information Security Management System (ISMS) and is explicitly required for high-risk AI systems under the EU AI Act for post-market monitoring and incident analysis. |
| **TEE/DID/Audit Chain Binding** | **ISO/IEC 27040 (Storage Security)** <br> **NIST SP 800-207 (Zero Trust)** | Provides a strong cryptographic foundation for data-in-use protection and identity verification. By binding a DID to a Trusted Execution Environment (TEE), we can ensure that an agent's actions are executed in a secure, isolated environment. This aligns with the principles of Zero Trust Architecture and provides verifiable integrity for data storage and processing, as recommended by ISO 27040. |
| **`core:Ontology` (Overall)** | **ISO/IEC 5392 (Knowledge Engineering)** <br> **ISO/IEC 21838 (Top-Level Ontologies)** | The entire project follows the best practices outlined in standards for ontology and knowledge engineering. By providing a modular, well-documented ontology with a clear top-level structure, we ensure that it is extensible, maintainable, and can be integrated with other domain or top-level ontologies, following the principles of ISO 21838. |
| **Semantic-Operational Model** | **ISO/IEC TR 24028 (Trustworthiness Overview)** | Our "Semantic-Operational" approach, where ontology concepts map to executable behaviors, provides a concrete method for achieving **transparency and explainability**—key components of AI trustworthiness as defined in ISO/IEC TR 24028. It makes the "why" behind an agent's action (the semantic intent) directly auditable alongside the "what" (the operational log). |

## 4. Conclusion

The Semantic Agent Ontology is strategically positioned to serve as a critical enabling technology for the next generation of trustworthy and interoperable AI systems. Its design directly supports the objectives of key ISO standards and major international regulations, providing a clear path for organizations to build and deploy compliant AI solutions.
