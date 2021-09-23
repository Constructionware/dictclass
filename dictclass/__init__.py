
class DictClass(object):
    """
    Converts a dictionary to a class.
    Basic Usage:
    data = dict(
        name='millamo',
        ref=49,
        height=145
    ) 
    data_class = DictClass(data)
    data_class.name
    millamo
    Nested Data:
    data = dict(
        name='millamo',
        ref=49,
        height=145
        size={"width":54,"depth":478,"length":1254,"typeof":"rod"}
    )
    data_class = DictClass(data)
    data_class.size
    {"width":54,"depth":478,"length":1254,"typeof":"rod"}

    """
    #
    def __init__(self, dictionary):
        self.local_dictclass(dictionary)        

    def local_dictclass(self, data:dict):
        for key in data:
            setattr(self, key, data[key])  

    def to_dict(self):
        return self.__dict__     
    
    def __repr__(self):
        """"""
        attrs = str([x for x in self.__dict__])
        return f"<DictClass: {attrs}>" 


