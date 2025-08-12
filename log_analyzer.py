import os
import sys
from datetime import datetime
import pandas as pd

def analyze_log(log_file, chunk_size=8192):
    """
    Analyze log file in chunks for better memory management
    """
    lines = 0
    error_count = 0    
    access_time = datetime.now()
    errors = []
    
    try:
        with open(log_file, 'r') as file:
            # Read file in chunks
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                    
                # Count lines in chunk
                lines += chunk.count('\n')
                # Count errors in chunk
                error_count += chunk.count('ERROR')

                for line in chunk.splitlines():
                    if 'ERROR' in line:
                        errors.append(line.strip())

        
        data = {
             'access_time': access_time,
            'number_of_lines': lines,
            'error_lines': error_count,          
            'errors': errors
            }
        
        write_to_csv(log_file,data)
        
        return data 
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        sys.exit(1)

def write_to_csv(log_file, data):
    try:
        timestamp = str(int(datetime.now().timestamp()))
        output_file = f"{timestamp}_log_report_{os.path.basename(log_file)}"
        # Creating DataFrame - handle errors list as separate rows
        if 'errors' in data and isinstance(data['errors'], list):
            # Create separate rows for each error
            rows = []
            for error in data['errors']:
                row = data.copy()
                row['errors'] = error  # Single error per row
                rows.append(row)
            df = pd.DataFrame(rows)
        else:
            df = pd.DataFrame([data])

        # Saving to CSV with all columns visible
        df.to_csv(f"{output_file}.csv", index=False)
        print(f"CSV file created: {output_file}.csv")
        return df
    except Exception as e:
        print(f"Error writing to CSV: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    if not os.path.exists(log_file):
        print(f"Error: The file {log_file} does not exist.")
        sys.exit(1)

    print(f"Analyzing log file: {log_file}")
    results = analyze_log(log_file)
    
    print("\nAnalysis Results:")
    print(f"Access time: {results['access_time']}")
    print(f"Total number of lines: {results['number_of_lines']:,}")
    print(f"Total number of errors: {results['error_lines']:,}")
   
if __name__ == "__main__":
    main()
