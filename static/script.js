async function searchMusic() {

let query = document.getElementById("searchInput").value

let response = await fetch(`/search?q=${query}`)
let data = await response.json()

let results = document.getElementById("results")
results.innerHTML = ""

data.forEach(track => {

let div = document.createElement("div")
div.classList.add("song")

div.innerHTML = `
<img src="${track.image}">
<h3>${track.name}</h3>
<p>${track.artist}</p>
${track.preview ? `<audio controls src="${track.preview}"></audio>` : "No preview"}
`

results.appendChild(div)

})

}