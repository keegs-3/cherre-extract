# src/extract/extract_properties.py
from src.cherre_api import run_query

QUERY = """
query GetProperties($limit: Int, $offset: Int) {
  core_properties(limit: $limit, offset: $offset) {
    property_id
    address {
      line
      city
      state
      zip
    }
    building_area
    year_built
    property_type
    ...
  }
}
"""

def get_properties(limit=1000, offset=0):
    return run_query(QUERY, {"limit": limit, "offset": offset})

