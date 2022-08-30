import requests

headers = {
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjY1NmVhM2Y0LWU4YTctNGEwOC1hOTFjLTdmMTMyOTQ3MGRiOCIsImlhdCI6MTY2MTc4NTk2Niwic3ViIjoiZGV2ZWxvcGVyL2NiN2M1OGYzLWYyNmUtYTljYS01NGVmLTI2MDg3NzI5ZDViNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE3OC4yMDAuMTgwLjk5Il0sInR5cGUiOiJjbGllbnQifV19.LT-_HPeEbDnfw3cdeZ3TjrwZjhaD49k8XdYluSEdvmHuuyuQKgwnC59QzxfzElu-7cT8uWjOzW9H3SPht9I5xg',
    'Accept': 'application/json'
}

members_and_tags = {}


def get_clan_info():
    clan = requests.get("https://api.clashofclans.com/v1/clans/%232YLR2QJVQ", headers=headers)
    war_info = requests.get("https://api.clashofclans.com/v1/clans/%232YLR2QJVQ/warlog", headers=headers)

    clanlist = clan.json()
    big_memberlist = clanlist["memberList"]
    i = 1
    for person_list in big_memberlist:
        temp_dict = {"Tag": person_list["tag"]}
        members_and_tags[person_list["name"]] = temp_dict
        i += 1
    print(members_and_tags)    
    
    war_info_jsn = war_info.json()   
    #print(war_info_jsn)

get_clan_info()