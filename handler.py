'''A simple handler that manipulate xml files.'''
import xml.dom.minidom
import xml.dom


class basic_handler(object):
    
    def __init__(self, version):
        self._version = version
        
   
    
class xml_handler(basic_handler):
    def __init__(self, version, schema_file=None):
        basic_handler.__init__(self, version)
        
    
    
    def _check_schema(self):
        pass
    
    
    def handle(self, xml_data):
        pass
    
