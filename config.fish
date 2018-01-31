set lolqoutefile /path/to/lol_champ_quotes.txt
set lolquote (string replace -a \t \n (tail -n+(random 1 (wc -l < $lolqoutefile)) $lolqoutefile | head -n1))
function fish_greeting	
	cowsay -f tux $lolquote
end
