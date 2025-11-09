# The Journey of a Smart Thermostat: From Design to Global Brand (OBM/ODM/OEM)

This use case illustrates the evolution of a Taiwanese company, InnovateTech Taiwan, through different manufacturing and branding models: Original Equipment Manufacturing (OEM), Original Design Manufacturing (ODM), and Original Brand Manufacturing (OBM). It demonstrates how the agent ontology can model the transition of business relationships, capabilities, and delegation structures across these phases.

## User Story: InnovateTech Taiwan's Transformation

### Phase 1: OEM (Original Equipment Manufacturer) - Precise Contract Manufacturing
**Scenario**: An American smart home brand, "ConnectedLiving," commissions InnovateTech to produce 100,000 smart thermostats (Model CL-T-200) based entirely on ConnectedLiving's designs.

### Workflow Breakdown:
1.  **Procurement Intent (ConnectedLiving)**:
    *   **Description**: ConnectedLiving's Procurement Agent initiates an order.
    *   **Ontology**: `Intent` (objective: "Manufacture 100,000 CL-T-200 thermostats according to design #CL-SPEC-2025"), `Agent` (ConnectedLiving Procurement Agent).
2.  **Delegation to Production (InnovateTech)**:
    *   **Description**: InnovateTech's Sales Agent receives the order and delegates production to its Production Agent.
    *   **Ontology**: `Delegation` (delegatedBy: Sales Agent, delegatesTo: Production Agent, delegationScope: "Strictly manufacture CL-T-200 as per provided specifications"). Key characteristic: no design modification allowed.
3.  **Manufacturing Action & Artifact**: 
    *   **Description**: The Production Agent executes manufacturing. 
    *   **Ontology**: `Action` (manufacturing), `Artifact` (100,000 thermostats, QC Report).
4.  **Accountability**: Recording confirms faithful execution of the client's design.
    *   **Ontology**: `TraceEvent` / `LedgerRecord`.

### Phase 2: ODM (Original Design Manufacturer) - Value-Added Design & Manufacturing
**Scenario**: InnovateTech, through its R&D, develops an optimized, low-power smart thermostat (Model IT-T-300) with predictive maintenance. They proactively offer this design to ConnectedLiving.

### Workflow Breakdown:
1.  **Capability Evolution (InnovateTech)**:
    *   **Description**: InnovateTech's R&D Agent develops new design capabilities.
    *   **Ontology**: New `Capability`: "Smart Energy-Efficient Thermostat Design."
2.  **Proactive Proposal**: 
    *   **Description**: InnovateTech's Sales Agent proposes IT-T-300 to ConnectedLiving.
    *   **Ontology**: `Artifact` (IT-T-300 design specifications).
3.  **New Procurement Intent (ConnectedLiving)**:
    *   **Description**: ConnectedLiving accepts the new design.
    *   **Ontology**: `Intent` (objective: "Procure 200,000 IT-T-300 thermostats, rebranded as 'ConnectedLiving EcoSense'").
4.  **Revised Delegation**: 
    *   **Description**: Delegation now based on InnovateTech's design, including branding requirements.
    *   **Ontology**: `Delegation` (delegationScope: based on `#IT-SPEC-300`, includes branding).

### Phase 3: OBM (Original Brand Manufacturer) - Owning the Brand
**Scenario**: InnovateTech decides to launch its own global brand, "InnovateHome."

### Workflow Breakdown:
1.  **Top-Level Brand Intent (InnovateTech)**:
    *   **Description**: InnovateTech's Brand Strategy Agent sets a high-level goal.
    *   **Ontology**: `Intent` (objective: "Launch 'InnovateHome' global brand; achieve 500,000 online sales in year 1").
2.  **Complex Multi-Layered Delegation**: 
    *   **Description**: The Brand Strategy Agent delegates various functions to specialized agents.
    *   **Ontology**: Multiple `Delegation` instances:
        *   To `Marketing_Agent`: "Execute global digital marketing."
        *   To `Production_Agent`: "Manufacture 500,000 units for own inventory."
        *   To `eCommerce_Agent`: "Manage online sales, payments, and logistics."
        *   To `SupplyChain_Agent`: "Manage global supply chain and component procurement" (integrating our previous 'Supplier Verification and Cross-Border Payment' use case here).
3.  **End-Consumer Interaction**: 
    *   **Description**: An end-consumer (represented by `Consumer_Agent`) places an order.
    *   **Ontology**: `Intent` (consumer's purchase intent), `Action` (payment processing, logistics orchestration by `eCommerce_Agent`).
4.  **End-to-End Accountability**: All operations, from budgets to customer orders, are recorded for a full business audit trail.
    *   **Ontology**: `TraceEvent` / `LedgerRecord` linking all entities.