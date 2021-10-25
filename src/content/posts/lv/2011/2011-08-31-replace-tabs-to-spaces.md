Title: Replace tabs to spaces
Date: 2011-08-31 09:55
Category: Sākums
Tags: 2011
Lang: en

```bash
find ./ -name *.php -exec sed -i 's/\t/ /g' {} \;
```

So I don't have to search for it again.
