from linepy import *


client = LINE()
client.log("Auth Token : " + str(client.authToken))

oepoll = OEPoll(client)

MySelf = client.getProfile()
print("My MID : " + MySelf.mid)


def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        client.acceptGroupInvitation(op.param1)
        client.leaveGroup(op.param1)
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
      
      
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP
})


while True:
    oepoll.trace()
