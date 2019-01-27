import bcolors as colors
class parameter:
	FILESYSTEM = "/tefuser1/tef/abp"
	NEEDED = 50
	COMMAND = "df -h | grep %s" % FILESYSTEM
	TITLE = colors.color.BOLD + colors.color.WARNING + '= ABP MAPPING SPACE =' + colors.color.ENDC