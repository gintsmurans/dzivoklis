Title: Ultimate guide to solve PUBG stuttering issues
Date: 2018-11-20 17:46
Category: Games
Tags: Games, Pubg
Lang: en

* Update (2020-02-03): Brought some things up to date.
* Update (2019-05-03): Few typo and speeling fixes.

So I have been fighting with fps drops and stuttering issues for quite a while now, and I have a decent system. Here is what I have found. This guide is for nvidia with a better GPU than CPU (apparently that stuff matters), and most probably won't work for everyone, but you can find ideas to increase performance.

1. Avoid hdd, go for ssd or even better M.2 NMVE drive. Last one loads games, and system it self, million times faster.
2. Go for performance middle ground. For example, download OpenHardwareMonitor, check that CPU and GPU utilisation is somewhat consistent. Later on that.
3. Make sure you have a decent mouse and keyboard, especially mouse. <s>Upgrading generic mouse to SteelSeries Rival was like a day versus night for me.</s> Switched to Logitech G305 and don't want to look back.
4. If it is an option for you, go for a 144Hz monitor. Even if your computer can handle only 90fps, its still a lot better than 60Hz. Also if your PC can handle it, just go with [240hz](https://www.youtube.com/watch?v=OX31kZbAXsA).
5. Turn off the G-Sync and V-Sync, it does make the game to look quite a bit smoother, but if you want maximum performance, I suggest turning it off. Also Fast sync may improve the looks but performance is somewhat limited. Yes I know its just 1 frame difference, but we are aiming for performance here.
6. Always use Fullscreen mode, without windows. It drains CPU a LOT.
7. Setup page file. Here is one example how to do it: [Page File Setup](https://www.geeksinphoenix.com/blog/post/2016/05/10/how-to-manage-windows-10-virtual-memory.aspx). Set same Initial size and Maximum size. If you have 4GB - don't play this game. If you have 8GB, set it to 4069 - no point setting it any larger.
8. Make sure your power settings are set to Maximum performance.
9. Also make sure you set texture filtering in nvidia control panel to performance, it will look worse, but as it turns out this greatly impacts fps drops and stuttering when tested 1% and 0.1% fps lows.
10. Usually you would think the bigger is better, but, as it turns out, thats not the case with mouse and keyboard polling rates. Decreasing polling rate from 1000hz to 500hz (I did it on both - mouse and keyboard) seems to be the single most effective way that reduced lagging feeling for me. I think what is happening here is that when a mouse is constantly sending movement updates at 1kHz, my cpu (or game?) couldn't handle it, thats why when I was clicking mouse buttons, they always felt like a bit delayed. At first I thought it is monitor being at 60Hz. After getting 144Hz monitor, I thought it is cpu, that cannot handle video processing. After smoothing fps out, I thought its nvidia settings. After tweaking those, I thought it is a buggy ssd, after upgrading ssd to m.2 it actually seemed better. Who knows. Then somebody on reddit suggested to look into mouse polling rate, and turns out that was the issue. Before this change I had set fps limit to 94, but in-game it was around 88-90. After changing polling rate it is now quite steady at 94. **This only applies if you have weaker or older CPU** - I have since then bought a new cpu and it is working same on both 500hz and 1000hz.

**GPU vs CPU**

This is also a big one. If you have a good GPU, but not so good CPU, and no limit on fps and graphics settings on the low side, you will notice stuttering, lagging, ping drops, etc. Thats because GPU says: I'm ready, give me more, but CPU cannot give more, because it is at 100%. If thats the case, you should either lower fps or give more work to the GPU, so it cannot handle so many frames. I went the first way and found that my CPU can handle 94fps, leaving room for system it self (background processes, networking, etc). Maybe it could do a bit more, but don't think I would gain much more with this cpu.
If you cannot get stable 60fps, most probably kills are gonna be hard to get. Sneaking around is still an option, though. :D
To figure out what CPU I would need I used this [site](https://pc-builds.com/calculator/). <s>But it looks like its not working at the moment.</s>

**NVidia Settings**

Click second mouse button on Desktop -> NVIDIA Control Panel -> Manage 3d Settings.
Global settings:

![GlobalSettings]({static}/images/pubg/nvidia-global-settings.png)

**Pubg specific settings**

![PubgSettings]({static}/images/pubg/nvidia-pubg-settings.png)

* One thing to mention, I am setting preferred refresh rate & maximum pre-rendered frames (suggested is to set it to 1) to application controlled, so it self figures out what it needs.

**G-Sync off**

![GSync]({static}/images/pubg/nvidia-gsync.png)

**Refresh Rate**
If your screen feels like 60hz, but you have a monitor that can do more, make sure its correctly set in nvidia settings:

![RefreshRate]({static}/images/pubg/nvidia-refresh-rate.png)


**In-Game settings**

![InGame]({static}/images/pubg/in-game-settings.png)

- AA - High caused a bit more fps drops, so I went with Medium. I wouldn't set it to Low, because it starts to look bad below Medium
- PP - Same as AA
- Shadows - Always Very Low
- Textures - Ultra puts more stress on GPU than on CPU. I'm not sure, but I guess choosing anything below Ultra does some scaling or additional loading or something that puts more strain on CPU.
- Effects - No need for them.
- Foliage - Same
- View distance - this is interesting one. It seems to put more stress on cpu, but setting it to low causes weird rendering when zooming - stuff is appearing when you scope, and gets lost when not scoping. Thats why I am choosing Medium here for it to be not so noticeable.
- You don't need rest of the settings.

**Open Hardware Monitor**

![OHWM]({static}/images/pubg/open-hw-monitor.png)

* Update settings until you get somewhat consistent GPU and CPU utilisation
