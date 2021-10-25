Title: MongoDB finding max value
Date: 2010-08-03 23:11
Category: Sākums
Tags: 2010
Lang: en

Hi,Recently I have started to learn some new stuff. One of them is MongoDB so called “NoSQL” database.What I have learned is that mongoDB is very simple. Running MongoDB and installation of PHP extension for it, took only some 10 minutes. Then fast overview of some source code at php.net manual and we are good to go. If you have some earlier experience with javascript and databases like MySQL, you shouldn’t have any problems with MongoDB. This morning I started to migrate table from MySQL to Mongo and did a mistake. I changed table in MySQL query but did not changed it in Mongo insert. So what I had was two tables in one Mongo collection.Fortunately those tables has some fields that are not in other table, so I came up with this code:

```php
self::$mdb->i18n->remove(array(':where' => new mongoCode('return (this.parent == 0 || this.parent > 0) && typeof this.last_access == "undefined";')));
```

Where “self::$mdb” is reference to php MongoDB object. I guess: “typeof this.last_access == "undefined”;“ would be just fine, either, but I used "this.parent” for double checking. Another problem with Mongo is to get max value of some field, so I decided to paste a code here to also remember this one if in case I need it someday. It finds max value of field “id” in collection “countries”.

```php
  $max_id = self::$mdb->execute(new mongoCode('
    find_max = [];
    db.properties.find([], {id : 1}).map(function(item){
        if (item.id)
        {
            find_max.push(parseFloat(item.id));
        }
    });
    return Math.max.apply(Math, find_max);
'));

print_r($max_id['retval']);
```

It is pure JavaScript inside of Mongo, so if you know javascript getting advanced stuff out of Mongo should be very easy for you.
