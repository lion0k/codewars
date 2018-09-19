<?php
function count_smileys($arr) {
	if (empty($arr)) {
		return 0;
	}
	$res = array_filter($arr, function($smile) {
		$aStr = str_split($smile);
		$cnt = count($aStr);
		if ($cnt > 3) {
			return false;
		}
		for ($i = 0; $i < $cnt; $i++) {
			switch ($i) {
				case 0:
					if ($aStr[$i] !== ':' && $aStr[$i] !== ';') {
						return false;
					}
					break;
				case 1:

					if ($aStr[$i] == ')' || $aStr[$i] == 'D') {
						return true;
					}
					if ($aStr[$i] != '-' && $aStr[$i] != '~') {
						return false;
					}
					break;
				case 2:
					if ($aStr[$i] == ')' || $aStr[$i] == 'D') {
						return true;
					}
					break;			
				}
		}
	});
  return count($res);
}

print_r(count_smileys([':)', ';(', ';}', ':-D']));

/*
 * countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
 *
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
Valid smiley face examples:
:) :D ;-D :~)
 *
 * */
