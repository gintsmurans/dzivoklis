Title: Finding a damn good wysiwyg editor
Date: 2010-08-19 01:08
Category: Sākums
Tags: 2010
Lang: en

I need to find a good wysiwyg editor for a project i'm currently working on. Here are my thoughts on some of the editors:

- [TinyMCE][1] : feature full editor, but it seems a bit messy with a lot of files. Implementing is also not very nice and friendly. Earlier I have experianced some problems validating html code.
- FCKEditor / [CKEditor][2] : Some years ago it was called FCKEditor, now I see that they have renamed it to CKEditor. I have used this one quite successfully. This is definitely better that TinyCME. Just downloaded the source code and I see that download package consists of 579 files. Wow! I need some simple wysiwyg editor, not this huge. And directory structure is really messed up.
- [markItUp][3] : 40 files - much better. Actually this is very interesting editor, althought it is not quite wysiwyg one. Judging from the example I have to replace "\n" to "&lt;br /&gt;" within my code. I don't want to do that. And also for average user html code will not be easy to handle. On other hand pasting documents from word and websites will end up with better results. It is also nice looking. So there are some pros and cons to consider.
- [jWYSIWYG][4] : So called jQuery wysiwyg editor. This one was my favourite for some time because of small footprint. It have only 3 files - js, css, and a gif file for a toolbar. Why I don't use it any more? Firstly it has a bad design. Next some features does not work very good on some browsers. There was some bug when slecting text in bold, toolbar do not show it is in bold. Also toolbar icons is somehow shifted. There was something else, I can't remeber now.
- [NicEdit][5] : They have nice website, also nice looking editor. This one I am currently using, but I'm searching for something else because there is no "html code" button as well as it cannot clean messy html code. And you can image what comes with when you copy something from the microsoft word. However this is really nice editor with small source - only two files - ideal if you need just some bold, italic text and some lists.
- [openWYSIWYG][6] : Didn't know about this one, so I gave it a try. 109 files in default archive. Quite much, but they seem good structured, not like Tiny and CK. From example I see, that it have table support, what does not have all those two files simple editors. Oh! It defines $ as shortcut to javascript "document.getElementById" function - this is bad, very bad, because I use $ to access jQuery. Ok, lets stop here: "openWYSIWYG does not support your browser" - I'm using google chrome. It seemed the good one... :(
- [FreeRichTextEditor][7] : Another rich text editor. This one has interesting switching between editor, html code and first one I see - Preview. It looks good, but not very good. But it also seems somehow left alone. It has only one version and author writes new posts twice a year.
- [jQuery RTE][8] , [HtmlBox][9] , [dsrte][10] , [WYMEditor][11] , [Xinha][12] , [htmlArea][13] , [TTW HTML][14] : I would choose none of these ones just because they have very bad designs and first impression about theire websites does it all even worse. Also I don't see any future for these ones.

Conclusion is that there is no prefect solution. Currently choices are:

1. feature full, but ugly
2. easy to use and implement, but feature less
3. nice looking and easy to implement, but not friendly for users
4. fully featured, but very heavy

By the way the best editor I have seen have wordpress and I see, that posterous is also using something similar. Maybe somebody knows if it can be downloaded separately?

*Note about WYSIWYM editors.*

I don't see where so called WYSIWYM (What You See Is What You Mean) editors could be handy, I would better use markup editor. If website admin is an average user, I guess he/she doesn't care if the text is in p tag, or div tag. One of these is [WYMEditor][15] . See example here: [http://files.wymeditor.org/wymeditor/trunk/src/examples/01-basic.html][16]

P.s. I am fan of jQuery, so I did leave out editors based on js libraries such as mootools, django, yahoo UI.

[1]: http://tinymce.moxiecode.com/
[2]: http://ckeditor.com/
[3]: http://markitup.jaysalvat.com/home/
[4]: http://code.google.com/p/jwysiwyg/
[5]: http://nicedit.com/
[6]: http://www.openwebware.com/
[7]: http://www.freerichtexteditor.com/
[8]: http://batiste.dosimple.ch/blog/2007-09/
[9]: http://remiya.com/cms/projects/jquery-plugins/htmlbox/
[10]: http://www.avidansoft.com/dsrte/index.php
[11]: http://www.wymeditor.org/demo/
[12]: http://xinha.webfactional.com/
[13]: http://www.htmlarea.com/
[14]: http://koivi.com/WYSIWYG-Editor/
[15]: http://www.wymeditor.org/demo/
[16]: http://files.wymeditor.org/wymeditor/trunk/src/examples/01-basic.html
