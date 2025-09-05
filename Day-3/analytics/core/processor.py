from .validator import validate_data
def process_data(Data):
    if (not validate_data(Data)):
      return f'processed data:{Data}'
    return 'Invalid Data'
 