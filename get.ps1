$year = 2020
$day = $args[0]

$my_file = "$day.in"
$base = "https://adventofcode.com/$year/day/$day/input"
curl $base -o $my_file -H 'Cookie: session=53616c7465645f5f633f94e4b53411336a564f1587e3758b4422e88fee028d0f9bc934522cdbf688372bd823146a9846'

