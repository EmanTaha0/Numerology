from Numerology import Numerology

def main():
    sNameEMT = input("Enter your name: ")
    sDOBEMT = input("Enter your Date Of Birth (mm-dd-yyyy or mm/dd/yyyy): ")

    clientEMT = Numerology(sNameEMT, sDOBEMT)

    iLifePathEMT = clientEMT.getLifePath()
    iBirthDayEMT = clientEMT.getBirthDay()
    iAttitudeEMT = clientEMT.getAttitude()
    iSoulEMT = clientEMT.getSoulNumber()
    iPersonalityEMT = clientEMT.getPersonality()
    iPowerNameEMT = clientEMT.getPowerName()

    print(f"{'Life Path Number:':<25}{iLifePathEMT}")
    print(f"{'Birth Day Number:':<25}{iBirthDayEMT}")
    print(f"{'Attitude Number:':<25}{iAttitudeEMT}")
    print(f"{'Soul Number:':<25}{iSoulEMT}")
    print(f"{'Personality Number:':<25}{iPersonalityEMT}")
    print(f"{'Power Name Number:':<25}{iPowerNameEMT}")

main()
