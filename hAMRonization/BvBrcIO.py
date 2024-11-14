import csv
from hAMRonization.Interfaces import hAMRonizedResultIterator
from hAMRonization.constants import GENE_PRESENCE

# list of mandatory fields not implimented by tools
required_metadata = [
    "input_file_name",
]

class BvBrcIOIterator(hAMRonizedResultIterator):
    def __init__(self, source, metadata):
        metadata["analysis_software_name"] = "BVBRC-Rast_Tk"
        metadata["genetic_variation_type"] = GENE_PRESENCE
        metadata["reference_database_name"] = "BVBRC-Rast_Tk"
        metadata["analysis_software_version"] = "1.3.0"
        metadata["reference_database_version"] = "1.3.0"
        self.metadata = metadata

            # on the left is the bvbrc csv column headers and the right are the hAMRonize fields.
        self.field_mapping = {
            'feature_id'                :"reference_accession", 
            'gene_symbol'               :"gene_symbol", 
            'gene_definition'           :"gene_name", 
            'function_x'                :"drug_class",
            'family_assignments'        :None, 
            'similarity_associations'   :None, 
            'quality'                   :None, 
            'type'                      :None,
            'function_y'                :None, 
            'feature_creation_event'    :None, 
            'annotations'               :None, 
            'feature_number'            :None,
            'contig'                    :"input_sequence_id", 
            'start'                     :"input_gene_start", 
            'orientation'               :"strand_orientation", 
            'end'                       :"input_gene_stop", 
            'pathways'                  :None, 
            'go_terms'                  :None,
            'ec_numbers'                :None, 
            'merged_event'              :None, 
            'hostname'                  :None, 
            'execute_time'              :None, 
            'parameters'                :None,
            'tool_name'                 :None, 
            'id'                        :None, 
            'version'                   :None, 
            'execution_time'            :None
            }
        
        super().__init__(source, self.field_mapping, self.metadata)

    def parse(self, handle):
        """
        Read each and return it
        """
        reader = csv.DictReader(handle, delimiter="\t")
        for result in reader:
            yield self.hAMRonize(result, self.metadata)
        
        
