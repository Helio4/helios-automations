--Script properties
script_name="Set styles by actor"
script_description="Set line style based on its actor"
script_author="Helio4"
script_version="1.0"

include("karaskel.lua")

--Main processing function
function setStyleByActor(sub, sel)

	local meta, styles = karaskel.collect_head(sub,false)
	
	--Go through all the lines in the selection
	for i=1,#sub do
		
		--Read in the line
		local line=sub[i]
		
		if line.actor ~= nil then
			style = styles[line.actor]
			if style ~= nil then
				line.style = style.name
			end
		end
		
		--Put the line back into the subtitles
		sub[i]=line
		
	end
	
	--Set undo point and maintain selection
	aegisub.set_undo_point(script_name)
	return sel
end

--Register macro (no validation function required)
aegisub.register_macro(script_name,script_description,setStyleByActor)
