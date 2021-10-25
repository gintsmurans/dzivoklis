Title: Nginx caching by cookie
Date: 2010-10-05 06:18
Category: Sākums
Tags: 2010
Lang: en

For one website I am working on I wanted to configure nginx so that when user is not logged in, site is taken from nginx cache, but when user is logged in, the site is loading from wordpress directly. Because of performance, of course. :) And also I had an requirement from IT Risks of my organization that wp-admin is accessible only from our network.

Here is the configuration file for a virtual host:

```
  # www.domain.lv
server {
    listen       80 default;
    server_name  www.domain.lv;

    root /path_to_root;
    index index.php index.html;

    charset utf-8;
    error_page  404 /index.php;
    access_log  /path_to_log_file;


    location ~ (/\.ht) {
        return 404;
    }

    location / {
      if (-f $request_filename) {
        expires 30d;
        break;
      }

      try_files $uri $uri/ /index.php;
    }


    location ~ ^/__cached/.+\.php$ {
        if ($uri ~ ^/__cached/(.+\.php)$)
        {
            set $path /$1;
        }

        fastcgi_cache NAME;
        fastcgi_cache_valid any 5m;
        fastcgi_cache_key $document_root$request_uri;
        fastcgi_cache_use_stale error timeout invalid_header http_500;
        fastcgi_ignore_headers  Cache-Control  Expires;

        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root/$path;
        fastcgi_split_path_info ^(.+\.php)(.*)$;
        include        fastcgi_params;
    }


    location ~ (wp-(admin/.*|login|register)\.php$) {
        if ($remote_addr !~ xxx\.x\.xx\..+|xxx\.x\.xx\..+|xxx\.xxx\.xxx\..+){
            return 404;
        }

        if (!-f $request_filename) {
            return 404;
        }

        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }


    location ~ \.php$ {
        if (!-f $request_filename) {
            return 404;
        }

        if ($http_cookie !~ "wordpress_logged_in_.+")
        {
            rewrite (.+) /__cached$1 last;
        }

        fastcgi_pass   127.0.0.1:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
        fastcgi_split_path_info ^(.+\.php)(.*)$;
        include        fastcgi_params;
    }
}
```

Now what we have here?

When request to php file come in “location ~ .php$” handles it. If it sees that there is no cookie with a name “wordpress_logged_in_.+” it makes internal redirect to this location: “location ~ ^/**cached/.+.php$ {” which cuts off the “**cached” directory and loads the script from the cache.

To achieve IT Risk policy, requests to wp-admin, wp-login.php and wp-register.php is handled by “location ~ (wp-(admin/.*|login|register).php$) {” location and ip addreses restricted by this line: “if ($remote_addr !~ xxx.x.xx..+|xxx.x.xx..+|xxx.xxx.xxx..+){ return 404; }”.

Now it seems to me quite easy to understand, but it took all day to get to this. I guess there could be a better solution, but for now this works for me. :)
