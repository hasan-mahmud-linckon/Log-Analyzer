# Log Analyzer

A Python tool for analyzing log files and extracting error information with CSV report generation.

## Features

- Analyzes log files in memory-efficient chunks
- Counts total lines and error occurrences
- Extracts detailed error messages
- Generates timestamped CSV reports
- Handles large log files efficiently


## Requirements

- Python 3.x
- pandas

## Installation

1. Clone this repository
2. Install dependencies:
```bash
git clone https://github.com/hasan-mahmud-linckon/Log-Analyzer.git
cd Log-Analyzer
pip install -r requirements.txt
```

## Usage

```bash
python log_analyzer.py <log_file>
```

### Example

```bash
python log_analyzer.py application.log
python log_analyzer.py system.log
```

## Output

The tool generates:
- Console output with analysis summary
- CSV report file with timestamp prefix (e.g., `1755026923_log_report_application.log.csv`)

### CSV Report Contains

- `access_time`: When the analysis was performed
- `number_of_lines`: Total lines in the log file
- `error_lines`: Number of lines containing errors
- `errors`: Individual error messages (one per row)

## Sample Log Files

The repository includes sample log files:
- `application.log`: Application-level logs with various severity levels
- `system.log`: System-level logs with kernel messages and service events


## Memory Efficiency

Uses chunk-based file reading (8KB chunks) to handle large log files without loading entire content into memory.