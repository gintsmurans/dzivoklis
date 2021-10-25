Title: Hacking of the wordpress
Date: 2010-11-15 01:41
Category: Sākums
Tags: 2010
Lang: en

Some weeks ago one of the web servers started to fail. The website showed gateway timeout errors. Restarting all three services (nginx, mysql and php-fpm) did the trick for some days and then it started again. So I was wondering, what the .. ? After some research I found out that each php-fpm process takes 100 or more MB of memory and there were, well some 5 or 6 processes. At some point web server started to use a swap space and of course became unavailable. Disabling of all the extensions, I had added to php, made no changes, so it should be website it self. Disabling of some wordpress plugins made it a bit better and made me wonder.

Recently I discovered a really nice tool from Facebook - XHProf. It is something similar to webgrind, just more cooler. It shows information about called functions, memory consumptions, cpu execution times, etc.

So I thought lets take a wordpress and put it under XHProf. It just blow my mind away. It made somewhere around 70 000 function calls. Oh yeah baby.. Today I put a fresh copy of wordpress onto another host and gave it another shot. Without Latvian language pack it makes around of 8 000 function calls. Seems ok. But when I add those language packs it varies somewhere between 50 000 and 60 000 function calls.

This is because of wordpress implementation of .mo files. I have always thought it is not the best way for storing language strings. It can't be translated online, it is slow and it takes a lot of memory to load those mo files.

Recently I have developed a translation tool for some websites and I thought to give it a try. It actually requires a bit of hacking of the wordpress core files, what I know is not the best practice, but still a tryout would be nice. This tool stores translated strings into the database and then there is a php class file on production side that takes those strings out of database and caches in php files as arrays. Cache is refreshed: 1. if apc is enabled, the hash key of site and language is not found there, or 2. the hash key is not found in table `cache`.

Now running this setup XHProf show, that only 17 386 function calls are made, it runs faster and takes less memory and the main thing - you can translate your wordpress interface online. Still lot of function calls, although.

To make this work, I had to rewrite parts of l10n.php file in wp-includes. Wordpress also would be better, if it would use more arrays as parameters and avoid call_user_func_array at all. I also decreased process count to two, one for each user and with [nginx fastcgi caching][1]  turned on, it can handle approximately 6000 requests per second. Nice.

If you are more interested how I made this, please ask in the comments or by e-mail (gm (at) gm (dot) lv).

[1]: http://gm.lv/markup-test
