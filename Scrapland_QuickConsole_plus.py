# Enables taking control of other Entities in Scrapland
# Put this code into a decompiled quickconsole.py next to the Scrap.exe
# For example usage see https://www.youtube.com/watch?v=0d1OkaUR5YE
# An already decompiled and modified QuickConsole.py see the Scrapland Discord: https://discord.gg/3du3SyJWnY


def unfree():
	global FreeCam
	cam = Scrap.GetEntity(Scrap.GetCam(0))
	cam.FreeCam = 0
	Scrap.Set("FreeCameraCollide",1)
	SInput.Bind(0,"Walk","NextAction","")

def camTargetEntity(e = None):
	if e == None:
		return Scrap.GetEntity(Scrap.GetEntity(Scrap.GetCam(0)).Target)
	Scrap.GetEntity(Scrap.GetCam(0)).Target = e.Name
	return e

def me():
	camE = camTargetEntity()
	if camE.Type == "WalkChar":
		meE = Scrap.UsrEntity(0)
		if meE == None:
			meE = Scrap.GetEntity("Player0")
		if meE == None:
			meE = Scrap.GetEntity("PlayerZ")
		return meE
	if camE.Type == "Car":
		return Scrap.GetEntity("PlayerShip")

def you():
	shipname = ''
	camE = camTargetEntity()
	if camE.UsrControl < 0:
		return camE
	if camE.Type == "WalkChar":
		return Scrap.GetEntity(camE.SelectedEntity)
	if camE.Type == "Car":
		import SLogic
		return Scrap.GetEntity(SLogic.GetNearestShip(camE.Pos, shipname))

def imyou():
	camE = camTargetEntity();
	youE = you()
	if youE:
		camE.UsrControl = -1
		if camE.Name == youE.Name:
			me().UsrControl = -1
			unfree()
		youE.UsrControl = 0
		camTargetEntity(youE)

def imme():
	youE = camTargetEntity()
	youE.UsrControl = -1
	meE = me()
	meE.UsrControl = 0
	camTargetEntity(meE)

def makeFriendOrEnemy(name, list = "Friends"):
	if name:
		newFriend = Scrap.GetEntity(name)
		if newFriend:
			newFriend.EntityList = list
			SAI.SetStateVehicle(0, name)

def youFriend():
	makeFriendOrEnemy(you().Name)

def yourName():
	printConsole(you().Name)

def createFriendOrEnemy(Name = "FriendPolice", TypeShip = "SPoli1", TypeEngine = "MPOLI1", AIProfile = "Rookie", list = "Friends"):
	import VehiclesNPC
	MakeShipAI(TypeShip, Name, TypeEngine)
	newFriend = Scrap.GetEntity(Name)
	newFriend.Descriptor = Name
	makeFriendOrEnemy(Name, list)
	pd = VehiclesNPC.GetIAProf(TypeShip)
	VehiclesNPC.SetAIProfile(pd, AIProfile)
	VehiclesNPC.ModAIProff(newFriend,pd)

def printConsole(text = ''):
	debugBkg = Scrap.Get('debug')
	Scrap.Set('debug',2)
	print text
	Scrap.Set('debug',debugBkg)

def ev(code = "1+1"):
	if Scrap.Get('debug') < 2:
		Scrap.Set('debug',2)
	print "Called: "+code+":"
	try:
		print eval(code)
	except:
		try:
			exec(code)
			print "executed"
		except:
			print "that didn't work"