from utils.mappers import *
from utils.scn_libs import *

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xml.dom.minidom
import xml.dom
import collections
import types
import os
    
class start_rpc_server:
    
      def __init__(self):
          server = SimpleXMLRPCServer(("192.168.0.1",12306),requestHandler=RequestHandler)
          server.register_instance(squish_rpc_server())
          print 'server started and listening on port 12306'
          server.serve_forever()
          

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
    

class squish_rpc_server(object):
    

    def __init__(self):
        self._scn_mapper = nmon_scn_mapper(versatile_lib, n_mon_lib)
        self._td_mapper = testdata_OM_mapper(None, None)
        self._xml_handler = xml_handler('1.0', None)
    
    
    def perform_GUI_test(self, xml_data):
        print 'received data %s' % xml_data
    
        paris = self._xml_handler.handle(xml_data)
        print paris
        for item in paris:
            print item
        for item in paris:
             self._scn_mapper.get_scn(item.get_name())(self._scn_mapper, self._td_mapper.get_data(item.get_value()))
        return True
        
