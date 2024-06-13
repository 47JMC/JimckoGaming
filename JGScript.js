function SendUserToGame() {
    let selectedGame = document.getElementById("DropdownSelectGame").value;
    let WhereToClick = "Click Me!";
    document.getElementById("DropdownSelectedGameLink").innerHTML = "You selected: <a href='" + selectedGame + "' target='_blank'>" + WhereToClick + "</a>";
}

document.addEventListener("DOMContentLoaded", function () {
    let gameSearchForm = document.getElementById("GameSearchForm");

    gameSearchForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the form from submitting and refreshing the page

        // Get the value of the input field
        let gameName = document.getElementById("GameSearchInput").value;
        let gameNamelower = gameName.toLowerCase();
        let Modedgamename = gameNamelower.replace(/ /g, "-");

        // Do something with the gameName, such as sending it to a server or performing a search
        console.log("Search for game:", gameName);
        window.location.href = "https://poki.com/en/g/" + Modedgamename
    });
});
