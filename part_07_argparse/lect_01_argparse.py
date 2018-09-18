'''
How to run this file.

Overview about what this script does
$python lect_01_argparse.py -h

Case 1: How to execute python file using positional arguments
$python lect_01_argparse.py 2 4
in above command 2 and 4 are treated as command line arguments.

Case 2: How to execute python script using optional arguments
$python lect_01_argparse.py -r=2 -H=4
OR
$python lect_01_argparse.py -H 4 -r 2
'''

import argparse
import math

parser = argparse.ArgumentParser(description = "Calculate cylinder volume.")
'''
The way to use command line arguments passed as positional arguments

parser.add_argument('radius', type=int, help="Cylinder radius")
parser.add_argument('height', type=int, help="Cylinder height")
'''

'''
The way to use command line argument passed as optional argument
'''
parser.add_argument('-r', '--radius', metavar='', type=int, required=True, help="Cylinder radius.")
parser.add_argument('-H', '--height', metavar='', type=int, required=True, help="Cylinder height.")

group = parser.add_mutually_exclusive_group()
group.add_argument('-q', '--quiet', action='store_true', help='Print output quietly.')
group.add_argument('-v', '--verborse', action='store_true', help='Print output with description.')

args = parser.parse_args()

def cylinder_volume(radius = 5, height = 2):
	volume = math.pi *(radius**2)* height
	return volume

if __name__ == '__main__':
	cylinder_vol = 0
	cylinder_vol = cylinder_volume(args.radius, args.height)

	if args.quiet:
		print(cylinder_vol)
	elif args.verborse:
		print('Volume of a cylinder with radius {:3d} and height {:3d} is {:4f}'.format(args.radius, args.height, cylinder_vol))
	else:
		print('Volume of a cylinder is {:4f}'.format(cylinder_vol))