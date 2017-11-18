# -*- coding: utf-8 -*-

import TOBY
import requests
from TOBY.lib.curve.ttypes import *
from datetime import datetime
# https://kaijento.github.io/2017/05/19/web-scraping-youtube.com/
# from imgurpython import ImgurClient
import time,random,sys,json,codecs,threading,glob,re

cl = TOBY.LINE()
cl.login(token="EmDWBuKWLLLBt90ecSMc.8IP5V5DRYP+TMZ4793seha.AXbnpWOuj2Z8d4p4xNSzZigwhhaCi/W8iEA7Lhq5vfM=")
cl.loginResult

ki = TOBY.LINE()
ki.login(token="EmVWcwg4TuadH5k4dCE9.lAJ8Nf7px9rAhNFBpZeQ/q.osjj3mfYdqpt+jhShflA4nPaj+foYOAa6uMiYPoE3s8=")
ki.loginResult

kc = TOBY.LINE()
kc.login(token="ElwI5KL54DgKPtK9jrw5./7UZHqSSlM96Yb3q38NjHq.1vQQdsVuL18YvBvttC2MvvSQ6EBeIpnO/eKMoC2YXpc=")
kc.loginResult

kl = TOBY.LINE()
kl.login(token="EmNXNFaELhIzJlenmLZ3.078HxyVgr8EsDXtPDhQuCW.j6EydMBGdwyNK25fuuwppYbNya38DxzkCjokPOMmxQk=")
kl.loginResult

kk = TOBY.LINE()
kk.login(token="EmINJAP9I5K1PY0GfZ55.4nKT373zE5mWJxiCYl2Yrq.jj/zeTwO2siTYBNFguZU3becwHAPGLQ0N6NZ0rd8vXo=")
kk.loginResult

# client_id = ''
# client_secret = ''
# access_token = ''
# refresh_token = ''

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

# album = None
# image_path = 'tmp/tmp.jpg'

pedoMessage ="""- !qua = Ngeratain
- Admadd @ = Nambah Admin
- Admrem @ = Hapus Admin
- Adminlist = Cek admin
- InviteMeTo: = Invite dengan gid
- Tolonk que grup/grup2/grup3/grup4/grup5
- Tolonk que kontact1/2/3/4/5
- Cname Tora 1 - 5:
- Cstatus Tora 1 - 5:
- Steal home @/dp@
- K on/off
- Join on/off
- Comment on/off
- Share on/off
- Mimic:on/off
- Mimic:add: @
- Mimic:del: @
- ListTarget
- Setadmin@#@ >> set
- Glist Tora 1 - 5
- spedasli >> speed BOT

"""

helpMessage ="""
||=====  P U B L I C  =====||

❂͜͡☆➣ Creator
❂͜͡☆➣ Tora say
❂͜͡☆➣ GCreator

||=====  A D M I N  =====||

❂͜͡☆➣ K on / off
❂͜͡☆➣ Id
❂͜͡☆➣ Mid
❂͜͡☆➣ Urloff >> Close url
❂͜͡☆➣ Urlon >> Open url
❂͜͡☆➣ Ginfo >> Info grup
❂͜͡☆➣ Cancel >> Cancel invitatio
❂͜͡☆➣ Gn <name> >> Ganti nama grup
❂͜͡☆➣ Gcreator:inv
❂͜͡☆➣ Out >> Mengeluarkan Bot
❂͜͡☆➣ Invite
❂͜͡☆➣ Gift >> Gift
❂͜͡☆➣ Respon
❂͜͡☆➣ Tagall
❂͜͡☆➣ Glist
❂͜͡☆➣ Spam:
❂͜͡☆➣ Set view >> Setpoint Sider
❂͜͡☆➣ Cek view >> Cek Sider

||=====  K O N T A K  =====||

❂͜͡☆➣ K Tora 1 >> Kontak BOT 1
❂͜͡☆➣ K Tora 2 >> Kontak BOT 2
❂͜͡☆➣ K Tora 3 >> Kontak BOT 3
❂͜͡☆➣ K Tora 4 >> Kontak BOT 4
❂͜͡☆➣ K Tora 5 >> Kontak BOT 5

||=====  P R O T E C T  =====||

❂͜͡☆➣ Guest On/Off
❂͜͡☆➣ Mad On/Off
❂͜͡☆➣ Qr On/Off
❂͜͡☆➣ Protect On/Off
❂͜͡☆➣ Ban @ 
❂͜͡☆➣ Unban @
❂͜͡☆➣ Kill Ban
❂͜͡☆➣ Kill @
❂͜͡☆➣ Nk <nama> >> Kick by nama
❂͜͡☆➣ Vk <tag> >> Kick by tag

=========================
Tora Bot v 1.3.41
http://line.me/R/ti/p/%40qua3481v
SUPPORT BY : Tora BOT ID
.
Mau BOT ini juga?
Ketik MAU
"""
KAC=[cl,ki,kc,kl,kk]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kc.getProfile().mid
Cmid = kl.getProfile().mid
Dmid = kk.getProfile().mid

Bots=[mid,Amid,Cmid,Bmid]
admin=["uba2bbc26cbac614974081010ca173898","uf551ba79db22c4ff0a6c2757cb3fe750"]
creator=["uba2bbc26cbac614974081010ca173898"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for adding me\nPlease add our Official Account\nhttp://line.me/R/ti/p/%40qua3481v\nInstagram: @Fidho_Redana\n\n\nPlease add the BOT Kerang Legend :v\nhttps://line.me/R/ti/p/%40yak6321p",
    "lang":"JP",
    "comment":"Tora Bot ID\nPlease add our Official Account\nhttp://line.me/R/ti/p/%40qua3481v\nInstagram: @Fidho_Redana",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectguest":False,
    "Protectcancel":False,
    "protectionOn":False,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImage2(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self._client.sendMessage(M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            cl.acceptGroupInvitation(op.param1)
            cl.sendText(op.param1, "Terimakasih sudah menggunakan BOT ini :)\nhttps://line.me/R/ti/p/%40qua3481v")
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    ki.sendText(op.param1,str(wait["message"]))
                    kc.sendText(op.param1,str(wait["message"]))
                    kl.sendText(op.param1,str(wait["message"]))
                    kk.sendText(op.param1,str(wait["message"]))

        #------Open QR Kick start------#
        if op.type == 10:
           if wait["ProtectQR"] == True:
               if op.param2 not in Bots:
                   G = cl.getGroup(op.param1)
                   G = ki.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   ki.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        #------Open QR Kick finish-----#

        #------Invite User Kick start------#
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in Bots:
                  random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Invite User Kick Finish------#

        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("��",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 17:
                group = random.choice(KAC).getGroup(op.param1)
                cb = Message()
                cb.to = op.param1
                cb.text = random.choice(KAC).getContact(op.param2).displayName + "\n\nSelamat Datang" + random.choice(KAC).getContact(op.param2).displayName + " di [" + group.name + "]\n" + "\n\nGCreator => " + group.creator.displayName
                random.choice(KAC).sendMessage(cb)
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)


        if op.type == 19:
            if op.param3 in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 random.choice(KAC).inviteIntoGroup(op.param1,admin)
            else:
                pass

        if op.type == 19:
            if op.param2 not in admin:
                 random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                 wait["blacklist"][op.param2] = True
                 print "kicker kicked"
            else:
                pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group��\n["+op.param1+"]\n��\n["+op.param2+"]\n�������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client������Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n�������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client������Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n�������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client������Ҏ��or����`�פ˴��ڤ��ʤ��顢\n["+op.param1+"]\n��\n["+op.param2+"]\n�������¤��Ǥ��ޤ���Ǥ�����\n�֥�å��ꥹ�Ȥ�׷�Ӥ��ޤ���")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    kl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message

        #------Cancel User Kick start------#
        if op.type == 32:
            if op.param2 not in Bots:
               kl.kickoutFromGroup(op.param1,[op.param2])
        #-----Cancel User Kick Finish------#

            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        kl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        kl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        kl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")
                        kl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        kl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
                        kl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL�0�9�6�9��\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,helpMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif msg.text in ["fr@@##@@"]:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,pedoMessage)
					else:
						cl.sendText(msg.to,helpt)
            elif "Tolonk que grup5 " in msg.text:
                bctxt = msg.text.replace("Tolonk que grup5 ", "")
                n = kk.getGroupIdsJoined()
                for manusia in n:
                    kk.sendText(manusia, (bctxt))
            elif "Tolonk que grup4 " in msg.text:
                bctxt = msg.text.replace("Tolonk que grup4 ", "")
                n = kl.getGroupIdsJoined()
                for manusia in n:
                    kl.sendText(manusia, (bctxt))
            elif "Tolonk que grup3 " in msg.text:
                bctxt = msg.text.replace("Tolonk que grup3 ", "")
                n = kc.getGroupIdsJoined()
                for manusia in n:
                    kc.sendText(manusia, (bctxt))
            elif "Tolonk que grup2 " in msg.text:
                bctxt = msg.text.replace("Tolonk que grup2 ", "")
                n = ki.getGroupIdsJoined()
                for manusia in n:
                    ki.sendText(manusia, (bctxt))
            elif "Tolonk que grup " in msg.text:
                bctxt = msg.text.replace("Tolonk que grup ", "")
                n = cl.getGroupIdsJoined()
                for manusia in n:
                    cl.sendText(manusia, (bctxt))
            elif "Tolonk que kontact1 " in msg.text:
                bctxt = msg.text.replace("Tolonk que kontact1 ", "")
                t = cl.getAllContactIds()
                for manusia in t:
                    cl.sendText(manusia, (bctxt))
            elif "Tolonk que kontact2 " in msg.text:
                bctxt = msg.text.replace("Tolonk que kontact2 ", "")
                t = ki.getAllContactIds()
                for manusia in t:
                    ki.sendText(manusia, (bctxt))
            elif "Tolonk que kontact3 " in msg.text:
                bctxt = msg.text.replace("Tolonk que kontact3 ", "")
                t = kc.getAllContactIds()
                for manusia in t:
                    kc.sendText(manusia, (bctxt))
            elif "Tolonk que kontact4" in msg.text:
                bctxt = msg.text.replace("Tolonk que kontact4 ", "")
                t = kl.getAllContactIds()
                for manusia in t:
                    kl.sendText(manusia, (bctxt))
            elif "Tolonk que kontact5" in msg.text:
                bctxt = msg.text.replace("Tolonk que kontact5 ", "")
                t = kk.getAllContactIds()
                for manusia in t:
                    kk.sendText(manusia, (bctxt))
            elif ("Gn " in msg.text):
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.name = msg.text.replace("Gn ","")
						cl.updateGroup(X)
					else:
						cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Kick ","")
					cl.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
				if msg.from_ in admin:
					midd = msg.text.replace("Invite ","")
					cl.findAndAddContactsByMid(midd)
					cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["K Tora 1"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': mid}
					cl.sendMessage(msg)
            elif msg.text in ["K Tora 2"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Amid}
					ki.sendMessage(msg)
            elif msg.text in ["K Tora 3"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Bmid}
					kc.sendMessage(msg)
            elif msg.text in ["K Tora 4"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Cmid}
					kl.sendMessage(msg)
            elif msg.text in ["K Tora 5"]:
				if msg.from_ in admin:
					msg.contentType = 13
					msg.contentMetadata = {'mid': Dmid}
					kk.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '5'}
					msg.text = None
					cl.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Tora 2 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '6'}
					msg.text = None
					ki.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Tora 3 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '8'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","Tora 4 gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '10'}
					msg.text = None
					kc.sendMessage(msg)
            elif msg.text in ["æ„�1�7�ã®ãƒ�1�7�ãƒ¬ã�1�7�¼ãƒ³ãƒ˄1�7","All gift"]:
				if msg.from_ in admin:
					msg.contentType = 9
					msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
										'PRDTYPE': 'THEME',
										'MSGTPL': '12'}
					msg.text = None
					kl.sendMessage(msg)
					kk.sendMessage(msg)
					kc.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						if X.invitee is not None:
							gInviMids = [contact.mid for contact in X.invitee]
							cl.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								kl.sendText(msg.to,"Ga ada yang pending")
							else:
								kl.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						G = k3.getGroup(msg.to)
						if G.invitee is not None:
							gInviMids = [contact.mid for contact in G.invitee]
							k3.cancelGroupInvitation(msg.to, gInviMids)
						else:
							if wait["lang"] == "JP":
								k3.sendText(msg.to,"No one is inviting")
							else:
								k3.sendText(msg.to,"Sorry, nobody absent")
					else:
						if wait["lang"] == "JP":
							k3.sendText(msg.to,"Can not be used outside the group")
						else:
							k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl","Link on","Urlon"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							kl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tora ourl","Tora link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = False
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done")
						else:
							ki.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tora 2 ourl","Tora 2 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 ourl","Cv3 link on"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = False
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done Chivas")
						else:
							kc.sendText(msg.to,"already open")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off","Urloff"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = cl.getGroup(msg.to)
						X.preventJoinByTicket = True
						cl.updateGroup(X)
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Done")
						else:
							cl.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can not be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tora curl","Tora link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = ki.getGroup(msg.to)
						X.preventJoinByTicket = True
						ki.updateGroup(X)
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Done")
						else:
							ki.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							ki.sendText(msg.to,"Can not be used outside the group")
						else:
							ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tora 2 curl","Tora 2 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kk.getGroup(msg.to)
						X.preventJoinByTicket = True
						kk.updateGroup(X)
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Done")
						else:
							kk.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kk.sendText(msg.to,"Can not be used outside the group")
						else:
							kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot3 curl","Bot3 link off"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						X = kc.getGroup(msg.to)
						X.preventJoinByTicket = True
						kc.updateGroup(X)
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Done")
						else:
							kc.sendText(msg.to,"already close")
					else:
						if wait["lang"] == "JP":
							kc.sendText(msg.to,"Can not be used outside the group")
						else:
							kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,msg.to)
            elif "All mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
					ki.sendText(msg.to,Amid)
					kl.sendText(msg.to,Bmid)
					kc.sendText(msg.to,Cmid)
            elif "Mid" == msg.text:
				if msg.from_ in admin:
					cl.sendText(msg.to,mid)
            elif "Tora 1 mid" == msg.text:
				if msg.from_ in admin:
					ki.sendText(msg.to,Amid)
            elif "Tora 2 mid" == msg.text:
				if msg.from_ in admin:
					kc.sendText(msg.to,Bmid)
            elif "Tora 3 mid" == msg.text:
				if msg.from_ in admin:
					kl.sendText(msg.to,Cmid)
            elif msg.text in ["Cury PP"]:
				if msg.from_ in admin:
					tl_text = msg.text.replace("TL","")
					cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cn ","")
					if len(string.decode('utf-8')) <= 20:
						profile = cl.getProfile()
						profile.displayName = string
						cl.updateProfile(profile)
						cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv1 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv1 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = ki.getProfile()
						profile_B.displayName = string
						ki.updateProfile(profile_B)
						ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Cv2 rename "]:
				if msg.from_ in admin:
					string = msg.text.replace("Cv2 rename ","")
					if len(string.decode('utf-8')) <= 20:
						profile_B = kk.getProfile()
						profile_B.displayName = string
						kk.updateProfile(profile_B)
						kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
				if msg.from_ in admin:
					mmid = msg.text.replace("Mc ","")
					msg.contentType = 13
					msg.contentMetadata = {"mid":mmid}
					cl.sendMessage(msg)
            elif msg.text in ["Guest On","guest on"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off","guest off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ1�7","K on","Contact on","é¡¯ç¤ºï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["contact"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å�1�7�˄1�7:ã‚ªãƒ�1�7�1�7","K off","Contact off","é¡¯ç¤ºï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["contact"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done ")
					else:
						wait["contact"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1�7��1�7�å�1�7�åń1�7 :ã‚ªãƒ1�7","Join on","Auto join:on","è‡ªå�1�7��1�7�åƒåń1�7 ï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå�1�7��1�7�å�1�7�åń1�7 :ã‚ªãƒ�1�7�1�7","Join off","Auto join:off","è‡ªå�1�7��1�7�åƒåń1�7 ï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["autoJoin"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoJoin"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
				if msg.from_ in admin:
					try:
						strnum = msg.text.replace("Gcancel:","")
						if strnum == "off":
							wait["autoCancel"]["on"] = False
							if wait["lang"] == "JP":
								cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
							else:
								cl.sendText(msg.to,"å…³äº�1�7�é�1�7�€è¯·æ‹�1�7�ç»ã€‚è¦æ�1�7�¶å¼€è¯·æŒ‡å®šäººæ�1�7�°å�1�7�é€")
						else:
							num =  int(strnum)
							wait["autoCancel"]["on"] = True
							if wait["lang"] == "JP":
								cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
							else:
								cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš�1�7�å°ç»�1�7�ç�1�7�¨è�1�7�ªåŠ¨é�1�7�€è¯·æ‹�1�7�ç»1�7")
					except:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Value is wrong")
						else:
							cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ1�7","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�1�7:ã‚ªãƒ�1�7�1�7","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå�1�7��1�7�é€€å�1�7�ºï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["leaveRoom"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["leaveRoom"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ�1�7�1�7:ã‚ªãƒ1�7","Share on","Share on"]:
				if msg.from_ in admin:
					if wait["timeline"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["å…±æœ�1�7�1�7:ã‚ªãƒ�1�7�1�7","Share off","Share off"]:
				if msg.from_ in admin:
					if wait["timeline"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["timeline"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif msg.text in ["Setadmin@#@"]:
				if msg.from_ in admin:
					md = ""
					if wait["contact"] == True: md+=" Contact : on\n"
					else: md+=" Contact : off\n"
					if wait["autoJoin"] == True: md+=" Auto join : on\n"
					else: md +=" Auto join : off\n"
					if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
					else: md+= " Group cancel : off\n"
					if wait["leaveRoom"] == True: md+=" Auto leave : on\n"
					else: md+=" Auto leave : off\n"
					if wait["timeline"] == True: md+=" Share : on\n"
					else:md+=" Share : off\n"
					if wait["autoAdd"] == True: md+=" Auto add : on\n"
					else:md+=" Auto add : off\n"
					if wait["commentOn"] == True: md+=" Comment : on\n"
					else:md+=" Comment : off\n"
					if wait["Protectcancel"] == True: md+="  Mad : on\n"
					else:md+=" Mad : off\n"
					if wait["Protectguest"] == True: md+=" Guest : on\n"
					else:md+=" Guest : off\n"
					cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album merit ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1�7�Œæ²¡åœ¨ã€ 1�7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1�7�ç�1�7�¸å�1�7�ń1�7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
						cl.sendText(msg.to,mg)
            elif "album " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album ","")
					album = cl.getAlbum(gid)
					if album["result"]["items"] == []:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"There is no album")
						else:
							cl.sendText(msg.to,"ç›¸å�1�7�Œæ²¡åœ¨ã€ 1�7")
					else:
						if wait["lang"] == "JP":
							mg = "The following is the target album"
						else:
							mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš�1�7�ç�1�7�¸å�1�7�ń1�7"
						for y in album["result"]["items"]:
							if "photoCount" in y:
								mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
							else:
								mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album remove ","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Deleted albums")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1�7�äº�1�7�çš�1�7�ç�1�7�¸å�1�7�Œã€ 1�7")
            elif msg.text in ["Group id","ç¾¤çµ„å�1�7�¨id"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsJoined()
					h = ""
					for i in gid:
						h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
					cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
				if msg.from_ in admin:
					gid = cl.getGroupIdsInvited()
					for i in gid:
						cl.rejectGroupInvitation(i)
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"All invitations have been refused")
					else:
						cl.sendText(msg.to,"æ‹�1�7�ç»äº�1�7�å�1�7�¨éƒ¨çš�1�7�é�1�7�€è¯·ã€�1�7�1�7")
            elif "album removeâ†�1�7�1�7" in msg.text:
				if msg.from_ in admin:
					gid = msg.text.replace("album removeâ†�1�7�1�7","")
					albums = cl.getAlbum(gid)["result"]["items"]
					i = 0
					if albums != []:
						for album in albums:
							cl.deleteAlbum(gid,album["id"])
							i += 1
					if wait["lang"] == "JP":
						cl.sendText(msg.to,str(i) + "Albums deleted")
					else:
						cl.sendText(msg.to,str(i) + "åˆ é™¤äº�1�7�äº�1�7�çš�1�7�ç�1�7�¸å�1�7�Œã€ 1�7")
            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ1�7","Add on","Auto add:on","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé–�1�7�1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already on")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["è‡ªå�1�7��1�7�è¿½åń1�7 :ã‚ªãƒ�1�7�1�7","Add off","Auto add:off","è‡ªå�1�7��1�7�è¿½åń1�7 ï¼šé—ń1�7"]:
				if msg.from_ in admin:
					if wait["autoAdd"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"already off")
						else:
							cl.sendText(msg.to,"done")
					else:
						wait["autoAdd"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif "Message change: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message change: ","")
					cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
				if msg.from_ in admin:
					wait["message"] = msg.text.replace("Message add: ","")
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message changed")
					else:
						cl.sendText(msg.to,"doneã€�1�7�1�7")
            elif msg.text in ["Message","è‡ªå�1�7��1�7�è¿½åń1�7 å•å€™èªžç¢ºèª1�7"]:
				if msg.from_ in admin:
					if wait["lang"] == "JP":
						cl.sendText(msg.to,"message change to\n\n" + wait["message"])
					else:
						cl.sendText(msg.to,"The automatic appending information is set as followsã€�1�7�\n\n" + wait["message"])
            elif "Comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"message changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
				if msg.from_ in admin:
					c = msg.text.replace("Add comment:","")
					if c in [""," ","\n",None]:
						cl.sendText(msg.to,"String that can not be changed")
					else:
						wait["comment"] = c
						cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ1�7","Comment on","Comment:on","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7��1�7�1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == True:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already on")
					else:
						wait["commentOn"] = True
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å¼€ã€�1�7�1�7")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒ˄1�7:ã‚ªãƒ�1�7�1�7","Comment on","Comment off","è‡ªå�1�7��1�7�é¦�1�7�Ä1�7 ç•™è¨€ï¼šé�1�7�ń1�7"]:
				if msg.from_ in admin:
					if wait["commentOn"] == False:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"already off")
					else:
						wait["commentOn"] = False
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"done")
						else:
							cl.sendText(msg.to,"è¦äº†å�1�7�³æ�1�7�­ã€ 1�7")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª1�7"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							cl.updateGroup(x)
						gurl = cl.reissueGroupTicket(msg.to)
						cl.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							ki.updateGroup(x)
						gurl = ki.reissueGroupTicket(msg.to)
						ki.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kk.updateGroup(x)
						gurl = kk.reissueGroupTicket(msg.to)
						kk.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						x = cl.getGroup(msg.to)
						if x.preventJoinByTicket == True:
							x.preventJoinByTicket = False
							kc.updateGroup(x)
						gurl = kc.reissueGroupTicket(msg.to)
						kc.sendText(msg.to,"line://ti/g/" + gurl)
					else:
						if wait["lang"] == "JP":
							cl.sendText(msg.to,"Can't be used outside the group")
						else:
							cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
				if msg.from_ in admin:
					wait["wblack"] = True
					cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
				if msg.from_ in admin:
					wait["dblack"] = True
					cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
				if msg.from_ in admin:
					if wait["commentBlack"] == {}:
						cl.sendText(msg.to,"confirmed")
					else:
						cl.sendText(msg.to,"Blacklist")
						mc = ""
						for mi_d in wait["commentBlack"]:
							mc += "" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						cl.sendText(msg.to,"already on")
					else:
						wait["clock"] = True
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"done")
            elif msg.text in ["Jam off"]:
				if msg.from_ in admin:
					if wait["clock"] == False:
						cl.sendText(msg.to,"already off")
					else:
						wait["clock"] = False
						cl.sendText(msg.to,"done")
            elif msg.text in ["Change clock "]:
				if msg.from_ in admin:
					n = msg.text.replace("Change clock ","")
					if len(n.decode("utf-8")) > 13:
						cl.sendText(msg.to,"changed")
					else:
						wait["cName"] = n
						cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
				if msg.from_ in admin:
					if wait["clock"] == True:
						now2 = datetime.now()
						nowT = datetime.strftime(now2,"(%H:%M)")
						profile = cl.getProfile()
						profile.displayName = wait["cName"] + nowT
						cl.updateProfile(profile)
						cl.sendText(msg.to,"Updated")
					else:
						cl.sendText(msg.to,"Please turn on the name clock")
#-----------------------------------------------
            elif msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-----------------------------------------------

            elif msg.text in ["Masuk"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							ki.acceptGroupInvitationByTicket(msg.to,Ticket)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							kl.acceptGroupInvitationByTicket(msg.to,Ticket)
							kk.acceptGroupInvitationByTicket(msg.to,Ticket)
							time.sleep(0.2)
							G = cl.getGroup(msg.to)
							G.preventJoinByTicket = True
							ki.updateGroup(G)
							kc.updateGroup(G)
							print "kicker ok" 
							G.preventJoinByTicket(G)
							kc.updateGroup(G)

            elif msg.text in ["Cv1 join"]:
				if msg.from_ in admin:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					ki.acceptGroupInvitationByTicket(msg.to,Ti)
					G = kk.getGroup(msg.to)
					G.preventJoinByTicket = True
					ki.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Cv2 join"]:
				if msg.from_ in admin:
					X = cl.getGroup(msg.to)
					X.preventJoinByTicket = False
					cl.updateGroup(X)
					invsend = 0
					Ti = cl.reissueGroupTicket(msg.to)
					kk.acceptGroupInvitationByTicket(msg.to,Ti)
					G = ki.getGroup(msg.to)
					G.preventJoinByTicket = True
					kk.updateGroup(G)
					Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
#.acceptGroupInvitationByTicket(msg.to,Ticket)
            elif msg.text in ["Cv3 join"]:
				if msg.from_ in admin:
							G = cl.getGroup(msg.to)
							ginfo = cl.getGroup(msg.to)
							G.preventJoinByTicket = False
							cl.updateGroup(G)
							invsend = 0
							Ticket = cl.reissueGroupTicket(msg.to)
							kc.acceptGroupInvitationByTicket(msg.to,Ticket)
							print "kicker ok"
							G.preventJoinByTicket = True
							kc.updateGroup(G)
#-----------------------------------------------
            elif msg.text in ["Out","out"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							cl.leaveGroup(msg.to)
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
							kc.leaveGroup(msg.to)
							kl.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 1"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Bye 2"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv1 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							ki.leaveGroup(msg.to)
						except:
							pass
            elif msg.text in ["Cv2 @bye"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kk.leaveGroup(msg.to)
						except:
							pass
				elif msg.text in ["Cv3 @bye"]:
					if msg.toType == 2:
						ginfo = cl.getGroup(msg.to)
						try:
							kc.leaveGroup(msg.to)
						except:
							pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							kk.sendText(msg.to,"Fuck You")
							kc.sendText(msg.to,"Fuck You")
							return
						for jj in matched_list:
							try:
								klist=[ki,kk,kc]
								kicker=random.choice(klist)
								kicker.kickoutFromGroup(msg.to,[jj])
								print (msg.to,[jj])
							except:
								print

            elif "Glist Tora 1" in msg.text:
                if msg.from_ in admin:
                        gid = cl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (cl.getGroup(i).name + " | Members : [ " + str(len (cl.getGroup(i).members))+" ]")
                        cl.sendText(msg.to, "#[Tora 1 GC]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "Glist Tora 2" in msg.text:
                if msg.from_ in admin:
                        gid = ki.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (ki.getGroup(i).name + " | Members : [ " + str(len (ki.getGroup(i).members))+" ]")
                        ki.sendText(msg.to, "#[Tora 2 GC]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "Glist Tora 3" in msg.text:
                if msg.from_ in admin:
                        gid = kc.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (kc.getGroup(i).name + " | Members : [ " + str(len (kc.getGroup(i).members))+" ]")
                        kc.sendText(msg.to, "#[Tora 3 GC]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "Glist Tora 4" in msg.text:
                if msg.from_ in admin:
                        gid = kl.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (kl.getGroup(i).name + " | Members : [ " + str(len (kl.getGroup(i).members))+" ]")
                        kl.sendText(msg.to, "#[Tora 4 GC]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "Glist Tora 5" in msg.text:
                if msg.from_ in admin:
                        gid = kk.getGroupIdsJoined()
                        h = ""
                        for i in gid:
                            h += "=> %s  \n" % (kl.getGroup(i).name + " | Members : [ " + str(len (kk.getGroup(i).members))+" ]")
                        kk.sendText(msg.to, "#[Tora 4 GC]# \n"+ h +"Total Group : " +"[ "+str(len(gid))+" ]")
            elif "!qua" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("!qua","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    cl.sendText(msg.to,"�� Mayhem\nMayhem is STARTING�7�8\n' abort' to abort�7�8")
                    ki.sendText(msg.to,"�� Mayhem ��\n46 victims shall yell hul��la��ba��loo�7�8\n/�0�5h�0�5l�0�5b�0�5�0�4lo�0�0o,�0�4h�0�5l�0�5b�0�5�0�5lo�0�0o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[cl,ki,kl,kc,kk]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done")
            elif "Nk " in msg.text:
				if msg.from_ in admin:
					if msg.from_ in admin:
						nk0 = msg.text.replace("Nk ","")
						nk1 = nk0.lstrip()
						nk2 = nk1.replace("@","")
						nk3 = nk2.rstrip()
						_name = nk3
						gs = cl.getGroup(msg.to)
						targets = []
						for s in gs.members:
							if _name in s.displayName:
								targets.append(s.mid)
						if targets == []:
							sendMessage(msg.to,"user does not exist")
							pass
						else:
							for target in targets:
									try:
										klist=[cl,ki,kk,kc,kl]
										kicker=random.choice(klist)
										kicker.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
									except:
										ki.sendText(msg.to,"Success")
										kk.sendText(msg.to,"Fuck You"),
            elif "Blacklist @ " in msg.text:
				if msg.from_ in admin:
					_name = msg.text.replace("Blacklist @ ","")
					_kicktarget = _name.rstrip(' ')
					gs = ki2.getGroup(msg.to)
					targets = []
					for g in gs.members:
						if _kicktarget == g.displayName:
							targets.append(g.mid)
							if targets == []:
								cl.sendText(msg.to,"Not found")
							else:
								for target in targets:
									try:
										wait["blacklist"][target] = True
										f=codecs.open('st2__b.json','w','utf-8')
										json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
										k3.sendText(msg.to,"Succes Cv")
									except:
										ki.sendText(msg.to,"error")
            elif "Ban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Ban]ok"
						_name = msg.text.replace("Ban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							ki.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Berhasil")
								except:
									ki.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
				if msg.from_ in admin:
					if msg.toType == 2:
						print "[Unban]ok"
						_name = msg.text.replace("Unban @","")
						_nametarget = _name.rstrip('  ')
						gs = cl.getGroup(msg.to)
						gs = ki.getGroup(msg.to)
						gs = kk.getGroup(msg.to)
						targets = []
						for g in gs.members:
							if _nametarget == g.displayName:
								targets.append(g.mid)
						if targets == []:
							cl.sendText(msg.to,"Tidak DiTemukan")
							ki.sendText(msg.to,"Tidak DiTemukan")
						else:
							for target in targets:
								try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									ki.sendText(msg.to,"Berhasil")
								except:
									ki.sendText(msg.to,"Berhasil")
#-----------------------------------------------
            elif "Vk " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
#-----------------------------------------------
            elif "Tora say " in msg.text:
					bctxt = msg.text.replace("Tora say ","")
					cl.sendText(msg.to,(bctxt))
            elif "Tora 2 say " in msg.text:
					bctxt = msg.text.replace("Tora 2 say ","")
					ki.sendText(msg.to,(bctxt))
            elif "Tora 3 say " in msg.text:
					bctxt = msg.text.replace("Tora 3 say ","")
					kc.sendText(msg.to,(bctxt))
            elif "Tora 4 say " in msg.text:
					bctxt = msg.text.replace("Tora 4 say ","")
					kl.sendText(msg.to,(bctxt))
            elif "Tora 5 say " in msg.text:
					bctxt = msg.text.replace("Tora 5 say ","")
					kk.sendText(msg.to,(bctxt))
            elif msg.text in ["Creator"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "uba2bbc26cbac614974081010ca173898"}
					cl.sendText(msg.to,"MyCreator")
					ki.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "ua500484c18f8d156af47f35fb9620fa1"}
					cl.sendText(msg.to,"My Official Account")
					kc.sendMessage(msg)
					msg.contentType = 13
					msg.contentMetadata = {'mid': "u8e39e61d312e45a89f728d6cce645591"}
					cl.sendText(msg.to,"My BOT")
					ki.sendMessage(msg)
            elif msg.text in ["Mau","mau","MAU"]:
					msg.contentType = 13
					msg.contentMetadata = {'mid': "ua500484c18f8d156af47f35fb9620fa1"}
					cl.sendText(msg.to,"Mau Bot Ini? Add OA nya!")
					ki.sendMessage(msg)
#-----------------------------------------------
            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
#-----------------------------------------------
            elif msg.text == "Set view":
                    cl.sendText(msg.to, "Hello sider :)")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Cek view":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "=== SIDER === %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif "Cstatus Tora 1:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus Tora 1:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                else:
                    cl.sendText(msg.to,"Done")
            elif "Cstatus Tora 2:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus Tora 2:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                else:
                    ki.sendText(msg.to,"Done")
            elif "Cstatus Tora 3:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus Tora 3:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                else:
                    kc.sendText(msg.to,"Done")
            elif "Cstatus Tora 4:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus Tora 4:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kl.getProfile()
                    profile.statusMessage = string
                    kl.updateProfile(profile)
                else:
                    kl.sendText(msg.to,"Done")
            elif "Cstatus Tora 5:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cstatus Tora 5:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                else:
                    kk.sendText(msg.to,"Done")
#-----------------------------------------------
            elif "Cname Tora 1:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname Tora 1:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
            elif "Cname Tora 2:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname Tora 2:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.displayName = string
                    Ki.updateProfile(profile)
            elif "Cname Tora 3:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname Tora 3:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
            elif "Cname Tora 4:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname Tora 4:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kl.getProfile()
                    profile.displayName = string
                    kl.updateProfile(profile)
            elif "Cname Tora 5:" in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("Cname Tora 5:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
#-----------------------------------------------
            elif "Stalk " in msg.text:
                print "[Command]Stalk executing"
                stalkID = msg.text.replace("Stalk ","")
                subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])
                files = glob.glob("tmp/*.jpg")
                for file in files:
                    os.rename(file,"tmp/tmp.jpg")
                fileTmp = glob.glob("tmp/tmp.jpg")
                if not fileTmp:
                    cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
                    print "[Command]Stalk,executed - no image found"
                else:
                    image = upload_tempimage(client)
                    cl.sendText(msg.to, format(image['link']))
                    subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
                    print "[Command]Stalk executed - succes"
#----------------------------------------------
            elif ".Music" in msg.text.lower():
	            songname = msg.text.lower().replace(".music","")
	            params = {"songname":" songname"}
	            r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
	            data = r.text
	            data = json.loads(data)
	            for song in data:
		            cl.sendMessage(msg.to, song[4])
#-----------------------------------------------
            elif msg.text in ["Backup","backup"]:
                if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Telah kembali semula")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
#-----------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in creator:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#------------------------------------------------
            elif msg.text in ["Gcreator"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    ginfo = ki.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    kc.sendText(msg.to, "Group Creator : " + gCreator1)
                    kl.sendText(msg.to, "Group Creator : " + gCreator1)
                    kc.sendMessage(msg)
                    kl.sendMessage(msg)
#-----------------------------------------------
            elif "Admadd @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admadd @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                        kc.sendText(msg.to,"Contact not found")
                        kl.sendText(msg.to,"Contact not found")
                        kk.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                                ki.sendText(msg.to,"Admin ditambahkan")
                                kc.sendText(msg.to,"Admin ditambahkan")
                                kl.sendText(msg.to,"Admin ditambahkan")
                                kk.sendText(msg.to,"Admin ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    kk.sendText(msg.to,"Command DiTolak")
                    kc.sendText(msg.to,"Lu bukan admin")
                    kl.sendText(msg.to,"Admin Tidak Bisa Menggunakan")
                    ki.sendText(msg.to,"Cuma Owner Yang bisa Menggunakan")
            elif "Admrem @" in msg.text:
                if msg.from_ in creator:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admrem @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                        ki.sendText(msg.to,"Contact not found")
                        kc.sendText(msg.to,"Contact not found")
                        kl.sendText(msg.to,"Contact not found")
                        kk.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                                ki.sendText(msg.to,"Admin Dihapus")
                                kc.sendText(msg.to,"Admin Dihapus")
                                kl.sendText(msg.to,"Admin Dihapus")
                                kk.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command DiTolak")
                    kc.sendText(msg.to,"Command DiTolak")
                    kl.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")
                    ki.sendText(msg.to,"Admin atau Member Tidak Bisa Menggunakan")

            elif msg.text in ["Adminlist","adminlist"]:
              if msg.from_ in creator:
                if admin == []:
                    cl.sendText(msg.to,"The adminlist is empty")
                    ki.sendText(msg.to,"The adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    ki.sendText(msg.to,"Tunggu...")
                    kc.sendText(msg.to,"Tunggu...")
                    kl.sendText(msg.to,"Tunggu...")
                    kk.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "=>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------------------------------
            elif msg.text in ["Mad On","mad on"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Dont cancel anyone ! cause me angry!")
                         ki.sendText(msg.to,"Jgn cancel undangan atau autokick!")
                     else:
                         cl.sendText(msg.to,"done")
                         ki.sendText(msg.to,"sudah")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                        ki.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                        ki.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"sudah")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                        ki.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                        ki.sendText(msg.to,"sudah")
#-----------------------------------------------
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                   print "[Command]dp executing"
                   _name = msg.text.replace("Steal dp @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except:
                               pass
                   print "[Command]dp executed"
#------------------------------------------
            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:                                                                   ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
#-----------------------------------------------------------
            elif msg.text in ["Protect Off","Mode Off"]:
              if msg.from_ in admin:
                if wait["Protectgroupname"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                    else:
                        cl.sendText(msg.to,"Gname OFF")
                else:
                    wait["Protectgroupname"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Gname Off")
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")      
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Block Invite Off")
                    else:
                        cl.sendText(msg.to,"done")
#-----------------------------------------------
            elif msg.text in ["Protect On","Mode On"]:
              if msg.from_ in admin:
                if wait["Protectgroupname"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"Gname ON")
                else:
                    wait["Protectgroupname"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel On")      
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"Block On")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Block On")
                    else:
                        cl.sendText(msg.to,"Block On")
#-----------------------------------------------
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
            	text = msg.text
            	if text is not None:
            		cl.sendText(msg.to,text)
            		ki.sendText(msg.to,text)
            	else:
            		if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            							 	 "STKID": "6",
            							 	 "STKPKGID": "1",
            							 	 "STKVER": "100" }
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            		elif msg.contentType == 13:
            			msg.contentType = 13
            			msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			cl.sendMessage(msg)
            			ki.sendMessage(msg)
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				cl.sendText(msg.to,"Mimic on")
            				ki.sendText(msg.to,"Mimic on")
            			else:
            				cl.sendText(msg.to,"Mimic already on")
            				ki.seneText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				cl.sendText(msg.to,"Mimic off")
            				ki.sendText(msg.to,"Mimic off")
            			else:
            				cl.sendText(msg.to,"Mimic already off")
            				ki.sendText(msg.to,"Mimic already off")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            				ki.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						cl.sendText(msg.to,"Success added target")
            						ki.sendText(msg.to,"Success added target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed")
            						ki.sendText(msg.to,"Failed")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			gInfo = ki.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				cl.sendText(msg.to,"No targets")
            				ki.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						cl.sendText(msg.to,"Success deleted target")
            						ki.sendText(msg.to,"Success deleted target")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						cl.sendText(msg.to,"Failed!")
            						ki.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
            				ki.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + ki.getContact(mi_d).displayName +" | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
                                ki.sendText(msg.to,lst + "\nTotal:" + total)
#-----------------------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#-----------------------------------------------
            elif "Copy @" in msg.text:
            	print "Clone succes"
            	if msg.toType == 2:
            	    if msg.from_ in admin:
            	        _name = msg.text.replace("Copy @","")
                        _nametarget = name.rstrip(" ")
                        gs = cl.getGroup(msg.to)
                        gs = ki.getGroup(msg.to)
                        targets = []
          
                        if _nametarget == g.displayName:
                                 targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Contact not found")
                            ki.sendText(msg.to,"Contact not found")
#-----------------------------------------------
            elif msg.text in ["Responsename","Respon"]:
				if msg.from_ in admin:
					cl.sendText(msg.to,"Tora Aktif")
					ki.sendText(msg.to,"Tora 2 Aktif")
					kc.sendText(msg.to,"Tora 3 Aktif")
					kl.sendText(msg.to,"Tora 4 Aktif")
					kk.sendText(msg.to,"Tora 5 Aktif")
#-----------------------------------------------
            elif msg.text in ["spedasli"]:
				if msg.from_ in admin:
					start = time.time()
					cl.sendText(msg.to, "SpeedBot..")
					elapsed_time = time.time() - start
					cl.sendText(msg.to, "%sseconds" % (elapsed_time))
					ki.sendText(msg.to, "%sseconds" % (elapsed_time))
					kc.sendText(msg.to, "%sseconds" % (elapsed_time))
					kl.sendText(msg.to, "%sseconds" % (elapsed_time))
					kk.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text in ["Sp","Speed","speed"]:
                fake=["0.000271114197 second","0.00019165887 second","0.00025112297 second","0.000218382292 second","0.00026668778 second","0.000218382117 second","0.0001193829922 second","0.0003524116 second"]
                fspeed=random.choice(fake)
                cl.sendText(msg.to,"Progress...")
                cl.sendText(msg.to,(fspeed))
                ki.sendText(msg.to,(fspeed))
                kl.sendText(msg.to,(fspeed))
                kc.sendText(msg.to,(fspeed))
                kk.sendText(msg.to,(fspeed))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")                  
            elif msg.text in ["Unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")					
            elif msg.text in ["Banlist"]:
				if msg.from_ in admin:
					if wait["blacklist"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Blacklist user")
						mc = ""
						for mi_d in wait["blacklist"]:
							mc += "�1�7" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Cek ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						cocoa = ""
						for mm in matched_list:
							cocoa += mm + "\n"
						cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.members]
						matched_list = []
						for tag in wait["blacklist"]:
							matched_list+=filter(lambda str: str == tag, gMembMids)
						if matched_list == []:
							cl.sendText(msg.to,"There was no blacklist user")
							return
						for jj in matched_list:
							cl.kickoutFromGroup(msg.to,[jj])
						cl.sendText(msg.to,"Bye...")
            elif msg.text in ["Clear"]:
				if msg.from_ in admin:
					if msg.toType == 2:
						group = cl.getGroup(msg.to)
						group = ki.getGroup(msg.to)
						gMembMids = [contact.mid for contact in group.invitee]
						for _mid in gMembMids:
							cl.cancelGroupInvitation(msg.to,[_mid])
						cl.sendText(msg.to,"Cancel Success!")
						ki.sendText(msg.to,"Cancel Success!")
            elif "album" in msg.text:
				if msg.from_ in admin:
					try:
						albumtags = msg.text.replace("album","")
						gid = albumtags[:6]
						name = albumtags.replace(albumtags[:34],"")
						cl.createAlbum(gid,name)
						cl.sendText(msg.to,name + "created an album")
					except:
						cl.sendText(msg.to,"Error")
            elif "fakecâ†�1�7�1�7" in msg.text:
				if msg.from_ in admin:
					try:
						source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
						name = "".join([random.choice(source_str) for x in xrange(10)])
						anu = msg.text.replace("fakecâ†�1�7�1�7","")
						cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
					except Exception as e:
						try:
							cl.sendText(msg.to,str(e))
						except:
							pass
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
			for zx in range(0,20):
				hasil = cl.activity(limit=20)
				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
					try:    
						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Autolike By: Tora Bot ID\nPlease add our Official Account\nhttp://line.me/R/ti/p/%40qua3481v")
						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Autolike By: Tora Bot ID\nPlease add our Official Account\nhttp://line.me/R/ti/p/%40qua3481v")
						ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Autolike By: Tora Bot ID\nPlease add our Official Account\nhttp://line.me/R/ti/p/%40qua3481v")
						kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Autolike By: Tora Bot ID\nPlease add our Official Account\nhttp://line.me/R/ti/p/%40qua3481v")
						kl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
						kl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Autolike By: Tora Bot ID\nPlease add our Official Account\nhttp://line.me/R/ti/p/%40qua3481v")
						print "DiLike"
					except:
							pass
				else:
						print "Sudah DiLike"
			time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
	
