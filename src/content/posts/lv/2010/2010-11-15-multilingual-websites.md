Title: Multilingual websites
Date: 2010-11-15 04:36
Category: Sākums
Tags: 2010
Lang: en

Another topic I wanted to cover today is international websites.

When we are talking about translating content into another languages
in general we have to choose between two models:

- Content of the website is mirrored in each language or
- Each language have their specific website structure and contents

Both of models have their pros and cons and of course there can be
some adoptions of both of them. This post is more about the second
one.

I tried to find some good solution to create multilingual website and
found nothing useful. Then I tried to find some plugin for wordpress,
because the site, that needed translation is already on it. I found
[WPMU][1] . But it somehow doesn’t felt right to use it.
It does too much altering of database and I can only imagine how much
action hooks it has. You see, I like simple things out of the box, I
don’t like to hack things around, creating a big mess doing so.
Although, it doesn’t goes along with my last post, sometimes you have
to choose between two worst things.

Actually the last post comes very closely with this one. After
implanting the new translations system, I started to think: “It would
be nice to detect right languge before defining WPLANG, define it
afterward and give back content in that language.” I already had heard
about wordpress mu, but I somehow forgot it. Until I saw somewhere in
wordpress 3.0 roadmap, that is has been merged with wordpress. That
could do the trick. Wordpress codex have very well described how to
enable [multisite
wordpress][2] . Although it
is a bit tricky, specially if your blog already have a content.

I choosed to have subdirectory blogs, and now we have 3 of them:

 - / - for latvian
 - /en - for english
 - /ru - for russian

If I would want to store our default blog under /lv directory I would
create another wordpress site and import posts under it from the
default one, and of course create an redirect from / to /lv. Maybe we
will go this way, don’t know it yet. For now blogs haven’t been
translated yet. I could bet we will run in some problems later, but
for now it looks like a good solution for multilingual blogs. Far
better, than giving each language a new copy of wordpress.

To change interface language of the site, only modifications I had to
do is in wp-config.php file:

```php
  if (strpos($_SERVER['REQUEST_URI'], '/ru') !== FALSE)
    {
        define ('WPLANG', 'ru');
    }
    elseif (strpos($_SERVER['REQUEST_URI'], '/en') !== FALSE)
    {
        define ('WPLANG', 'en');
    }
    else
    {
        define ('WPLANG', 'lv');
    }
```

In general I don’t like wordpress (and I am saying it after all
this:), but it has been great if you need to get things done fast and
don’t worry much about performance, or worry a little bit of it.

[1]: http://wpmu.org/
[2]: http://codex.wordpress.org/Create_A_Network
