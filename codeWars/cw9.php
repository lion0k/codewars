<?php
function is_solved(array $board) {
	$arr = [];
	$res = -1;
	$isXwin = false;
	$isOwin = false;
	for ($i = 0; $i < 3; $i++) {
		if (in_array(0, $board[$i])) {
			return -1;
		}
		switch ($i) {
			case 0:
				$arr['x1'] = $board[$i][0];
				$arr['x2'] = $board[$i][1];
				$arr['x3'] = $board[$i][2];
				break;
			case 1:
				$arr['y1'] = $board[$i][0];
				$arr['y2'] = $board[$i][1];
				$arr['y3'] = $board[$i][2];
				break;
			case 2:
				$arr['z1'] = $board[$i][0];
				$arr['z2'] = $board[$i][1];
				$arr['z3'] = $board[$i][2];
				break;		
		}
	}
	$temp = $arr['x1'] + $arr['x2'] + $arr['x3'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}
	$temp = $arr['x1'] + $arr['y1'] + $arr['z1'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}
	$temp = $arr['x1'] + $arr['y2'] + $arr['z3'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}
	$temp = $arr['x3'] + $arr['y3'] + $arr['z3'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}
	$temp = $arr['z1'] + $arr['z2'] + $arr['z3'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}
	$temp = $arr['y1'] + $arr['y2'] + $arr['y3'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}
	$temp = $arr['x2'] + $arr['y2'] + $arr['z2'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}
	$temp = $arr['x3'] + $arr['y2'] + $arr['z1'] ;
	if ($temp === 3 || $temp === 6) {
		($temp === 3) ? $isXwin = true : $isOwin = true;	
	}

	if ((!$isXwin && !$isOwin) || ($isXwin && $isOwin)) {
		return 0;
	} elseif ($isXwin) {
		return 1;
	} else {
		return 2;
	}
}

$play = [[0, 0, 1], [0, 1, 2], [2, 1, 0]];
$play2 = [[1, 2, 1], [1, 1, 2], [1, 2, 2]];
$play3 = [[1, 2, 1], [2, 2, 1], [2, 2, 2]];
$play4 = [[1, 1, 1], [2, 2, 2], [2, 1, 1]];


print_r(is_solved($play));
print_r(is_solved($play2));
print_r(is_solved($play3));
print_r(is_solved($play4));


