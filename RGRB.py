import random
from flask import Flask, render_template,request



app =Flask(__name__)
@app.route('/', methods=['Get','POST'])
def index():
    godpicture="SmiteLogo.png"
    roleplayed= ""
    build=""
    warning =""
    godList = ["Achilles", "Agni", "Ah Muzen Cab", "Ah Puch", "Amaterasu", "Anhur", "Anubis", "Ao Kuang", "Aphrodite",
               "Apollo", "Arachne", "Ares", "Artemis", "Artio", "Athena"
        , "Awilix", "Bacchus", "Bakasura", "Baron Samedi", "Bastet", "Bellona", "Cabrakan", "Camazotz", "Cerberus",
               "Cernunnos", "Chaac", "Chang'e", "Chernobog", "Chiron", "Chronos",
               "Cu Chulainn", "Cupid", "Da Ji", "Discordia", "Erlang Shen", "Fafnir", "Fenrir", "Freya", "Genesha",
               "Geb", "Guan Yu", "Hachiman", "Hades", "He Bo", "Heimdallr",
               "Hel", "Hera", "Hercules", "Horus", "Hou yi", "Hun Batz", "Isis", "Izanami", "Janus", "Jing Wei",
               "Jormungandr", "Kali", "Khepri", "King Arthur", "Kukulkan", "Kumbhakarna", "Kuzenbo",
               "Loki", "Medusa", "Mercury", "Merlin", "Ne Zha", "Neith", "Nemesis", "Nike", "Nox", "Nu Wa", "Odin",
               "Olorun", "Osiris", "Pele", "Persephone",
               "Posiedon", "Ra", "Raijin", "Rama", "Ratatoskr", "Ravana", "Scylla", "Serqet", "Set", "Odin", "Skadi",
               "Sobek", "Sol",
               "Sun Wukong", "Susano", "Sylvanus", "Terra", "Thanatos", "The Morrigan", "Thor", "Thoth", "Tyr", "Ullr",
               "Vamana", "Vulcan", "Xbalanque", "Xing Tian", "Yemoja",
               "Ymir", "Zeus", "Zhong Kui"]

    godPicList = ["Achilles.jpg", "Agni.jpg", "AhMuzenCab.jpg", "AhPuch.jpg", "Amaterasu.jpg", "Anhur.jpg",
                  "Anubis.jpg", "AoKuang.jpg", "Aphrodite.jpg", "Apollo.jpg"
        , "Arachne.jpg", "Ares.jpg", "Artemis.jpg", "Artio.jpg", "Athena.jpg", "Awilix.jpg", "Bacchus.jpg",
                  "Bakasura.jpg", "BaronSamedi.jpg", "Bastet.jpg", "Bellona.jpg", "Cabrakan.jpg"
        , "Camazotz.jpg", "Cerberus.jpg", "Cernunnos.jpg", "Chaac.jpg", "Chang'e.jpg", "Chernobog.jpg", "Chiron.jpg",
                  "Chronos.jpg", "CuChulainn.jpg", "Cupid.jpg", "DaJi.jpg", "Discordia.jpg"
        , "ErlangShen.jpg", "Fafnir.jpg", "Fenrir.jpg", "Freya.jpg", "Genesha.jpg", "Geb.jpg", "GuanYu.jpg",
                  "Hachiman.jpg", "Hades.jpg", "HeBo.jpg", "Heimdallr.jpg", "Hel.jpg", "Hera.jpg", "Hercules.jpg"
        , "Horus.jpg", "Houyi.jpg", "HunBatz.jpg", "Isis.jpg", "Izanami.jpg", "Janus.jpg", "JingWei.jpg",
                  "Jormungandr.jpg", "Kali.jpg", "Khepri.jpg", "KingArthur.jpg", "Kukulkan.jpg", "Kumbhakarna.jpg",
                  "Kuzenbo.jpg"
        , "Loki.jpg", "Medusa.jpg", "Mercury.jpg", "Merlin.jpg", "NeZha.jpg", "Neith.jpg", "Nemesis.jpg", "Nike.jpg",
                  "Nox.jpg", "NuWa.jpg", "Odin.jpg", "Olorun.jpg", "Osiris.jpg", "Pele.jpg", "Persephone.jpg"
        , "Posiedon.jpg", "Ra.jpg", "Raijin.jpg", "Rama.jpg", "Ratatoskr.jpg", "Ravana.jpg", "Scylla.jpg", "Serqet.jpg",
                  "Set.jpg", "Odin.jpg", "Skadi.jpg", "Sobek.jpg", "Sol.jpg", "SunWukong.jpg"
        , "Susano.jpg", "Sylvanus.jpg", "Terra.jpg", "Thanatos.jpg", "TheMorrigan.jpg", "Thor.jpg", "Thoth.jpg",
                  "Tyr.jpg", "Ullr.jpg", "Vamana.jpg", "Vulcan.jpg", "Xbalanque.jpg"
        , "XingTian.jpg", "Yemoja.jpg", "Ymir.jpg", "Zeus.jpg", "Zhong Kui.jpg"]

    physicalDamageBuilds = ["No Pen", "Attack Speed", "Movement Speed", "Health Items", "Max Power", "Critical Strike",
                            "Stacking Items", "No Stacking Items"]
    magicalDamageBuilds = ["No Pen", "Attack Speed", "Movement Speed", "Health Items", "Max Power", "Stacking Items",
                           "No Stacking Items"]
    magicalSupportBuilds = ["No Physical Protections", "No Magical Protections", "Movement Speed", "Health Items",
                            "Full Protections"]
    physicalSupportBuilds = ["No Physical Protections", "No Magical Protections", "Movement Speed", "Health Items",
                             "Full Protections"]
    physicalSoloBuilds = ["No Physical Protections", "No Magical Protections", "Movement Speed", "Health Items",
                          "Full Protections", "Hybrid", "Attack Speed", "Critical Strike", "Full Damage",
                          "Stacking Items"]
    magicalSoloBuilds = ["No Physical Protections", "No Magical Protections", "Movement Speed", "Health Items",
                         "Full Protections", "Hybrid", "Attack Speed", "Full Damage", "Stacking Items"]

    guardianpiclist = [godPicList[11], godPicList[13], godPicList[14], godPicList[16], godPicList[21], godPicList[23],
                       godPicList[35], godPicList[38], godPicList[39], godPicList[55], godPicList[57]
        , godPicList[60], godPicList[61], godPicList[88], godPicList[92], godPicList[93], godPicList[103],
                       godPicList[104], godPicList[105]]

    hunterpiclist = [godPicList[2], godPicList[5], godPicList[9], godPicList[12], godPicList[24], godPicList[27],
                     godPicList[28], godPicList[31], godPicList[41]
        , godPicList[44], godPicList[49], godPicList[52], godPicList[54], godPicList[63], godPicList[67],
                     godPicList[80], godPicList[87], godPicList[99], godPicList[102]]

    assassinpiclist = [godPicList[10], godPicList[15], godPicList[17], godPicList[19], godPicList[22], godPicList[32],
                       godPicList[36], godPicList[50], godPicList[56], godPicList[62]
        , godPicList[64], godPicList[66], godPicList[68], godPicList[75], godPicList[81], godPicList[82],
                       godPicList[84], godPicList[85], godPicList[91], godPicList[94], godPicList[96]]

    warriorpiclist = [godPicList[0], godPicList[4], godPicList[20], godPicList[25], godPicList[30], godPicList[34],
                      godPicList[40], godPicList[47], godPicList[48]
        , godPicList[58], godPicList[69], godPicList[72], godPicList[74], godPicList[90], godPicList[98],
                      godPicList[100]]

    magepiclist = [godPicList[1], godPicList[3], godPicList[6], godPicList[7], godPicList[8], godPicList[18],
                   godPicList[26], godPicList[29], godPicList[33], godPicList[37], godPicList[42], godPicList[43]
        , godPicList[45], godPicList[46], godPicList[51], godPicList[53], godPicList[59], godPicList[65],
                   godPicList[70], godPicList[71], godPicList[73], godPicList[76], godPicList[77], godPicList[78]
        , godPicList[79], godPicList[83], godPicList[89], godPicList[96], godPicList[97], godPicList[101],
                   godPicList[106], godPicList[107]]

    guardianlist = [godList[11], godList[13], godList[14], godList[16], godList[21], godList[23], godList[35],
                    godList[38], godList[39], godList[55], godList[57]
        , godList[60], godList[61], godList[88], godList[92], godList[93], godList[103], godList[104], godList[105]]

    hunterlist = [godList[2], godList[5], godList[9], godList[12], godList[24], godList[27], godList[28], godList[31],
                  godList[41], godList[44], godList[49], godList[52], godList[54], godList[63], godList[67]
        , godList[80], godList[87], godList[99], godList[102]]

    assassinlist = [godList[10], godList[15], godList[17], godList[19], godList[22], godList[32], godList[36],
                    godList[50], godList[56], godList[62], godList[64], godList[66], godList[68], godList[75]
        , godList[81], godList[82], godList[84], godList[85], godList[91], godList[94], godList[96]]

    warriorlist = [godList[0], godList[4], godList[20], godList[25], godList[30], godList[34], godList[40], godList[47],
                   godList[48], godList[58], godList[69], godList[72], godList[74], godList[90]
        , godList[98], godList[100]]

    magelist = [godList[1], godList[3], godList[6], godList[7], godList[8], godList[18], godList[26], godList[29],
                godList[33], godList[37], godList[42], godList[43], godList[45], godList[46]
        , godList[51], godList[53], godList[59], godList[65], godList[70], godList[71], godList[73], godList[76],
                godList[77], godList[78], godList[79], godList[83], godList[89], godList[96], godList[97], godList[101]
        , godList[106], godList[107]]

    if request.method =="POST":
        role=request.form.getlist('role')
        classes=request.form.getlist('class')
        if(len(classes)==0 or len(role)==0):
          warning="You have to choose at least one class and one role"
        if (len(classes) and len(role)!=0):
          warning = ""
        if(len(classes)!= 0 and len(role) != 0):
          print("your class is %s" % classes)
          chosenRole= role[random.randrange(0,len(role))]
          chosenClass = classes[random.randrange(0, len(classes))]
          roleplayed= chosenRole
          if(chosenClass=="Guardian"):
              godpicture=guardianpiclist[random.randrange(0, len(guardianpiclist))]
          elif (chosenClass == "Assassin"):
              godpicture = assassinpiclist[random.randrange(0, len(assassinpiclist))]
          elif (chosenClass == "Hunter"):
              godpicture = hunterpiclist[random.randrange(0, len(hunterpiclist))]
          elif (chosenClass == "Mage"):
              godpicture = magepiclist[random.randrange(0, len(magepiclist))]
          elif (chosenClass == "Warrior"):
              godpicture = warriorpiclist[random.randrange(0, len(warriorpiclist))]
        
          if ((chosenRole == "Jungle" or chosenRole == "ADC" or chosenRole == "Mid")and (chosenClass == "Assassin" or  chosenClass == "Hunter" or  chosenClass == "Warrior")):
              build = physicalDamageBuilds[random.randrange(0, len(physicalDamageBuilds))]
              print(1)

          elif ((chosenRole == "Jungle" or chosenRole == "ADC" or chosenRole == "Mid") and( chosenClass == "Mage" or  chosenClass == "Guardian")):
              build = magicalDamageBuilds[random.randrange(0, len(magicalDamageBuilds))]
              print(2)
          elif (chosenRole == "Support" and (chosenClass == "Assassin" or  chosenClass == "Hunter"
          or  chosenClass == "Warrior")):
              build = physicalSupportBuilds[random.randrange(0, len(physicalSupportBuilds))]
              print(3)
          elif (chosenRole == "Support"and (chosenClass == "Mage" or  chosenClass == "Guardian")):
              build = magicalSupportBuilds[random.randrange(0, len(magicalSupportBuilds))]
              print(4)
          elif (chosenRole == "Solo" and( chosenClass == "Assassin" or chosenClass == "Hunter" or chosenClass == "Warrior")):
              build = physicalSoloBuilds[random.randrange(0, len(physicalSoloBuilds))]
              print(5)
          elif (chosenRole == "Solo"  and  (chosenClass == "Mage" or chosenClass == "Guardian")):
              build = magicalSoloBuilds[random.randrange(0, len(magicalSoloBuilds))]
              print(6)



    return render_template("profile.html",godpicture=godpicture,roleplayed=roleplayed,build=build,warning=warning)

if __name__=="__main__":
    app.run(debug=True)



randomRole, randomClass= True, True


