import logging 

logging.basicConfig(filename='app.log', 
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO)


def create_employee(id, name, job_title, salary, join_date):    
    emp = {
        'id':id, 
        'name': name, 
        'job_title': job_title, 
        'salary': salary, 
        'join_date': join_date
    }
    employees=read_all()
    employees.append(emp)
    with open('employee.dat', 'rb') as writer:
       pickle.dump(employees,)
    logging.info(f'{name} Employee Created.')
def read_all():
    return employees