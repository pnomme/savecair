# Simple savecair command line interface
# Supports commands, but no sensors yet
#  
import asyncio, time, sys, getopt, os
from configobj import ConfigObj
from pathlib import Path
from systemair.savecair.systemair import SystemAIR
def printUsage():
        print("")
        print("Savecair v0.9 - simple command line interface for SystemAir SaveCair IAM module")
        print("")
        print("Usage: %s [ options ]" % sys.argv[0])
        print("")
        print("Options:")
        print("       --auto (-a)")
        print("       --crowded (-c)")
        print("       --fireplace (-f)")
        print("       --holiday (-h)")
        print("       --manual (-m)")
        print("       --refresh (-r)")
        print("       --away (-a)")
        print("")
        print("       --temp=nn (nn=target degrees)")
        print("")
        print("Report issues at https://github.com/pnomme/savecair")
        print("")

if __name__ == "__main__":
    config = ConfigObj(str(Path.home()) + '/.config/savecair/savecair.conf')
    key_iam_id = config["iam_id"]
    key_iam_password = config["iam_pwd"]
    async def main(argv):
        sa = SystemAIR(iam_id=key_iam_id, password=key_iam_password)
        try:
                opts, args = getopt.getopt(argv, "acfhmrwt?", ["auto","crowded","fireplace","holiday","manual","refresh","away","temp=","help"])
        except getopt.GetoptError:
                printUsage()
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-?", "--help"):
                    printUsage()
                    sys.exit(2)
        await sa.connect()
        await sa.login()
        if not opts: 
            printUsage()
            sys.exit(2)
            opmode = sa.get_current_operation()
            print (opmode)
            sys.exit(2)
        print ("Setting SystemAIR to ", end='')
        for opt, arg in opts:
                if opt in ("-a", "--auto"):
                    await sa.set_auto_mode()
                    print ("AUTO")
                elif opt in ("-c", "--crowded"):
                    await sa.set_crowded_mode()
                    print ("CROWDED")
                elif opt in ("-f", "--fireplace"):
                    await sa.set_fireplace_mode()
                    print ("FIREPLACE")
                elif opt in ("-h", "--holiday"):
                    await sa.set_holiday_mode()
                    print ("HOLIDAY")
                elif opt in ("-m", "--manual"):
                    await sa.set_manual_mode()
                    print ("MANUAL")
                elif opt in ("-r", "--refresh"):
                    await sa.set_refresh_mode()
                    print ("REFRESH")
                elif opt in ("-w", "--away"):
                    await sa.set_away_mode()
                    print ("AWAY")
                elif opt in ("-t", "--temp"):
                    temp = int(arg)
                    await sa.set_temperature(temp)
                    print (temp,"degrees")

                
    asyncio.get_event_loop().run_until_complete(main(sys.argv[1:]))

