# dictclass
Converts a python dictionary to a class object.

## Basic Usage

```
  data = dict(
       name='millamo',
       ref=49,
       height=145
       ) 
data_class = DictClass(data)
```


```
        
    data_class.name
    millamo

```

        """

            Nested Data:
            data = dict(
                name='millamo',
                ref=49,
                height=145
                size={"width":54,"depth":478,"length":1254,"typeof":"rod"}
            )
            data_class = DictClass(data)

         """
 
         """

            data_class.size
            {"width":54,"depth":478,"length":1254,"typeof":"rod"}

         """

   
