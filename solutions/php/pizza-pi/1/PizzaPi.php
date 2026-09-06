<?php

class PizzaPi
{
    public function calculateDoughRequirement(int $pizzas, $persons)
    {
        return $pizzas * (($persons * 20) + 200);
    }

    public function calculateSauceRequirement(int $pizzas, $can)
    {
        return ($pizzas * 125) / $can;
    }

    public function calculateCheeseCubeCoverage(int $dimension, $thickness, $diameter)
    {
        return floor(($dimension ** 3) / ($thickness * 3.14 * $diameter));


    }

    public function calculateLeftOverSlices(int $pizzas, $friends)
    {
        return ($pizzas * 8) % $friends;
    }
}
