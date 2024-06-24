from datetime import datetime

def rename_file():
    current_date = datetime.now()
    date_format = current_date.strftime('%Y%m%d')
    new_file_name = f'TMOC_UTS_{str(date_format)}.xlsx'
    return new_file_name