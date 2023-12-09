
import Scrap

# Below maxgpu function is created by olokos and meant to more easily change some graphical related settings by easy switches
# /maxgpu 0 - fully revert all including testing to default
# /maxgpu 1 - revert to default but keep testing enabled
# /maxgpu 2 - enable improved graphics
# /maxgpu 3 - increase animation interpolation also
# /maxgpu 4 - enable testing layouts

# feel free to replace R._LightLimit and the value next to it with different values

def maxgpu(parameter):
	if parameter is 0:	# fully revert all to original game values
		Scrap.Set('R_LightLimit', 4)	# Max. enabled lights per model (0..6) def. 4
		Scrap.Set('MipmapColor', 0)		# Colorize each mipmap level (0/1) def. 0
		Scrap.Set('MipmapFade', 0)		# Fadeout each mipmap level (0/1) def. 0
		Scrap.Set('SharpenMore', 0)		# Extra sharpen for each mipmap level (0/1) def. 0
		# Scrap.Set('TextureLOD',0)		# Most detailed mipmap level used (0=disable) def. 0
		Scrap.Set('DUDVMipmap', 1)		# Allow mipmapping for DUDV textures (0/1) def. 1
		Scrap.Set('BumpMipmap', 0)		# Allow mipmapping for bump textures (0/1) def. 0
		Scrap.Set('BuildDDS', 0)		# Build DDS Textures (0/1) def. 0
		Scrap.Set('ModelAmbient', 0)	# Extra ambient light for models (def. 0)
		Scrap.Set('RenderLightmap', 1)	# Render lightmap mode (0/1/2) def. 1
		Scrap.Set('MatEmissive', 0)		# Extra amount of emissive lighting (def. 0.000000)

		#Also restoring testing values
		Scrap.Set('ShowMapWireFrame',0)		# Show map wireframe mode (0/1/2) def. 0
		Scrap.Set('R_SkipAnimInterp',0)		# Disable interpolation between animations (0/1) def. 0
		Scrap.Set('R_SkipUpdateVis',0)		# Skip model visibility test (0/1) def. 0
		Scrap.Set('R_ModelFastIsVis',1)		# Use FastIsVisible for model visibility pre-test (0/1/2) def. 1
		Scrap.Set('R_ModelPortalVis',1)		# Use portals for model visibility test (0/1) def. 1
		Scrap.Set('R_ShowModelSector',0)	# Show model sector (0/1/2) def. 0
		Scrap.Set('R_ShowModelLights',0)	# Show model lights (0/1/2) def. 0
		Scrap.Set('R_ShowModelPos',0)		# Show model position (0/1/2) def. 0
		Scrap.Set('R_ShowModelBox',0)		# Show model bounding box (0/1/2/3) def. 0

		printConsole("Fully reverted all settings back to original! \n")

	if parameter is 1:	# revert to default without removing testing
		Scrap.Set('R_LightLimit', 4)	# Max. enabled lights per model (0..6) def. 4
		Scrap.Set('MipmapColor', 0)		# Colorize each mipmap level (0/1) def. 0
		Scrap.Set('MipmapFade', 0)		# Fadeout each mipmap level (0/1) def. 0
		Scrap.Set('SharpenMore', 0)		# Extra sharpen for each mipmap level (0/1) def. 0
		# Scrap.Set('TextureLOD',0)		# Most detailed mipmap level used (0=disable) def. 0
		Scrap.Set('DUDVMipmap', 1)		# Allow mipmapping for DUDV textures (0/1) def. 1
		Scrap.Set('BumpMipmap', 0)		# Allow mipmapping for bump textures (0/1) def. 0
		Scrap.Set('BuildDDS', 0)		# Build DDS Textures (0/1) def. 0
		Scrap.Set('ModelAmbient', 0)	# Extra ambient light for models (def. 0)
		Scrap.Set('RenderLightmap', 1)	# Render lightmap mode (0/1/2) def. 1
		Scrap.Set('MatEmissive', 0)		# Extra amount of emissive lighting (def. 0.000000)

		printConsole("Fully reverted settings back to original, without touching testing! \n")

	if parameter is 2:	# improved graphics
		Scrap.Set('R_LightLimit',6)			# Max. enabled lights per model (0..6) def. 4
		Scrap.Set('MipmapColor',1)			# Colorize each mipmap level (0/1) def. 0
		Scrap.Set('MipmapFade',1)			# Fadeout each mipmap level (0/1) def. 0
		Scrap.Set('SharpenMore',1)			# Extra sharpen for each mipmap level (0/1) def. 0
		Scrap.Set('DUDVMipmap',1)			# Allow mipmapping for DUDV textures (0/1) def. 1
		Scrap.Set('BumpMipmap',1)			# Allow mipmapping for bump textures (0/1) def. 0
		Scrap.Set('BuildDDS',1)				# Build DDS Textures (0/1) def. 0
		#Scrap.Set('TextureLOD',0)			# Most detailed mipmap level used (0=disable) def. 0
		#Scrap.Set('ModelAmbient',0)		# Extra ambient light for models (def. 0) # setting to 1 removes it, -1 is fullbright
		#Scrap.Set('RenderLightmap',1)		# Render lightmap mode (0/1/2) def. 1
		#Scrap.Set('MatEmissive',1)			# Extra amount of emissive lighting (def. 0.000000) #too bright

		printConsole("Applied improved graphics! \n")

	if parameter is 3:	# some small animation changes
		Scrap.Set('R_AnimInterpMult',2)		# Multiplier of interpolation between animations def. 1.000000

		printConsole("Applied animation interp mult 2! \n")

	if parameter is 4:	# testing
		Scrap.Set('ShowMapWireFrame', 2)		# Show map wireframe mode (0/1/2) def. 0
		Scrap.Set('R_SkipAnimInterp', 1)		# Disable interpolation between animations (0/1) def. 0
		#Scrap.Set('R_SkipUpdateVis', 1)		# Skip model visibility test (0/1) def. 0
		Scrap.Set('R_ModelFastIsVis', 0)		# Use FastIsVisible for model visibility pre-test (0/1/2) def. 1
		Scrap.Set('R_ModelPortalVis', 0)		# Use portals for model visibility test (0/1) def. 1
		#Scrap.Set('R_ShowModelSector', 2)		# Show model sector (0/1/2) def. 0
		#Scrap.Set('R_ShowModelLights', 2)		# Show model lights (0/1/2) def. 0
		#Scrap.Set('R_ShowModelPos', 3)		# Show model position (0/1/2) def. 0
		Scrap.Set('R_ShowModelBox', 1)		# Show model bounding box (0/1/2/3) def. 0

		printConsole("Applied testing variables! \n")
