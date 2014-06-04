import types



class versatile_lib(object):
    def __init__(self, version):
        self._version = version

    
    def click_button(self, button_name):
        print 'try to click ' + button_name
    
    
    def select_table(self, table_name):
        print 'try to select table ' +table_name
    
    
    def __str__(self):
        return '[versatile lib version %s]' % self._version
        
class n_mon_lib(versatile_lib):
    def __init__(self, n_mon_version):
        versatile_lib.__init__(self, n_mon_version)
    
    '''
    def row_exists_in_table(self, table_name, cell_name):
        print "table %s-- has cell %s" % (table_name, cell_name)
    '''
        
    def row_exists_in_table(self, args):
        if types.ListType !=type(args):
            raise Exception('arg type is wrong')
        print "table %s-- has cell %s" % (args[0],args[1])
    
    
    def __str__(self):
        return '[ scn lib for nmon %s]' % self._version 
    
    def __getattr__(self, attr):
        if attr == 'version': 
            print 'fetch...'
            return self.version 
        else: 
            raise AttributeError(attr)

class um_lib(versatile_lib):
    pass    
