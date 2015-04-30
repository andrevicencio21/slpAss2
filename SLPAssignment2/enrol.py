import os.path


def read_lines(filename):
    finalLines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.rstrip() is not "" and line.rstrip()[0] is not "#":
            if "#" not in line:
                finalLines.append(line.rstrip('\n'))
            else:
                finalLines.append(line[0: line.find('#')])
    f.close()
    print finalLines #remove later
    return finalLines
    
def read_table(filename):
    finalLines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        finalLines.append(line.rstrip('\n').split(':'))
    f.close()
    print finalLines #remove later
    return finalLines
    
def write_lines(filename, lines):
    backup = None
    if os.path.isfile(filename):
        f = open(filename, 'w+') #try and make this the actual test don't do os.path.isffile
        backup = f.readlines()
    else:
        f = open(filename, 'w')
    try:
        for line in lines:
            f.write(str(line) + '\n')
        f.close()
        return 1
    except:
        if backup is not None:
            f.write(backup)
        f.close()
        return 0
      
class Enrol():
    
    
    def __init__(self, path):
        '''
        The constructor.
        It accepts one (and only one) argument, the path to the data directory where enrolment records are kept. It
        should support both absolute and relative path names. When the object is constructed, it should read enrolment
        records from the specified directory
        '''
        self.path = path
        
        
    def subjects(self):
        '''
        Accepts no argument.
        Returns a list of all subject codes (string) in the enrolment system. There is no specified order
        '''
        return
    
    def subject_name(self, subjectCode):
        '''
        Accepts one (and only one) argument: a subject code (string).
        Returns a string which is the name of the specified subject.
        Raises KeyError if the specified subject code does not exist.
        '''
        return

    def classes(self, subjectCode):
        '''
        Accepts one (and only one) argument: a subject code (string).
        Returns a list of class codes (string) for the specified subject. There is no specified order.
        Raises KeyError if the specified subject code does not exist.
        '''
    def class_info(self, subjectCode):
        '''
        Accepts one (and only one) argument: a class code (string).
        Returns class information in a tuple of the form (subjectcode, time, venue, tutor, students).
        The first four elements are strings. The last item is a list of the student IDs (string) enrolled in the class. There is no
        specified order of the student IDs.
        Raises KeyError if the specified class code does not exist.
        '''
    
    def check_student(self, studId, subjectCode):
        print 'f'
    
    def enrol(self, studId, classCode):
        print 'f'
    
    
    
    
    
    
    
    
    