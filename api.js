var result= document.getElementById('result')




function getResult(){
    fetch("https://partners.every.org/v0.2/search/pets?apiKey=4933b0c2806cbae1f1cb3f4803b611b3")
  .then((response) => response.json())
  .then((data)=>  {
    let arr = data.nonprofits 
    for (let i = 0; i < arr.length; i++){
        result.innerHTML += `<li>${arr[i].name}</li>`;
    }
  })
}



getResult();