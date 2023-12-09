# By @romibi
# Enables taking control of other Entities in Scrapland
# Put this code into a decompiled quickconsole.py next to the Scrap.exe
# For example usage see https://www.youtube.com/watch?v=0d1OkaUR5YE
# An already decompiled and modified QuickConsole.py see the Scrapland Discord: https://discord.gg/3du3SyJWnY

import Scrap

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
	import Scrap
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
			import SAI
			SAI.SetStateVehicle(0, name)

def youFriend():
	makeFriendOrEnemy(you().Name)

def yourName():
	import Utils
	Utils.printConsole(you().Name)

def MakeShipAI(TypeShip = "SPoli1", Name="PlayerJoker", TypeEngine = "MPoli1", FactorDamageGetAway = 0.1, ControlStrafe = 2, ControlBrake = 0, ControlBoost = 1, StupidPathFinding = 0, MaxTimeStrafe = 4, MaxVelStrafe = 0.5, ControlAim = 3, CadenceShoot = 4, AngAttack = 0.785, FactorDamageItemLife = 0.25):
	import Vehicles
	import SVec
	global PlayerPos
	global PlayerAng
	global OffsetPos
	global OffsetPosNorm
	global Ang

	c = Scrap.GetEntity(Scrap.GetEntity(Scrap.GetCam(0)).Target)
	OffsetPos = 0,0,-1
	OffsetPos = SVec.Rotate3D(OffsetPos,c.Ang)
	OffsetPosNorm = SVec.Norm(OffsetPos)
	OffsetPos = SVec.Prod(OffsetPosNorm,1000)
	PlayerPos = SVec.Add(c.Pos,OffsetPos)

	PlayerAng = OffsetPosNorm
	Ang = SVec.GetRotAng(PlayerAng[0],PlayerAng[1],PlayerAng[2])
	PlayerAng = Ang[0],Ang[1],0
	PlayerAng = SVec.NormAng(PlayerAng[0]),SVec.NormAng(PlayerAng[1]),0

	o1            = Scrap.CreateEntity(Name, PlayerPos[0], PlayerPos[1], PlayerPos[2], "Car")
	Vehicles.SetStdProperties(o1.Name, TypeShip,"P_Police")
	o1.Descriptor = "Assasin"
	o1.TgType     = "killer"
	o1.Ang        = PlayerAng
	import SAI
	SAI.EnableAIVehicle(o1.Name, 1, FactorDamageGetAway, ControlStrafe, ControlBrake, ControlBoost, StupidPathFinding, MaxTimeStrafe, MaxVelStrafe, ControlAim, CadenceShoot, AngAttack, FactorDamageItemLife)

def createFriendOrEnemy(Name = "FriendPolice", TypeShip = "SPoli1", TypeEngine = "MPOLI1", AIProfile = "Rookie", list = "Friends"):
	import VehiclesNPC
	MakeShipAI(TypeShip, Name, TypeEngine)
	newFriend = Scrap.GetEntity(Name)
	newFriend.Descriptor = Name
	makeFriendOrEnemy(Name, list)
	pd = VehiclesNPC.GetIAProf(TypeShip)
	VehiclesNPC.SetAIProfile(pd, AIProfile)
	VehiclesNPC.ModAIProff(newFriend,pd)

