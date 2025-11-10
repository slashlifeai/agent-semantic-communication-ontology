import os
import glob
from rdflib import Graph

def convert_ttl_to_jsonld(ttl_file, jsonld_file):
    """Converts a single TTL file to a JSON-LD file."""
    g = Graph()
    try:
        g.parse(ttl_file, format='turtle')
        g.serialize(destination=jsonld_file, format='json-ld', indent=2)
        print(f"Successfully converted {ttl_file} to {jsonld_file}")
    except Exception as e:
        print(f"Error converting {ttl_file}: {e}")

def main():
    """
    Finds all .ttl files in the 'ontologies' directory and its subdirectories
    and converts them to .jsonld files in the same directory.
    """
    ontologies_dir = 'ontologies'
    # Using glob to find all .ttl files recursively
    ttl_files = glob.glob(os.path.join(ontologies_dir, '**', '*.ttl'), recursive=True)

    if not ttl_files:
        print("No .ttl files found in the 'ontologies' directory.")
        return

    for ttl_file in ttl_files:
        # Create the output filename by replacing the extension
        jsonld_file = os.path.splitext(ttl_file)[0] + '.jsonld'
        convert_ttl_to_jsonld(ttl_file, jsonld_file)

if __name__ == "__main__":
    main()
