<?php
$input=<<<END
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

END;
$arr = explode("\n", $input);

$elfsCalories = [0,0,0];
$currentElfCalories = 0;

foreach($arr as $line) {
	if ((int)$line === 0) {
		if (min($elfsCalories) < $currentElfCalories) {
			$keys = array_keys($elfsCalories, min($elfsCalories));
			$elfsCalories[$keys[0]] = $currentElfCalories;
		}
		$currentElfCalories = 0;
	} else {
		$currentElfCalories += (int)$line;
	}
}


var_dump($elfsCalories);
echo array_sum($elfsCalories);