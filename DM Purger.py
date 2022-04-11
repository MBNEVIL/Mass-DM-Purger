import discord
import asyncio
import os
from colorama import Fore
from colorama import Back
from colorama import Style




token = input("Insert Token: ")
os.system("cls")
os.system(f'mode 125,18')
os.system("title DM/SERVER PURGER -  CODED BY mbn evil#9731")

print(f"""{Fore.LIGHTBLUE_EX}{Style.BRIGHT} ▄▀▀█▄▄   ▄▀▀▄ ▄▀▄      ▄▀▀▄▀▀▀▄  ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄ 
█ ▄▀   █ █  █ ▀  █     █   █   █ █   █    █ █   █   █ █        ▐  ▄▀   ▐ █   █   █ 
▐ █    █ ▐  █    █     ▐  █▀▀▀▀  ▐  █    █  ▐  █▀▀█▀  █    ▀▄▄   █▄▄▄▄▄  ▐  █▀▀█▀  
  █    █   █    █         █        █    █    ▄▀    █  █     █ █  █    ▌   ▄▀    █  
 ▄▀▄▄▄▄▀ ▄▀   ▄▀        ▄▀          ▀▄▄▄▄▀  █     █   ▐▀▄▄▄▄▀ ▐ ▄▀▄▄▄▄   █     █   
█     ▐  █    █        █                    ▐     ▐   ▐         █    ▐   ▐     ▐   
▐        ▐    ▐        ▐                                        ▐                  
type $purgedm if u wanna purge a dm type $purgeserver if u wanna purge server 
                                         code by mbn evil#9731                                                       """)

 

class MyClient(discord.Client):
  async def on_message(self, message):
      if(message.author!=self.user):
          return
      channels=[]
      if(message.content=="$purgeserver"):
          channels=message.channel.guild.channels
      elif(message.content=="$purgedm"):
          channels.append(message.channel)
      else:
          return
      for channel in channels:
          print(channel)
          try:
              async for mss in channel.history(limit=None):
                  if(mss.author==self.user):
                      print(f'{Fore.LIGHTWHITE_EX}[ {Fore.LIGHTBLUE_EX}DELETED {Fore.LIGHTWHITE_EX}] ' + mss.content)
                      try:
                          await mss.delete()
                      except:
                          print(f'{Fore.RED}Failed to delete message.')
          except:
              print(f'{Fore.RED}Failed to read history.')
         

client=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
client.run(token, bot=False)