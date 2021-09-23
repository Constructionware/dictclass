# dictclass
Converts a python dictionary to a class object.

## Basic Usage

```
from dictclass import DictClass

data = dict(
       name='millamo',
       ref=49,
       height=145
       ) 

dict_class = DictClass(data)

```

Access the key bindings with the dot notation.

```        
dict_class.name
millamo

```


 ###  Handling Nested Data
    
 ```
 data = dict(
                name='millamo',
                ref=49,
                height=145
                size={"width":54,"depth":478,"length":1254,"typeof":"rod"}
            )

dict_class = DictClass(data)

 ```
   
 ```
dict_class.size
{"width":54,"depth":478,"length":1254,"typeof":"rod"}

dict_class.size['width']
54

```
Prefered method to access nested data 

```
dict_class.size.get('width', None)
54
 ```
 
 ### Installation:
 
 You can install dictclass directly from github!
 
 pip install git+https://github.com/Constructionware/dictclass.git
 
 
 #### Cheers!
