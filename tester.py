blak = Color3.new(0,0,0)
blue = Color3.new(0/255,0/255,255/255)
tef = "SourceSans"
whit = Color3.new(255/255,255/255,255/255)
local cka = Instance.new("ScreenGui")
cka.Name= "PenguinGui"
cka.ResetOnSpawn = false
cka.DisplayOrder = 1024
cka.Parent = game.Players./localplayer/.PlayerGui
local ckaframe = Instance.new("Frame", cka)
ckaframe.Name = "CkaFrame"
ckaframe.Position = UDim2.new(0,0,0.3,0)
ckaframe.Size = UDim2.new(0,0,0,0)
pcall(function() game.InsertService:LoadAsset(92669856136915):GetChildren()[1].Parent = ckaframe end)
local frame = Instance.new("Frame")
frame.Parent = ckaframe
frame.BackgroundColor3 = blak
frame.BorderColor3 = blue
frame.BorderSizePixel = 3
frame.Name = "Frame"
frame.Position = UDim2.new(0,3,0.3,0)
frame.Size = UDim2.new(0,300,0,400)
local pges = Instance.new("Frame")
pges.Parent = frame
pges.BackgroundColor3 = blak
pges.BorderColor3 = blue
pges.BorderSizePixel = 3
pges.Name = "Pages"
pges.Position = UDim2.new(0,0,0,0)
pges.Size = UDim2.new(1,0,1,0)
local cope = Instance.new("TextButton")
cope.Parent = ckaframe
cope.Active = true
cope.AutoButtonColor = true
cope.BackgroundColor3 = blak
cope.BorderColor3 = blue
cope.BorderSizePixel = 3
cope.Name = "Close/Open"
cope.Position = UDim2.new(0,3,0.3,380)
cope.Selectable = true
cope.Size = UDim2.new(0,300,0,20)
cope.ZIndex = 3
cope.Font = "SourceSans"
cope.FontSize = "Size18"
cope.Text = "Close"
cope.TextColor3 = Color3.new(255,255,255)
cope.TextXAlignment = "Center"
cope.TextYAlignment = "Center"
cope.MouseButton1Down:connect(function()
	if cope.Text == "Close" then
		frame.Visible = false
		cope.Text = "Open" else
		frame.Visible = true
		cope.Text = "Close"	
	end	
end)
local page1 = Instance.new("Frame")
page1.Parent = pges	
page1.BackgroundColor3 = blak
page1.BorderColor3 = blue
page1.BorderSizePixel = 3
page1.Name = "Page1"
page1.Position = UDim2.new(0,0,0,83)
page1.Size = UDim2.new(1,0,1,-106)
page1.ZIndex = 2
page1.Visible = true
local page2 = Instance.new("Frame")
page2.Parent = pges
page2.BackgroundColor3 = blak
page2.BorderColor3 = blue
page2.BorderSizePixel = 3
page2.Name = "Page2"
page2.Position = UDim2.new(0,0,0,83)
page2.Size = UDim2.new(1,0,1,-106)
page2.ZIndex = 2
page2.Visible = false
local page3 = Instance.new("Frame")
page3.Parent = pges
page3.BackgroundColor3 = blak
page3.BorderColor3 = blue
page3.BorderSizePixel = 3
page3.Name = "Page3"
page3.Position = UDim2.new(0,0,0,83)
page3.Size = UDim2.new(1,0,1,-106)
page3.ZIndex = 2
page3.Visible = false
local page4 = Instance.new("Frame")
page4.Parent = pges
page4.BackgroundColor3 = blak
page4.BorderColor3 = blue
page4.BorderSizePixel = 3
page4.Name = "Page4"
page4.Position = UDim2.new(0,0,0,83)
page4.Size = UDim2.new(1,0,1,-106)
page4.ZIndex = 2
page4.Visible = false
local page5 = Instance.new("Frame")
page5.Parent = pges
page5.BackgroundColor3 = blak
page5.BorderColor3 = blue
page5.BorderSizePixel = 3
page5.Name = "Page5"
page5.Position = UDim2.new(0,0,0,83)
page5.Size = UDim2.new(1,0,1,-106)
page5.ZIndex = 2
page5.Visible = false
page = Instance.new("Frame")
page.Parent = frame
page.BackgroundColor3 = blak
page.BorderColor3 = blue
page.BorderSizePixel = 3
page.Name = "Settings"
page.Position = UDim2.new(1,3,0,0)
page.Size = UDim2.new(1,0,1,0)
page.ZIndex = 1
page.Visible = true
right = Instance.new("TextButton")
right.Parent = frame	
right.BackgroundColor3 = blak
right.BorderColor3 = blue
right.BorderSizePixel = 3
right.Name = ">"
right.Position = UDim2.new(0.5,3,0,40)
right.Size = UDim2.new(0.5,-3,0,40)
right.ZIndex = 2
right.Font = tef
right.FontSize = "Size48"
right.Text = ">"
right.TextColor3 = whit
addonr = Instance.new("TextButton")
addonr.Parent = page5	
addonr.BackgroundColor3 = blak
addonr.BorderColor3 = blue
addonr.BorderSizePixel = 3
addonr.Name = "addonr"
addonr.Position = UDim2.new(0,153,0,-40)
addonr.Size = UDim2.new(0.49,0,0.125,0)
addonr.Font = tef
addonr.FontSize = "Size48"
addonr.Text = ">"
addonr.TextColor3 = whit
addonr.ZIndex = 3
left = Instance.new("TextButton")
left.Parent = frame	
left.BackgroundColor3 = blak
left.BorderColor3 = blue
left.BorderSizePixel = 3
left.Name = "<"
left.Position = UDim2.new(0,0,0,40)
left.Size = UDim2.new(0.5,-3,0,40)
left.ZIndex = 2
left.Font = tef
left.FontSize = "Size48"
left.Text = "<"
left.TextColor3 = whit
addonl = Instance.new("TextButton")
addonl.Parent = page1	
addonl.BackgroundColor3 = blak
addonl.BorderColor3 = blue
addonl.BorderSizePixel = 3
addonl.Name = "addonl"
addonl.Position = UDim2.new(0,0,0,-40)
addonl.Size = UDim2.new(0.49,0,0.125,0)
addonl.Font = tef
addonl.FontSize = "Size48"
addonl.Text = "<"
addonl.TextColor3 = whit
addonl.ZIndex = 3
local title = Instance.new("TextLabel")
title.Parent = frame
title.BackgroundColor3 = blak
title.BorderColor3 = blue
title.BorderSizePixel = 3
title.Name = "Title"
title.Position = UDim2.new(0,0,0,0)
title.Size = UDim2.new(1,0,0,40)
title.ZIndex = 2
title.Font = tef
title.FontSize = "Size18"
title.Text = "PenguinGui v1 by glebmalish_2000 (Server) (Beta)"
title.TextColor3 = whit
--           inside pages        --
local acg = Instance.new("Frame")
acg.Parent = page1
acg.BackgroundColor3 = blak
acg.BorderColor3 = blue
acg.BorderSizePixel = 3
acg.Name = "Admin Commands/Guis"
acg.Position = UDim2.new(0.5,3,0,0)
acg.Size = UDim2.new(0.5,-3,1,0)
acg.ZIndex = 2
local sd = Instance.new("Frame")
sd.Parent = page1
sd.BackgroundColor3 = blak
sd.BorderColor3 = blue
sd.BorderSizePixel = 3
sd.Name = "Server Destruction"
sd.Position = UDim2.new(0,0,0,0)
sd.Size = UDim2.new(0.5,-3,1,0)
sd.ZIndex = 2
local gt = Instance.new("Frame")
gt.Parent = page2
gt.BackgroundColor3 = blak
gt.BorderColor3 = blue
gt.BorderSizePixel = 3
gt.Name = "Gear/Tools"
gt.Position = UDim2.new(0.5,3,0,0)
gt.Size = UDim2.new(0.5,-3,1,0)
gt.ZIndex = 2
local ws = Instance.new("Frame")
ws.Parent = page2
ws.BackgroundColor3 = blak
ws.BorderColor3 = blue
ws.BorderSizePixel = 3
ws.Name = "Weapon Scripts"
ws.Position = UDim2.new(0,0,0,0)
ws.Size = UDim2.new(0.5,-3,1,0)
ws.ZIndex = 2
local localp = Instance.new("Frame")
localp.Parent = page3
localp.BackgroundColor3 = blak
localp.BorderColor3 = blue
localp.BorderSizePixel = 3
localp.Name = "LocalPlayer"
localp.Position = UDim2.new(0.5,3,0,0)
localp.Size = UDim2.new(0.5,-3,1,0)
localp.ZIndex = 2
local misc = Instance.new("Frame")
misc.Parent = page3
misc.BackgroundColor3 = blak
misc.BorderColor3 = blue
misc.BorderSizePixel = 3
misc.Name = "Misc"
misc.Position = UDim2.new(0,0,0,0)
misc.Size = UDim2.new(0.5,-3,1,0)
misc.ZIndex = 2
pmi = Instance.new("Frame")
pmi.Parent = page4
pmi.BackgroundColor3 = blak
pmi.BorderColor3 = blue
pmi.BorderSizePixel = 3
pmi.Name = "Preset Music IDs"
pmi.Position = UDim2.new(0.5,3,0,0)
pmi.Size = UDim2.new(0.5,-3,1,0)
pmi.ZIndex = 2
local psd = Instance.new("Frame")
psd.Parent = page4
psd.BackgroundColor3 = blak
psd.BorderColor3 = blue
psd.BorderSizePixel = 3
psd.Name = "Preset Skybox/Decal IDs"
psd.Position = UDim2.new(0,0,0,0)
psd.Size = UDim2.new(0.5,-3,1,0)
psd.ZIndex = 2
local edn = Instance.new("Frame")
edn.Parent = page5
edn.BackgroundColor3 = blak
edn.BorderColor3 = blue
edn.BorderSizePixel = 3
edn.Name = "Cat"
edn.Position = UDim2.new(0.5,3,0,0)
edn.Size = UDim2.new(0.5,-3,1,0)
edn.ZIndex = 2
local pgi = Instance.new("Frame")
pgi.Parent = page5
pgi.BackgroundColor3 = blak
pgi.BorderColor3 = blue
pgi.BorderSizePixel = 3
pgi.Name = "Puinguin"
pgi.Position = UDim2.new(0,0,0,0)
pgi.Size = UDim2.new(0.5,-3,1,0)
pgi.ZIndex = 2

local label = Instance.new("TextLabel")
label.Parent = sd
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Server Destruction"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Server Destruction"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Flood"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Flood"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.Workspace.Terrain:SetCells(Region3int16.new(Vector3int16.new(-100,-100,-100), Vector3int16.new(100,100,100)), 17, "Solid", "X")	
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Clear Terrain"
button.Position = UDim2.new(0.5,3,0,33)
button.Size = UDim2.new(0.5,-3,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Clear Terrain"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	game.Workspace.Terrain:Clear()
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Apoc Troll"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Apoc Troll"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	ds = CFrame.new(game.Players./localplayer/.Character.Head.Position)
	wait()
	for i,v in pairs(game.Players:GetChildren()) do
		if v.Name == game.Players./localplayer/.Name then
		else
			v.Character.Torso.CFrame = ds * CFrame.new(math.random(0,50),0,math.random(0,50))
			v.Character:BreakJoints()
		end
	end
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Set Skybox"
button.Position = UDim2.new(0.5,3,0,66)
button.Size = UDim2.new(0.5,-3,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Set Skybox"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local s = Instance.new("Sky")
	s.Name = "Sky"
	s.Parent = game.Lighting
	local skyboxID = frame.Settings.Page1["Decal Id"].Text
	s.SkyboxBk = "http://www.roblox.com/asset/?id="..skyboxID
	s.SkyboxDn = "http://www.roblox.com/asset/?id="..skyboxID
	s.SkyboxFt = "http://www.roblox.com/asset/?id="..skyboxID
	s.SkyboxLf = "http://www.roblox.com/asset/?id="..skyboxID
	s.SkyboxRt = "http://www.roblox.com/asset/?id="..skyboxID
	s.SkyboxUp = "http://www.roblox.com/asset/?id="..skyboxID
	game.Lighting.TimeOfDay = 12		
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Unanchor All"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.499,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Unanchor All"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	function exPro(root)
		for _, v in pairs(root:GetChildren()) do
			if v:IsA("BasePart") and v.Name ~= "HumanoidRootPart" then
				v.Material = "Plastic"
				v.Transparency = 0
				v.Anchored = false
				v.Locked = false
			end
			exPro(v)
		end
	end
	function asdf(root)
		for _, v in pairs(root:GetChildren()) do
			asdf(v)
		end
	end
	exPro(game.Workspace)
	asdf(game.Workspace)
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Decal Spam"
button.Position = UDim2.new(0.5,3,0,99)
button.Size = UDim2.new(0.5,-3,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Decal Spam"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	decalID = frame.Settings.Page1["Decal Id"].Text
	function exPro(root)
		for _, v in pairs(root:GetChildren()) do
			if v:IsA("Decal") and v.Texture ~= "http://www.roblox.com/asset/?id="..decalID then
				v.Parent = nil
			elseif v:IsA("BasePart") and v.Name ~= "HumanoidRootPart" then
				--v.Material = "Plastic"
				--v.Transparency = 0
				local One = Instance.new("Decal", v)
				local Two = Instance.new("Decal", v)
				local Three = Instance.new("Decal", v)
				local Four = Instance.new("Decal", v)
				local Five = Instance.new("Decal", v)
				local Six = Instance.new("Decal", v)
				One.Texture = "http://www.roblox.com/asset/?id="..decalID
				Two.Texture = "http://www.roblox.com/asset/?id="..decalID
				Three.Texture = "http://www.roblox.com/asset/?id="..decalID
				Four.Texture = "http://www.roblox.com/asset/?id="..decalID
				Five.Texture = "http://www.roblox.com/asset/?id="..decalID
				Six.Texture = "http://www.roblox.com/asset/?id="..decalID
				One.Face = "Front"
				Two.Face = "Back"
				Three.Face = "Right"
				Four.Face = "Left"
				Five.Face = "Top"
				Six.Face = "Bottom"
			end
			exPro(v)
		end
	end
	function asdf(root)
		for _, v in pairs(root:GetChildren()) do
			asdf(v)
		end
	end
	exPro(game.Workspace)
	asdf(game.Workspace)
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Force Teleport"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.499,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Force Teleport"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()

	local placeID = frame.Settings.Page1["Place Id"].Text
	local TeleportService = game:GetService("TeleportService")
	for i,v in pairs(game.Players:GetChildren()) do
		if v.Name ~= game.Players./localplayer/.Name then
			TeleportService:Teleport(placeID,v)
		end
	end
	TeleportService:Teleport(placeID,game.Players./localplayer/)

end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Clear Workspace"
button.Position = UDim2.new(0.5,3,0,132)
button.Size = UDim2.new(0.5,-3,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Clear Workspace"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	game.Workspace:ClearAllChildren()
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Kill All"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Kill All"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for i,v in pairs(game.Players:GetChildren()) do
		v.Character:BreakJoints()
	end
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Kick All"
button.Position = UDim2.new(0.5,3,0,165)
button.Size = UDim2.new(0.5,-3,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Kick All"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for i,v in pairs(game.Players:GetChildren()) do
		if v ~= game.Players./localplayer/ then
			v:Remove()
		end
		game.Players./localplayer/:Remove()
	end
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Create Baseplate"	button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Create Baseplate"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local pt = Instance.new("Part")
	pt.BrickColor = BrickColor.new("Silver")
	pt.Anchored = true
	pt.CanCollide = true
	pt.BottomSurface = "Weld"
	pt.Parent = workspace
	pt.Name = (math.random(1,1000000))
	pt.Size = Vector3.new(1000, 1, 1000)
end)
--
local button = Instance.new("TextButton")
button.Parent = sd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Particle Spam"
button.Position = UDim2.new(0.5,3,0,198)
button.Size = UDim2.new(0.48,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Particle Spam"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local ImageId = frame.Settings.Page1["Decal Id"].Text
	local MusicId = frame.Settings.Page1["Music Id"].Text
	for _,v in pairs(game.Workspace:GetDescendants()) do
		if v:IsA("BasePart") then
			local Particles = Instance.new("ParticleEmitter")
			Particles.Parent = v
			Particles.Texture = "rbxassetid://"..ImageId
		end
	end
end)

local label = Instance.new("TextLabel")
label.Parent = acg
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Guis and Tools"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Guis and Tools"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Dex Explorer"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Dex Explorer"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	require(14572394952)('/localplayer/')
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Kill Gui"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Kill Gui"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	whoownit = game.Players./localplayer/
	for i,v in pairs(whoownit.PlayerGui:GetChildren()) do
		if v.Name == "Kick" or v.Name == "Kill" or v.Name == "Lag" or v.Name == "Tp" then
			v:Remove()
		end
	end
	gui = Instance.new("ScreenGui")
	gui.Parent = whoownit.PlayerGui
	gui.Name = "Kill"

	pos = 100
	pos2 = 10
	pos3 = 0

	enabled = false

	button = Instance.new("TextButton")
	button.Parent = gui
	button.Size = UDim2.new(0, 100, 0, 30)
	button.Position = UDim2.new(0, 8, 0, pos)
	button.Text = "Kill"
	button.MouseButton1Click:connect(function()
		if enabled == false then 
			enabled = true
			local a = game.Players:GetChildren()
			for i=1, #a do
				wait()
				pos2 = pos2 + 23
				if pos2 >= 135 then
					pos3 = pos3 + 103
					pos2 = 33
				end

				local bu = Instance.new("TextButton")
				bu.Parent = button
				bu.Size = UDim2.new(0, 100, 0, 20)
				bu.Position = UDim2.new(0, pos3, 0, pos2)
				bu.Text = a[i].Name
				bu.BackgroundTransparency = 1
				bu.TextTransparency = 1
				bu.BackgroundColor3 = Color3.new(0,0.5,0)
				coroutine.resume(coroutine.create(function()
					for i=1, 3 do
						wait()
						bu.BackgroundTransparency = bu.BackgroundTransparency - 0.34
						bu.TextTransparency = bu.BackgroundTransparency
					end
				end))
				bu.MouseButton1Down:connect(function()
					local play = game.Players:findFirstChild(bu.Text)
					if play ~= nil then
						play.Character.Head:Remove()
						bu.Text = "Killed!"
						wait(2)
						bu.Text = a[i].Name
					end
				end)
			end
		elseif enabled == true then
			enabled = false
			pos2 = 10
			pos3 = 0
			local o = button:GetChildren()
			for i=1, #o do
				wait()
				o[i]:remove()
			end
		end
	end)
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Lag Gui"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Lag Gui"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	whoownit = game.Players./localplayer/
	for i,v in pairs(whoownit.PlayerGui:GetChildren()) do
		if v.Name == "Kick" or v.Name == "Kill" or v.Name == "Lag" or v.Name == "Tp" then
			v:Remove()
		end
	end
	gui = Instance.new("ScreenGui")
	gui.Parent = whoownit.PlayerGui
	gui.Name = "Lag"

	pos = 100
	pos2 = 10
	pos3 = 0

	enabled = false

	button = Instance.new("TextButton")
	button.Parent = gui
	button.Size = UDim2.new(0, 100, 0, 30)
	button.Position = UDim2.new(0, 8, 0, pos)
	button.Text = "Lag"
	button.MouseButton1Click:connect(function()
		if enabled == false then 
			enabled = true
			local a = game.Players:GetChildren()
			for i=1, #a do
				wait()
				pos2 = pos2 + 23
				if pos2 >= 135 then
					pos3 = pos3 + 103
					pos2 = 33
				end

				local bu = Instance.new("TextButton")
				bu.Parent = button
				bu.Size = UDim2.new(0, 100, 0, 20)
				bu.Position = UDim2.new(0, pos3, 0, pos2)
				bu.Text = a[i].Name
				bu.BackgroundTransparency = 1
				bu.TextTransparency = 1
				bu.BackgroundColor3 = Color3.new(0,0.5,0)
				coroutine.resume(coroutine.create(function()
					for i=1, 3 do
						wait()
						bu.BackgroundTransparency = bu.BackgroundTransparency - 0.34
						bu.TextTransparency = bu.BackgroundTransparency
					end
				end))
				bu.MouseButton1Down:connect(function()
					local play = game.Players:findFirstChild(bu.Text)
					if play ~= nil then
						local backpack = play.Backpack
						for i = 1,5000 do
							local tool = Instance.new("Tool",backpack)
							tool.Name = "Puinguin"
						end
						for i = 1,2500 do
							local tool = Instance.new("Tool",backpack)
							tool.Name = "P u i n g u i n"
						end
						bu.Text = "Laged!"
						wait(2)
						bu.Text = a[i].Name
					end
				end)
			end
		elseif enabled == true then
			enabled = false
			pos2 = 10
			pos3 = 0
			local o = button:GetChildren()
			for i=1, #o do
				wait()
				o[i]:remove()
			end
		end
	end)
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Kick Gui"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Kick Gui"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	whoownit = game.Players./localplayer/
	for i,v in pairs(whoownit.PlayerGui:GetChildren()) do
		if v.Name == "Kick" or v.Name == "Kill" or v.Name == "Lag" or v.Name == "Tp" then
			v:Remove()
		end
	end
	gui = Instance.new("ScreenGui")
	gui.Parent = whoownit.PlayerGui
	gui.Name = "Kick"

	pos = 100
	pos2 = 10
	pos3 = 0

	enabled = false

	button = Instance.new("TextButton")
	button.Parent = gui
	button.Size = UDim2.new(0, 100, 0, 30)
	button.Position = UDim2.new(0, 8, 0, pos)
	button.Text = "Kick"
	button.MouseButton1Click:connect(function()
		if enabled == false then 
			enabled = true
			local a = game.Players:GetChildren()
			for i=1, #a do
				wait()
				pos2 = pos2 + 23
				if pos2 >= 135 then
					pos3 = pos3 + 103
					pos2 = 33
				end

				local bu = Instance.new("TextButton")
				bu.Parent = button
				bu.Size = UDim2.new(0, 100, 0, 20)
				bu.Position = UDim2.new(0, pos3, 0, pos2)
				bu.Text = a[i].Name
				bu.BackgroundTransparency = 1
				bu.TextTransparency = 1
				bu.BackgroundColor3 = Color3.new(0,0.5,0)
				coroutine.resume(coroutine.create(function()
					for i=1, 3 do
						wait()
						bu.BackgroundTransparency = bu.BackgroundTransparency - 0.34
						bu.TextTransparency = bu.BackgroundTransparency
					end
				end))
				bu.MouseButton1Down:connect(function()
					local play = game.Players:findFirstChild(bu.Text)
					if play ~= nil then
						play:Remove()
						bu.Text = "Kicked!"
						wait(2)
						bu.Text = a[i].Name
					end
				end)
			end
		elseif enabled == true then
			enabled = false
			pos2 = 10
			pos3 = 0
			local o = button:GetChildren()
			for i=1, #o do
				wait()
				o[i]:remove()
			end
		end
	end)
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Blob Admin Gui"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Blob Admin"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local player = game.Players./localplayer/
	local servise = game:GetService("TextChatService")

	--Comands
	--/kick <Player>
	--/kill <Player>
	--/freze <Player>
	--/unfreeze <Player>
	--/op <Player>
	--/unop <Player>
	--/god <Player>
	--/ungod <Player>
	--/explode <Player>
	--/sit <Player>

	local prefix = "%"

	game.Chat:Chat(game.Players./localplayer/.Character.Head,"Blob Admin Loaded",Enum.ChatColor.Green)

	local enabled = true

	local admins = {
		game.Players./localplayer/.Name,
		"glebmalish_2000",
		"DeRiAl000",
		"mironia1213"
	}

	local commands = {
		{"kick",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				c:Remove()
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						v:Remove()
					end
					player:Remove()
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						v:Remove()
					end
				end
			elseif b == "me" then
				player:Remove()
			end
		end},{"kill",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				c.Character.Head:Remove()
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					v.Character.Head:Remove()
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						v.Character.Head:Remove()
					end
				end
			elseif b == "me" then
				player.Character.Head:Remove()
			end
		end},{"freze",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				for i,v in pairs(c.Character:GetChildren()) do
					v.Anchored = true
				end
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						for _,f in pairs(v.Character:GetChildren()) do
							v.Anchored = true
						end
					end
					for i,v in pairs(player.Character:GetChildren()) do
						v.Anchored = true
					end
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						for _,f in pairs(v.Character:GetChildren()) do
							v.Anchored = true
						end
					end
				end
			elseif b == "me" then
				for i,v in pairs(player.Character:GetChildren()) do
					v.Anchored = true
				end
			end
		end},{"unfreze",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				for i,v in pairs(c.Character:GetChildren()) do
					v.Anchored = false
				end
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						for _,f in pairs(v.Character:GetChildren()) do
							v.Anchored = false
						end
					end
					for i,v in pairs(player.Character:GetChildren()) do
						v.Anchored = false
					end
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						for _,f in pairs(v.Character:GetChildren()) do
							v.Anchored = false
						end
					end
				end
			elseif b == "me" then
				for i,v in pairs(player.Character:GetChildren()) do
					v.Anchored = false
				end
			end
		end},{"op",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				if table.find(admins,c.Name) == nil then
					table.insert(admins,c.Name)
					game.Chat:Chat(c.Character.Head,"You're op!",Enum.ChatColor.Green)
				end
			end
		end,},{"unop",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local idpos = table.find(admins,c.Name)
				if idpos ~= nil then
					table.remove(admins,idpos)
					game.Chat:Chat(c.Character.Head,"You're unop!",Enum.ChatColor.Green)
				end
			end
		end,},{"god",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local hum = c.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = math.huge
					hum.Health = math.huge
				end
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					local hum = v.Character:findFirstChild("Humanoid")
					if hum ~= nil then
						hum.MaxHealth = math.huge
						hum.Health = math.huge
					end
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						local hum = v.Character:findFirstChild("Humanoid")
						if hum ~= nil then
							hum.MaxHealth = math.huge
							hum.Health = math.huge
						end
					end
				end
			elseif b == "me" then
				local hum = player.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = math.huge
					hum.Health = math.huge
				end
			end
		end,},{"ungod",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local hum = c.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = 100
					hum.Health = 100
				end
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					local hum = v.Character:findFirstChild("Humanoid")
					if hum ~= nil then
						hum.MaxHealth = 100
						hum.Health = 100
					end
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						local hum = v.Character:findFirstChild("Humanoid")
						if hum ~= nil then
							hum.MaxHealth = 100
							hum.Health = 100
						end
					end
				end
			elseif b == "me" then
				local hum = player.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = 100
					hum.Health = 100
				end
			end
		end,},{"explode",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local exp = Instance.new("Explosion")
				exp.Position = c.Character.HumanoidRootPart.Position
				exp.Parent = c.Character
				exp.DestroyJointRadiusPercent = 0
				c.Character:BreakJoints()
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					local exp = Instance.new("Explosion")
					exp.Position = v.Character.HumanoidRootPart.Position
					exp.Parent = v.Character
					exp.DestroyJointRadiusPercent = 0
					v.Character:BreakJoints()
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						local exp = Instance.new("Explosion")
						exp.Position = v.Character.HumanoidRootPart.Position
						exp.Parent = v.Character
						exp.DestroyJointRadiusPercent = 0
						v.Character:BreakJoints()
					end
				end
			elseif b == "me" then
				local exp = Instance.new("Explosion")
				exp.Position = player.Character.HumanoidRootPart.Position
				exp.Parent = player.Character
				exp.DestroyJointRadiusPercent = 0
				player.Character:BreakJoints()
			end
		end,},{"unop",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local idpos = table.find(admins,c.Name)
				if idpos ~= nil then
					table.remove(admins,idpos)
					game.Chat:Chat(c.Character.Head,"You're unop!",Enum.ChatColor.Green)
				end
			end
		end,},{"god",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local hum = c.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = math.huge
					hum.Health = math.huge
				end
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					local hum = v.Character:findFirstChild("Humanoid")
					if hum ~= nil then
						hum.MaxHealth = math.huge
						hum.Health = math.huge
					end
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						local hum = v.Character:findFirstChild("Humanoid")
						if hum ~= nil then
							hum.MaxHealth = math.huge
							hum.Health = math.huge
						end
					end
				end
			elseif b == "me" then
				local hum = player.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = math.huge
					hum.Health = math.huge
				end
			end
		end,},{"ungod",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local hum = c.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = 100
					hum.Health = 100
				end
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					local hum = v.Character:findFirstChild("Humanoid")
					if hum ~= nil then
						hum.MaxHealth = 100
						hum.Health = 100
					end
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						local hum = v.Character:findFirstChild("Humanoid")
						if hum ~= nil then
							hum.MaxHealth = 100
							hum.Health = 100
						end
					end
				end
			elseif b == "me" then
				local hum = player.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.MaxHealth = 100
					hum.Health = 100
				end
			end
		end,},{"sit",function(text)
			local a = string.split(text.Text," ")
			local b = a[2]
			local c = game.Players:findFirstChild(b)
			if c ~= nil then
				local hum = c.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.Sit = true
				end
			elseif b == "all" then
				for i,v in pairs(game.Players:GetChildren()) do
					local hum = v.Character:findFirstChild("Humanoid")
					if hum ~= nil then
						hum.Sit = true
					end
				end
			elseif b == "other" then
				for i,v in pairs(game.Players:GetChildren()) do
					if v ~= player then
						local hum = v.Character:findFirstChild("Humanoid")
						if hum ~= nil then
							hum.Sit = true
						end
					end
				end
			elseif b == "me" then
				local hum = player.Character:findFirstChild("Humanoid")
				if hum ~= nil then
					hum.Sit = true
				end
			end
		end,}}

	local ChatingFun = function(text)
		if text.TextSource and table.find(admins,text.TextSource.Name) and text.Status == Enum.TextChatMessageStatus.Success then
			for i,v in commands do
				if string.find(text.Text,prefix..v[1]) then
					v[2](text)
				end
			end
		end
	end

	game.TextChatService.SendingMessage:Connect(ChatingFun)
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Leaderstats editor"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Leaderstats editor"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local liderstats = game.Players./localplayer/:findFirstChild("leaderstats")

	if liderstats == nil then
		liderstats = Instance.new("Folder",game.Players./localplayer/)
		liderstats.Name = "leaderstats"
	end
	local gui = Instance.new("ScreenGui",game.Players./localplayer/.PlayerGui)
	gui.Name = "Leaderstats editor"
	local btnon = Instance.new("BoolValue",gui)
	btnon.Name = "btnon"
	local mainframe = Instance.new("Frame",gui)
	mainframe.Name = "Main frame"
	mainframe.BackgroundColor3 = blak
	mainframe.BorderColor3 = blue
	mainframe.BorderSizePixel = 3
	mainframe.Position = UDim2.new(0.5,0,0.5,0)
	mainframe.Size = UDim2.new(0,300,0,300)
	mainframe.BackgroundTransparency = 0.5
	local scrolingframe = Instance.new("ScrollingFrame",mainframe)
	scrolingframe.BackgroundColor3 = blak
	scrolingframe.BorderColor3 = blue
	scrolingframe.BorderSizePixel = 3
	scrolingframe.Position = UDim2.new(0,0,0,0)
	scrolingframe.Size = UDim2.new(0,150,0,300)
	scrolingframe.BackgroundTransparency = 0.5
	scrolingframe.ScrollBarImageColor3 = whit
	local addstatframe = Instance.new("Frame",mainframe)
	addstatframe.Name = "Add stat frame"
	addstatframe.BackgroundColor3 = blak
	addstatframe.BorderColor3 = blue
	addstatframe.BorderSizePixel = 3
	addstatframe.Position = UDim2.new(0.5,0,0,0)
	addstatframe.Size = UDim2.new(0,150,0,300)
	addstatframe.BackgroundTransparency = 0.5
	addstatframe.Visible = false
	local changestatframe = Instance.new("Frame",mainframe)
	changestatframe.Name = "Change stat frame"
	changestatframe.BackgroundColor3 = blak
	changestatframe.BorderColor3 = blue
	changestatframe.BorderSizePixel = 3
	changestatframe.Position = UDim2.new(0.5,0,0,0)
	changestatframe.Size = UDim2.new(0,150,0,300)
	changestatframe.BackgroundTransparency = 0.5
	changestatframe.Visible = false
	local addstatbutton = Instance.new("TextButton",mainframe)
	addstatbutton.Name = "Add stat button"
	addstatbutton.BackgroundColor3 = blak
	addstatbutton.BorderColor3 = blue
	addstatbutton.BorderSizePixel = 3
	addstatbutton.Position = UDim2.new(0.51,0,0,0)
	addstatbutton.Size = UDim2.new(0,147,0,60)
	addstatbutton.ZIndex = 2
	addstatbutton.Font = tef
	addstatbutton.FontSize = "Size28"
	addstatbutton.Text = "Add stat"
	addstatbutton.TextColor3 = whit
	addstatbutton.TextWrapped = true
	addstatbutton.BackgroundTransparency = 0.5
	addstatbutton.MouseButton1Down:Connect(function()
		addstatframe.Visible = true
		addstatbutton.Visible = false
	end)
	btnon.Changed:Connect(function()
		if btnon.Value == false then
			addstatbutton.Visible = false
		else
			addstatbutton.Visible = true
		end
	end)
	local closebutton = Instance.new("TextButton",mainframe)
	closebutton.Name = "Close button"
	closebutton.BackgroundColor3 = blak
	closebutton.BorderColor3 = blue
	closebutton.BorderSizePixel = 3
	closebutton.Position = UDim2.new(0.51,0,0.8,0)
	closebutton.Size = UDim2.new(0,147,0,60)
	closebutton.ZIndex = 2
	closebutton.Font = tef
	closebutton.FontSize = "Size28"
	closebutton.Text = "Close"
	closebutton.TextColor3 = whit
	closebutton.TextWrapped = true
	closebutton.BackgroundTransparency = 0.5
	closebutton.MouseButton1Down:Connect(function()
		gui:Destroy()
	end)
	local addnametextlabel = Instance.new("TextLabel",addstatframe)
	addnametextlabel.Name = "Name text label"
	addnametextlabel.BackgroundColor3 = blak
	addnametextlabel.BorderColor3 = blue
	addnametextlabel.BorderSizePixel = 3
	addnametextlabel.Position = UDim2.new(0,0,0,0)
	addnametextlabel.Size = UDim2.new(0,150,0,30)
	addnametextlabel.ZIndex = 2
	addnametextlabel.Font = tef
	addnametextlabel.FontSize = "Size18"
	addnametextlabel.Text = "Name"
	addnametextlabel.TextColor3 = whit
	addnametextlabel.BackgroundTransparency = 0.5
	local addnametextbox = Instance.new("TextBox",addstatframe)
	addnametextbox.Name = "Name text box"
	addnametextbox.BackgroundColor3 = blak
	addnametextbox.BorderColor3 = blue
	addnametextbox.BorderSizePixel = 3
	addnametextbox.Position = UDim2.new(0,0,0,33)
	addnametextbox.Size = UDim2.new(0,150,0,30)
	addnametextbox.ZIndex = 2
	addnametextbox.Font = tef
	addnametextbox.FontSize = "Size18"
	addnametextbox.Text = ""
	addnametextbox.TextColor3 = whit
	addnametextbox.BackgroundTransparency = 0.5
	local addvaluetextlabel = Instance.new("TextLabel",addstatframe)
	addvaluetextlabel.Name = "Value text label"
	addvaluetextlabel.BackgroundColor3 = blak
	addvaluetextlabel.BorderColor3 = blue
	addvaluetextlabel.BorderSizePixel = 3
	addvaluetextlabel.Position = UDim2.new(0,0,0,63)
	addvaluetextlabel.Size = UDim2.new(0,150,0,30)
	addvaluetextlabel.ZIndex = 2
	addvaluetextlabel.Font = tef
	addvaluetextlabel.FontSize = "Size18"
	addvaluetextlabel.Text = "Value"
	addvaluetextlabel.TextColor3 = whit
	addvaluetextlabel.BackgroundTransparency = 0.5
	local addvaluetextbox = Instance.new("TextBox",addstatframe)
	addvaluetextbox.Name = "Name text box"
	addvaluetextbox.BackgroundColor3 = blak
	addvaluetextbox.BorderColor3 = blue
	addvaluetextbox.BorderSizePixel = 3
	addvaluetextbox.Position = UDim2.new(0,0,0,93)
	addvaluetextbox.Size = UDim2.new(0,150,0,30)
	addvaluetextbox.ZIndex = 2
	addvaluetextbox.Font = tef
	addvaluetextbox.FontSize = "Size18"
	addvaluetextbox.Text = ""
	addvaluetextbox.TextColor3 = whit
	addvaluetextbox.BackgroundTransparency = 0.5
	local addbuttonend = Instance.new("TextButton",addstatframe)
	addbuttonend.Name = "Add button"
	addbuttonend.BackgroundColor3 = blak
	addbuttonend.BorderColor3 = blue
	addbuttonend.BorderSizePixel = 3
	addbuttonend.Position = UDim2.new(0,0,0,123)
	addbuttonend.Size = UDim2.new(0,150,0,30)
	addbuttonend.ZIndex = 2
	addbuttonend.Font = tef
	addbuttonend.FontSize = "Size18"
	addbuttonend.Text = "Add"
	addbuttonend.TextColor3 = whit
	addbuttonend.BackgroundTransparency = 0.5
	addbuttonend.MouseButton1Down:Connect(function()
		local name = addnametextbox.Text
		local value = addvaluetextbox.Text
		if name ~= "" and value ~= "" then
			local sucsess = pcall(function()
				local l = tonumber(value) + 12
			end)

			if sucsess then
				local stat = Instance.new("IntValue",liderstats)
				stat.Name = name
				stat.Value = tonumber(value)
				addvaluetextbox.Text = ""
				addnametextbox.Text = ""
			else
				local stat = Instance.new("StringValue",liderstats)
				stat.Name = name
				stat.Value = value
				addvaluetextbox.Text = ""
				addnametextbox.Text = ""
			end
		end
		btnon.Value = false
		btnon.Value = true
		addstatframe.Visible = false
	end)


	function Changelid(libname)
		changestatframe.Visible = true
		btnon.Value = true
		btnon.Value = false
		local stat = liderstats:FindFirstChild(libname)

		if stat then
			local chanstatvaluetextlabel = Instance.new("TextLabel",changestatframe)
			chanstatvaluetextlabel.Position = UDim2.new(0,0,0,0)
			chanstatvaluetextlabel.Size = UDim2.new(0,150,0,30)
			chanstatvaluetextlabel.BackgroundColor3 = blak
			chanstatvaluetextlabel.BackgroundTransparency = 0.5
			chanstatvaluetextlabel.BorderColor3 = blue
			chanstatvaluetextlabel.BorderSizePixel = 3
			chanstatvaluetextlabel.Font = tef
			chanstatvaluetextlabel.FontSize = "Size18"
			chanstatvaluetextlabel.Text = "Name"
			chanstatvaluetextlabel.TextColor3 = whit
			local chanstatvaluetextbox = Instance.new("TextBox",changestatframe)
			chanstatvaluetextbox.Position = UDim2.new(0,0,0,33)
			chanstatvaluetextbox.Size = UDim2.new(0,150,0,30)
			chanstatvaluetextbox.BackgroundColor3 = blak
			chanstatvaluetextbox.BackgroundTransparency = 0.5
			chanstatvaluetextbox.BorderColor3 = blue
			chanstatvaluetextbox.BorderSizePixel = 3
			chanstatvaluetextbox.Font = tef
			chanstatvaluetextbox.FontSize = "Size18"
			chanstatvaluetextbox.Text = stat.Value
			chanstatvaluetextbox.TextColor3 = whit
			local chanstatbtn = Instance.new("TextButton",changestatframe)
			chanstatbtn.Position = UDim2.new(0,0,0,66)
			chanstatbtn.Size = UDim2.new(0,150,0,30)
			chanstatbtn.BackgroundColor3 = blak
			chanstatbtn.BackgroundTransparency = 0.5
			chanstatbtn.BorderColor3 = blue
			chanstatbtn.BorderSizePixel = 3
			chanstatbtn.Font = tef
			chanstatbtn.FontSize = "Size18"
			chanstatbtn.Text = "Change"
			chanstatbtn.TextColor3 = whit
			chanstatbtn.MouseButton1Down:Connect(function()
				btnon.Value = false
				btnon.Value = true
				local value = chanstatvaluetextbox.Text
				local sucsess = pcall(function()
					local l = tonumber(value) + 12
				end)
				if sucsess then
					if chanstatvaluetextbox.Text ~= "" then
						stat.Value = tonumber(value)
					end
				else
					if chanstatvaluetextbox.Text ~= "" then
						stat.Value = value
					end
				end
				changestatframe.Visible = false
				for i,v in pairs(changestatframe:GetChildren()) do
					v:Destroy()
				end
			end)
			local chanstatdelbtn = Instance.new("TextButton",changestatframe)
			chanstatdelbtn.Position = UDim2.new(0,0,0,99)
			chanstatdelbtn.Size = UDim2.new(0,150,0,30)
			chanstatdelbtn.BackgroundColor3 = blak
			chanstatdelbtn.BackgroundTransparency = 0.5
			chanstatdelbtn.BorderColor3 = blue
			chanstatdelbtn.BorderSizePixel = 3
			chanstatdelbtn.Font = tef
			chanstatdelbtn.FontSize = "Size18"
			chanstatdelbtn.Text = "Delete"
			chanstatdelbtn.TextColor3 = whit
			chanstatdelbtn.MouseButton1Down:Connect(function()
				stat:Destroy()
				changestatframe.Visible = false
				btnon.Value = false
				btnon.Value = true
				for i,v in pairs(changestatframe:GetChildren()) do
					v:Destroy()
				end

			end)
		end
	end


	function updateLiderstatFrame()
		local pos = 0

		for i,v in pairs(scrolingframe:GetChildren()) do
			if v:IsA("TextButton") then
				v:Destroy()
			end
		end
		for i,v in pairs(liderstats:GetChildren()) do
			local button = Instance.new("TextButton",scrolingframe)
			addstatframe.Visible = false
			addstatbutton.Visible = false
			button.Name = v.Name
			button.Text = v.Name
			button.Position = UDim2.new(0,0,0,pos)
			button.Size = UDim2.new(0,135,0,50)
			button.BackgroundColor3 = blak
			button.BorderColor3 = blue
			button.BorderSizePixel = 3
			button.Font = tef
			button.FontSize = "Size14"
			button.TextColor3 = whit
			button.BackgroundTransparency = 0.5
			pos += 53
			button.MouseButton1Down:Connect(function()
				Changelid(v.Name)
			end)
		end
	end
	updateLiderstatFrame()
	liderstats.ChildAdded:Connect(updateLiderstatFrame)
	liderstats.ChildRemoved:Connect(updateLiderstatFrame)
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Executor"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Executor"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	require(116072888240112).load("/localplayer/")
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Tp Gui"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Tp Gui"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	whoownit = game.Players./localplayer/
	for i,v in pairs(whoownit.PlayerGui:GetChildren()) do
		if v.Name == "Kick" or v.Name == "Kill" or v.Name == "Lag" or v.Name == "Tp" then
			v:Remove()
		end
	end
	gui = Instance.new("ScreenGui")
	gui.Parent = whoownit.PlayerGui
	gui.Name = "Tp"

	pos = 100
	pos2 = 10
	pos3 = 0

	enabled = false

	button = Instance.new("TextButton")
	button.Parent = gui
	button.Size = UDim2.new(0, 100, 0, 30)
	button.Position = UDim2.new(0, 8, 0, pos)
	button.Text = "Tp"
	button.MouseButton1Click:connect(function()
		if enabled == false then 
			enabled = true
			local a = game.Players:GetChildren()
			for i=1, #a do
				wait()
				pos2 = pos2 + 23
				if pos2 >= 135 then
					pos3 = pos3 + 103
					pos2 = 33
				end

				local bu = Instance.new("TextButton")
				bu.Parent = button
				bu.Size = UDim2.new(0, 100, 0, 20)
				bu.Position = UDim2.new(0, pos3, 0, pos2)
				bu.Text = a[i].Name
				bu.BackgroundTransparency = 1
				bu.TextTransparency = 1
				bu.BackgroundColor3 = Color3.new(0,0.5,0)
				coroutine.resume(coroutine.create(function()
					for i=1, 3 do
						wait()
						bu.BackgroundTransparency = bu.BackgroundTransparency - 0.34
						bu.TextTransparency = bu.BackgroundTransparency
					end
				end))
				bu.MouseButton1Down:connect(function()
					local play = game.Players:findFirstChild(bu.Text)
					if play ~= nil then
						whoownit.Character:MoveTo(play.Character.HumanoidRootPart.Position)
						bu.Text = "Teleported!"
						wait(0.5)
						bu.Text = a[i].Name
					end
				end)
			end
		elseif enabled == true then
			enabled = false
			pos2 = 10
			pos3 = 0
			local o = button:GetChildren()
			for i=1, #o do
				wait()
				o[i]:remove()
			end
		end
	end)
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Remote Finder"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Remote Finder"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local RemoteEventObject

	local gui = Instance.new("ScreenGui",game.Players./localplayer/.PlayerGui)
	gui.Name = "Remote Finder"
	local mainframe = Instance.new("Frame",gui)
	mainframe.Name = "MainFrame"
	mainframe.Position = UDim2.new(0.5,0,0.5,0)
	mainframe.Size = UDim2.new(0,350,0,250)
	mainframe.BackgroundTransparency = 0.5
	mainframe.BackgroundColor3 = blak
	mainframe.BorderSizePixel = 3
	mainframe.BorderColor3 = blue
	local scroll = Instance.new("ScrollingFrame",mainframe)
	scroll.Position = UDim2.new(0,0,0,0)
	scroll.Size = UDim2.new(0,200,0,213)
	scroll.BackgroundTransparency = 0.5
	scroll.BackgroundColor3 = blak
	scroll.BorderSizePixel = 3
	scroll.BorderColor3 = blue
	scroll.CanvasSize = UDim2.new(0,0,100,0)
	local close = Instance.new("TextButton",mainframe)
	close.Position = UDim2.new(0,0,0,217)
	close.Size = UDim2.new(0,200,0,33)
	close.BackgroundTransparency = 0.5
	close.BackgroundColor3 = blak
	close.BorderSizePixel = 3
	close.BorderColor3 = blue
	close.TextColor3 = whit
	close.Text = "Close"
	close.TextSize = 14
	close.Name = "Close Button"
	close.MouseButton1Down:connect(function()
		gui:remove()
	end)
	local infoframe = Instance.new("Frame",mainframe)
	infoframe.Name = "InfoFrame"
	infoframe.Position = UDim2.new(0,203,0,0)
	infoframe.Size = UDim2.new(0,150,0,246)
	infoframe.BackgroundTransparency = 0.5
	infoframe.BackgroundColor3 = blak
	infoframe.BorderSizePixel = 3
	infoframe.BorderColor3 = blue
	local infoname = Instance.new("TextLabel",infoframe)
	infoname.Position = UDim2.new(0,0,0,0)
	infoname.Size = UDim2.new(0,147,0,100)
	infoname.BackgroundTransparency = 0.5
	infoname.BackgroundColor3 = blak
	infoname.BorderSizePixel = 3
	infoname.BorderColor3 = blue
	infoname.TextColor3 = whit
	infoname.Text = "Full Name: "
	infoname.TextSize = 8
	infoname.Name = "InfoName"
	infoname.TextWrapped = true
	local fireserverbtn = Instance.new("TextButton",infoframe)
	fireserverbtn.Position = UDim2.new(0,0,0.5,0)
	fireserverbtn.Size = UDim2.new(0,147,0,50)
	fireserverbtn.BackgroundTransparency = 0.5
	fireserverbtn.BackgroundColor3 = blak
	fireserverbtn.BorderSizePixel = 3
	fireserverbtn.BorderColor3 = blue
	fireserverbtn.TextColor3 = whit
	fireserverbtn.Text = "FireServer"
	fireserverbtn.TextSize = 14
	fireserverbtn.Name = "FireServerButton"
	fireserverbtn.MouseButton1Down:Connect(function()  
		if RemoteEventObject ~= nil then
			if RemoteEventObject:IsA("RemoteEvent") then
				RemoteEventObject:InvokeClient(game.Players./localplayer/)
			elseif RemoteEventObject:IsA("RemoteFunction") then
				RemoteEventObject:InvokeServer(game.Players./localplayer/)
			end
		end
	end)
	local updateBtn = Instance.new("TextButton",infoframe)
	updateBtn.Position = UDim2.new(0,0,0.812,0)
	updateBtn.Size = UDim2.new(0,147,0,50)
	updateBtn.BackgroundTransparency = 0.5
	updateBtn.BackgroundColor3 = blak
	updateBtn.BorderSizePixel = 3
	updateBtn.BorderColor3 = blue
	updateBtn.TextColor3 = whit
	updateBtn.Text = "Update"
	updateBtn.TextSize = 18
	updateBtn.Name = "UpdateButton"
	updateBtn.MouseButton1Down:Connect(function()
		UpdateScrollingFrame()
	end)

	function UpdateScrollingFrame ()
		for i,v in pairs(scroll:GetChildren()) do
			v:remove()
		end
		local pos = 0
		for i,v in pairs(game:GetDescendants()) do
			if v:IsA("RemoteEvent") or v:IsA("RemoteFunction") then
				local button = Instance.new("TextButton",scroll)
				button.Position = UDim2.new(0,0,0,pos)
				button.Size = UDim2.new(0,200,0,30)
				button.BackgroundTransparency = 0.5
				button.BackgroundColor3 = blak
				button.BorderSizePixel = 3
				button.BorderColor3 = blue
				button.TextColor3 = whit
				button.Text = v.Name
				button.TextSize = 14
				button.Name = v.Name
				button.MouseButton1Down:Connect(function()
					infoname.Text = "Full Name: " .. v:GetFullName()
					RemoteEventObject = v
					if v:IsA("RemoteEvent") then
						fireserverbtn.Text = "FireClient"
					elseif v:IsA("RemoteFunction") then
						fireserverbtn.Text = "InvokeClient"
					end
					
				end)
				pos += 33
			end
		end
	end
	UpdateScrollingFrame()
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Scripts Hub"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Scripts Hub"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	local hubscripts = {
		{"Forsaken",loadstring(game:HttpGet("https://raw.githubusercontent.com/MaybeNotMandy/forsaken/refs/heads/main/sae"))},
		{"Grow a Garden",loadstring(game:HttpGet("https://raw.githubusercontent.com/greywaterstill/GAG/refs/heads/main/nathub.lua"))},
		{"Steal a Brainrot",loadstring(game:HttpGet("https://raw.githubusercontent.com/tienkhanh1/spicy/main/Chilli.lua"))}
	}
	
	
	local gui = Instance.new("ScreenGui",game.Players./localplayer/.PlayerGui)
	gui.Name = "Scripts Hub"
	local closebtn = Instance.new("TextButton",gui)
	closebtn.Name = "Close"
	closebtn.Text = "Close"
	closebtn.Position = UDim2.new(0.5,0,0.5,303)
	closebtn.Size = UDim2.new(0,200,0,30)
	closebtn.ZIndex = 2
	closebtn.Font = tef
	closebtn.FontSize = "Size14"
	closebtn.TextColor3 = whit
	closebtn.BackgroundTransparency = 0.5
	closebtn.BorderColor3 = blue
	closebtn.BackgroundColor3 = blak
	closebtn.BorderSizePixel = 3
	closebtn.MouseButton1Down:Connect(function()
		gui:remove()
	end)
	local scroll = Instance.new("ScrollingFrame",gui)
	scroll.BackgroundColor3 = blak
	scroll.BorderColor3 = blue
	scroll.BorderSizePixel = 3
	scroll.Position = UDim2.new(0.5,0,0.5,0)
	scroll.Size = UDim2.new(0,200,0,300)
	scroll.ZIndex = 2
	scroll.BackgroundTransparency = 0.5 
	
	local pos = 0
	
	for i,v in hubscripts do
		local btn = Instance.new("TextButton",scroll)
		btn.Name = v[1]
		btn.Position = UDim2.new(0,0,0,pos)
		btn.Size = UDim2.new(1,0,0,30)
		btn.ZIndex = 2
		btn.Font = tef
		btn.FontSize = "Size14"
		btn.Text = v[1]
		btn.TextColor3 = whit
		btn.BackgroundTransparency = 0.5
		btn.BackgroundColor3 = blak
		btn.BorderSizePixel = 3
		btn.TextWrapped = true
		btn.MouseButton1Down:Connect(function()
			v[2]()
		end)
		pos += 33
	end
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Teleport to Poses"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Teleport to Poses"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local poses = game.Players./localplayer/:findFirstChild("TpPoses")

	if poses == nil then
		poses = Instance.new("Folder",game.Players./localplayer/)
		poses.Name = "TpPoses"
	end
	local gui = Instance.new("ScreenGui",game.Players./localplayer/.PlayerGui)
	gui.Name = "Leaderstats editor"
	local btnon = Instance.new("BoolValue",gui)
	btnon.Name = "btnon"
	local mainframe = Instance.new("Frame",gui)
	mainframe.Name = "Main frame"
	mainframe.BackgroundColor3 = blak
	mainframe.BorderColor3 = blue
	mainframe.BorderSizePixel = 3
	mainframe.Position = UDim2.new(0.5,0,0.5,0)
	mainframe.Size = UDim2.new(0,300,0,300)
	mainframe.BackgroundTransparency = 0.5
	local scrolingframe = Instance.new("ScrollingFrame",mainframe)
	scrolingframe.BackgroundColor3 = blak
	scrolingframe.BorderColor3 = blue
	scrolingframe.BorderSizePixel = 3
	scrolingframe.Position = UDim2.new(0,0,0,0)
	scrolingframe.Size = UDim2.new(0,150,0,300)
	scrolingframe.BackgroundTransparency = 0.5
	scrolingframe.ScrollBarImageColor3 = whit
	local addstatframe = Instance.new("Frame",mainframe)
	addstatframe.Name = "Add stat frame"
	addstatframe.BackgroundColor3 = blak
	addstatframe.BorderColor3 = blue
	addstatframe.BorderSizePixel = 3
	addstatframe.Position = UDim2.new(0.5,0,0,0)
	addstatframe.Size = UDim2.new(0,150,0,300)
	addstatframe.BackgroundTransparency = 0.5
	addstatframe.Visible = false
	local changestatframe = Instance.new("Frame",mainframe)
	changestatframe.Name = "Change stat frame"
	changestatframe.BackgroundColor3 = blak
	changestatframe.BorderColor3 = blue
	changestatframe.BorderSizePixel = 3
	changestatframe.Position = UDim2.new(0.5,0,0,0)
	changestatframe.Size = UDim2.new(0,150,0,300)
	changestatframe.BackgroundTransparency = 0.5
	changestatframe.Visible = false
	local addstatbutton = Instance.new("TextButton",mainframe)
	addstatbutton.Name = "Add stat button"
	addstatbutton.BackgroundColor3 = blak
	addstatbutton.BorderColor3 = blue
	addstatbutton.BorderSizePixel = 3
	addstatbutton.Position = UDim2.new(0.51,0,0,0)
	addstatbutton.Size = UDim2.new(0,147,0,60)
	addstatbutton.ZIndex = 2
	addstatbutton.Font = tef
	addstatbutton.FontSize = "Size28"
	addstatbutton.Text = "Add pos"
	addstatbutton.TextColor3 = whit
	addstatbutton.TextWrapped = true
	addstatbutton.BackgroundTransparency = 0.5
	addstatbutton.MouseButton1Down:Connect(function()
		addstatframe.Visible = true
		addstatbutton.Visible = false
	end)
	btnon.Changed:Connect(function()
		if btnon.Value == false then
			addstatbutton.Visible = false
		else
			addstatbutton.Visible = true
		end
	end)
	local closebutton = Instance.new("TextButton",mainframe)
	closebutton.Name = "Close button"
	closebutton.BackgroundColor3 = blak
	closebutton.BorderColor3 = blue
	closebutton.BorderSizePixel = 3
	closebutton.Position = UDim2.new(0.51,0,0.8,0)
	closebutton.Size = UDim2.new(0,147,0,60)
	closebutton.ZIndex = 2
	closebutton.Font = tef
	closebutton.FontSize = "Size28"
	closebutton.Text = "Close"
	closebutton.TextColor3 = whit
	closebutton.TextWrapped = true
	closebutton.BackgroundTransparency = 0.5
	closebutton.MouseButton1Down:Connect(function()
		gui:Destroy()
	end)
	local addnametextlabel = Instance.new("TextLabel",addstatframe)
	addnametextlabel.Name = "Name text label"
	addnametextlabel.BackgroundColor3 = blak
	addnametextlabel.BorderColor3 = blue
	addnametextlabel.BorderSizePixel = 3
	addnametextlabel.Position = UDim2.new(0,0,0,0)
	addnametextlabel.Size = UDim2.new(0,150,0,30)
	addnametextlabel.ZIndex = 2
	addnametextlabel.Font = tef
	addnametextlabel.FontSize = "Size18"
	addnametextlabel.Text = "Name"
	addnametextlabel.TextColor3 = whit
	addnametextlabel.BackgroundTransparency = 0.5
	local addnametextbox = Instance.new("TextBox",addstatframe)
	addnametextbox.Name = "Name text box"
	addnametextbox.BackgroundColor3 = blak
	addnametextbox.BorderColor3 = blue
	addnametextbox.BorderSizePixel = 3
	addnametextbox.Position = UDim2.new(0,0,0,33)
	addnametextbox.Size = UDim2.new(0,150,0,30)
	addnametextbox.ZIndex = 2
	addnametextbox.Font = tef
	addnametextbox.FontSize = "Size18"
	addnametextbox.Text = ""
	addnametextbox.TextColor3 = whit
	addnametextbox.BackgroundTransparency = 0.5
	local addbuttonend = Instance.new("TextButton",addstatframe)
	addbuttonend.Name = "Add button"
	addbuttonend.BackgroundColor3 = blak
	addbuttonend.BorderColor3 = blue
	addbuttonend.BorderSizePixel = 3
	addbuttonend.Position = UDim2.new(0,0,0,99)
	addbuttonend.Size = UDim2.new(0,150,0,30)
	addbuttonend.ZIndex = 2
	addbuttonend.Font = tef
	addbuttonend.FontSize = "Size18"
	addbuttonend.Text = "Add"
	addbuttonend.TextColor3 = whit
	addbuttonend.BackgroundTransparency = 0.5
	addbuttonend.MouseButton1Down:Connect(function()
		local name = addnametextbox.Text
		local value = game.Players./localplayer/.Character.HumanoidRootPart.Position
		if name ~= "" then
			local stat = Instance.new("Vector3Value",poses)
			stat.Name = name
			stat.Value = value
			addnametextbox.Text = ""
		end
		btnon.Value = false
		btnon.Value = true
		addstatframe.Visible = false
	end)


	function Changelid(libname)
		changestatframe.Visible = true
		btnon.Value = true
		btnon.Value = false
		local stat = poses:FindFirstChild(libname)

		if stat then
			local chanstatbtn = Instance.new("TextButton",changestatframe)
			chanstatbtn.Position = UDim2.new(0,0,0,0)
			chanstatbtn.Size = UDim2.new(0,150,0,30)
			chanstatbtn.BackgroundColor3 = blak
			chanstatbtn.BackgroundTransparency = 0.5
			chanstatbtn.BorderColor3 = blue
			chanstatbtn.BorderSizePixel = 3
			chanstatbtn.Font = tef
			chanstatbtn.FontSize = "Size18"
			chanstatbtn.Text = "Change"
			chanstatbtn.TextColor3 = whit
			chanstatbtn.MouseButton1Down:Connect(function()
				btnon.Value = false
				btnon.Value = true
				local value = game.Players./localplayer/.Character.HumanoidRootPart.Position
				
				stat.Value = value
				
				changestatframe.Visible = false
				for i,v in pairs(changestatframe:GetChildren()) do
					v:Destroy()
				end
			end)
			local chanstatdelbtn = Instance.new("TextButton",changestatframe)
			chanstatdelbtn.Position = UDim2.new(0,0,0,33)
			chanstatdelbtn.Size = UDim2.new(0,150,0,30)
			chanstatdelbtn.BackgroundColor3 = blak
			chanstatdelbtn.BackgroundTransparency = 0.5
			chanstatdelbtn.BorderColor3 = blue
			chanstatdelbtn.BorderSizePixel = 3
			chanstatdelbtn.Font = tef
			chanstatdelbtn.FontSize = "Size18"
			chanstatdelbtn.Text = "Delete"
			chanstatdelbtn.TextColor3 = whit
			chanstatdelbtn.MouseButton1Down:Connect(function()
				stat:Destroy()
				changestatframe.Visible = false
				btnon.Value = false
				btnon.Value = true
				for i,v in pairs(changestatframe:GetChildren()) do
					v:Destroy()
				end

			end)
			local tpbtn = Instance.new("TextButton",changestatframe)
			tpbtn.Position = UDim2.new(0,0,0,66)
			tpbtn.Size = UDim2.new(0,150,0,30)
			tpbtn.BackgroundColor3 = blak
			tpbtn.BackgroundTransparency = 0.5
			tpbtn.BorderColor3 = blue
			tpbtn.BorderSizePixel = 3
			tpbtn.Font = tef
			tpbtn.FontSize = "Size18"
			tpbtn.Text = "Teleport"
			tpbtn.TextColor3 = whit
			tpbtn.MouseButton1Down:Connect(function()
				changestatframe.Visible = false
				btnon.Value = false
				btnon.Value = true
				game.Players./localplayer/.Character:MoveTo(stat.Value)
			end)
			local tpforsebtn = Instance.new("TextButton",changestatframe)
			tpforsebtn.Position = UDim2.new(0,0,0,99)
			tpforsebtn.Size = UDim2.new(0,150,0,30)
			tpforsebtn.BackgroundColor3 = blak
			tpforsebtn.BackgroundTransparency = 0.5
			tpforsebtn.BorderColor3 = blue
			tpforsebtn.BorderSizePixel = 3
			tpforsebtn.Font = tef
			tpforsebtn.FontSize = "Size18"
			tpforsebtn.Text = "Force Teleport"
			tpforsebtn.TextColor3 = whit
			tpforsebtn.MouseButton1Down:Connect(function()
				changestatframe.Visible = false
				btnon.Value = false
				btnon.Value = true
				for i=1,100 do
					game.Players./localplayer/.Character:MoveTo(stat.Value)
					wait(0.01)
				end
				game.Players./localplayer/.Character:MoveTo(stat.Value)
			end)
		end
	end


	function updateLiderstatFrame()
		local pos = 0

		for i,v in pairs(scrolingframe:GetChildren()) do
			if v:IsA("TextButton") then
				v:Destroy()
			end
		end
		for i,v in pairs(poses:GetChildren()) do
			local button = Instance.new("TextButton",scrolingframe)
			addstatframe.Visible = false
			addstatbutton.Visible = false
			button.Name = v.Name
			button.Text = v.Name
			button.Position = UDim2.new(0,0,0,pos)
			button.Size = UDim2.new(0,135,0,50)
			button.BackgroundColor3 = blak
			button.BorderColor3 = blue
			button.BorderSizePixel = 3
			button.Font = tef
			button.FontSize = "Size14"
			button.TextColor3 = whit
			button.BackgroundTransparency = 0.5
			pos += 53
			button.MouseButton1Down:Connect(function()
				Changelid(v.Name)
			end)
		end
	end
	updateLiderstatFrame()
	poses.ChildAdded:Connect(updateLiderstatFrame)
	poses.ChildRemoved:Connect(updateLiderstatFrame)
end)
local button = Instance.new("TextButton")
button.Parent = acg
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	
end)
local label = Instance.new("TextLabel")
label.Parent = gt
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Tools"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Tools"
label.TextColor3 = whit
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Noclip Tool"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Noclip Tool"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(253890420):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "F3X Tools"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "F3X Tools"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	require(4869378421).F3X('/localplayer/')
end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Steal All Tools"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Steal All Tools"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for i,v in pairs(game:GetDescendants()) do
		if v:IsA("Tool") then
			v.Parent = game.Players./localplayer/.Backpack
		end
	end
end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Gravity Coil"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Gravity Coil"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(16688968):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Speed Coil"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Speed Coil"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(99119158):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Nuke Tool"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Nuke Tool"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(10694662894):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Handcuffs Tool"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Handcuffs Tool"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(2628738594):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = gt
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local label = Instance.new("TextLabel")
label.Parent = ws
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Weapon Script"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Weapon Script"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Sword"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Sword"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(47433):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "HyperLazer Gun"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "HyperLazer Gun"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(130113146):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Knife"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Knife"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(4366818128):GetChildren()[1].Parent = game.Players.glebmalish_2000.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Subspace Tripmine"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Subspace Tripmine"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(11999247):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Forsaken Mafioso"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Forsaken Mafioso"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	require(89847131483512).Forsaken("/localplayer/","Mafioso")
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Ice Staff"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Ice Staff"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(19704064):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Staff Of The Winds"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Staff Of The Winds"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(18462637):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Knife"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Knife"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(4366818128):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Ban Hammer"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Ban Hammer"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	require(5448035802).Hammer("/localplayer/","BanHammer")
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Rainbow Periastron Omega"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Rainbow Periastron Omega"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	game.InsertService:LoadAsset(159229806):GetChildren()[1].Parent = game.Players./localplayer/.Backpack
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Server Admin"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Server Admin"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	require(4665394711).load("/localplayer/")
end)
local button = Instance.new("TextButton")
button.Parent = ws
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Sans"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Sans"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	require(4952709475).load("/localplayer/")
end)
local label = Instance.new("TextLabel")
label.Parent = localp
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Local Player"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Local Player"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Billboard Name Gui"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Billboard Name Gui"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	if game.Players./localplayer/.Character.Head:FindFirstChild("BillboardGui") then
		game.Players./localplayer/.Character.Head:FindFirstChild("BillboardGui"):Remove()	
	end
	plr = game.Players./localplayer/.Name
	y = Instance.new("BillboardGui")
	y.Size = UDim2.new(0,100,0,150)
	y.StudsOffset = Vector3.new(0,1,0)
	y.Parent = game.Players[plr].Character.Head
	y.Adornee = game.Players[plr].Character.Head
	f = Instance.new("TextLabel")
	f.Parent = y
	f.BackgroundTransparency = 1
	f.Position = UDim2.new(0,0,0,-50)
	f.Size = UDim2.new(0,100,0,100)
	f.Font = "Arial"
	f.FontSize = "Size48"
	f.Text = game.Players./localplayer/.DisplayName
	f.TextStrokeColor3 = Color3.new(0,0,0)
	f.TextColor3 = blue
	f.TextStrokeTransparency = 0
	f.TextYAlignment = "Bottom"
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Heal"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Heal"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.Players./localplayer/.Character.Humanoid.Health = game.Players./localplayer/.Character.Humanoid.MaxHealth
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Set Walkspeed"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Set\nWalkspeed"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.Players./localplayer/.Character.Humanoid.WalkSpeed = frame.Settings.Page2["WalkSpeed"].Text
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Clone"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Clone"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	local Main = game.Players:GetHumanoidDescriptionFromUserId(game.Players./localplayer/.CharacterAppearanceId)
	local morph = game.Players:CreateHumanoidModelFromDescription(Main, Enum.HumanoidRigType.R6)
	morph:SetPrimaryPartCFrame(game.Players./localplayer/.Character.PrimaryPart.CFrame)
	morph.Parent = game.workspace
	morph.Name = "plyclon"
	local char = morph
	local model = Instance.new("Model", char)
	local clone = char.Head:Clone()
	local hum = Instance.new("Humanoid", model)
	local weld = Instance.new("Weld", clone)
	model.Name = game.Players./localplayer/.Name
	clone.Parent = model
	hum.Name = "TAG"
	hum.MaxHealth = 100
	hum.Health = 100
	weld.Part0 = clone
	weld.Part1 = char.Head
	char.Head.Transparency = 1
	morph.Humanoid.HealthChanged:Connect(function()
		function remgui()
			for _,v in pairs(game.Players./localplayer/.PlayerGui:GetChildren()) do
				if v.Name == "Modeshow" then
					v:remove()
				end
			end
		end

		function inform(text,delay)
			remgui()
			local sc = Instance.new("ScreenGui")
			sc.Parent = game.Players./localplayer/.PlayerGui
			sc.Name = "Modeshow"
			local bak = Instance.new("Frame",sc)
			bak.BackgroundColor3 = Color3.new(1,1,1)
			bak.Size = UDim2.new(0.94,0,0.1,0)
			bak.Position = UDim2.new(0.03,0,0.037,0)
			bak.BorderSizePixel = 0
			local gi = Instance.new("TextLabel",sc)
			gi.Size = UDim2.new(0.92,0,0.09,0)
			gi.BackgroundColor3 = Color3.new(0,0,0)
			gi.Position = UDim2.new(0.04,0,0.042,0)
			gi.TextColor3 = Color3.new(1,1,1)
			gi.FontSize = "Size12"
			gi.Text = text
			coroutine.resume(coroutine.create(function()
				wait(delay)
				sc:remove()
			end))
		end

		if morph.Humanoid.Health == 0 then
			inform("Clone Killed!",2)
		end
	end)
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Delete all clones"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Delete all clones"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	for i,v in pairs(workspace:GetChildren()) do
		if v.Name == "plyclon" then
			v:remove()
		end
	end
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Set\nJumpPower"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Set\nJumpPower"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.Players./localplayer/.Character.Humanoid.JumpPower = frame.Settings.Page2["JumpPower"].Text
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Spin Gui"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Spin Gui"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local gui = Instance.new("ScreenGui",game.Players./localplayer/.PlayerGui)
	gui.Name = "SpinGui"
	
	local enabled = Instance.new("BoolValue",gui)
	enabled.Name = "enabled"
	
	local mainframe = Instance.new("Frame",gui)
	mainframe.Position = UDim2.new(0.5,0,0.7,0)
	mainframe.Size = UDim2.new(0,100,0,100)
	mainframe.BackgroundColor3 = Color3.new(0,0,0)
	mainframe.BackgroundTransparency = 0.5
	mainframe.BorderSizePixel = 0
	mainframe.ZIndex = 2
	mainframe.BackgroundColor3 = blak
	mainframe.BorderColor3 = blue
	mainframe.BorderSizePixel = 3
	local button = Instance.new("TextButton",mainframe)
	button.Position = UDim2.new(0,0,0,0)
	button.Size = UDim2.new(1,0,1,0)
	button.ZIndex = 2
	button.Font = tef
	button.FontSize = "Size14"
	button.Text = "Spin false"
	button.TextColor3 = whit
	button.BackgroundTransparency = 0.5
	button.BorderColor3 = blue
	button.BorderSizePixel = 3
	button.BackgroundColor3 = blak
	button.TextSize = 24
	button.MouseButton1Down:connect(function()
		enabled.Value = not enabled.Value
		button.Text = "Spin "..tostring(enabled.Value)
	end)
	
	local rootpart = game.Players./localplayer/.Character.HumanoidRootPart
	
	enabled.Changed:connect(function()
		local spinSpeed = frame.Settings.Page2["SpinSpeed"].Text
		while enabled.Value do
			rootpart.CFrame = rootpart.CFrame * CFrame.Angles(0,math.rad(spinSpeed),0)
			wait(0.001)
		end
	end)
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Floating Pad"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Floating Pad"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local name = game.Players./localplayer/.Name

	if game.Workspace:FindFirstChild("FloatingPad;" .. name) then
		game.Workspace:FindFirstChild("FloatingPad;" .. name):Destroy()
		return
	end
	
	local p = Instance.new("Part")
	p.Name = "FloatingPad;" .. name
	p.Parent = workspace
	p.Locked = true
	p.BrickColor = BrickColor.new("White")
	p.BrickColor = BrickColor.new(104)
	p.Size = Vector3.new(8, 1.2, 8)
	p.Anchored = true
	local m = Instance.new("CylinderMesh")
	m.Scale = Vector3.new(1, 0.5, 1)
	m.Parent = p
	while p ~= nil do
		p.CFrame = CFrame.new(game.Players:findFirstChild(name).Character.Torso.CFrame.x, game.Players:findFirstChild(name).Character.Torso.CFrame.y - 4, game.Players:findFirstChild(name).Character.Torso.CFrame.z)
		task.wait()
	end
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Chicken Arms"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Chicken Arms R6"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local Chicken = game.Players./localplayer/.Character
	Chicken.Torso["Left Shoulder"].C0 = CFrame.new(-1.5, 0.5, 0) * CFrame.fromEulerAnglesXYZ(0,math.pi/2,0) * CFrame.fromEulerAnglesXYZ(math.pi/2, 0, 0) * CFrame.fromEulerAnglesXYZ(0,-math.pi/2,0)
	Chicken.Torso["Left Shoulder"].C1 = CFrame.new(0, 0.5, 0)
	Chicken.Torso["Right Shoulder"].C0 = CFrame.new(1.5, 0.5, 0) * CFrame.fromEulerAnglesXYZ(0,-math.pi/2,0) * CFrame.fromEulerAnglesXYZ(math.pi/2, 0, 0) * CFrame.fromEulerAnglesXYZ(0,-math.pi/2,0)
	Chicken.Torso["Right Shoulder"].C1 = CFrame.new(0, 0.5, 0)
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Head Shake"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Head Shake R6"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	for X = 1, math.huge, 0.2 do 
		wait() 
		game.Players./localplayer/.Character.Torso.Neck.C0 = CFrame.new(math.sin(X) / 1,1.5,0) 
		game.Players./localplayer/.Character.Torso.Neck.C1 = CFrame.new(0,0,0) 
	end 
	for X = 1, math.huge, 0.1 do 
		wait() 
		game.Players./localplayer/.Character.Name.Torso.Neck.C0 = CFrame.new(0,1.5,0) * CFrame.fromAxisAngle(Vector3.new(0,1,0), X) 
		game.Players./localplayer/.Character.Name.Torso.Neck.C1 = CFrame.new(0,0,0) 
	end 
	for _,c in pairs(game.Players:GetChildren()) do
		c.Character.Head.Mesh.Scale = Vector3.new(100, 100, 100)
	end
	for _,c in pairs(game.Players:GetChildren()) do
		c.Character.Head.Mesh.Scale = Vector3.new(1.25, 1.25, 1.25)
	end
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Mesh Disco"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Mesh Disco R6"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	plr = game.Players./localplayer/.Character
	meshes = {"Brick","Cylinder","Head","Sphere","Torso","Wedge"}
	h = game.Players./localplayer/.Character.Head.Mesh
	t = Instance.new("SpecialMesh",plr.Torso)
	la = Instance.new("SpecialMesh",plr["Left Arm"])
	ra = Instance.new("SpecialMesh",plr["Right Arm"])
	ll = Instance.new("SpecialMesh",plr["Left Leg"])
	rl = Instance.new("SpecialMesh",plr["Right Leg"])
	while plr.Humanoid.Health ~= 0 do
		wait(0.1)
		h.MeshType = meshes[math.random(1,#meshes)]
		h.Parent.BrickColor = BrickColor.Random()
		t.MeshType = meshes[math.random(1,#meshes)]
		t.Parent.BrickColor = BrickColor.Random()
		la.MeshType = meshes[math.random(1,#meshes)]
		la.Parent.BrickColor = BrickColor.Random()
		ra.MeshType = meshes[math.random(1,#meshes)]
		ra.Parent.BrickColor = BrickColor.Random()
		ll.MeshType = meshes[math.random(1,#meshes)]
		ll.Parent.BrickColor = BrickColor.Random()
		rl.MeshType = meshes[math.random(1,#meshes)]
		rl.Parent.BrickColor = BrickColor.Random()
	end	
end)
local button = Instance.new("TextButton")
button.Parent = localp
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Disco Character"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Disco Character"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	presets = {"Bright red","Bright yellow","Bright orange","Bright violet","Bright blue","Bright bluish green","Bright green"}
	while game.Players./localplayer/.Character.Health ~= 0 do
		wait(0.5)
		ye = game.Players./localplayer/.Character:GetChildren()
		for i,v in pairs(ye) do
			if v.className == "Part" then
				v.BrickColor = BrickColor.new(presets[math.random(1,#presets)])
			end
		end
	end
end)
local label = Instance.new("TextLabel")
label.Parent = misc
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Misc"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Misc"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Become Owner in Personal Server"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Become Owner [PS]"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	while game.Players./localplayer/.PersonalServerRank<255 do
		game:GetService("PersonalServerService"):Promote(game.Players./localplayer/)
	end
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Disco Fog"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Disco Fog"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	local basics = {Color3.new(255/255,0/255,0/255),Color3.new(255/255,85/255,0/255),Color3.new(218/255,218/255,0/255),Color3.new(0/255,190/255,0/255),Color3.new(0/255,85/255,255/255),Color3.new(0/255,0/255,127/255),Color3.new(170/255,0/255,255/255),Color3.new(0/255,204/255,204/255),Color3.new(255/255,85/255,127/255),Color3.new(0/255,0/255,0/255),Color3.new(255/255,255/255,255/255)}
	game.Lighting.FogStart = 25
	game.Lighting.FogEnd = 300
	while true do
		wait(0.5)
		game.Lighting.FogColor = basics[math.random(1,#basics)]
	end
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Play Music"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Play Music"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for i,v in pairs(game.Workspace:GetChildren()) do
		if v.className == "Sound" then
			v:Stop()
			v:Remove()	
		end	
	end
	s = Instance.new("Sound",workspace)
	s.SoundId = "rbxassetid://"..frame.Settings.Page1["Music Id"].Text
	s.Volume = 1
	s.Looped = true
	s.Pitch = frame.Settings.Page1["Music Pitch"].Text
	if frame.Settings.Page1["Music Id"].Text == "72089843969979" then
		s.PlaybackSpeed = 0.19
	end
	s:Play()
	wait(.1)
	s:Play()
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Stop Music"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Stop Music"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for i,v in pairs(game.Workspace:GetChildren()) do
		if v.className == "Sound" then
			v:Stop()
			v:Remove()	
		end	
	end
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Restore Skybox"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Restore\nSkybox"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	for i,v in pairs(game.Lighting:GetChildren()) do
		v:Remove()
	end
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Restore Game"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Restore\nGame"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for i,v in pairs(game.Lighting:GetChildren()) do
		v:Remove()
	end
	
	for i,v in pairs(game.Teams:GetChildren()) do
		v:Remove()
	end
	
	local playersFolder = Instance.new("Folder",game.Workspace)
	playersFolder.Name = "Players"
	
	for i,v in pairs(game.Workspace:GetDescendants()) do
		if v.className == "Model" and game.Players:FindFirstChild(v.Name) ~= nil and v:FindFirstChild("Humanoid") ~= nil then
			v.Parent = playersFolder
		end
	end

	local ToDelete = {
	game.Workspace,
	game.ReplicatedStorage,
	game.ServerScriptService,
	game.StarterGui,
	game.StarterPack,
	game.StarterPlayer.StarterPlayerScripts,
	game.StarterPlayer.StarterCharacterScripts,
	game.Teams
	}
	
	for _,v in pairs(ToDelete) do
		for _,vv in pairs(v:GetChildren()) do
			if v.Name ~= "Terrain" and v.Name ~= "Camera" and v ~= playersFolder then
				v:Remove()
			end
		end
	end
	
	local pt = Instance.new("Part")
	pt.BrickColor = BrickColor.new("Silver")
	pt.Anchored = true
	pt.CanCollide = true
	pt.BottomSurface = "Weld"
	pt.Parent = workspace
	pt.Name = (math.random(1,1000000))
	pt.Size = Vector3.new(1000, 1, 1000)
	pt.Color = Color3.new(0, 0.4, 0)
	
	if game["Run Service"]:IsServer() then
		local house = game.InsertService:LoadAsset(76404164510571)
		house.Parent = game.Workspace
		house.Name = "House"
		house:MoveTo(Vector3.new(-33.889, 22.8, 52.982))
	end
	
	local spawns = Instance.new("SpawnLocation")
	spawns.Position = Vector3.new(-33.889, 22.8, 52.982)
	spawns.Parent = game.Workspace
	spawns.Name = "SpawnLocation"
	spawns.Anchored = true
	for i,v in pairs(playersFolder:GetChildren()) do
		v.Parent = game.Workspace
		v:MoveTo(spawns.Position)
	end
	
	playersFolder:Destroy()
	
	local notify = Instance.new("Message",game.Workspace)
	notify.Text = "Game restored."
	wait(2)
	notify:Remove()
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Restore Decals"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Restore\nDecals"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for _,v in pairs(game:GetDescendants()) do
	if v:IsA("Decal") then
		v.Parent = nil
	end
end
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Restore Particles"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Restore\nParticles"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	for _,v in pairs(game:GetDescendants()) do
	if v:IsA("ParticleEmitter") then
		v.Parent = nil
	end
end
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Save Game"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Save Game"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	local ToSave = {
		game.Workspace,
		game.ReplicatedStorage,
		game.ServerScriptService,
		game.StarterGui,
		game.StarterPack,
		game.StarterPlayer.StarterPlayerScripts,
		game.StarterPlayer.StarterCharacterScripts,
		game.Teams,
		game.Lighting
	}
	
	local saveStorage = game.ServerStorage:FindFirstChild("SaveStorage")
	if saveStorage == nil then
		saveStorage = Instance.new("Folder",game.ServerStorage)
		saveStorage.Name = "SaveStorage"
	end
	
	for _,v in saveStorage:GetChildren() do
		v:Destroy()
	end
	
	for _,v in ToSave do
		local saveFolder = Instance.new("Folder",saveStorage)
		saveFolder.Name = v.Name
	end

	for _,v in ToSave do
		for _,vv in v:GetChildren() do
			if vv.Name ~= "Terrain" and vv.Name ~= "Camera" then
				if game.Players:FindFirstChild(vv.Name) == nil then
					pcall(function()
						local clone = vv:Clone()
						clone.Parent = saveStorage[v.Name]
						if clone:IsA("Script") or clone:IsA("LocalScript") then
							clone:SetAttribute("beEnable",clone.Enabled)
							clone.Enabled = false
						end
					end)
				end
			end
		end
	end
	
	local endMessage = Instance.new("Message",workspace)
	endMessage.Text = "Game saved"
	wait(3)
	endMessage:Destroy()
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Load Game"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Load Game"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	local ToLoad = {
		game.Workspace,
		game.ReplicatedStorage,
		game.ServerScriptService,
		game.StarterGui,
		game.StarterPack,
		game.StarterPlayer.StarterPlayerScripts,
		game.StarterPlayer.StarterCharacterScripts,
		game.Teams,
		game.Lighting
	}
	
	local saveStorage = game.ServerStorage:FindFirstChild("SaveStorage")
	local plrFolder = game.Workspace:FindFirstChild("Players")
	if plrFolder == nil then
		plrFolder = Instance.new("Folder",game.Workspace)
		plrFolder.Name = "Players"
	end
	for _,v in pairs(game.Players:GetChildren()) do
		v.Character.Parent = plrFolder
	end
	if saveStorage ~= nil then
		for _,v in ToLoad do
			for _,vv in v:GetChildren() do
				if vv.Name ~= "Terrain" and vv.Name ~= "Camera" then
					if vv ~= plrFolder then
						vv:Destroy()
					end
				end
			end
		end
			
		for _,v in ToLoad do
			for _,vv in saveStorage[v.Name]:GetChildren() do
				local clone = vv:Clone()
				clone.Parent = v
				if clone:IsA("Script") or clone:IsA("LocalScript") then
					local atr = clone:GetAttributes()
					if atr ~= nil then
						clone.Enabled = atr["beEnable"]
					else
						clone.Enabled = false
					end
				end
			end			
		end	
		local endMessage = Instance.new("Message",workspace)
		endMessage.Text = "Game loaded"
		wait(3)
		endMessage:Destroy()
	else
		local endMessage = Instance.new("Message",workspace)
		endMessage.Text = "Save Not Found"
		wait(3)
		endMessage:Destroy()
	end
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Time Day"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Time Day"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.Lighting.ClockTime = 12
end)
local button = Instance.new("TextButton")
button.Parent = misc
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Time Night"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Time Night"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	game.Lighting.ClockTime = 0
end)
local label = Instance.new("TextLabel")
label.Parent = pmi
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Preset Music IDs"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Preset Music IDs"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Chop Suey"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Chop Suey"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 1846919373
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Electro Sp00k"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Electro Sp00k"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 72089843969979
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Scream"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Scream"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 138097458	
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Fun"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Fun"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 4702564143
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Cat chase"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Cat chase"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 1839444520
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "ERROR 264"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "ERROR 264"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 140009716850576
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Ready Or Not"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Ready Or Not"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 83683960727365
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "FREAKBOB"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "FREAKBOB"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 133170570098799
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Chil"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Chil"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 1848354536
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Raining Tacos"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Raining Tacos"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 142376088
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Elevator"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Elevator"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 1841647093
end)
local button = Instance.new("TextButton")
button.Parent = pmi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "ROBLOX PHONK"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "ROBLOX PHONK"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Music Id"].Text = 136932193331774
end)
local label = Instance.new("TextLabel")
label.Parent = psd
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Preset Decal IDs"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Preset Decal IDs"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Thomas"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Thomas"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 160456772
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Penguin"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Penguin"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 104745398169988
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Cool Cat"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Cool Cat"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 8073107221
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Gaming"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Gaming"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 8508980527
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Epic Face"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Epic Face"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 56369539
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Troll Face"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Troll Face"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 7120897383
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Super Clown"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Super Clown"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 7866490119
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Super Guy"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Super Guy"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 11818627057
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Happy"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Happy"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 2296760918
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Spoky"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Spoky"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 45524735
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "comfortable headphones"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "comfortable\nheadphones"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 124142247223281
end)
local button = Instance.new("TextButton")
button.Parent = psd
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Fun"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Fun"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	frame.Settings.Page1["Decal Id"].Text = 12886904115
end)
local label = Instance.new("TextLabel")
label.Parent = edn
label.Name = "Text"
label.Size = UDim2.new(1,0,1,0)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size14"
label.Text = "Empty"
label.TextColor3 = whit
label.BackgroundColor3 = blak
label.TextWrapped = true
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.TextXAlignment = "Left"
label.TextYAlignment = "Top"
label.TextSize = "32"
label.TextColor3 = whit
label.Text = "Its Testing\n\nJust Testing\n\nInspired by\nCoolGui"
--do there
local label = Instance.new("TextLabel")
label.Parent = pgi
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Test Tools"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 2
label.Font = tef
label.FontSize = "Size18"
label.Text = "Test Tools"
label.TextColor3 = whit

local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Give gleb Guis"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Give gleb Guis"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local assecure = Instance.new("Accessory",game.Players./localplayer/.Character)
	assecure.AccessoryType = Enum.AccessoryType.Front
	local handle = Instance.new("Part",assecure)
	handle.Name = "Handle"
	handle.Size = Vector3.new(5.022,1.706,2.083)
	handle.CanCollide = false
	local mesh = Instance.new("SpecialMesh",handle)
	mesh.MeshId = "rbxassetid://83949411845340"
	mesh.TextureId = "rbxassetid://111795190105906"
	mesh.Offset = Vector3.new(0, 0, -1)
	local atacment = Instance.new("Attachment",handle)
	atacment.Position = Vector3.new(0.095,-0.324,0.437)
	atacment.SecondaryAxis = Vector3.new(0.009,1,-0.018)
	atacment.Axis = Vector3.new(0.998,-0.01,-0.058)
	local weld = Instance.new("Weld",handle)
	weld.Part0 = game.Players./localplayer/.Character.HumanoidRootPart
	weld.Part1 = handle
end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Tp to random player"
button.Position = UDim2.new(0.5,0,0,33)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Tp to random player"
button.TextColor3 = whit
button.TextWrapped = true
button.MouseButton1Down:connect(function()
	local a = game.Players:GetChildren()
	local plrchose = a[math.random(1,#a)]
	if plrchose ~= game.Players./localplayer/ then
		game.Players./localplayer/.Character:MoveTo(plrchose.Character.HumanoidRootPart.Position)
	end
end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Disco all"
button.Position = UDim2.new(0,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Disco all"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	if game.StarterPlayer.StarterCharacterScripts:FindFirstChild("DiscoAllScript") then
		game.StarterPlayer.StarterCharacterScripts.DiscoAllScript:Destroy()
		return
	end
	game.InsertService:LoadAsset(130320595834716):GetChildren()[1].Parent = game.StarterPlayer.StarterCharacterScripts
end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Get closest player"
button.Position = UDim2.new(0.5,0,0,66)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Get closest\nplayer"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	local a = game.Players:GetChildren()
	local b = {
		Player = nil,
		Distance = nil
	}
	for i,v in pairs(a) do
		if v ~= game.Players./localplayer/ then
			if a.Distance == nil then
				b.Player = v
				b.Distance = v:DistanceFromCharacter(game.Players./localplayer/.Character.HumanoidRootPart.Position)
			else
				if v:DistanceFromCharacter(game.Players./localplayer/.Character.HumanoidRootPart.Position) < b.Distance then
					b.Player = v
					b.Distance = v.DistanceFromCharacter
				end
			end
		end
	end
	
	if b.Player == nil and b.Distance == nil then
		local mes = Instance.new("Message")
		mes.Parent = game.Players./localplayer/.PlayerGui
		mes.Text = "No players found"
		wait(1.5)
		mes:Destroy()
	else
		local mes = Instance.new("Message")
		mes.Parent = game.Players./localplayer/.PlayerGui
		mes.Text = "The closest player is "..b.Player.Name.." and the distance is "..b.Distance
		wait(1.5)
		mes:Destroy()
	end
end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0.5,0,0,99)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0.5,0,0,132)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0.5,0,0,165)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
local button = Instance.new("TextButton")
button.Parent = pgi
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Empty"
button.Position = UDim2.new(0.5,0,0,198)
button.Size = UDim2.new(0.5,0,0,30)
button.ZIndex = 2
button.Font = tef
button.FontSize = "Size14"
button.Text = "Empty"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()

end)
--settings--
local pge1 = Instance.new("Frame")
pge1.Parent = page
pge1.BorderColor3 = blue
pge1.BackgroundColor3 = blak
pge1.BorderSizePixel = 3
pge1.Name = "Page1"
pge1.Position = UDim2.new(0,0,0,83)
pge1.Size = UDim2.new(1,0,1,-83)
pge1.ZIndex = 1

local pge2 = Instance.new("Frame")
pge2.Parent = page
pge2.BorderColor3 = blue
pge2.BackgroundColor3 = blak
pge2.BorderSizePixel = 3
pge2.Name = "Page2"
pge2.Position = UDim2.new(0,0,0,83)
pge2.Size = UDim2.new(1,0,1,-83)
pge2.ZIndex = 1
pge2.Visible = false
local lft = Instance.new("TextButton")
lft.Parent = page
lft.BorderColor3 = blue
lft.BackgroundColor3 = blak
lft.BorderSizePixel = 3
lft.Name = ">"
lft.Position = UDim2.new(0.5,3,0,40)
lft.Size = UDim2.new(0.5,-3,0,40)
lft.ZIndex = 1
lft.Font = tef
lft.FontSize = "Size48"
lft.Text = ">"
lft.TextColor3 = whit
lft.MouseButton1Down:connect(function()
	if pge1.Visible == true then
		pge1.Visible = false
		pge2.Visible = true
	elseif pge2.Visible == true then
		pge2.Visible = false
		pge1.Visible = true
	end	
end)
local rgt = Instance.new("TextButton")
rgt.Parent = page
rgt.BorderColor3 = blue
rgt.BackgroundColor3 = blak
rgt.BorderSizePixel = 3
rgt.Name = "<"
rgt.Position = UDim2.new(0,0,0,40)
rgt.Size = UDim2.new(0.5,0,0,40)
rgt.ZIndex = 1
rgt.Font = tef
rgt.FontSize = "Size48"
rgt.Text = "<"
rgt.TextColor3 = whit
rgt.MouseButton1Down:connect(function()
	if pge1.Visible == true then
		pge1.Visible = false
		pge2.Visible = true
	elseif pge2.Visible == true then
		pge2.Visible = false
		pge1.Visible = true
	end	
end)

local sbutton = Instance.new("TextButton")
sbutton.Parent = page
sbutton.BackgroundColor3 = blak
sbutton.BorderColor3 = blue
sbutton.BorderSizePixel = 3
sbutton.Name = "SettingsButton"
sbutton.Position = UDim2.new(1,3,0,0)
sbutton.Size = UDim2.new(0,27,1,0)
sbutton.Font = tef
sbutton.FontSize = "Size48"
sbutton.TextColor3 = whit
sbutton.Text = "<"
cango = true
sbutton.MouseButton1Down:connect(function()
	if cango == true then
		if sbutton.Text == "<" then
			sbutton.Text = ">"
			cango = false
			repeat
				wait()
				page.Position = UDim2.new(1,page.Position.X.Offset-10,0,0)
			until page.Position.X.Offset <= -293
			wait()
			page.Position = UDim2.new(1,-300,0,0)
			cango = true
		else
			sbutton.Text = "<"
			cango = false
			repeat
				wait()
				page.Position = UDim2.new(1,page.Position.X.Offset+10,0,0)
			until page.Position.X.Offset >= -10
			wait()
			page.Position = UDim2.new(1,3,0,0)
			cango = true
		end	
	end
end)
local title = Instance.new("TextLabel")
title.Parent = page
title.BackgroundColor3 = blak
title.BorderColor3 = blue
title.BorderSizePixel = 3
title.Name = "Title"
title.Position = UDim2.new(0,0,0,0)
title.Size = UDim2.new(1,0,0,40)
title.ZIndex = 1
title.Font = tef
title.FontSize = "Size24"
title.Text = "Settings"
title.TextColor3 = whit

local label = Instance.new("TextLabel")
label.Parent = pge1
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "God label"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "God"
label.TextColor3 = whit
local button = Instance.new("TextButton")
button.Parent = pge1
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "God Btn"
button.Position = UDim2.new(0,0,0,33)
button.Size = UDim2.new(1,0,0,30)
button.ZIndex = 1
button.Font = tef
button.FontSize = "Size24"
button.Text = "Off"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	if button.Text == "Off" then
		button.Text = "On"
		game.Players./localplayer/.Character.Humanoid.MaxHealth = math.huge
		game.Players./localplayer/.Character.Humanoid.Health = math.huge
	else
		button.Text = "Off"
		game.Players./localplayer/.Character.Humanoid.MaxHealth = 100
		game.Players./localplayer/.Character.Humanoid.Health = 100
	end
end)

local label = Instance.new("TextLabel")
label.Parent = pge1
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "NoTarget label"
label.Position = UDim2.new(0,0,0,66)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "NoTarget"
label.TextColor3 = whit
local button = Instance.new("TextButton")
button.Parent = pge1
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "NoTarget Btn"
button.Position = UDim2.new(0,0,0,99)
button.Size = UDim2.new(1,0,0,30)
button.ZIndex = 1
button.Font = tef
button.FontSize = "Size24"
button.Text = "Off"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	if button.Text == "Off" then
		button.Text = "On"
		for i,v in pairs(game.Players./localplayer/.Character:GetChildren()) do
			if v:IsA("Part") or v:IsA("MeshPart") then
				v.CanCollide = false
				v.CanTouch = false
				v.CanQuery = false
			end
		end
	else
		button.Text = "Off"
		for i,v in pairs(game.Players./localplayer/.Character:GetChildren()) do
			if v:IsA("Part") or v:IsA("MeshPart") then
				v.CanCollide = true
				v.CanTouch = true
				v.CanQuery = true
			end
		end
	end
end)

local label = Instance.new("TextLabel")
label.Parent = pge1
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Invisibility label"
label.Position = UDim2.new(0,0,0,132)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "Invisibility"
label.TextColor3 = whit
local button = Instance.new("TextButton")
button.Parent = pge1
button.BackgroundColor3 = blak
button.BorderColor3 = blue
button.BorderSizePixel = 3
button.Name = "Invisibility Btn"
button.Position = UDim2.new(0,0,0,165)
button.Size = UDim2.new(1,0,0,30)
button.ZIndex = 1
button.Font = tef
button.FontSize = "Size24"
button.Text = "Off"
button.TextColor3 = whit
button.MouseButton1Down:connect(function()
	function exPro (root,ex)
		for i,v in pairs(root:GetChildren()) do
			if v:IsA("Part") or v:IsA("MeshPart") or v:IsA("Decal") then
				if v.Name ~= "HumanoidRootPart" then
					v.Transparency = ex
				end
			end
			exPro(v,ex)
		end
	end

	function fsdz (root)
		for i,v in pairs(root:GetChildren()) do
			fsdz(v)
		end
	end

	if button.Text == "Off" then
		button.Text = "On"
		for i,v in pairs(game.Players./localplayer/.Character:GetChildren()) do
			if v:IsA("Part") or v:IsA("MeshPart") then
				exPro(game.Players./localplayer/.Character,1)
				fsdz(game.Players./localplayer/.Character)
			end
		end
	else
		button.Text = "Off"
		for i,v in pairs(game.Players./localplayer/.Character:GetChildren()) do
			if v:IsA("Part") or v:IsA("MeshPart") then
				exPro(game.Players./localplayer/.Character,0)
				fsdz(game.Players./localplayer/.Character)
			end
		end
	end
end)
local label = Instance.new("TextLabel")
label.Parent = pge1
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Decal Id label"
label.Position = UDim2.new(0,0,0,198)
label.Size = UDim2.new(0.5,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "Decal Id"
label.TextColor3 = whit
local textbox = Instance.new("TextLabel")
textbox.Parent = pge1
textbox.BackgroundColor3 = blak
textbox.BorderColor3 = blue
textbox.BorderSizePixel = 3
textbox.Name = "Decal Id"
textbox.Position = UDim2.new(0,0,0,231)
textbox.Size = UDim2.new(0.5,0,0,30)
textbox.ZIndex = 1
textbox.Font = tef
textbox.FontSize = "Size18"
textbox.Text = "104745398169988"
textbox.TextColor3 = whit
local label = Instance.new("TextLabel")
label.Parent = pge1
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Music Id label"
label.Position = UDim2.new(0.5,0,0,198)
label.Size = UDim2.new(0.5,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "Music Id"
label.TextColor3 = whit
local textbox = Instance.new("TextLabel")
textbox.Parent = pge1
textbox.BackgroundColor3 = blak
textbox.BorderColor3 = blue
textbox.BorderSizePixel = 3
textbox.Name = "Music Id"
textbox.Position = UDim2.new(0.5,0,0,231)
textbox.Size = UDim2.new(0.5,0,0,30)
textbox.ZIndex = 1
textbox.Font = tef
textbox.FontSize = "Size18"
textbox.Text = "1839444520"
textbox.TextColor3 = whit
local label = Instance.new("TextLabel")
label.Parent = pge1
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Place Id label"
label.Position = UDim2.new(0,0,0,264)
label.Size = UDim2.new(0.5,0,0,25)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "Place Id"
label.TextColor3 = whit
local textbox = Instance.new("TextLabel")
textbox.Parent = pge1
textbox.BackgroundColor3 = blak
textbox.BorderColor3 = blue
textbox.BorderSizePixel = 3
textbox.Name = "Place Id"
textbox.Position = UDim2.new(0,0,0,290)
textbox.Size = UDim2.new(0.5,0,0,25)
textbox.ZIndex = 1
textbox.Font = tef
textbox.FontSize = "Size18"
textbox.Text = "9503966785"
textbox.TextColor3 = whit
local label = Instance.new("TextLabel")
label.Parent = pge1
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "Music Pitch label"
label.Position = UDim2.new(0.5,0,0,264)
label.Size = UDim2.new(0.5,0,0,25)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "Music Pitch"
label.TextColor3 = whit
local textbox = Instance.new("TextLabel")
textbox.Parent = pge1
textbox.BackgroundColor3 = blak
textbox.BorderColor3 = blue
textbox.BorderSizePixel = 3
textbox.Name = "Music Pitch"
textbox.Position = UDim2.new(0.5,0,0,290)
textbox.Size = UDim2.new(0.5,0,0,25)
textbox.ZIndex = 1
textbox.Font = tef
textbox.FontSize = "Size18"
textbox.Text = "1"
textbox.TextColor3 = whit

local label = Instance.new("TextLabel")
label.Parent = pge2
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "WalkSpeed label"
label.Position = UDim2.new(0,0,0,0)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "WalkSpeed"
label.TextColor3 = whit
local textbox = Instance.new("TextButton")
textbox.Parent = pge2
textbox.BackgroundColor3 = blak
textbox.BorderColor3 = blue
textbox.BorderSizePixel = 3
textbox.Name = "WalkSpeed"
textbox.Position = UDim2.new(0,0,0,33)
textbox.Size = UDim2.new(1,0,0,30)
textbox.ZIndex = 1
textbox.Font = tef
textbox.FontSize = "Size24"
textbox.Text = "50"
textbox.TextColor3 = whit
textbox.MouseButton1Down:Connect(function()
	local val = tonumber(textbox.Text)
	if val >= 150 then
		textbox.Text = "25"
	else
		val += 25
		textbox.Text = val
	end
end)

local label = Instance.new("TextLabel")
label.Parent = pge2
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "JumpPower label"
label.Position = UDim2.new(0,0,0,66)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "JumpPower"
label.TextColor3 = whit
local textbox = Instance.new("TextButton")
textbox.Parent = pge2
textbox.BackgroundColor3 = blak
textbox.BorderColor3 = blue
textbox.BorderSizePixel = 3
textbox.Name = "JumpPower"
textbox.Position = UDim2.new(0,0,0,99)
textbox.Size = UDim2.new(1,0,0,30)
textbox.ZIndex = 1
textbox.Font = tef
textbox.FontSize = "Size24"
textbox.Text = "150"
textbox.TextColor3 = whit
textbox.MouseButton1Down:Connect(function()
	local val = tonumber(textbox.Text)
	if val >= 300 then
		textbox.Text = "50"
	else
		val += 50
		textbox.Text = val
	end
end)

local label = Instance.new("TextLabel")
label.Parent = pge2
label.BackgroundColor3 = blak
label.BorderColor3 = blue
label.BorderSizePixel = 3
label.Name = "SpinSpeed label"
label.Position = UDim2.new(0,0,0,132)
label.Size = UDim2.new(1,0,0,30)
label.ZIndex = 1
label.Font = tef
label.FontSize = "Size24"
label.Text = "SpinSpeed"
label.TextColor3 = whit
local textbox = Instance.new("TextButton")
textbox.Parent = pge2
textbox.BackgroundColor3 = blak
textbox.BorderColor3 = blue
textbox.BorderSizePixel = 3
textbox.Name = "SpinSpeed"
textbox.Position = UDim2.new(0,0,0,165)
textbox.Size = UDim2.new(1,0,0,30)
textbox.ZIndex = 1
textbox.Font = tef
textbox.FontSize = "Size24"
textbox.Text = "100"
textbox.TextColor3 = whit
textbox.MouseButton1Down:Connect(function()
	local val = tonumber(textbox.Text)
	if val >= 500 then
		textbox.Text = "50"
	else
		val += 50
		textbox.Text = val
	end
end)

local dragToggle = nil
local dragSpeed = 0.25
local dragStart = nil
local startPos = nil
local function updateInput(input)
	local delta = input.Position - dragStart
	local position = UDim2.new(startPos.X.Scale, startPos.X.Offset + delta.X,
		startPos.Y.Scale, startPos.Y.Offset + delta.Y)
	game:GetService("TweenService"):Create(ckaframe, TweenInfo.new(dragSpeed), {Position = position}):Play()
end
frame.Title.InputBegan:Connect(function(input)
	if (input.UserInputType == Enum.UserInputType.MouseButton1 or input.UserInputType == Enum.UserInputType.Touch) then 
		dragToggle = true
		dragStart = input.Position
		startPos = ckaframe.Position
		input.Changed:Connect(function()
			if input.UserInputState == Enum.UserInputState.End then
				dragToggle = false
			end
		end)
	end
end)
game:GetService("UserInputService").InputChanged:Connect(function(input)
	if input.UserInputType == Enum.UserInputType.MouseMovement or input.UserInputType == Enum.UserInputType.Touch then
		if dragToggle then
			updateInput(input)
		end
	end
end)

CurrentPage = 1

function FlipPage(Way)
	local NewPage = CurrentPage+Way
	if pges:findFirstChild("Page"..NewPage)~=nil then
		CurrentPage = NewPage
		local P = pges:GetChildren()
		for i = 1, #P do
			P[i].Visible = false
		end
		pges:findFirstChild("Page"..NewPage).Visible = true
	end
end
right.MouseButton1Down:connect(function()FlipPage(1) end)
left.MouseButton1Down:connect(function()FlipPage(-1) end)
page1.addonl.MouseButton1Down:connect(function()CurrentPage=6 FlipPage(-1) end)
page5.addonr.MouseButton1Down:connect(function()CurrentPage=0 FlipPage(1) end)

-----------------------------------------------------------------------------
