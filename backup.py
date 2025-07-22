import shutil

def backup_data():
    shutil.copyfile('finance_manager.db', 'backup.db')
    print("✅ Backup created as 'backup.db'")

def restore_data():
    shutil.copyfile('backup.db', 'finance_manager.db')
    print("✅ Data restored from 'backup.db'")
