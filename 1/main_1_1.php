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

$elfNo = 0;
$elfCalories = 0;

$currentElfNo = 0;
$currentElfCalories = 0;

foreach($arr as $line) {
	if ((int)$line === 0) {
		$currentElfNo++;
		if ($elfCalories <= $currentElfCalories) {
			$elfNo = $currentElfNo;
			$elfCalories = $currentElfCalories;
		}
		$currentElfCalories = 0;


	} else {
		$currentElfCalories += (int)$line;
	}
}

echo $elfNo.' | '. $elfCalories;