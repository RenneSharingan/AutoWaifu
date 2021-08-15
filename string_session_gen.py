from pyrogram import Client

API_KEY = int(input("Enter API KEY: "))
API_HASH = input("Enter API HASH: ")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    app.send_message(
        "me",
        f"#AutoWaifu #STRING_SESSION\n\n```{app.export_session_string()}```"
    )
    print("Done !, session string has been sent to saved messages!")
