Webhose API Image Search
============================
#### Access image metadata and labels using the Webhose API image recognition feature

#### Demo Page:
https://webhose.io/cool-stuff/visual-search-demo/


##### Basic Example:
```python

    from webhose_api_image_search import ImageSearch
    
    image_search = ImageSearch(<YOUR_API_KEY>)
    images = image_search.get_images('brown bear')
    
    current_image = images[0]
    
    print current_image.thread_title
    print current_image.thread_url
    print ', '.join(current_image.labels)

```

Output:
```text
    Old Faithful - Yellowstone
    https://www.tripadvisor.com/ShowTopic-g60999-i481-k12501338-Old_Faithful-Yellowstone_National_Park_Wyoming.html
    Brown bear, Mammal, Wildlife, Animal, Bear
```

##### Perform an extra API call to get meta info in depth

```python
    meta_info = current_image.get_meta_info()
    
    print meta_info['mime_type']
    print '%s x %s pix.' % (meta_info['width'], meta_info['height'])

```

Output:
```text
    JPEG
    550 x 367 pix.
```

API Key
-------

To make use of the webhose.io API, you need to obtain a token that would be
used on every request. To obtain an API key, create an account at
https://webhose.io/auth/signup, and then go into
https://webhose.io/dashboard to see your token.


Installing
----------
You can install from source:

``` bash

    $ git clone https://github.com/Webhose/webhose-api-image-search
    $ cd webhose-api-image-search
    $ python setup.py install
    
 ```
 
