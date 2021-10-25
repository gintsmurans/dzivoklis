Title: iPhone navigation back button
Date: 2011-03-25 06:59
Category: Sākums
Tags: 2011
Lang: en

It turns out, that navigation bar back button is set from parent controller that pushed new view controller. So if you want to hide back button you have to hide it in first view controller and then push the new one.

But if you have many places where you need to push new view controllers and have back button, but only one place where it needs to be set it is not very efficient to set it every time to not hidden. The solution is this code called from view controller pushed:

```Objective-C
[self.navigationController.parentViewController.navigationItem setHidesBackButton:YES];
```

Don't forget to show it when view disapears.

It also applies to custom back buttons - you have to apply it to first view controller, not the one is being pushed on.
