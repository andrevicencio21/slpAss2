import os


def read_lines(file):
    """
    Returns a list of all lines (string) in the specified file in its original order, except for lines starting with a #. The lines
    returned must not end with new-line character(s).
    """
    f = open(os.path.join(Enrol.path, file))
    if f is None:
        print 'f'
        print 'There is no file'
    

def read_table(file):
    """
    Reads a file of colon-delimited lines and returns a list of lists in the original order, with each line being represented
    as a list of strings, split on colons. For example, if the file example contains:
    foo:1:12
    bar:2:hello
    Then read_table('example') will return a Python list [['foo','1','12'],['bar','2','hello']].
    """
    print 'f'

def write_lines(filename, lines):
    write = True
    """
    Writes a list of strings safely to the specified file. Overwrites the file if it already exists. Line separators should be
    added where necessary. If an error occurs during the process (i.e. an exception is caught), it swallows the
    exception, restore the original file (if applicable) and returns 0. Returns 1 if the operation was successful.
    """
    if write:
        return 1
    elif write is False:
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
    
    
    
    
    
    
    
    
    