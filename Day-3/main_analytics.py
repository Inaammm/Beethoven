from analytics.IO.reader import reader_data
from analytics.IO.writer import write_data
from analytics.core.processor import process_data
from analytics.tools.formatter import format_data


data = reader_data()
data1 = process_data(data)
data2 = format_data(data1)
print(write_data(data2))