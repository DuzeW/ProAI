import csv
import pandas as pd
from datetime import datetime
import os

class MetricsLogger:
    def __init__(self, file_name="metrics.csv", excel_name="metrics.xlsx"):
        self.file_name = file_name
        self.excel_name = excel_name
        self.columns = [
            "Task", "Agent", "Model", "Response Time (s)",
            "Success", "Response Size (tokens)",
            "API Cost (tokens)", "Error Count", "Details", "Timestamp"
        ]
        self._initialize_file()

    def _initialize_file(self):
        # Initialize the CSV file with headers if it doesn't exist
        try:
            with open(self.file_name, mode="x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(self.columns)
        except FileExistsError:
            pass

    def log(self, task, agent, model, response_time, success, response_size, api_cost, error_count, details):
        row = [
            task, agent, model, response_time, success,
            response_size, api_cost,
            error_count, details, datetime.now().isoformat()
        ]
        # Append to CSV
        with open(self.file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(row)
        # Update Excel
        self._update_excel()

    def _update_excel(self):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(self.file_name)
            # Save the DataFrame as an Excel file
            df.to_excel(self.excel_name, index=False)
        except Exception as e:
            print(f"Error updating Excel file: {e}")
