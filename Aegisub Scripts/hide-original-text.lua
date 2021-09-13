local tr = aegisub.gettext

script_name = tr"Hide Original Text"
script_description = tr"Puts all the uncommented lines between brackets"
script_author = "Helio4"
script_version = "1"

function hide_text(subs, sel)
    for _, i in ipairs(sel) do
        local line = subs[i]
        if line.actor ~= "comment" then
          line.text = "{" .. line.text .. "}"
        end
        subs[i] = line
    end
    aegisub.set_undo_point(tr"hide original text")
end

aegisub.register_macro(script_name, script_description, hide_text)
