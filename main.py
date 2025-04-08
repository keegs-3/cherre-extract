# main.py
from src.extract import extract_properties

if __name__ == "__main__":
    props = extract_properties.get_properties()
    print(f"✅ Pulled {len(props)} property records")

