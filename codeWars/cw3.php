<?php
function is_prime(int $n): bool {
  if ($n < 2) {
    return false;
  }
  if ($n === 2) {
    return true;
  }
  $isPrime = true;
  for ($i = 2; $i < $n; $i++){
      if($n % $i === 0) {
        $isPrime = false;
      }
  }
  return $isPrime;
}
print_r(is_prime(3) . PHP_EOL);
print_r(is_prime(6) . PHP_EOL);
