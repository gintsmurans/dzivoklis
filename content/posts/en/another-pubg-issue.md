Title: Another PUBG issue
Date: 2019-05-03 16:02
Category: Games
Tags: Games, Pubg
Lang: en

Update (2020-02-03): Brought some things up to date.

I have been "whining" on reddit about pubg issues for a while now, ~~and I think I finally figured it out.~~ - to be honest pubg is a weird game. I have been playing lot of COD:MW lately and some CS:GO too, and sometimes I win, sometimes I lose there, as it should be cosidering that I am quite average gamer here. But PUBG is an annoying nightmare, nothing works for me, I lose 95% of time even if its not an RNG case. Anyway the following is still relevant.

> _Take a look at my [other post]({filename}ultimate-guide-to-pubg-stuttering-issues.md) on how to get a better performance in Pubg._

**Lets start from the beginning?**

I put together a computer just for gaming around a year ago. At the time x299 chipset just came out and I thought - the newer, the better, so I bought Aorus Gaming 3, X299 + i5-7640x + HyperX FURY DDR4-2133 with some generic (shitty) PSU, RX550 GPU, generic mouse and keyboard, SSD, and upgraded stock cooler to a better one from Cooler Master.

First - the GPU - RX550 just couldn't handle anything more than CS GO, so after a while I got a chance to upgrade to a used 980ti and later got 1080 ti for free (nice).

While other games were fine, Pubg was not, I was constantly loosing, so I thought it must be something in the hardware and kept upgrading.

Started with the mouse and keyboard to ones from Steelseries - I am very happy with those. Next, PSU to corsair rm750x, because I was seeing some strange voltage drops in HWMonitor and, as the generic one once was on fumes (I know :)), I thought thats probably the case why I get stutterings. It wasn't.

Gave my ram away to a friend and upgraded to Crucial Ballistix Tactical DDR4-2666 - this actually improved framerates, but not the stuttering/delayed action feeling. Later on had a chance to upgrade to m.2 drive, which improved loading times, but not much more.

Then I thought about upgrading CPU, because clearly i5 was bottlenecking the GPU, but figured to start with OC'ing the i5. Before that I knew that current cooler is not gonna handle it, so that was upgraded to Corsair H115i PRO AIO cooler. Currently I am running i5-7640x at 5Ghz without any problems, only just upgraded one of the stock fan on H115i to Noctua nf-a14 industrialppc-2000, because temperatures sometimes went over 80 degrees. It is quite a lot louder, but thats ok. Did this solve stuttering / delayed action feeling - no, although pubg fps is now around 180 - 240fps, which is very good for pubg.

**Now the best part.** I had a 100Mbit optical internet from my provider and at some point I upgraded it to 250Mbit. One evening we were playing pubg and a friend of mine had already lost the game, was spectating me, while waiting. And he says something like: "He got you!". And when he was at the "He" part of the sentence, only then I saw, that I died in the game. Then I thought - **how the hell he saw that before me?** So I went investigating over google (again) and found out something called bufferbloat. It turns out, over very fast networks, network devices does a lot of data buffering, which can cause latency issues in realtime applications like fast paced games. So I searched for a network bufferbloat tester thing and found [this site](http://www.dslreports.com/speedtest) which additionally to speedtest, also tests for a bufferbloat. My router has this thing called QOS, where I can setup manual speed limit for a network device, so I did that. Tested speedtest from dslreports against various speed limits and found out that 50Mbit was the best one with A+ bufferbloat rating. Then I tried playing the game and it was like a night versus day kind of thing. Now I finally can pickup items while running, and I wouldn't die before seeing my opponents, etc. So this is after all those upgrades and 600+ hours on Pubg thinking I am so bad at this gaming stuff.

Although I had a suspicion that something is not ok with .. well .. something, it was so torturing thinking that I just suck at pubg, but still having this suspicion of something else to blame for that delayed action. Also I think my CSGO gameplay has improved a bit after this. So far Fornite seems to have the best impact of them all - I can finally land those shots, also far away ones, unlike before 85% (I am guessing here, but it was really bad) of all the shots would be missing the target. Haven't had a chance to play much of Apex, to tell anything about it.

Thats it.

> TL;DR: Too fast internet was causing delays while playing online fps games.
