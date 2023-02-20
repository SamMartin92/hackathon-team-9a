var result = document.getElementById('result')
var choice = document.getElementById('choice')
var button = document.getElementById('button1')

var causes = ["animals", "athletics", "autism", "black-led", "buddhism", "cancer", "cats", "christianity",
    "climate", "conservation", "coronavirus", "culture", "dance", "disabilities", "disease", "dogs", "education", "environment",
    "food-security", "gender-equality", "health", "hinduism", "housing", "humans", "immigrants", "indigenous-peoples",
    "islam", "judaism", "justice", "legal", "lgbt", "libraries", " mental-health", "middle-east", "museums", "music", "oceans",
    "poverty", "racial-justice", "refugees", "religion", "reproductive-justice", "research", "science", "seniors",
    "space", "theater", "transgender", "ukraine", "veterans", "water", "wildfires", "wildlife", "women-led", "womens-health",
    "youth"
]

//https://stackoverflow.com/questions/1026069/how-do-i-make-the-first-letter-of-a-string-uppercase-in-javascript
function capitalizeFirstLetter(string) {
    return string[0].toUpperCase() + string.slice(1);
}

function loadOptions() {
    for (let i = 0; i < causes.length; i++){
        choice.innerHTML += `<option value="${causes[i]}">${capitalizeFirstLetter(causes[i]).replace("-", " ")}</option>`
    }
}

function getResult() {
    result.innerHTML = ""

    fetch(`https://partners.every.org/v0.2/browse/${choice.value}?apiKey=4933b0c2806cbae1f1cb3f4803b611b3`)
        .then((response) => response.json())
        .then((data) => {
            let arr = data.nonprofits
            for (let i = 0; i < arr.length; i++) {
                result.innerHTML += `
        <div class="col-md-4 col-sm-6">
        <div class="card ngo-cards">
        <img src="${arr[i].coverImageUrl}" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">${arr[i].name}</h5>
          <p class="card-text">${arr[i].description}</p>
        </div>
        <hr/>
        <div class="card-body logo-link-div">
          <a href="${arr[i].profileUrl}" class="card-link" target="_blank">Learn more</a>
          <img src="${arr[i].logoUrl}">
        </div>
      </div>
      </div>`;
            }
        })
}


button.addEventListener("click", getResult)
loadOptions();