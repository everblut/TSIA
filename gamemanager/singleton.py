#!/usr/bin/env python2

class Singleton(type):
    def __init__(self,name,bases,dic):
        super(Singleton,self).__init__(name,bases,dic)
        self.instance = None
        
    def __call__(self,*args,**kw):
        if self.instance is None:
            self.instance = super(Singleton,self).__call__(*args,**kw)
        return self.instance
