class parent(object):
    def __init__(self):
       self.Name="hi"

class child(parent):
      def __init__(self,*args,**kwargs):
        super(child, self).__init__(*args, **kwargs)
        junk=1

c=child()
print("%s"%c.Name)
