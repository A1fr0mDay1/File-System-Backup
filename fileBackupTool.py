import logging

class BackupSystem:
    def __init__(self, source_directory, backup_directory):
        self.source_directory = source_directory
        self.backup_directory = backup_directory
        self.backup_history_file = self.backup_directory / "backup_history.json"

    # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.backup_directory / "backup.log"),
                logging.StreamHandler()
            ]
        )