import random as ra
import os
import time as ti
a=['山上还有山','十张口，一颗心','说它小，下边大，说它大，上边小',
   '一只黑狗，不叫不吼','差一点六斤','家中添一口','自小在一起，目前少联系',
   '点点成金','一人一张口，下面长只手','四面都是山,山山都相连','种花要除草,一人来一刀',
   '存心不让出大门,你说烦人不烦人','一只狗，两个口，谁遇它谁发愁',
   '格外大方','七十二小时','需要一半,留下一半','综合门市','守门员',
   '半青半紫','一口吃掉牛尾巴','一大二小','一月七日','人不在其位',
   '刀出鞘','十二点','十个哥哥','上下难分','文武两全','水上工程',
   '半个月亮','打断念头','多一半','春风吹又生','王先生在石头上',
   '挥手告别','推开又来','半字写下','此字只一个，二字边下躲','曰字加竖不加点',
   '一口分两家','二口在下下','三口叠罗汉']
b=['出','思','尖','默','兵','豪','省','全','拿','田','化',
   '闷','哭','回','晶','雷','闹','闪','素','告','奈','脂',
   '立','力','斗','克','卡','斌','汞','胖','心','夕','薪',
   '碧','军','摊','干','些','神','日','吕','品']
print("初始化中......|-|-|-|-")
cml=os.listdir("c:/")
if not ("猜字谜" in cml):
	os.mkdir("c:/猜字谜")
fill=open('c:/猜字谜/scrores.txt','a+',encoding='utf-8')
clist=os.listdir("C:/猜字谜")
if ("答案.txt" in clist) and ("题目.txt" in clist):
	nd=open('c:/猜字谜/答案.txt','a+',encoding='utf-8')
	nt=open('c:/猜字谜/题目.txt','a+',encoding='utf-8')
	nd.seek(0)
	nt.seek(0)
	nt1=nt.read()
	nt=nt1.split("-")
	nd1=nd.read()
	nd=nd1.split("-")
	if nt[len(nt)-1]=="":
		nt.pop(len(nt)-1)
	if nd[len(nd)-1]=="":
		nd.pop(len(nd)-1)
	for i in range(len(nd)):
		a.append(nt[i])
		b.append(nd[i])
d=len(a)
little=["BBBBBBBBBBBBBBBBBB......","Fuck You","As seen on TV!","Awesome!","100% pure!","May contain nuts!","More polygons!","Moderately attractive!","Limited edition!","Flashing letters!","It's here!","Best in class!","It's finished!","Kind of dragon free!",
		"Excitement!","More than 500 sold!","One of a kind!","Heaps of hits on YouTube!","Indev!","Spiders everywhere!","Check it out!","Holy cow, man!","It's a game!","Made in Sweden!","Uses LWJGL!","Reticulating splines!",
		"Minecraft!","Yaaay!","Singleplayer!","Keyboard compatible!","Ingots!","Exploding creepers!","That's no moon!","l33t!","Create!","Survive!","Dungeon!","Exclusive!","The bee's knees!","Closed source!","Classy!","Wow!",
		"Not on steam!","Oh man!","Awesome community!","Pixels!","Teetsuuuuoooo!","Kaaneeeedaaaa!","Now with difficulty!","Enhanced!","90 bug free!","Pretty!","12 herbs and spices!","Fat free!","Absolutely no memes!",
		"Free dental!","Ask your doctor!","Minors welcome!","Cloud computing!","Legal in Finland!","Hard to label!","Technically good!","Bringing home the bacon!","Indie!","GOTY!","Ceci n'est pas une title screen!",
		"Euclidian!","Now in 3D!","Inspirational!","Herregud!","Complex cellular automata!","Yes, sir!","Played by cowboys!","Now on OpenGL 3.2 core profile!","Thousands of colors!","Try it!","Age of Wonders is better!",
		"Try the mushroom stew!","Sensational!","Hot tamale, hot hot tamale!","Play him off, keyboard cat!","Guaranteed!","Macroscopic!","Bring it on!","Random splash!","Call your mother!","Monster infighting!","Loved by millions!",
		"Ultimate edition!","Freaky!","You've got a brand new key!","Water proof!","Uninflammable!","Whoa, dude!","All inclusive!","Tell your friends!","NP is not in P!","Music by C418!","Livestreamed!","Haunted!","Polynomial!",
		"Terrestrial!","All is full of love!","Full of stars!","Scientific!","Not as cool as Spock!","Collaborate and listen!","Never dig down!","Take frequent breaks!","Not linear!","Han shot first!","Nice to meet you!",
		"Buckets of lava!","Ride the pig!","Larger than Earth!","sqrt(-1) love you!","Phobos anomaly!","Punching wood!","Falling off cliffs!","1 sugar!","150% hyperbole!","Synecdoche!","Let's danec!","Seecret Friday update!",
		"Reference implementation!","Kiss the sky!","20 GOTO 10!","Verlet integration!","Peter Griffin!","Do not distribute!","Cogito ergo sum!","4815162342 lines of code!","A skeleton popped out!","The sum of its parts!",
		"BTAF used to be good!","I miss ADOM!","umop-apisdn!","OICU812!","Bring me Ray Cokes!","Finger-licking!","Thematic!","Pneumatic!","Sublime!","Octagonal!","Une baguette!","Gargamel plays it!","Rita is the new top dog!",
		"SWM forever!","Representing Edsbyn!","Matt Damon!","Supercalifragilisticexpialidocious!","Consummate V's!","Cow Tools!","Double buffered!","Fan fiction!","Flaxkikare!","Jason!Jason!Jason!","Hotter than the sun!",
		"Internet enabled!","Autonomous!","Engage!","Fantasy!","DRR!DRR!DRR!","Kick it root down!","Regional resources!","Woo, facepunch!","Woo, somethingawful!","Woo, tigsource!","Woo, worldofminecraft!","Woo, reddit!",
		"Woo, 2pp!","Google anlyticsed!","Now supports åäö!","Give us Gordon!","Tip your waiter!","Very fun!","12345 is a bad password!","Vote for net neutrality!","Lives in a pineapple under the sea!","MAP11 has two names!",
		"Omnipotent!","Gasp!","...!","Bees, bees, bees, bees!","Jag känner en bot!","This text is hard to read if you play the game at the default resolution, but at 1080p it's fine!","Haha, LOL!","Hampsterdance!","Menger sponge!",
		"idspispopd!","Eple (original edit)!","So fresh, so clean!","Slow acting portals!","Try the Nether!","Don't look directly at the bugs!","Oh, ok, Pigmen!","Finally with ladders!","Scary!","Play Minecraft, Watch Topgear, Get Pig!",
		"Twittered about!","Jump up, jump up, and get down!","Joel is neat!","A riddle, wrapped in a mystery!","This parrot is no more!","It has ceased to be!","Welcome to your Doom!","Stay a while, stay forever!","Stay a while and listen!",
		"Treatment for your rash!","Autological"," is!","Information wants to be free!","Almost never"," is an interesting concept!","Lots of truthiness!","The creeper is a spy!","Turing complete!","It's groundbreaking!",
		"Let our battle's begin!","The sky is the limit!","Jeb has amazing hair!","Ryan also has amazing hair!","Casual gaming!","Undefeated!","Kinda like Lemmings!","Follow the train, CJ!","Leveraging synergy!","This message will never appear on the splash screen, isn't that weird?",
		"DungeonQuest is unfair!","90210!","Check out the far lands!","Tyrion would love it!","Also try VVVVVV!","Also try Super Meat Boy!","Also try Terraria!","Also try Mount And Blade!","Also try Project Zomboid!","Also try World of Goo!",
		"Also try Limbo!","Also try Pixeljunk Shooter!","Also try Braid!","That's super!","Bread is pain!","Read more books!","Khaaaaaaaaan!","Less addictive than TV Tropes!","More addictive than lemonade!","Bigger than a bread box!",
		"Millions of peaches!","Fnord!","This is my true form!","Don't bother with the clones!","Pumpkinhead!","Made by Jeb!","Has an ending!","Finally complete!","Feature packed!","Boots with the fur!","Stop, hammertime!",
		"Testificates!","Conventional!","Homeomorphic to a 3-sphere!","Doesn't avoid double negatives!","Place ALL the blocks!","Does barrel rolls!","Meeting expectations!","PC gaming since 1873!","Ghoughpteighbteau tchoghs!",
		"Déjà vu!","Déjà vu!","Got your nose!","Haley loves Elan!","Afraid of the big, black bat!","Doesn't use the U-word!","Child's play!","See you next Friday or so!","From the streets of Södermalm!","150 bpm for 400000 minutes!",
		"Technologic!","Funk soul brother!","Pumpa kungen!","日本是SBハロー！","한국 안녕하세요!","Helo Cymru!","Cześć Polsko!","你好中国！","Γεια σου Ελλάδα!","My life for Aiur!","Lennart lennart = new Lennart();","I see your vocabulary has improved!",
		"Who put it there?","You can't explain that!","if not ok then return end","§1C§2o§3l§4o§5r§6m§7a§8t§9i§ac","§kFUNKY LOL","Big Pointy Teeth!","Bekarton guards the gate!","Mmmph, mmph!","Don't feed avocados to parrots!",
		"Swords for everyone!","Plz reply to my tweet!",".party()!","Take her pillow!","Put that cookie down!","Pretty scary!","I have a suggestion.","Now with extra hugs!","Java 16 + 1 = 17!","Woah.","HURNERJSGER?","What's up, Doc?",
		"Now contains 32 random daily cats!","That's Numberwang!","pls rt","Do you want to join my server?","Put a little fence around it!","Throw a blanket over it!","One day, somewhere in the future, my work will be quoted!",
		"Too strong for this dream. To tell them how to live is to prevent them living.I will not tell the player how to live.  The player is growing restless.  I will tell the player a story.But not the truth.  No. A story that contains the truth safely, in a cage of words.  Not the naked truth that can burn over any distance.Give it a body, again. Yes. Player...Use its name.  PLAYERNAME. Player of games.  Good."]
print("初始化完成")
print("猜字谜Build:1.8,库存量:"+str(d),end="个\n")
print("------"+ra.choice(little)+"------",end="\n\n")
print("loading,plese wait......")
ti.sleep(18)
os.system("cls")
s=input("你要直接玩还是先加入自己的字谜？1为直接玩，2为自己单次加字谜，3为自己历史性添加字谜:")
if s!="1" and s!="2" and s!="3":
	print("请输入1,2,3中的一个选项!!!")
	ti.sleep(2)
	fill.close()
	os._exit(1)
elif s=="2":
	z=0
	while z!="5":
		while True:
			z=input("输5退出，或输入字谜：")
			if z=="":
				print("字谜不能为空，请重新输入")
			else:				
				if z!="5":
					while True:
						x=input("答案:")
						if x=="":
							print("答案不能为空，请重新输入")
						else:
							a.append(z)
							b.append(x)
							d=d+1
							print("现有库存:"+str(d))
							break						
				else:
					print("现有库存:"+str(d))
					print("退出中......")
					os.system("cls")
					break
elif s=="3":
	print("手动录入方法：请打开系统盘下的猜字谜文件\n夹后将字谜保存在“题目.txt”，用\n“-”分隔，以相同顺序与方法在同一目录创建\n“答案.txt”写入答案，分隔符一样，请按你输\n字谜的顺序输答案。")
	print("自动输入中！")
	nd=open('c:/猜字谜/答案.txt','a+',encoding='utf-8')
	nt=open('c:/猜字谜/题目.txt','a+',encoding='utf-8')
	z=0
	while z!="5":
		while True:
			z=input("输5退出，或输入字谜：")
			if z=="":
				print("字谜不能为空，请重新输入")
			else:				
				if z!="5":
					while True:
						x=input("答案:")
						if x=="":
							print("答案不能为空，请重新输入")
						else:
							nt.write(z+"-")
							nd.write(x+"-")
							break						
				else:
					print("退出中......")
					break
	nt.close()
	nd.close()
	ti.sleep(5)
	fill.close()
	os._exit(1)
while True:
	c=int(input("你要猜几个?"))
	if c>d:
		print("请少猜一点")
	else:
		break
g=0
h=0
for i in range(c):
	e=ra.randint(0,d-1)
	while True:
		f=input("字谜："+a[e]+"你猜谜底是什么?")
		if f=="":
			print("答案不能为空，请重新输入")
		else:
			break
	if f==b[e]:
		print("你答对了！")
		a.pop(e)
		b.pop(e)
		g+=1
		d-=1
	else:
		print("你答错了！答案是："+b[e])
		a.pop(e)
		b.pop(e)
		h+=1
		d-=1
print("总共：{}个,对了{}个,错了{}个".format(c,g,h))
n=fill.tell()
fill.seek(0)
res = len(fill.readlines())+1
fill.seek(n)
fill.write("闯关时间:"+ti.strftime("%F(YYYY-MM-DD) %A %H:%M:%S")+"    为总次数的第{}次,总共{}个,对了{}个,错了{}个!!".format(res,c,g,h)+"\n")
fill.seek(0)
print(fill.read())
endd=input("按Enter退出,输DelHis删除历史成绩并退出:")
fill.close()
if(endd=="DelHis"):
	file=open('c:/猜字谜/scrores.txt','w',encoding='utf-8')
	file.write("")
	print("删除成功！！！")
print("彩蛋")
ti.sleep(2)
for i in range(10):
	os.system("cls")
	print("鸡你太美！！！！")
	print("陈建凯最帅！！！！")
	print("python咸猪手欢迎你使用！！！！")
	print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB......")
	print("《最恐怖的六一》")
	print("《实用的Crafter方块》")
	print("《前方高能!!!》")
	print(ra.choice(little))
	print(ra.choice(little))
	print(ra.choice(little))
	print(ra.choice(little))
	ti.sleep(5)
os.system("cls")
print("exting......")
ti.sleep(1)