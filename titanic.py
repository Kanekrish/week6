import csv

# Global variables
records = []
headings = []


# Function to load data from a CSV file
def load_data(file_path):
    global headings, records
    print("Loading data...")

    # Open the file for reading
    with open(file_path, 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.reader(csv_file)

        # Read the first line and assign it to headings
        headings = next(csv_reader)

        # Read remaining lines and add them to records
        for row in csv_reader:
            records.append(row)
    print(f"Successfully loaded {len(records)} records.")
    print("Done!")
