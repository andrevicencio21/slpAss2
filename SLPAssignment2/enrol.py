def read_lines(file):
    """
    Returns a list of all lines (string) in the specified file in its original order, except for lines starting with a #. The lines
    returned must not end with new-line character(s).
    """
    print 'f'

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
        # readLine(path)
        
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
      
    def enrol(self, studId, classCode):
        '''
        Accepts two (and only two) arguments: a student ID (string) and a class code (string).
        Returns 1 if successful, None if not. Before attempting to enrol a student into a class, it checks whether the
        number of students in the class is less than the capacity of the venue of the class. If not, then there is no space in
        the class and it fails. Otherwise, if the student is already enrolled in a class (including the specified class to be
        enrolled into) in the same subject as the specified class, the student is removed from the current enrolled class
        before being placed into the new one (i.e. the one specified by the second argument).
        Raises KeyError if the specified class code does not exist.
        For better modularisation, you should write internal methods to be used by defined methods for common tasks.
        Names for internal methods should start with a single underscore (_), to distinguish from “public” methods.
        Within the enrol module, you should also create an EnrolTest class which is a subclass of unittest.TestCase.
        The EnrolTest class should provide adequate test coverage for all utility functions and methods in the enrol
        module. You should include at least one test per function/method.
        The enrol module will be assessed by an automated script during marking. The marking script will expect the
        module to strictly conform to this specification. You will lose a significant portion (or even all) of the marks if your
        module does not exactly meet the specification. Keep in mind that both Python and Linux are case-sensitive.
        '''
    
    
    
    
    
    
    
    
    
    