import os
import commands
import lib.bcolors as colors
import lib.parameters as parameters

def sufficient(indicator):
	result_color = colors.color.WARNING
	def getCommand(color):
		global color_space
		color_space = color_space.replace(space[2], colors.color.BOLD+color+space[2]+colors.color.ENDC+colors.color.WARNING)
		comm = "echo '%sFilesystem            Size  Used%s%s Avail %s%sUse  Mounted on'  && echo  '%s'" %(colors.color.WARNING,colors.color.BOLD,color,
		colors.color.ENDC,colors.color.WARNING,color_space)
		return comm
	if indicator == 'NOK':
		result_color = colors.color.FAIL
		os.system(getCommand(result_color))

	elif indicator == 'OK': 
		result_color = colors.color.OKGREEN
		os.system(getCommand(result_color))

print "\n%s\n" % parameters.parameter.TITLE

needed = parameters.parameter.NEEDED
state, out  = commands.getstatusoutput(parameters.parameter.COMMAND)
color_space = out
out = out.split(' ')
space = [ i for i in out if i != '' ]
disp = int(space[2].replace("G", ''))


if disp <= needed:
	sufficient('NOK')
	print colors.color.BOLD + colors.color.FAIL + 'Liberar espacio. Se necesitan al menos %sG libres.' % parameters.parameter.NEEDED
elif disp > needed:
	sufficient('OK')
	print colors.color.BOLD + colors.color.OKGREEN + 'Espacio suficiente.'

print colors.color.ENDC