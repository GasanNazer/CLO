"using strict"

let count = 0;

function myFunction() {
    let element = $("#elementSelector option:selected").text();
    let startYear = $("#startYear option:selected").text();
    let endYear = $("#endYear option:selected").text();
    console.log(element);
    console.log(startYear);
    console.log(endYear);
    let imageName = element + "_" + startYear + "_" + endYear + ".png";
    console.log(imageName);

    clear();
    let imageParent = document.getElementById("body");
    let image = document.createElement("img");
    image.id = "id";
    image.className = "classImg";
    image.src = "images/charts/" + imageName; // image.src = "IMAGE URL/PATH"
    imageParent.appendChild(image);

}

function clear() {
    document.getElementById("body").innerHTML = "";
}