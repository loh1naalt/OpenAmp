create table Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    role TEXT /*('user', 'admin')*/

)

CREATE TABLE Playlists(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    PlaylistName TEXT,
    PlaylistUploader TEXT,
    FOREIGN KEY("PlaylistUploader") REFERENCES "Users"("id")
)

CREATE TABLE Songs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    SongName TEXT,
    SongArtist TEXT,
    serverdirtosong TEXT,
    SongDuration INTEGER,
    PlaylistId INTEGER,
    SongUploader TEXT,
    FOREIGN KEY("SongUploader") REFERENCES "Users"("id")
    FOREIGN KEY("PlaylistId") REFERENCES "Playlists"("id")
)

/*CREATE TABLE UserSongPlaylists(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Userid INTEGER,
    Songid INTEGER,
    PlaylistId INTEGER,
    FOREIGN KEY("Userid") REFERENCES "Users"("id")
    FOREIGN KEY("Songid") REFERENCES "Songs"("id")
    FOREIGN KEY("PlaylistId") REFERENCES "Playlists"("id")
)*/
