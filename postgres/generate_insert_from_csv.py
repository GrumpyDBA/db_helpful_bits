import csv
from typing import Optional

def generate_insert_statements(
    csv_file_path: str,
    table_name: str,
    output_file_path: Optional[str] = None
) -> None:
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        
        # Read the header row for column names
        header = next(reader)
        # Begin building the multi-row INSERT statement
        insert_script = f"INSERT INTO {table_name} ({', '.join(header)}) VALUES \n"
        
        # Build the value tuples
        value_rows = []
        for row in reader:
            processed_values = []
            for val in row:
                # Remove leading/trailing whitespace
                val = val.strip()
                if val == "":
                    # Insert NULL if blank
                    processed_values.append("NULL")
                else:
                    # Otherwise, wrap in quotes (or handle escaping as needed)
                    processed_values.append(f"'{val}'")
            
            # Create a single tuple like ('val1', 'val2', NULL, 'val4', ...)
            value_rows.append(f"({', '.join(processed_values)})")
        
        # Combine all tuples into one multi-row insert statement
        insert_script += ",\n".join(value_rows) + ";"
        
        if output_file_path is None:
            print(insert_script)
        else:
            with open(output_file_path, "w", encoding='utf-8') as output_file:
                output_file.write(insert_script)

if __name__ == "__main__":
    csv_path: str = "/Users/soandso/Downloads/my_source_data.csv"
    output_file_path: str = "/Users/soandso/Downloads/my_table.sql"
    table_name: str = "my_table"
    generate_insert_statements(csv_path, table_name, output_file_path)
