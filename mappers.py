from scn_libs import *
from handlers import *
import types
import re
import logging

class basic_scn_mapper(object):
    def __init__(self, scn_lib, scn_file=None):
        self._dic = {}
        self._lib = scn_lib
        self._map()
    
    
    
    ''' could extend to some scn_file in the future'''
    def _map(self):
        
        self._dic = {'ClickButton':'click_button', 'SelectTable':'select_table'}
    
    def get_scn(self, keyword):
        try:
            if keyword in self._dic.keys():
                if self._dic.get(keyword) in self._lib.__dict__.keys():
                    
                    return self._lib.__dict__[self._dic.get(keyword)]
                else:
                    raise Exception('keyword not supported in basic_scn_mapper')
            else:
                raise Exception('keyword not supported in basic_scn_mapper')
        except:
            raise Exception('errors happened in basic_scn_mapper')
        
        
    def __str__(self):
        return '[mapped lib is %s]' % self._lib

class nmon_scn_mapper(basic_scn_mapper):
    def __init__(self, scn_lib, n_mon_lib, nmon_scn_file=None):
        basic_scn_mapper.__init__(self, scn_lib)
        self._nmon_lib = n_mon_lib
        self._map_nmon()
    
        
    ''' could extend to some nmon_scn_file in the future'''
    def _map_nmon(self):
        
        # self._dic.setdefault({'rowExistInTable':'row_exists_in_table' })
        self._dic.setdefault('rowExistInTable', 'row_exists_in_table')
        
        
    def get_scn(self, keyword):
        try:
            if keyword in self._dic.keys():
                if self._dic.get(keyword) in self._lib.__dict__.keys():
                    return self._lib.__dict__[self._dic.get(keyword)]
                
                elif self._dic.get(keyword) in self._nmon_lib.__dict__.keys():
                    return self._nmon_lib.__dict__[self._dic.get(keyword)]
                else:
                    raise Exception('keyword not supported by nmon_scn_mapper')
            else:
                raise Exception('keyword not supported by nmon_scn_mapper')
        except:
            raise Exception('error happend in nmon_scn_mapper ')
    
    def __str__(self):
        return '[mapped lib is %s]' % self._nmon_lib

class um_scn_mapper(basic_scn_mapper):
    pass
