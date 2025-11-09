# Ontologies Directory Overview

This directory is the core of the Semantic Agent Ontology project, containing all formal definitions of the semantic model for AI Agents. It is structured to provide a clear separation between the core ontology modules, their JSON-LD contexts, JSON Schema profiles, and usage examples.

## Directory Structure

*   **`.ttl` files (e.g., `core.ttl`, `agent.ttl`)**: These are the primary ontology modules, defined using the [Turtle (Terse RDF Triple Language)](https://www.w3.org/TR/turtle/) syntax. Each `.ttl` file defines a specific aspect of the agent ontology (e.g., core concepts, agent identity, capabilities, delegation, ledger, etc.). The main entry point for the complete ontology is `ontology.ttl`, which imports all other modules.

*   **`context/`**: This subdirectory contains [JSON-LD Context](https://www.w3.org/TR/json-ld11/#the-context) files (e.g., `agent.jsonld`, `capability.jsonld`). These files are crucial for mapping JSON data structures to the semantic terms defined in the `.ttl` ontologies. They act as a bridge, allowing JSON documents to be interpreted as Linked Data.

*   **`profiles/`**: This subdirectory contains [JSON Schema](https://json-schema.org/) validation profiles (e.g., `agent.jsonld`, `capability.jsonld`). These schemas define the expected structure and data types for JSON documents that conform to specific parts of the ontology. They are used for data validation, ensuring that agent-related data adheres to the defined model.

*   **`examples/`**: This subdirectory provides concrete [JSON-LD examples](https://www.w3.org/TR/json-ld11/#examples) that illustrate how to use the ontology and its associated schemas. These examples demonstrate various aspects of agent definitions, delegations, ledger records, and other semantic constructs, serving as practical guides for implementers.

## How to Use

*   **For Semantic Web Tools:** Load the `ontology.ttl` file into any RDF/OWL compatible tool to explore the full semantic model.
*   **For JSON-LD Processing:** Use the context files in `context/` to expand or compact JSON-LD documents. For instance, when processing an `agent.jsonld` example, reference `context/agent.jsonld`.
*   **For Data Validation:** Use the JSON Schema files in `profiles/` with a JSON Schema validator to ensure your JSON data conforms to the expected structure.
*   **For Learning:** Refer to the `examples/` to understand practical applications of the ontology.
