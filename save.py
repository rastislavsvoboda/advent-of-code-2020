import argparse
import subprocess

parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('day',type=int)
parser.add_argument('--year', type=int, default=2020)
args = parser.parse_args()



cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session=53616c7465645f5f633f94e4b53411336a564f1587e3758b4422e88fee028d0f9bc934522cdbf688372bd823146a9846"'.format(
    args.year, args.day)

output = subprocess.check_output(cmd, shell=True)
print(output)
