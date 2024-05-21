function SendUserToGame() {
    let selectedGame = document.getElementById("DropdownSelectGame").value;
    let WhereToClick = "Click Me!";
    document.getElementById("DropdownSelectedGameLink").innerHTML = "You selected: <a href='" + selectedGame + "' target='_blank'>" + WhereToClick + "</a>";
}

document.addEventListener("DOMContentLoaded", function() {
    let gameSearchForm = document.getElementById("GameSearchForm");

    gameSearchForm.addEventListener("submit", function(event) {
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

// Function to get date, month , year
function doCountdown() {
    let today = new Date();
    let date = today.getDate()
    let month = today.getMonth() + 1
    let year = today.getFullYear();

    let hajj_date = "31"
    let hajj_month = "5"
    let hajj_year = "2024"

    let remaining_days = hajj_date - date
    let remaining_months = hajj_month - month
    let remaining_years = hajj_year - year

    console.log(remaining_days, remaining_months, remaining_years)

    document.getElementById("days").innerHTML = remaining_days + " Days Remaining";
    document.getElementById("months").innerHTML = remaining_months + " Months Remaining";
    document.getElementById("years").innerHTML = remaining_years + " Years Remaining";

}

document.addEventListener("DOMContentLoaded", function() {
    // Function to run on a specific page
    doCountdown() 
    console.log("This function runs only on the specified page!");
        // Your function code here
    
});