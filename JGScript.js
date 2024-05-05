function SendUserToGame() {
    let selectedGame = document.getElementById("GamesSelect").value;
    let WhereToClick = "Click Me!"
    document.getElementById("SelectedGame").innerHTML = "You selected: <a href='" + selectedGame + "' target='_blank'>" + WhereToClick + "</a>";
}
